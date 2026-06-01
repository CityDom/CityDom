init offset = 20

define new_ui_font_menu = "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
define new_ui_font_text = "fonts/citydom_ui/Raleway.ttf"
define new_ui_font_title = "fonts/citydom_ui/CinzelDecorative-Bold.ttf"
define citydom_font_logo = "fonts/citydom_ui/CinzelDecorative-Bold.ttf"
define citydom_font_serif = "fonts/citydom_ui/CormorantInfant.ttf"
define citydom_font_serif_italic = "fonts/citydom_ui/CormorantInfant-Italic.ttf"
define citydom_font_ui = "fonts/citydom_ui/Raleway.ttf"
define citydom_dialogue_font_name = "fonts/citydom_dialogue/Cinzel.ttf"
define citydom_dialogue_font_body = "fonts/citydom_dialogue/Lora.ttf"
define citydom_dialogue_font_ui = "fonts/citydom_dialogue/Outfit.ttf"
define new_ui_scale = 0.24

define citydom_ui_asset_root = "gui/citydom_ui_v2"
define citydom_legacy_ui_asset_root = "gui/new_ui"
define citydom_legacy_menu_asset_root = "gui/new_ui/menu"

define citydom_color_primary = "#ff9bd9f2"
define citydom_color_primary_soft = "#ffb9e1f2"
define citydom_color_primary_muted = "#e879a0d9"
define citydom_color_secondary = "#e6beffe6"
define citydom_color_secondary_muted = "#c084d480"
define citydom_color_text = "#ffffffcc"
define citydom_color_text_muted = "#ffffff99"
define citydom_color_text_bright = "#fffffff2"
define citydom_color_transparent = "#00000000"
define citydom_color_shadow = "#00000099"
define citydom_color_shadow_strong = "#000000e6"
define citydom_color_shadow_soft = "#00000080"
define citydom_color_setting_outline = "#7d1bb366"
define citydom_color_black_outline_strong = "#000000cc"
define citydom_color_black_outline_soft = "#000000aa"

define citydom_color_main_dust = "#f9a8d4"
define citydom_color_logo_city = "#d77dff"
define citydom_color_logo_dom = "#cd96ffa6"
define citydom_color_main_patreon_bg = "#140626a6"
define citydom_color_main_patreon_bg_hover = "#28104ccc"
define citydom_color_main_patreon_text = "#c89bf0b3"
define citydom_color_main_subtext = "#b482dc80"

define citydom_color_menu_idle = "#ebd2ffd1"
define citydom_color_menu_title = "#ffc8f0"
define citydom_color_ui_title = "#ffd2f4"
define citydom_color_slot_text = "#d8b6f0c9"
define citydom_color_slot_name = "#e8d4fce0"
define citydom_color_slot_date = "#d8b6f0d9"
define citydom_color_nav_idle = "#a06ec861"

define citydom_color_settings_section = "#ff8df8f2"
define citydom_color_settings_option = "#f1c4ffff"
define citydom_color_settings_option_idle = "#a078c880"
define citydom_color_settings_option_outline = "#8b28c866"
define citydom_color_settings_value = "#ff9df8ff"
define citydom_color_settings_divider = "#c084d414"

define citydom_color_backdrop_dark = "#07020e78"
define citydom_color_backdrop_purple = "#2b0a4552"
define citydom_color_backdrop_glow = "#7c1fb926"
define citydom_color_backdrop_warm = "#e879a012"

define citydom_color_button_hover_soft = "#ffffff10"
define citydom_color_button_hover = "#ffffff12"
define citydom_color_button_selected = "#ffffff0d"
define citydom_color_white = "#ffffff"

define citydom_color_dialogue_name = "#d864ff55"
define citydom_color_dialogue_continue = "#f472b68a"
define citydom_color_dialogue_quick = "#c4a1d280"
define citydom_color_dialogue_input = "#ff8bd7f2"
define citydom_color_dialogue_caret = "#ff9bd9"

define citydom_color_history_overlay_dark = "#160023b8"
define citydom_color_history_overlay_purple = "#50106f5c"
define citydom_color_history_name = "#ff6c9dcc"
define citydom_color_history_body = "#e9ddf2d9"
define citydom_color_history_empty = "#c6a5d18c"
define citydom_color_history_narration = "#c08cc98a"
define citydom_color_history_footer = "#c79bd985"
define citydom_color_history_title_outline = "#8d36c080"

define citydom_color_confirm_overlay = "#04010c8c"
define citydom_color_confirm_message = "#f0dcffe6"
define citydom_color_confirm_yes = "#ffc3e1f2"
define citydom_color_confirm_no_hover = "#d8aee8d9"
define citydom_color_confirm_no_idle = "#a078c3a6"

default citydom_bottom_nav_previous_id = "save"
default citydom_history_scene_id = None

init python:
    def citydom_ui_asset(name):
        return "%s/%s.png" % (citydom_ui_asset_root, name)

    def citydom_legacy_ui_asset(name):
        return "%s/%s.png" % (citydom_legacy_ui_asset_root, name)

    def citydom_legacy_menu_asset(name):
        return "%s/%s.png" % (citydom_legacy_menu_asset_root, name)

    def _citydom_cubic_bezier_value(a, b, t):
        return (3.0 * a * (1.0 - t) * (1.0 - t) * t) + (3.0 * b * (1.0 - t) * t * t) + (t * t * t)

    def _citydom_cubic_bezier_slope(a, b, t):
        return (3.0 * a * (1.0 - t) * (1.0 - t)) + (6.0 * (b - a) * (1.0 - t) * t) + (3.0 * (1.0 - b) * t * t)

    def citydom_menu_curve(t):
        guess = t
        for _i in range(5):
            slope = _citydom_cubic_bezier_slope(0.25, 0.45, guess)
            if abs(slope) < 0.001:
                break
            guess -= (_citydom_cubic_bezier_value(0.25, 0.45, guess) - t) / slope
            guess = max(0.0, min(1.0, guess))
        return _citydom_cubic_bezier_value(0.46, 0.94, guess)

    def citydom_settings_slider_fraction(value):
        try:
            adjustment = value.get_adjustment()
            range_value = float(adjustment.range)
            if range_value <= 0.0:
                return 0.0
            return min(1.0, max(0.0, float(adjustment.value) / range_value))
        except Exception:
            pass
        return 0.0

    def citydom_action_selected(action):
        try:
            if isinstance(action, (list, tuple)):
                return any(citydom_action_selected(item) for item in action)
            return bool(action.get_selected())
        except Exception:
            return False

    def citydom_dialogue_gradient_name(name):
        return AlphaMask(
            citydom_ui_asset("dialogue_name_gradient"),
            Text(name, style="new_ui_name_text_mask")
        )

    def citydom_history_current_scene_id():
        try:
            filename, _line = renpy.get_filename_line()
            if filename and filename != "unknown":
                return filename
        except Exception:
            pass
        return citydom_history_scene_id

    def citydom_history_tag_entry(entry):
        scene_id = citydom_history_current_scene_id()
        entry.citydom_scene_id = scene_id
        renpy.store.citydom_history_scene_id = scene_id

    if citydom_history_tag_entry not in config.history_callbacks:
        config.history_callbacks.append(citydom_history_tag_entry)

style new_ui_menu_text is default:
    font new_ui_font_menu
    size 44
    color citydom_color_menu_idle
    hover_color citydom_color_primary_soft
    selected_color citydom_color_primary_soft
    outlines [ (1, citydom_color_shadow_strong, 1, 1) ]

style new_ui_return_text is new_ui_menu_text:
    size 70

style new_ui_title_text is default:
    font new_ui_font_title
    size 58
    color citydom_color_menu_title
    outlines [ (1, citydom_color_shadow, 1, 1) ]
    kerning 12

style new_ui_label_text is default:
    font citydom_font_ui
    size 18
    color citydom_color_secondary_muted
    outlines [ ]
    kerning 3

style new_ui_small_text is default:
    font citydom_font_ui
    size 22
    color citydom_color_secondary
    outlines [ ]

style citydom_ui_title_text is default:
    font new_ui_font_title
    size 58
    color citydom_color_ui_title
    kerning 12
    outlines [ (1, citydom_color_shadow, 1, 1) ]

style citydom_ui_slot_text is default:
    font citydom_font_ui
    size 18
    color citydom_color_slot_text
    outlines [ ]

style citydom_ui_slot_name_text is citydom_ui_slot_text:
    font citydom_font_serif_italic
    size 26
    color citydom_color_slot_name

style citydom_ui_slot_date_text is citydom_ui_slot_text:
    color citydom_color_slot_date

style citydom_ui_card_chip_text is default:
    font citydom_font_ui
    size 12
    color citydom_color_primary_muted
    kerning 2
    outlines [ ]

style citydom_settings_section_text is default:
    font citydom_font_ui
    size 12
    color citydom_color_settings_section
    kerning 4
    outlines [ (1, citydom_color_setting_outline, 0, 0) ]

style citydom_settings_option_text is default:
    font citydom_font_ui
    size 16
    color citydom_color_settings_option
    kerning 1
    outlines [ (1, citydom_color_settings_option_outline, 0, 0) ]

style citydom_settings_value_text is default:
    font citydom_font_ui
    size 12
    color citydom_color_settings_value
    outlines [ (1, citydom_color_setting_outline, 0, 0) ]

style citydom_settings_note_text is default:
    font citydom_font_ui
    size 12
    color citydom_color_settings_value
    kerning 3
    outlines [ (1, citydom_color_setting_outline, 0, 0) ]

transform citydom_card_idle:
    zoom 1.0
    yoffset 0

transform citydom_card_hover:
    zoom 1.025
    yoffset -3

transform citydom_card_pop:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        easein 0.16 zoom 1.0
    on hover:
        easeout 0.22 zoom 1.025

transform citydom_confirm_button_pop:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        easein 0.16 zoom 1.0
    on hover:
        easeout 0.22 zoom 1.045

transform citydom_confirm_overlay_fade:
    on show:
        alpha 0.0
        linear 0.28 alpha 1.0
    on hide:
        linear 0.24 alpha 0.0

transform citydom_confirm_panel_show:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        alpha 0.0
        zoom 0.96
        yoffset 12
        easeout 0.32 alpha 1.0 zoom 1.0 yoffset 0
    on hide:
        easein 0.24 alpha 0.0 zoom 0.98 yoffset 12

transform citydom_file_content_show:
    subpixel True
    on show:
        alpha 0.0
        yoffset 14
        easeout 0.24 alpha 1.0 yoffset 0
    on hide:
        easein 0.18 alpha 0.0 yoffset -10

transform citydom_main_bg_fade:
    on show:
        alpha 0.0
        linear 1.4 alpha 1.0

transform citydom_main_menu_item_motion(delay=0.0):
    subpixel True
    on show:
        alpha 0.0
        xoffset -16
        pause delay
        warp citydom_menu_curve 0.45 alpha 1.0 xoffset 0
    on idle:
        warp citydom_menu_curve 0.45 xoffset 0 zoom 1.0
    on hover:
        warp citydom_menu_curve 0.45 xoffset 10 zoom 1.0

transform citydom_main_delayed_show(delay=0.0):
    subpixel True
    on show:
        alpha 0.0
        yoffset 8
        pause delay
        easeout 0.40 alpha 1.0 yoffset 0

transform citydom_main_dust(opacity=0.3, drift=16, duration=4.0):
    alpha opacity
    yoffset 0
    block:
        linear (duration / 2.0) alpha (opacity * 0.25) yoffset -drift
        linear (duration / 2.0) alpha opacity yoffset 0
        repeat

transform citydom_settings_option_motion:
    subpixel True
    on idle:
        easein 0.16 xoffset 0 zoom 1.0
    on hover:
        easeout 0.16 xoffset 2 zoom 1.0
    on selected_idle:
        easein 0.16 xoffset 0 zoom 1.0
    on selected_hover:
        easeout 0.16 xoffset 2 zoom 1.0

transform citydom_bottom_nav_active_motion(start_x=0, end_x=0):
    subpixel True
    xpos start_x
    on show:
        alpha 1.0
        warp citydom_menu_curve 0.30 xpos end_x
    on replace:
        warp citydom_menu_curve 0.30 xpos end_x

style citydom_settings_slider_hitbox is bar:
    left_bar Solid(citydom_color_transparent)
    right_bar Solid(citydom_color_transparent)
    hover_left_bar Solid(citydom_color_transparent)
    hover_right_bar Solid(citydom_color_transparent)
    thumb citydom_legacy_menu_asset("transparent_thumb")
    thumb_offset 0

screen citydom_settings_panel(x, y, w=695, h=170):
    add Frame(citydom_ui_asset("panel_bg_opaque"), 12, 12):
        xpos x
        ypos y
        xysize (w, h)
    add Frame(citydom_ui_asset("panel_bg"), 12, 12):
        xpos x
        ypos y
        xysize (w, h)

screen citydom_menu_backdrop():
    if main_menu:
        add citydom_ui_asset("main_bg_3")

    add Solid(citydom_color_backdrop_dark)
    add Solid(citydom_color_backdrop_purple)
    add Transform(citydom_ui_asset("card_empty_base"), xysize=(1920, 1080), alpha=0.22)
    add Solid(citydom_color_backdrop_glow)
    add Solid(citydom_color_backdrop_warm)

screen citydom_settings_radio(x, y, label, action, icon_name):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (270, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add (citydom_ui_asset("radio_on") if _selected else citydom_ui_asset("radio_off")) xpos 0 ypos 6
        add Transform(citydom_ui_asset("settings_icon_%s_%s" % (icon_name, "active" if _selected else "idle")), xysize=(16, 16)) xpos 34 ypos 8

        text label:
            xpos 62
            ypos 6
            style "citydom_settings_option_text"
            color (citydom_color_secondary if _selected else citydom_color_settings_option_idle)

screen citydom_settings_check(x, y, label, action):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (300, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add (citydom_ui_asset("check_on") if _selected else citydom_ui_asset("check_off")) xpos 0 ypos 6

        text label:
            xpos 34
            ypos 6
            style "citydom_settings_option_text"
            color (citydom_color_secondary if _selected else citydom_color_settings_option_idle)

screen citydom_settings_slider(x, y, label, value, icon_name, bar_w=650):
    $ _fraction = citydom_settings_slider_fraction(value)
    $ _percent = int(round(_fraction * 100))
    $ _fill_w = int(bar_w * _fraction)

    add Transform(citydom_ui_asset("settings_icon_%s_muted" % icon_name), xysize=(16, 16)) xpos x ypos y + 2

    text label.upper():
        xpos x + 32
        ypos y + 2
        style "citydom_settings_section_text"
        kerning 3

    text "%d%%" % _percent:
        xpos x + bar_w - 45
        ypos y + 2
        xsize 45
        text_align 1.0
        style "citydom_settings_value_text"

    add Transform(citydom_ui_asset("slider_empty"), xysize=(bar_w, 8)):
        xpos x
        ypos y + 36

    if _fill_w > 0:
        add Crop((0, 0, _fill_w, 8), Transform(citydom_ui_asset("slider_full"), xysize=(bar_w, 8))):
            xpos x
            ypos y + 36

    add citydom_ui_asset("slider_thumb"):
        xpos int(x + (_fraction * bar_w) - 10)
        ypos y + 30

    bar:
        xpos x
        ypos y + 28
        xysize (bar_w, 24)
        style "citydom_settings_slider_hitbox"
        value value

screen citydom_settings_switch(x, y, label, action, icon_name, row_w=650):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (row_w, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add Transform(citydom_ui_asset("settings_icon_%s_muted" % icon_name), xysize=(16, 16)) xpos -4 ypos 2

        text label.upper():
            xpos 27
            ypos 1
            style "citydom_settings_section_text"
            kerning 3

        add (citydom_ui_asset("switch_on") if _selected else citydom_ui_asset("switch_off")) xpos (row_w - 36) ypos 2

style new_ui_transparent_button is button:
    background None
    hover_background citydom_color_button_hover
    selected_background citydom_color_button_selected

style citydom_ui_clear_button is button:
    background None
    hover_background None
    selected_background None

style citydom_ui_card_button is button:
    background None
    hover_background None
    selected_background None
    padding (0, 0, 0, 0)
    xpadding 0
    ypadding 0
    margin (0, 0, 0, 0)

style new_ui_dialogue_text is default:
    font citydom_dialogue_font_body
    size 23
    color citydom_color_text
    outlines [ (1, citydom_color_shadow, 0, 1) ]
    line_spacing 6

style new_ui_name_text is default:
    font citydom_dialogue_font_name
    size 20
    color citydom_color_dialogue_name
    outlines [ (1, citydom_color_dialogue_name, 0, 0), (1, citydom_color_shadow_soft, 0, 1) ]
    kerning 5
    layout "nobreak"

style new_ui_name_text_mask is default:
    font citydom_dialogue_font_name
    size 20
    color citydom_color_white
    outlines [ ]
    kerning 5
    layout "nobreak"

style citydom_dialogue_hidden_text is default:
    size 1
    color citydom_color_transparent
    outlines [ ]

style citydom_dialogue_continue_text is default:
    font citydom_dialogue_font_ui
    size 10
    bold True
    color citydom_color_dialogue_continue
    outlines [ ]
    kerning 3

style citydom_dialogue_quick_button is button:
    background None
    hover_background None
    selected_background None
    padding (0, 0, 0, 0)
    xpadding 0
    ypadding 0

style citydom_dialogue_quick_button_text is button_text:
    font citydom_dialogue_font_ui
    size 11
    color citydom_color_dialogue_quick
    hover_color citydom_color_primary
    selected_color citydom_color_primary
    outlines [ ]
    kerning 0
    xalign 0.5
    yalign 0.5

style citydom_dialogue_input_text is default:
    font citydom_dialogue_font_body
    size 30
    color citydom_color_dialogue_input
    outlines [ (1, citydom_color_shadow, 0, 1) ]
    background None
    caret Transform(Solid(citydom_color_dialogue_caret), xysize=(2, 34))

style citydom_history_title_text is default:
    font citydom_dialogue_font_name
    size 42
    color citydom_color_primary
    outlines [ (1, citydom_color_history_title_outline, 0, 0), (1, citydom_color_shadow, 0, 1) ]
    kerning 13

style citydom_history_name_text is default:
    font citydom_dialogue_font_name
    size 14
    color citydom_color_history_name
    outlines [ ]
    kerning 4

style citydom_history_body_text is default:
    font citydom_dialogue_font_body
    size 18
    color citydom_color_history_body
    outlines [ (1, citydom_color_shadow, 0, 1) ]
    line_spacing 4

style citydom_history_empty_text is citydom_history_body_text:
    color citydom_color_history_empty
    text_align 0.5

style citydom_history_narration_text is default:
    font citydom_dialogue_font_ui
    size 16
    color citydom_color_history_narration
    outlines [ ]
    kerning 5
    text_align 0.5

style citydom_history_footer_button is button:
    xsize 92
    ysize 46
    background None
    hover_background Frame(citydom_ui_asset("history_footer_button_hover"), 8, 8, 8, 8)
    padding (0, 0, 0, 0)

style citydom_history_footer_button_text is button_text:
    font citydom_dialogue_font_ui
    size 10
    color citydom_color_history_footer
    hover_color citydom_color_primary
    outlines [ ]
    kerning 1
    xalign 0.5
    yalign 0.5

style new_ui_choice_button is button:
    xsize 500
    ysize 56
    background Frame(citydom_ui_asset("choice_glass_idle"), 6, 6, 6, 6)
    hover_background Frame(citydom_ui_asset("choice_glass_hover"), 6, 6, 6, 6)
    padding (0, 0, 0, 0)

style new_ui_choice_button_text is button_text:
    font citydom_dialogue_font_ui
    size 20
    color citydom_color_text_muted
    hover_color citydom_color_text_bright
    selected_color citydom_color_text_bright
    xalign 0.0
    yalign 0.5
    xoffset 28
    outlines [ (1, citydom_color_shadow, 0, 1) ]

transform citydom_dialogue_panel_show:
    subpixel True
    alpha 0.0
    yoffset 16
    warp citydom_hud_curve 0.40 alpha 1.0 yoffset 0

transform citydom_dialogue_engine_text_hidden:
    alpha 0.0

transform citydom_choice_button_show(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset 6
    pause delay
    warp citydom_hud_curve 0.26 alpha 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.16 xoffset 3
    on idle:
        warp citydom_hud_curve 0.16 xoffset 0
