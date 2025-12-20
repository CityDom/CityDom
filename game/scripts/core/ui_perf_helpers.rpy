
init python:
    def hud_refresh():
        try:
            renpy.restart_interaction()
        except Exception:
            pass
