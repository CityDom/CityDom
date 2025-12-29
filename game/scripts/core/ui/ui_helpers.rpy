
init python:
    def hud_refresh():
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    def should_show_room_buttons():
        return not (store.MapScreenShown or store.StatsScreenShown)

    def start_event_from_screen(bg, label):
        if bg:
            try:
                renpy.show("event_bg", what=renpy.display.im.Image(bg), layer="master")
            except Exception:
                pass
        store.hideEventScreens()
        renpy.jump(label)
