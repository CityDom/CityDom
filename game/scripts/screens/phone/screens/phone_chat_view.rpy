style citydom_chat_name_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 14
    color "#efd5ff"
    outlines [ ]
    kerning 1

style citydom_chat_bubble_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 11
    color "#ead8ff"
    outlines [ ]
    line_spacing 2

style citydom_chat_time_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 7
    color "#8d65b370"
    outlines [ ]

style citydom_chat_placeholder_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 12
    color "#d9b9f4cc"
    outlines [ ]

screen citydom_chat_message_bubble(message, index):
    $ _is_left = message.get("speaker", "left") == "left"
    $ _x = 18 if _is_left else 74
    $ _bubble = "gui/citydom_ui_v2/phone_chat_bubble_left.png" if _is_left else "gui/citydom_ui_v2/phone_chat_bubble_right.png"
    $ _align = 0.0 if _is_left else 1.0

    vbox:
        xpos _x
        xsize 248
        spacing 2
        at citydom_chat_bubble_motion(index)

        if message.get("emoji") is not None:
            text message["emoji"]:
                size 34
                xalign _align
        elif message.get("image") is not None:
            imagebutton:
                idle im.Scale(message["image"], 210, 126)
                hover im.Scale(message["image"], 210, 126)
                xalign _align
                action NullAction()
        elif message.get("text") is not None:
            frame:
                xalign _align
                xmaximum 238
                background Frame(_bubble, 18, 18, 18, 18)
                padding (12, 9, 12, 9)

                text message["text"]:
                    xmaximum 208
                    style "citydom_chat_bubble_text"

        text "Now":
            xalign _align
            style "citydom_chat_time_text"

screen Conversation_screen():
    default yadj = ui.adjustment()
    default chat_yadj = ui.adjustment()
    default previous_range = 0.0

    $ conversations = get_conversations()
    $ selected_valid = selected_chat in conversations

    if citydom_chat_closing:
        timer 0.28 action Function(citydom_chat_finish_close)

    if not selected_valid:
        timer 0.01 action Function(citydom_chat_finish_close)

    if selected_valid:
        $ messages = conversations.get(selected_chat, [])
        $ conversation_length = len(messages)
        $ current_index = current_message.get(selected_chat, 0)
        $ max_messages = min(current_index + 1, conversation_length)
        $ has_next_message = current_index < conversation_length - 1
        $ is_image_or_emoji = is_next_right_image_or_emoji(messages, current_index) if has_next_message else False
        $ auto_advance = setup_auto_advance(selected_chat)

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
                    if citydom_chat_closing:
                        at citydom_chat_screen_hide
                    else:
                        at citydom_chat_screen_show

                    add AlphaMask("gui/citydom_ui_v2/phone_chat_bg.png", "gui/citydom_ui_v2/phone_rounded_mask.png")

                    button:
                        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                        background None
                        hover_background None
                        action NullAction()

                    fixed:
                        xpos 0
                        ypos 0
                        xysize (340, 112)

                        imagebutton:
                            idle "gui/citydom_ui_v2/phone_inventory_back_idle.png"
                            hover "gui/citydom_ui_v2/phone_inventory_back_hover.png"
                            xpos 16
                            ypos 54
                            action Function(citydom_chat_back_to_messages)

                        imagebutton:
                            idle citydom_message_avatar_displayable(selected_chat, 48)
                            hover citydom_message_avatar_displayable(selected_chat, 48)
                            xpos 54
                            ypos 44
                            action Function(handleBackgroundPreview, selected_chat)

                        text selected_chat:
                            xpos 124
                            ypos 62
                            xsize 160
                            style "citydom_chat_name_text"

                    add Solid("#c084d41f", xysize=(340, 1)):
                        xpos 0
                        ypos 110

                    viewport:
                        id "message_viewport"
                        yadjustment yadj
                        yinitial 0.0
                        xpos 0
                        ypos 112
                        xysize (340, 478)
                        draggable True
                        mousewheel True
                        scrollbars None

                        vbox:
                            spacing 8
                            xsize 340

                            python:
                                was_at_bottom = yadj.value + yadj.page >= yadj.range

                            null height 8

                            for i in range(max_messages):
                                use citydom_chat_message_bubble(messages[i], i)

                            if typing_indicator and selected_chat == delay_selected_chat:
                                frame:
                                    xpos 18
                                    xmaximum 238
                                    background Frame("gui/citydom_ui_v2/phone_chat_bubble_left.png", 18, 18, 18, 18)
                                    padding (12, 9, 12, 9)
                                    text "Typing..." at typing_anim:
                                        style "citydom_chat_bubble_text"
                                        color "#c9a8e6"

                            if not has_next_message:
                                frame:
                                    xpos 62
                                    xmaximum 216
                                    background Frame("gui/citydom_ui_v2/phone_chat_bubble_left.png", 18, 18, 18, 18)
                                    padding (12, 9, 12, 9)
                                    text "No messages left":
                                        style "citydom_chat_bubble_text"
                                        color "#c9a8e6"

                            null height 18

                            python:
                                if was_at_bottom and yadj.range > previous_range:
                                    try:
                                        yadj.change(float("inf"))
                                    except Exception:
                                        yadj.value = float("inf")
                                previous_range = yadj.range

                    if auto_advance["should_setup"]:
                        timer auto_advance["delay"] action auto_advance["actions"] repeat True

                    fixed:
                        xpos 0
                        ypos 590
                        xysize (340, 90)

                        add Solid("#c084d41f", xysize=(340, 1)):
                            xpos 0
                            ypos 0

                        if not is_image_or_emoji:
                            add "gui/citydom_ui_v2/phone_message_input.png":
                                xpos 18
                                ypos 16

                            viewport:
                                xpos 34
                                ypos 26
                                xysize (220, 28)
                                draggable True
                                mousewheel True
                                yadjustment chat_yadj
                                scrollbars None

                                vbox:
                                    spacing 4
                                    if displayed_text == "" and has_next_message:
                                        text _("Type a message..."):
                                            style "citydom_chat_placeholder_text"
                                    else:
                                        text displayed_text:
                                            style "citydom_chat_bubble_text"
                                            xmaximum 214

                                    python:
                                        lines = (len(displayed_text) // char_limit_per_line) + 1 if displayed_text else 1
                                        if lines > 2:
                                            chat_yadj.value = float("inf")
                                        else:
                                            chat_yadj.value = 0

                            imagebutton:
                                idle ("gui/citydom_ui_v2/phone_message_send_active.png" if (message_complete and has_next_message) else "gui/citydom_ui_v2/phone_message_send_idle.png")
                                hover ("gui/citydom_ui_v2/phone_message_send_active.png" if (message_complete and has_next_message) else "gui/citydom_ui_v2/phone_message_send_idle.png")
                                xpos 282
                                ypos 18
                                action If(message_complete and has_next_message, [Function(reset_typing), Function(renpy.restart_interaction)], NullAction())

                            add ("gui/citydom_ui_v2/phone_message_send_arrow_active.png" if (message_complete and has_next_message) else "gui/citydom_ui_v2/phone_message_send_arrow_idle.png"):
                                xpos 282
                                ypos 18

                            for key in typing_keys:
                                key key action Function(advance_typing_message)
                            key "K_RETURN" action If((message_complete and has_next_message) or is_image_or_emoji, [Function(reset_typing), Function(renpy.restart_interaction)])

                        if is_image_or_emoji:
                            imagebutton:
                                idle "gui/citydom_ui_v2/phone_message_send_active.png"
                                hover "gui/citydom_ui_v2/phone_message_send_active.png"
                                xpos 282
                                ypos 18
                                action [Function(reset_typing), SetVariable("message_complete", True), Function(renpy.restart_interaction)]
                            add "gui/citydom_ui_v2/phone_message_send_arrow_active.png":
                                xpos 282
                                ypos 18

            use citydom_phone_status_layer

transform typing_anim:
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat
