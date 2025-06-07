
screen Conversation_screen():
    # Determine if the next right message is an image or emoji
    $ is_image_or_emoji = False
    $ conversation_length = len(get_conversations().get(selected_chat, []))
    if selected_chat in current_message and current_message[selected_chat] < conversation_length - 1:
        $ next_right_message = get_conversations()[selected_chat][current_message[selected_chat] + 1]
        $ is_image_or_emoji = next_right_message.get("speaker") == "right" and ('emoji' in next_right_message or 'image' in next_right_message)
    frame:
        xpos 1550 ypos 100 background "ChatBackscreen.png"
        
        hbox:
            xpos 15 ypos 25
            imagebutton: 
                idle im.AlphaMask(im.Scale("MessangerIcons/ChatImage_{}_Idle.png".format(selected_chat), 60, 60), im.Scale("circle_mask.png", 60, 60))
                action Function(handleBackgroundPreview, selected_chat)
            text selected_chat color "#FFFFFF" size 25 xpos 10 ypos 10

        viewport:
            xpos 9 ypos 100 draggable True mousewheel True area (9, 150, 330, 510)
            vbox:
                id "message_container" spacing 20
                
                if selected_chat not in current_message:
                    $ current_message[selected_chat] = current_message.get(selected_chat, 0)

                # Load messages once
                $ messages = get_conversations().get(selected_chat, [])
                $ max_messages = min(current_message[selected_chat] + 1, len(messages))
                
                for i in range(max_messages):
                    $ message = messages[i]
                    
                    # Check for emoji-only messages (no bubble)
                    if 'emoji' in message:
                        if message['speaker'] == 'left':
                            $ xpos_val = 10
                        else:
                            $ xpos_val = 250  # Adjusted xpos for right-side emoji to move it slightly left
                        hbox:
                            xpos xpos_val
                            text message['emoji'] size 50  # Display emoji-only text larger
                    elif 'image' in message:
                        $ xpos_val = 10 if message['speaker'] == 'left' else 90
                        hbox:
                            xpos xpos_val
                            imagebutton:
                                idle im.Scale(message['image'], 200, 120)
                                action NullAction()
                    elif 'text' in message:
                        if message['speaker'] == 'right':
                            $ xpos_val = 300
                            hbox:
                                xalign 1.0 xpos xpos_val
                                frame:
                                    xalign 1.0
                                    background Frame("right_bubble.png", 10, 10, 10, 10)
                                    text message['text'] size 17 xmaximum 230
                        else:
                            $ xpos_val = 10
                            hbox:
                                xpos xpos_val
                                frame:
                                    background Frame("left_bubble.png", 10, 10, 10, 10)
                                    text message['text'] size 17 xmaximum 230

                # Display "Typing..." bubble if typing indicator is active
                if typing_indicator and selected_chat == delay_selected_chat:
                    hbox:
                        xpos 10
                        frame:
                            background Frame("left_bubble.png", 10, 10, 10, 10)
                            text "Typing..." size 17 xmaximum 230 color "#BBBBBB"

                # Display "No messages left" bubble if at the end of chat
                if current_message[selected_chat] >= len(messages) - 1:
                    hbox:
                        xpos 80
                        frame:
                            background Frame("left_bubble.png", 10, 10, 10, 10)
                            text "No messages left" size 17 xmaximum 230 color "#BBBBBB"

                if current_message[selected_chat] < conversation_length - 1 and not message_in_progress:
                    $ next_message = messages[current_message[selected_chat] + 1]

                    if next_message.get('speaker') == 'left':
                        # Determine the type of the next message
                        if 'emoji' in next_message or 'image' in next_message:
                            $ delay = 2.0  # Fixed delay for emoji or image messages
                        else:
                            $ delay = calculate_delay(next_message.get('text', ''))  # Calculate delay for text messages
                        
                        $ set_typing_state(True, selected_chat)
                        timer delay action Function(handle_message_advance, selected_chat) repeat True
        # Conditionally display the typebar and send button based on the next message type
        if not is_image_or_emoji:
            $ char_limit_per_line = 21
            $ typebar_image = "rounded_typebar.png" if len(displayed_text) <= char_limit_per_line else "rounded_taller_typebar.png"
            add typebar_image xpos 9 ypos 618

            frame:
                xpos 20 ypos 625
                background None
                area (0, 0, 230, 44)  # Fixed area for one or two lines

                viewport id "chat_viewport":
                    xpos 0
                    ypos -5
                    draggable True
                    mousewheel True
                    yinitial 9999
                    area (0, 0, 230, 46)  # Fixed viewport area

                    vbox:
                        spacing 5 
                        if displayed_text == "" and current_message[selected_chat] < len(messages) - 1:
                            text "Type your message" size 20 color "#BBBBBB" line_leading 0 xmaximum 230 ypos -2
                        else:
                            text "[displayed_text]" size 20 color "#FFFFFF" line_leading 0 xmaximum 230 ypos -2
            if message_complete and current_message[selected_chat] < len(messages) - 1:
                # Enable the send button when the message is complete, and there are more messages.
                imagebutton:
                    idle "SendMessageButton_idle.png" xpos 245 ypos 605
                    action Function(reset_typing)
            else:
                # Disable the send button otherwise.
                imagebutton:
                    idle "SendMessageButtonDisabled_idle.png" xpos 245 ypos 605
                    action NullAction()

            # Define key bindings for advancing message in the typebar
            key "a" action Function(advance_typing_message)
            key "b" action Function(advance_typing_message)
            key "c" action Function(advance_typing_message)
            key "d" action Function(advance_typing_message)
            key "e" action Function(advance_typing_message)
            key "f" action Function(advance_typing_message)
            key "g" action Function(advance_typing_message)
            key "h" action Function(advance_typing_message)
            key "i" action Function(advance_typing_message)
            key "j" action Function(advance_typing_message)
            key "k" action Function(advance_typing_message)
            key "l" action Function(advance_typing_message)
            key "m" action Function(advance_typing_message)
            key "n" action Function(advance_typing_message)
            key "o" action Function(advance_typing_message)
            key "p" action Function(advance_typing_message)
            key "q" action Function(advance_typing_message)
            key "r" action Function(advance_typing_message)
            key "s" action Function(advance_typing_message)
            key "t" action Function(advance_typing_message)
            key "u" action Function(advance_typing_message)
            key "v" action Function(advance_typing_message)
            key "w" action Function(advance_typing_message)
            key "x" action Function(advance_typing_message)
            key "y" action Function(advance_typing_message)
            key "z" action Function(advance_typing_message)
            key "0" action Function(advance_typing_message)
            key "1" action Function(advance_typing_message)
            key "2" action Function(advance_typing_message)
            key "3" action Function(advance_typing_message)
            key "4" action Function(advance_typing_message)
            key "5" action Function(advance_typing_message)
            key "6" action Function(advance_typing_message)
            key "7" action Function(advance_typing_message)
            key "8" action Function(advance_typing_message)
            key "9" action Function(advance_typing_message)
            key "K_SPACE" action Function(advance_typing_message)
            key "K_RETURN" action Function(advance_typing_message)
            key "K_BACKSPACE" action Function(advance_typing_message)
            key "K_RETURN" action If(
                (message_complete and current_message[selected_chat] < len(messages) - 1) or is_image_or_emoji,
                Function(reset_typing)
            )

        if is_image_or_emoji:
            imagebutton:
                idle "SendMessageButton_idle.png" xpos 245 ypos 605
                action [Function(reset_typing), SetVariable("message_complete", True)]

        imagebutton:
            xpos 280 ypos 30 idle "back_idle.png"
            action [
                Function(set_typing_state, False),
                Function(clear_typing_state),
                SetVariable("selected_chat", ""), 
                SetVariable("Messanger", True), 
                SetVariable("ShowConversationScreen", False)
            ]

label scroll_chat_viewport:
    $ renpy.scroll("chat_viewport", 1.0, delay=0)
    return