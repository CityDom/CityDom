screen Messanger_screen():
    # Pull data into the screen scope
    $ chat_names = get_chat_names()
    $ conversations = get_conversations()
    $ cur = current_message

    frame:
        xpos 1550
        ypos 100
        background "BackgroundsScreen.png"

        text "Chats" xpos 15 ypos 25 color "#FFFFFF"

        # Scrollable list of chats
        viewport:
            xpos 9
            ypos 100
            draggable True
            mousewheel True
            area (9, 100, 330, 510)

            vbox:
                spacing 12

                for name in chat_names:
                    hbox:
                        spacing 12
                        yminimum 80  # let the 80x80 avatar fit (avoid clipping)

                        imagebutton:
                            idle im.AlphaMask(
                                im.Scale("MessangerIcons/ChatImage_{}_Idle.png".format(name), 80, 80),
                                im.Scale("circle_mask.png", 80, 80)
                            )
                            action [
                                SetVariable("selected_chat", name),
                                SetVariable("ShowConversationScreen", True),
                                SetVariable("Messanger", False)
                            ]

                        vbox:
                            # If your BG is light, switch to color "#000000"
                            text name color "#FFFFFF" size 25

                            $ msgs = conversations.get(name, [])
                            if msgs:
                                $ last_loaded_message_index = min(cur.get(name, 0), len(msgs) - 1)
                                $ last_loaded_message = msgs[last_loaded_message_index]

                                if 'text' in last_loaded_message and last_loaded_message['text'] is not None:
                                    $ display_text = truncate_message(last_loaded_message['text'])
                                    text display_text size 15 color "#CCCCCC"
                                elif 'image' in last_loaded_message and last_loaded_message['image'] is not None:
                                    text "Image" size 15 color "#CCCCCC"
                                elif 'emoji' in last_loaded_message and last_loaded_message['emoji'] is not None:
                                    text last_loaded_message['emoji'] size 20
                            else:
                                text "No messages yet" size 15 color "#777777"

        imagebutton:
            idle "back_idle.png"
            xpos 280
            ypos 30
            action [
                Function(reset_current_message, selected_chat),
                SetVariable("selected_chat", ""),
                SetVariable("Messanger", False),
                SetVariable("ShowPhone", True)
            ]
