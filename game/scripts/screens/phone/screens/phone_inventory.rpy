default citydom_inventory_closing = False

init python:
    CITYDOM_INVENTORY_TOTAL_SLOTS = 32
    CITYDOM_INVENTORY_SAMPLE_ITEMS = ()

    def citydom_inventory_back_to_phone():
        store.ShowPhone = True
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_home_returning = True
        store.citydom_inventory_closing = True
        renpy.restart_interaction()

    def citydom_inventory_finish_close():
        store.ShowInventory = False
        store.citydom_inventory_closing = False
        renpy.restart_interaction()

transform citydom_inventory_screen_show:
    subpixel True
    alpha 0.0
    xoffset 340
    warp citydom_hud_curve 0.32 alpha 1.0 xoffset 0

transform citydom_inventory_screen_hide:
    subpixel True
    alpha 1.0
    xoffset 0
    warp citydom_hud_curve 0.30 alpha 0.0 xoffset 340

transform citydom_inventory_slot_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        yoffset 10
        pause 0.06 + (index * 0.012)
        warp citydom_hud_curve 0.22 alpha 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.14 zoom 1.06 yoffset -2
    on idle:
        warp citydom_hud_curve 0.14 zoom 1.0 yoffset 0

style citydom_inventory_title_text is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 16
    color "#ffe6fb"
    outlines [ (1, "#ff5bd680", 0, 0) ]
    kerning 4

style citydom_inventory_count_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 8
    color "#ff8df8bf"
    outlines [ ]
    kerning 2

screen citydom_inventory_slot(index):
    $ _col = index % 4
    $ _row = index // 4
    $ _x = 4 + (_col * 74)
    $ _y = _row * 74
    $ _filled = index < len(CITYDOM_INVENTORY_SAMPLE_ITEMS)
    $ _image = "gui/citydom_ui_v2/%s" % CITYDOM_INVENTORY_SAMPLE_ITEMS[index] if _filled else "gui/citydom_ui_v2/phone_inventory_empty_slot.png"

    imagebutton:
        idle _image
        hover _image
        xpos _x
        ypos _y
        at citydom_inventory_slot_motion(index)
        action NullAction()

screen inventory_screen():
    if citydom_inventory_closing:
        timer 0.32 action Function(citydom_inventory_finish_close)

    if not ShowPhone:
        fixed:
            at citydom_phone_overlay_static
            add "gui/citydom_ui_v2/phone_overlay_dim.png"

    fixed:
        xpos CITYDOM_PHONE_X + (CITYDOM_PHONE_W // 2)
        ypos CITYDOM_PHONE_Y + (CITYDOM_PHONE_H // 2)
        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
        at citydom_phone_frame_static

        viewport:
            xpos 0
            ypos 0
            xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
            draggable False
            mousewheel False
            scrollbars None
            child_size (CITYDOM_PHONE_W, CITYDOM_PHONE_H)

            fixed:
                xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                if citydom_inventory_closing:
                    at citydom_inventory_screen_hide
                else:
                    at citydom_inventory_screen_show

                add "gui/citydom_ui_v2/phone_inventory_bg.png"

                imagebutton:
                    idle "gui/citydom_ui_v2/phone_inventory_back_idle.png"
                    hover "gui/citydom_ui_v2/phone_inventory_back_hover.png"
                    xpos 20
                    ypos 54
                    action Function(citydom_inventory_back_to_phone)

                text _("Inventory"):
                    xcenter 170
                    ypos 56
                    style "citydom_inventory_title_text"

                text "%d / %d ITEMS" % (len(CITYDOM_INVENTORY_SAMPLE_ITEMS), CITYDOM_INVENTORY_TOTAL_SLOTS):
                    xcenter 170
                    ypos 80
                    style "citydom_inventory_count_text"

                add "gui/citydom_ui_v2/chain_divider_phone.png":
                    xcenter 170
                    ypos 112

                viewport:
                    xpos 20
                    ypos 142
                    xysize (300, 500)
                    mousewheel True
                    draggable True
                    scrollbars None

                    fixed:
                        xysize (300, 584)

                        for index in range(CITYDOM_INVENTORY_TOTAL_SLOTS):
                            use citydom_inventory_slot(index)

        add "gui/citydom_ui_v2/phone_dynamic_island.png":
            xpos 126
            ypos 14

        add "gui/citydom_ui_v2/phone_status_pill.png":
            xpos 20
            ypos 8

        text citydom_phone_time_text():
            xpos 31
            ypos 13
            style "citydom_phone_status_text"

        add "gui/citydom_ui_v2/phone_status_icons_pill.png":
            xpos 248
            ypos 8
