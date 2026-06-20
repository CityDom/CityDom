#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::io::Write;
use serde::Serialize;

#[cfg(windows)]
use tauri::Manager;

#[cfg(windows)]
use windows_sys::core::BOOL;

#[cfg(windows)]
use windows_sys::Win32::{
    Foundation::{HWND, LPARAM, POINT, RECT},
    Graphics::Gdi::ClientToScreen,
    UI::{
        HiDpi::GetDpiForWindow,
        WindowsAndMessaging::{
            EnumWindows, GetClientRect, GetWindow, GetWindowRect, GetWindowThreadProcessId,
            IsIconic, IsWindow, IsWindowVisible, PostMessageW, SetWindowLongPtrW, SetWindowPos,
            ShowWindow, GWLP_HWNDPARENT, GW_OWNER, SWP_NOACTIVATE, SWP_NOOWNERZORDER, SW_HIDE,
            SW_SHOWNA, WM_CLOSE,
        },
    },
};

#[cfg(windows)]
const POLL_INTERVAL_MS: u64 = 50;

#[cfg(windows)]
#[derive(Clone, Copy, Debug)]
struct LogicalLayout {
    design_width: f64,
    design_height: f64,
    x: f64,
    y: f64,
    width: f64,
    height: f64,
}

#[cfg(windows)]
#[derive(Clone, Copy)]
struct GeometryResult {
    owner_client: RECT,
    dpi: u32,
    scale: f64,
    letterbox_x: f64,
    letterbox_y: f64,
    target: RECT,
}

#[cfg(windows)]
struct WindowSearch {
    pid: u32,
    hwnd: HWND,
    area: i64,
}

fn argument_value(name: &str) -> Option<String> {
    let mut args = std::env::args();
    while let Some(arg) = args.next() {
        if arg == name {
            return args.next();
        }
    }
    None
}

fn numeric_arg(name: &str) -> Option<f64> {
    argument_value(name)?.parse::<f64>().ok()
}

#[cfg(windows)]
fn owner_pid_arg() -> Option<u32> {
    argument_value("--owner-pid")?.parse::<u32>().ok()
}

#[cfg(windows)]
fn logical_layout_args() -> LogicalLayout {
    LogicalLayout {
        design_width: numeric_arg("--design-width").unwrap_or(1920.0),
        design_height: numeric_arg("--design-height").unwrap_or(1080.0),
        x: numeric_arg("--logical-x").unwrap_or(408.0),
        y: numeric_arg("--logical-y").unwrap_or(160.0),
        width: numeric_arg("--logical-width").unwrap_or(430.0),
        height: numeric_arg("--logical-height").unwrap_or(760.0),
    }
}

#[cfg(windows)]
fn geometry_log(message: &str) {
    let path = std::env::temp_dir().join("city-dom-character-viewer-geometry.log");
    if let Ok(mut file) = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(path)
    {
        let elapsed = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .map(|value| value.as_millis())
            .unwrap_or_default();
        let _ = writeln!(file, "[{elapsed}] {message}");
    }
    eprintln!("{message}");
}

#[cfg(windows)]
fn timing_log(event: &str) {
    let Some(path) = argument_value("--timing-log-path") else {
        return;
    };
    if let Ok(mut file) = std::fs::OpenOptions::new().create(true).append(true).open(path) {
        let elapsed = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .map(|value| value.as_millis())
            .unwrap_or_default();
        let _ = writeln!(file, "[{elapsed}] {event}");
    }
}

#[cfg(windows)]
fn status_wants_visible() -> bool {
    let Some(path) = argument_value("--status-path") else {
        return true;
    };
    std::fs::read_to_string(path)
        .map(|status| status.contains("\"state\":\"visible\""))
        .unwrap_or(false)
}

#[tauri::command]
fn write_bridge_status(path: String, contents: String) -> Result<(), String> {
    std::fs::write(path, contents).map_err(|error| error.to_string())
}

#[tauri::command]
fn append_bridge_timing(path: String, line: String) -> Result<(), String> {
    let mut file = std::fs::OpenOptions::new()
        .create(true)
        .append(true)
        .open(path)
        .map_err(|error| error.to_string())?;
    file.write_all(line.as_bytes()).map_err(|error| error.to_string())
}

#[tauri::command]
fn read_bridge_command(path: String) -> Result<Option<String>, String> {
    match std::fs::read_to_string(path) {
        Ok(contents) => Ok(Some(contents)),
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => Ok(None),
        Err(error) => Err(error.to_string()),
    }
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct NativeBridgeOptions {
    embedded: bool,
    shell_only: bool,
    command_path: Option<String>,
    status_path: Option<String>,
    timing_log_path: Option<String>,
    zoom: Option<f64>,
    min_distance: Option<f64>,
    max_distance: Option<f64>,
    always_on_top: bool,
}

#[tauri::command]
fn get_native_bridge_options() -> NativeBridgeOptions {
    NativeBridgeOptions {
        embedded: argument_value("--embed")
            .map(|value| matches!(value.to_ascii_lowercase().as_str(), "1" | "true" | "yes"))
            .unwrap_or(false),
        shell_only: argument_value("--shell-only")
            .map(|value| matches!(value.to_ascii_lowercase().as_str(), "1" | "true" | "yes"))
            .unwrap_or(false),
        command_path: argument_value("--command-path"),
        status_path: argument_value("--status-path"),
        timing_log_path: argument_value("--timing-log-path"),
        zoom: numeric_arg("--zoom"),
        min_distance: numeric_arg("--min-distance"),
        max_distance: numeric_arg("--max-distance"),
        always_on_top: argument_value("--always-on-top")
            .map(|value| matches!(value.to_ascii_lowercase().as_str(), "1" | "true" | "yes"))
            .unwrap_or(false),
    }
}

#[cfg(windows)]
fn rect_size(rect: &RECT) -> (i32, i32) {
    (rect.right - rect.left, rect.bottom - rect.top)
}

#[cfg(windows)]
fn same_rect(left: &RECT, right: &RECT) -> bool {
    left.left == right.left
        && left.top == right.top
        && left.right == right.right
        && left.bottom == right.bottom
}

#[cfg(windows)]
unsafe extern "system" fn enum_windows_proc(hwnd: HWND, lparam: LPARAM) -> BOOL {
    let search = unsafe { &mut *(lparam as *mut WindowSearch) };
    let mut window_pid = 0u32;
    unsafe {
        GetWindowThreadProcessId(hwnd, &mut window_pid);
    }

    if window_pid != search.pid
        || unsafe { IsWindowVisible(hwnd) } == 0
        || !unsafe { GetWindow(hwnd, GW_OWNER) }.is_null()
    {
        return 1;
    }

    let Some(rect) = window_rect(hwnd) else {
        return 1;
    };
    let (width, height) = rect_size(&rect);
    let area = i64::from(width.max(0)) * i64::from(height.max(0));
    if area > search.area {
        search.hwnd = hwnd;
        search.area = area;
    }

    1
}

#[cfg(windows)]
fn find_owner_window(pid: u32) -> Option<HWND> {
    let mut search = WindowSearch {
        pid,
        hwnd: std::ptr::null_mut(),
        area: -1,
    };
    unsafe {
        let _ = EnumWindows(
            Some(enum_windows_proc),
            &mut search as *mut WindowSearch as LPARAM,
        );
    }

    (!search.hwnd.is_null()).then_some(search.hwnd)
}

#[cfg(windows)]
fn window_rect(hwnd: HWND) -> Option<RECT> {
    let mut rect = RECT {
        left: 0,
        top: 0,
        right: 0,
        bottom: 0,
    };
    (unsafe { GetWindowRect(hwnd, &mut rect) } != 0).then_some(rect)
}

#[cfg(windows)]
fn client_screen_rect(hwnd: HWND) -> Option<RECT> {
    let mut client = RECT {
        left: 0,
        top: 0,
        right: 0,
        bottom: 0,
    };
    let mut origin = POINT { x: 0, y: 0 };
    if unsafe { GetClientRect(hwnd, &mut client) } == 0
        || unsafe { ClientToScreen(hwnd, &mut origin) } == 0
    {
        return None;
    }

    Some(RECT {
        left: origin.x,
        top: origin.y,
        right: origin.x + client.right - client.left,
        bottom: origin.y + client.bottom - client.top,
    })
}

#[cfg(windows)]
fn calculate_geometry(owner_hwnd: HWND, layout: LogicalLayout) -> Option<GeometryResult> {
    let owner_client = client_screen_rect(owner_hwnd)?;
    let (client_width, client_height) = rect_size(&owner_client);
    if client_width <= 0
        || client_height <= 0
        || layout.design_width <= 0.0
        || layout.design_height <= 0.0
    {
        return None;
    }

    let scale = (client_width as f64 / layout.design_width)
        .min(client_height as f64 / layout.design_height);
    let game_width = layout.design_width * scale;
    let game_height = layout.design_height * scale;
    let letterbox_x = (client_width as f64 - game_width) * 0.5;
    let letterbox_y = (client_height as f64 - game_height) * 0.5;

    let left = owner_client.left + (letterbox_x + layout.x * scale).round() as i32;
    let top = owner_client.top + (letterbox_y + layout.y * scale).round() as i32;
    let width = (layout.width * scale).round().max(1.0) as i32;
    let height = (layout.height * scale).round().max(1.0) as i32;

    Some(GeometryResult {
        owner_client,
        dpi: unsafe { GetDpiForWindow(owner_hwnd) },
        scale,
        letterbox_x,
        letterbox_y,
        target: RECT {
            left,
            top,
            right: left + width,
            bottom: top + height,
        },
    })
}

#[cfg(windows)]
fn apply_geometry(
    reason: &str,
    owner_hwnd: HWND,
    viewer_hwnd: HWND,
    layout: LogicalLayout,
) -> Option<GeometryResult> {
    let result = calculate_geometry(owner_hwnd, layout)?;
    unsafe {
        SetWindowPos(
            viewer_hwnd,
            std::ptr::null_mut(),
            result.target.left,
            result.target.top,
            result.target.right - result.target.left,
            result.target.bottom - result.target.top,
            SWP_NOACTIVATE | SWP_NOOWNERZORDER,
        );
    }

    let actual = window_rect(viewer_hwnd).unwrap_or(result.target);
    let (client_width, client_height) = rect_size(&result.owner_client);
    geometry_log(&format!(
        "geometry reason={reason} owner_hwnd={:?} viewer_outer_hwnd={:?} client={}x{} origin=({}, {}) dpi={} scale={:.6} letterbox=({:.2}, {:.2}) logical=({:.2}, {:.2}, {:.2}, {:.2}) target=({}, {}, {}, {}) actual=({}, {}, {}, {})",
        owner_hwnd,
        viewer_hwnd,
        client_width,
        client_height,
        result.owner_client.left,
        result.owner_client.top,
        result.dpi,
        result.scale,
        result.letterbox_x,
        result.letterbox_y,
        layout.x,
        layout.y,
        layout.width,
        layout.height,
        result.target.left,
        result.target.top,
        result.target.right - result.target.left,
        result.target.bottom - result.target.top,
        actual.left,
        actual.top,
        actual.right - actual.left,
        actual.bottom - actual.top,
    ));

    Some(result)
}

#[cfg(windows)]
fn monitor_owner_window(
    owner_hwnd: HWND,
    viewer_hwnd: HWND,
    layout: LogicalLayout,
    initial: GeometryResult,
) {
    let owner_handle = owner_hwnd as isize;
    let viewer_handle = viewer_hwnd as isize;

    std::thread::spawn(move || {
        let owner_hwnd = owner_handle as HWND;
        let viewer_hwnd = viewer_handle as HWND;
        let mut previous = initial;
        let mut hidden_for_minimize = false;

        loop {
            std::thread::sleep(std::time::Duration::from_millis(POLL_INTERVAL_MS));

            if unsafe { IsWindow(owner_hwnd) } == 0 || unsafe { IsWindow(viewer_hwnd) } == 0 {
                if unsafe { IsWindow(viewer_hwnd) } != 0 {
                    geometry_log("owner window closed; closing viewer");
                    unsafe {
                        PostMessageW(viewer_hwnd, WM_CLOSE, 0, 0);
                    }
                }
                break;
            }

            if unsafe { IsIconic(owner_hwnd) } != 0 {
                if !hidden_for_minimize {
                    geometry_log("owner minimized; hiding viewer");
                    unsafe {
                        ShowWindow(viewer_hwnd, SW_HIDE);
                    }
                    hidden_for_minimize = true;
                }
                continue;
            }

            if hidden_for_minimize {
                if let Some(restored) = apply_geometry("restore", owner_hwnd, viewer_hwnd, layout) {
                    previous = restored;
                }
                if status_wants_visible() {
                    unsafe {
                        ShowWindow(viewer_hwnd, SW_SHOWNA);
                    }
                }
                hidden_for_minimize = false;
                continue;
            }

            let Some(current) = calculate_geometry(owner_hwnd, layout) else {
                continue;
            };
            let actual = window_rect(viewer_hwnd);
            let owner_changed = !same_rect(&current.owner_client, &previous.owner_client)
                || current.dpi != previous.dpi;
            let viewer_drifted = actual
                .map(|rect| !same_rect(&rect, &current.target))
                .unwrap_or(false);

            if owner_changed || viewer_drifted {
                let reason = if owner_changed {
                    "owner-change"
                } else {
                    "viewer-drift"
                };
                if let Some(applied) = apply_geometry(reason, owner_hwnd, viewer_hwnd, layout) {
                    previous = applied;
                }
            }
        }
    });
}

#[cfg(windows)]
fn configure_owned_window(app: &mut tauri::App) {
    let Some(owner_pid) = owner_pid_arg() else {
        return;
    };
    let Some(owner_hwnd) = find_owner_window(owner_pid) else {
        geometry_log(&format!(
            "no visible top-level owner window for pid={owner_pid}"
        ));
        return;
    };
    let Some(window) = app.get_webview_window("main") else {
        geometry_log("Tauri main WebviewWindow was not found");
        return;
    };
    let Ok(tauri_hwnd) = window.hwnd() else {
        geometry_log("Tauri main outer HWND was unavailable");
        return;
    };
    let viewer_hwnd = tauri_hwnd.0 as HWND;
    timing_log("tauri_window_created");

    unsafe {
        SetWindowLongPtrW(viewer_hwnd, GWLP_HWNDPARENT, owner_hwnd as isize);
    }

    let layout = logical_layout_args();
    geometry_log(&format!(
        "attached owner_pid={owner_pid} owner_hwnd={:?} tauri_outer_hwnd={:?}",
        owner_hwnd, viewer_hwnd
    ));
    let Some(initial) = apply_geometry("initial", owner_hwnd, viewer_hwnd, layout) else {
        geometry_log("initial geometry calculation failed");
        return;
    };

    monitor_owner_window(owner_hwnd, viewer_hwnd, layout, initial);
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_cli::init())
        .invoke_handler(tauri::generate_handler![
            write_bridge_status,
            append_bridge_timing,
            read_bridge_command,
            get_native_bridge_options
        ])
        .on_page_load(|_webview, payload| {
            #[cfg(windows)]
            timing_log(&format!("webview_page_loaded url={}", payload.url()));
        })
        .setup(|app| {
            #[cfg(windows)]
            {
                timing_log("tauri_app_setup");
                configure_owned_window(app);
            }

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running City Dom character viewer");
}
