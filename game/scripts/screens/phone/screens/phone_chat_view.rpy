screen Conversation_screen():
    default yadj = ui.adjustment()
    default chat_yadj = ui.adjustment()
    default previous_range = 0.0

    $ conversations = get_conversations()
    $ selected_valid = selected_chat in conversations

    if not selected_valid:
        frame:
            xpos 1550 ypos 100 background "ChatBackscreen.png"
            text "No chat selected" xpos 20 ypos 25 color "#FFFFFF" size 25
            imagebutton:
                xpos 280 ypos 30 idle "back_idle.png"
                action [
                    Function(set_typing_state, False),
                    Function(clear_typing_state),
                    SetVariable("selected_chat", ""),
                    SetVariable("Messanger", True),
                    SetVariable("ShowConversationScreen", False)
                ]
    else:
        $ messages = conversations.get(selected_chat, [])
        $ conversation_length = len(messages)
        $ current_index = current_message.get(selected_chat, 0)
        $ max_messages = min(current_index + 1, conversation_length)
        $ has_next_message = current_index < conversation_length - 1
        $ is_image_or_emoji = is_next_right_image_or_emoji(messages, current_index) if has_next_message else False
        $ auto_advance = setup_auto_advance(selected_chat)

        frame:
            xpos 1550 ypos 100 background "ChatBackscreen.png"
            
            hbox:
                xpos 15 ypos 25
                imagebutton: 
                    idle im.AlphaMask(im.Scale("MessangerIcons/ChatImage_{}_Idle.png".format(selected_chat), 60, 60), im.Scale("circle_mask.png", 60, 60))
                    action Function(handleBackgroundPreview, selected_chat)
                text selected_chat color "#FFFFFF" size 25 xpos 10 ypos 10

            viewport:
                id "message_viewport"
                yadjustment yadj
                yinitial 1.0
                xpos 9 ypos 100 draggable True mousewheel True area (9, 150, 330, 510)
                vbox:
                    id "message_container" spacing 20
                    
                    python:
                        was_at_bottom = yadj.value + yadj.page >= yadj.range

                    for i in range(max_messages):
                        $ message = messages[i]
                        $ speaker = message.get('speaker', 'left')
                        $ is_left = speaker == 'left'
                        $ xpos_val = 10 if is_left else (250 if 'emoji' in message else 90 if 'image' in message else 300)
                        
                        hbox:
                            xpos xpos_val
                            if 'text' in message and not is_left:
                                xalign 1.0
                            
                            if 'emoji' in message:
                                text message['emoji'] size 50
                            elif 'image' in message:
                                imagebutton:
                                    idle im.Scale(message['image'], 200, 120)
                                    action NullAction()
                            elif 'text' in message:
                                frame:
                                    if not is_left:
                                        xalign 1.0
                                    background Frame("left_bubble.png" if is_left else "right_bubble.png", 10, 10, 10, 10)
                                    text message['text'] size 17 xmaximum 230

                    if typing_indicator and selected_chat == delay_selected_chat:
                        hbox xpos 10:
                            frame background Frame("left_bubble.png", 10, 10, 10, 10):
                                text "Typing..." at typing_anim size 17 xmaximum 230 color "#BBBBBB"

                    if not has_next_message:
                        hbox xpos 80:
                            frame background Frame("left_bubble.png", 10, 10, 10, 10):
                                text "No messages left" size 17 xmaximum 230 color "#BBBBBB"

                    null height 50

                    python:
                        if was_at_bottom and yadj.range > previous_range:
                            yadj.value = float('inf')
                        previous_range = yadj.range

            if auto_advance['should_setup']:
                timer auto_advance['delay'] action auto_advance['actions'] repeat True

            if not is_image_or_emoji:
                $ typebar_image = "rounded_typebar.png" if len(displayed_text) <= char_limit_per_line else "rounded_taller_typebar.png"
                add typebar_image xpos 9 ypos 618

                frame:
                    xpos 20 ypos 625 background None area (0, 0, 230, 44)
                    viewport id "chat_viewport" xpos 0 ypos -5 draggable True mousewheel True yadjustment chat_yadj yinitial 0.0 area (0, 0, 230, 46):
                        vbox spacing 5:
                            if displayed_text == "" and has_next_message:
                                text "Type your message" size 20 color "#BBBBBB" line_leading 0 xmaximum 230 ypos -2
                            else:
                                text "[displayed_text]" size 20 color "#FFFFFF" line_leading 0 xmaximum 230 ypos -2
                            
                            python:
                                lines = (len(displayed_text) // char_limit_per_line) + 1 if displayed_text else 1
                                if lines > 2:
                                    chat_yadj.value = float('inf')
                                else:
                                    chat_yadj.value = 0

                imagebutton:
                    xpos 245 ypos 605
                    idle ("SendMessageButton_idle.png" if (message_complete and has_next_message) else "SendMessageButtonDisabled_idle.png")
                    action If(message_complete and has_next_message, [Function(reset_typing), Function(renpy.restart_interaction)], NullAction())

                for key in typing_keys:
                    key key action Function(advance_typing_message)
                key "K_RETURN" action If((message_complete and has_next_message) or is_image_or_emoji, [Function(reset_typing), Function(renpy.restart_interaction)])

            if is_image_or_emoji:
                imagebutton:
                    idle "SendMessageButton_idle.png" xpos 245 ypos 605
                    action [Function(reset_typing), SetVariable("message_complete", True), Function(renpy.restart_interaction)]

            imagebutton:
                xpos 280 ypos 30 idle "back_idle.png"
                action [
                    Function(set_typing_state, False),
                    Function(clear_typing_state),
                    SetVariable("selected_chat", ""), 
                    SetVariable("Messanger", True), 
                    SetVariable("ShowConversationScreen", False)
                ]

transform typing_anim:
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat
