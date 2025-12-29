
init python:
    def hud_refresh():
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    def should_show_room_buttons():
        return not (store.MapScreenShown or store.StatsScreenShown)
