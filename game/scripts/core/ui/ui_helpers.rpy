
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

screen event_imagebutton(idle, hover, xpos, ypos, bg, label, focus_mask=True):
    imagebutton:
        idle idle
        hover hover
        xpos xpos
        ypos ypos
        action Function(start_event_from_screen, bg, label)
        if focus_mask is not None:
            focus_mask focus_mask
