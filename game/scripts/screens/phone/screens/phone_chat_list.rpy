default citydom_messages_closing = False
default citydom_chat_closing = False

init python:
    CITYDOM_MESSAGE_CONTACT_COLORS = {
        "Jennifer": "#e8798c",
        "Isabella": "#788cff",
        "Claire": "#50dc8c",
        "Maria": "#e879dc",
        "Carmen": "#f0aa5a",
    }

    def citydom_message_contact_accent(name):
        return CITYDOM_MESSAGE_CONTACT_COLORS.get(name, "#c084d4")

    def citydom_message_avatar_displayable(name, size):
        prefix = "phone_chat_avatar_final" if size <= 48 else "phone_message_avatar_final"
        path = "gui/citydom_ui_v2/%s_%s.png" % (prefix, name)
        if not renpy.loadable(path):
            path = "gui/citydom_ui_v2/%s_Isabella.png" % prefix
        return path

    def citydom_message_preview_for(name, conversations, current_message):
        messages = conversations.get(name, [])
        if not messages:
            return "No messages yet"

        index = min(current_message.get(name, 0), len(messages) - 1)
        message = messages[index]
        if message.get("text") is not None:
            return truncate_message(message.get("text", ""), 36)
        if message.get("image") is not None:
            return "Image"
        if message.get("emoji") is not None:
            return "Emoji"
        return "No messages yet"

    def citydom_messages_back_to_phone():
        store.ShowPhone = True
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_home_returning = True
        store.citydom_messages_closing = True
        renpy.restart_interaction()

    def citydom_messages_finish_close():
        store.Messanger = False
        store.ShowConversationScreen = False
        store.citydom_messages_closing = False
        store.citydom_chat_closing = False
        store.selected_chat = ""
        renpy.restart_interaction()

    def citydom_open_chat(name):
        store.selected_chat = name
        store.ShowConversationScreen = True
        store.citydom_chat_closing = False
        renpy.restart_interaction()

    def citydom_chat_back_to_messages():
        store.citydom_chat_closing = True
        set_typing_state(False)
        clear_typing_state()
        renpy.restart_interaction()

    def citydom_chat_finish_close():
        store.ShowConversationScreen = False
        store.citydom_chat_closing = False
        store.selected_chat = ""
        renpy.restart_interaction()

transform citydom_messages_screen_show:
    subpixel True
    alpha 0.0
    xoffset 340
    warp citydom_hud_curve 0.32 alpha 1.0 xoffset 0

transform citydom_messages_screen_hide:
    subpixel True
    alpha 1.0
    xoffset 0
    warp citydom_hud_curve 0.30 alpha 0.0 xoffset 340

transform citydom_message_row_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        xoffset -16
        pause 0.06 + (index * 0.055)
        warp citydom_hud_curve 0.24 alpha 1.0 xoffset 0
    on hover:
        warp citydom_hud_curve 0.14 xoffset 4
    on idle:
        warp citydom_hud_curve 0.14 xoffset 0

transform citydom_chat_screen_show:
    subpixel True
    alpha 0.0
    xoffset 340
    warp citydom_hud_curve 0.28 alpha 1.0 xoffset 0

transform citydom_chat_screen_hide:
    subpixel True
    alpha 1.0
    xoffset 0
    warp citydom_hud_curve 0.26 alpha 0.0 xoffset 340

transform citydom_chat_bubble_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        yoffset 10
        zoom 0.96
        pause min(index, 8) * 0.04
        warp citydom_hud_curve 0.20 alpha 1.0 yoffset 0 zoom 1.0

style citydom_messages_title_text is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 16
    color "#ffe6fb"
    outlines [ (1, "#ff5bd680", 0, 0) ]
    kerning 4

style citydom_messages_subtitle_text is citydom_inventory_count_text

style citydom_message_name_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 15
    color "#efd5ff"
    outlines [ ]
    kerning 1

style citydom_message_preview_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 10
    color "#a67ccc"
    outlines [ ]

style citydom_message_time_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 8
    color "#8d65b399"
    outlines [ ]

style citydom_message_initial_text is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 18
    color "#f3c8ff"
    outlines [ (1, "#ff5bd660", 0, 0) ]

screen citydom_phone_status_layer():
    add "gui/citydom_ui_v2/phone_frame_overlay.png"

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

screen citydom_message_contact_row(name, conversations, current_message, index):
    $ _preview = citydom_message_preview_for(name, conversations, current_message)

    button:
        xpos 20
        ypos index * 78
        xysize (300, 76)
        background "gui/citydom_ui_v2/phone_message_row_idle.png"
        hover_background "gui/citydom_ui_v2/phone_message_row_hover.png"
        at citydom_message_row_motion(index)
        action Function(citydom_open_chat, name)

        add citydom_message_avatar_displayable(name, 68):
            xpos -4
            ypos 2

        text name:
            xpos 78
            ypos 15
            xsize 160
            style "citydom_message_name_text"

        text _preview:
            xpos 78
            ypos 39
            xsize 170
            style "citydom_message_preview_text"

        text "Now":
            xpos 250
            ypos 17
            xsize 40
            text_align 1.0
            style "citydom_message_time_text"

screen Messanger_screen():
    $ chat_names = get_chat_names()
    $ conversations = get_conversations()

    if citydom_messages_closing:
        timer 0.32 action Function(citydom_messages_finish_close)

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
                if citydom_messages_closing:
                    at citydom_messages_screen_hide
                else:
                    at citydom_messages_screen_show

                add AlphaMask("gui/citydom_ui_v2/phone_messages_bg.png", "gui/citydom_ui_v2/phone_rounded_mask.png")

                button:
                    xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                    background None
                    hover_background None
                    action NullAction()

                imagebutton:
                    idle "gui/citydom_ui_v2/phone_inventory_back_idle.png"
                    hover "gui/citydom_ui_v2/phone_inventory_back_hover.png"
                    xpos 20
                    ypos 54
                    action Function(citydom_messages_back_to_phone)

                text _("Chats"):
                    xcenter 170
                    ypos 56
                    style "citydom_messages_title_text"

                text _("%d conversations") % len(chat_names):
                    xcenter 170
                    ypos 80
                    style "citydom_messages_subtitle_text"

                add "gui/citydom_ui_v2/chain_divider_phone.png":
                    xcenter 170
                    ypos 112

                viewport:
                    xpos 0
                    ypos 136
                    xysize (340, 500)
                    draggable True
                    mousewheel True
                    scrollbars None

                    fixed:
                        xysize (340, max(500, len(chat_names) * 78))

                        for index, name in enumerate(chat_names):
                            use citydom_message_contact_row(name, conversations, current_message, index)

        use citydom_phone_status_layer
