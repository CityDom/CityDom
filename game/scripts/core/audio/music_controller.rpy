default music_loop_fade = 1.0
default music_loop_volume_floor = 0.3
default music_loop_fading_out = False
default music_loop_last_pos = 0.0
default music_loop_track = None
default music_afternoon_hour = 8  # 2 PM
default music_night_hour = 12  # 6 PM

init python:
    MUSIC_TRACKS = {
        0: "audio/music_morning_looped.ogg",
        1: "audio/music_afternoon_looped.ogg",
        2: "audio/music_night_looped.ogg",
    }

    def _is_main_menu():
        if getattr(store, "force_music_in_tests", False):
            return False
        try:
            if renpy.context()._main_menu:
                return True
        except Exception:
            pass
        try:
            return bool(store.main_menu)
        except Exception:
            return False

    def _get_time_music_track():
        if _is_main_menu():
            return None
        try:
            hour = store.calendar.Hours
        except Exception:
            hour = 0
        if hour < store.music_afternoon_hour:
            return MUSIC_TRACKS[0]
        if hour < store.music_night_hour:
            return MUSIC_TRACKS[1]
        return MUSIC_TRACKS[2]

    def _update_music_loop(track):
        if not track:
            return
        if renpy.music.get_playing("music") != track:
            return
        duration = renpy.music.get_duration("music")
        pos = renpy.music.get_pos("music")
        if not duration or pos is None:
            return
        if pos < store.music_loop_last_pos:
            store.music_loop_fading_out = False
            renpy.music.set_volume(1.0, delay=store.music_loop_fade, channel="music")
        store.music_loop_last_pos = pos
        remaining = duration - pos
        if (not store.music_loop_fading_out) and remaining <= store.music_loop_fade:
            store.music_loop_fading_out = True
            renpy.music.set_volume(store.music_loop_volume_floor, delay=remaining, channel="music")

    def _ensure_background_music():
        desired = _get_time_music_track()
        current = renpy.music.get_playing("music")
        tracked = store.music_loop_track
        if desired is None:
            if current:
                renpy.music.stop(channel="music", fadeout=1.0)
            store.music_loop_track = None
            store.music_loop_fading_out = False
            store.music_loop_last_pos = 0.0
            return
        if tracked != desired or current != desired:
            store.music_loop_track = desired
            store.music_loop_fading_out = False
            store.music_loop_last_pos = 0.0
            renpy.music.set_volume(1.0, delay=0, channel="music")
            renpy.music.play(desired, channel="music", loop=True, fadein=1.0, fadeout=1.0)
            return
        _update_music_loop(desired)

    if not hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks = []
    if _ensure_background_music not in config.after_load_callbacks:
        config.after_load_callbacks.append(_ensure_background_music)

    if "music" not in config.main_menu_stop_channels:
        config.main_menu_stop_channels.append("music")
