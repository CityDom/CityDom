default citydom_call_panel_opening = False
default citydom_call_panel_closing = False

init python:
    CITYDOM_CALL_PANEL_ITEMS = (
        {
            "name": "Mhyrorin",
            "icon": "CallToMeImages/Mhyrorin_CallToMeIcon_idle.png",
            "action": Jump("MhyrorinCallToMeDialog"),
        },
        {
            "name": "Isabella",
            "icon": "CallToMeImages/Isabella_CallToMeIcon_idle.png",
            "action": Jump("IsabellaCallToMeDialog"),
        },
        {
            "name": "Jennifer",
            "icon": "CallToMeImages/Jennifer_CallToMeIcon_idle.png",
            "action": Jump("JenniferCallToMeDialog"),
        },
        {
            "name": "Claire",
            "icon": "CallToMeImages/Claire_CallToMeIcon_idle.png",
            "action": Jump("ClaireCallToMeDialog"),
        },
    )

    CITYDOM_CALL_PANEL_X = 1920 - 20 - 88
    CITYDOM_CALL_PANEL_Y = 20 + 44 + 12
    CITYDOM_CALL_AVATAR_SIZE = 64

    def citydom_call_panel_start_open():
        store.citydom_call_panel_opening = True
        store.citydom_call_panel_closing = False
        store.set_hud_panels(ShowCallForSidebar=True)
        renpy.restart_interaction()

    def citydom_call_panel_start_close():
        if not store.ShowCallForSidebar:
            return
        store.citydom_call_panel_opening = False
        store.citydom_call_panel_closing = True
        renpy.restart_interaction()

    def citydom_call_panel_finish_open():
        store.citydom_call_panel_opening = False
        renpy.restart_interaction()

    def citydom_call_panel_finish_hide():
        store.ShowCallForSidebar = False
        store.citydom_call_panel_closing = False
        renpy.restart_interaction()

    def citydom_call_panel_toggle():
        if store.citydom_call_panel_closing:
            return
        if store.ShowCallForSidebar:
            citydom_call_panel_start_close()
        else:
            citydom_call_panel_start_open()

transform citydom_call_panel_show:
    subpixel True
    alpha 0.0
    yoffset -22
    pause 0.04
    warp citydom_hud_curve 0.42 alpha 1.0 yoffset 0

transform citydom_call_panel_static:
    subpixel True
    alpha 1.0
    yoffset 0

transform citydom_call_panel_hide:
    subpixel True
    alpha 1.0
    yoffset 0
    pause 0.20
    warp citydom_hud_curve 0.30 alpha 0.0 yoffset -18

transform citydom_call_avatar_show(index=0):
    subpixel True
    alpha 0.0
    zoom 0.74
    yoffset -28
    pause 0.10 + (index * 0.075)
    warp citydom_hud_curve 0.38 alpha 1.0 zoom 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.16 zoom 1.08
    on idle:
        warp citydom_hud_curve 0.16 zoom 1.0

transform citydom_call_avatar_static:
    subpixel True
    alpha 1.0
    zoom 1.0
    yoffset 0
    on hover:
        warp citydom_hud_curve 0.16 zoom 1.08
    on idle:
        warp citydom_hud_curve 0.16 zoom 1.0

transform citydom_call_avatar_hide(index=0, count=1):
    subpixel True
    alpha 1.0
    zoom 1.0
    yoffset 0
    pause (count - index - 1) * 0.06
    warp citydom_hud_curve 0.32 alpha 0.0 zoom 0.82 yoffset -28

style citydom_call_name_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 9
    color "#ff9df8"
    outlines [ (1, "#7d1bb366", 0, 0) ]
    kerning 3

screen citydom_call_avatar(item, index):
    default _is_hovered = False
    $ _x = CITYDOM_CALL_PANEL_X + 12
    $ _y = CITYDOM_CALL_PANEL_Y + 16 + (index * 80)
    $ _idle = Composite((CITYDOM_CALL_AVATAR_SIZE, CITYDOM_CALL_AVATAR_SIZE), (0, 0), Transform(item["icon"], xysize=(CITYDOM_CALL_AVATAR_SIZE, CITYDOM_CALL_AVATAR_SIZE)), (0, 0), "gui/citydom_ui_v2/hud_call_avatar_idle.png")
    $ _hover = Composite((CITYDOM_CALL_AVATAR_SIZE, CITYDOM_CALL_AVATAR_SIZE), (0, 0), Transform(item["icon"], xysize=(CITYDOM_CALL_AVATAR_SIZE, CITYDOM_CALL_AVATAR_SIZE)), (0, 0), "gui/citydom_ui_v2/hud_call_avatar_hover.png")

    imagebutton:
        idle _idle
        hover _hover
        xpos _x
        ypos _y
        if citydom_call_panel_opening:
            at citydom_call_avatar_show(index)
        elif citydom_call_panel_closing:
            at citydom_call_avatar_hide(index, len(CITYDOM_CALL_PANEL_ITEMS))
        else:
            at citydom_call_avatar_static
        focus_mask True
        hovered SetScreenVariable("_is_hovered", True)
        unhovered SetScreenVariable("_is_hovered", False)
        action item["action"]

    if _is_hovered:
        fixed:
            xpos _x - 136
            ypos _y + 18
            xysize (126, 28)
            at citydom_call_label_show

            add "gui/citydom_ui_v2/hud_call_name_tag.png"
            text item["name"].upper():
                xalign 0.5
                yalign 0.5
                style "citydom_call_name_text"

transform citydom_call_label_show:
    subpixel True
    alpha 0.0
    xoffset 6
    easeout 0.12 alpha 1.0 xoffset 0

screen sidebar_screen():
    if citydom_call_panel_opening:
        timer 0.72 action Function(citydom_call_panel_finish_open)

    if citydom_call_panel_closing:
        timer 0.72 action Function(citydom_call_panel_finish_hide)

    fixed:
        xpos CITYDOM_CALL_PANEL_X
        ypos CITYDOM_CALL_PANEL_Y
        xysize (88, 344)
        if citydom_call_panel_opening:
            at citydom_call_panel_show
        elif citydom_call_panel_closing:
            at citydom_call_panel_hide
        else:
            at citydom_call_panel_static

        add "gui/citydom_ui_v2/hud_call_panel_bg.png"

    for index, item in enumerate(CITYDOM_CALL_PANEL_ITEMS):
        use citydom_call_avatar(item, index)
