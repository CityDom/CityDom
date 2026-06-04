default citydom_memory_trace_enabled = True
default citydom_memory_trace_interval = 60.0

init 5 python:
    import os
    import time

    _citydom_memory_trace_last_at = 0.0

    def _citydom_process_memory_mb():
        try:
            import ctypes
            from ctypes import wintypes

            class PROCESS_MEMORY_COUNTERS_EX(ctypes.Structure):
                _fields_ = [
                    ("cb", wintypes.DWORD),
                    ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t),
                    ("PrivateUsage", ctypes.c_size_t),
                ]

            counters = PROCESS_MEMORY_COUNTERS_EX()
            counters.cb = ctypes.sizeof(PROCESS_MEMORY_COUNTERS_EX)
            process = ctypes.windll.kernel32.GetCurrentProcess()
            ok = ctypes.windll.psapi.GetProcessMemoryInfo(
                process,
                ctypes.byref(counters),
                counters.cb,
            )

            if not ok:
                return None

            return {
                "rss": counters.WorkingSetSize / 1048576.0,
                "private": counters.PrivateUsage / 1048576.0,
                "peak_rss": counters.PeakWorkingSetSize / 1048576.0,
            }
        except Exception:
            return None

    def _citydom_image_cache_stats():
        try:
            cache = renpy.display.im.cache
            total_mb = cache.get_total_size() * 4.0 / 1048576.0
            limit_mb = getattr(cache, "cache_limit", 0) * 4.0 / 1048576.0
            entries = len(getattr(cache, "cache", {}))
            preloads = len(getattr(cache, "preloads", ()))
            renders = len(cache.get_renders())
            return total_mb, limit_mb, entries, preloads, renders
        except Exception:
            return None, None, None, None, None

    def _citydom_visible_panels():
        names = (
            "ShowPhone",
            "ShowInventory",
            "showWallpaperScreen",
            "ShowConversationScreen",
            "ShowCalendarScreen",
            "Messanger",
            "showWallpaperPreview",
            "ShowCallForSidebar",
            "StatsScreenShown",
            "MapScreenShown",
        )
        return ",".join([name for name in names if getattr(store, name, False)]) or "none"

    def citydom_memory_trace(reason="timer", force=False):
        global _citydom_memory_trace_last_at

        if not getattr(store, "citydom_memory_trace_enabled", True):
            return

        now = time.time()
        interval = float(getattr(store, "citydom_memory_trace_interval", 60.0) or 60.0)
        if not force and now - _citydom_memory_trace_last_at < interval:
            return
        _citydom_memory_trace_last_at = now

        memory = _citydom_process_memory_mb() or {}
        cache_mb, cache_limit_mb, cache_entries, cache_preloads, cache_renders = _citydom_image_cache_stats()
        calendar_obj = getattr(store, "calendar", None)

        renpy.log(
            "CITYDOM_MEMORY_TRACE reason=%s pid=%s rss_mb=%.1f private_mb=%.1f peak_rss_mb=%.1f "
            "image_cache_mb=%s image_cache_limit_mb=%s image_cache_entries=%s image_preloads=%s image_renders=%s "
            "day=%s hour=%s period=%s location=%r location_img=%r panels=%s selected_character=%r"
            % (
                reason,
                os.getpid(),
                memory.get("rss", -1.0),
                memory.get("private", -1.0),
                memory.get("peak_rss", -1.0),
                "%.1f" % cache_mb if cache_mb is not None else "unknown",
                "%.1f" % cache_limit_mb if cache_limit_mb is not None else "unknown",
                cache_entries if cache_entries is not None else "unknown",
                cache_preloads if cache_preloads is not None else "unknown",
                cache_renders if cache_renders is not None else "unknown",
                getattr(calendar_obj, "Day", "unknown"),
                getattr(calendar_obj, "Hours", "unknown"),
                getattr(calendar_obj, "period_index", "unknown"),
                getattr(store, "Location", "unknown"),
                getattr(store, "Location_img", "unknown"),
                _citydom_visible_panels(),
                getattr(store, "selected_character", "unknown"),
            )
        )

    if "citydom_memory_trace_timer" not in config.overlay_screens:
        config.overlay_screens.append("citydom_memory_trace_timer")

screen citydom_memory_trace_timer():
    if citydom_memory_trace_enabled:
        timer citydom_memory_trace_interval repeat True action Function(citydom_memory_trace, "timer")
