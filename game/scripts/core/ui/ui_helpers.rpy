
init python:
    CHARACTER_HOVER_TINT = "#ff9ecb"
    OBJECT_HOVER_TINT = "#ffd966"
    DEFAULT_HOVER_TINT_ALPHA = 0.28
    CHARACTER_HOVER_PREFIXES = (
        "HouseScreens/",
        "ScenesScreens/",
        "ClassRoomButtons/",
        "ArtClass/",
        "BioClass/",
        "SwimClass/",
        "SchoolFirstPause/",
    )
    OBJECT_HOVER_PREFIXES = (
        "SchoolDoors/",
        "TransparentDoors/",
        "MCEvents/HouseButtons/",
    )
    _TINTED_HOVER_CACHE = {}

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

    def make_tinted_hover_displayable(idle, tint=OBJECT_HOVER_TINT, alpha=DEFAULT_HOVER_TINT_ALPHA):
        key = (idle, tint, alpha)
        hover = _TINTED_HOVER_CACHE.get(key)
        if hover is not None:
            return hover

        size = renpy.image_size(idle)
        tint_layer = Transform(
            AlphaMask(Solid(tint, xysize=size), idle),
            alpha=alpha
        )
        hover = Composite(size, (0, 0), idle, (0, 0), tint_layer)
        _TINTED_HOVER_CACHE[key] = hover
        return hover

    def infer_hover_tint(idle):
        if not idle:
            return None
        for prefix in CHARACTER_HOVER_PREFIXES:
            if idle.startswith(prefix):
                return CHARACTER_HOVER_TINT
        for prefix in OBJECT_HOVER_PREFIXES:
            if idle.startswith(prefix):
                return OBJECT_HOVER_TINT
        return None

    def resolve_tinted_button_hover(button_def, default_tint=None):
        if button_def.get("hover_tint"):
            return make_tinted_hover_displayable(
                button_def["idle"],
                button_def.get("hover_tint"),
                button_def.get("hover_tint_alpha", DEFAULT_HOVER_TINT_ALPHA)
            )
        inferred_tint = infer_hover_tint(button_def.get("idle"))
        if inferred_tint:
            return make_tinted_hover_displayable(
                button_def["idle"],
                inferred_tint,
                button_def.get("hover_tint_alpha", DEFAULT_HOVER_TINT_ALPHA)
            )
        if default_tint:
            return make_tinted_hover_displayable(
                button_def["idle"],
                default_tint,
                button_def.get("hover_tint_alpha", DEFAULT_HOVER_TINT_ALPHA)
            )
        return button_def.get("hover", button_def["idle"])

screen event_imagebutton(idle, hover, xpos, ypos, bg, label, focus_mask=True):
    imagebutton:
        idle idle
        hover hover
        xpos xpos
        ypos ypos
        action Function(start_event_from_screen, bg, label)
        if focus_mask is not None:
            focus_mask focus_mask
