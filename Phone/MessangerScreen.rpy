init python:    
    # Define a function to truncate messages longer than 20 characters
    def truncate_message(text, max_length=20):
        """Truncate the text to a maximum length, appending '...' if it was truncated."""
        if len(text) > max_length:
            return text[:max_length] + "..."
        else:
            return text

    def reset_current_message(chat_name):
        """Reset the current message index for the specified chat."""
        if chat_name in renpy.store.conversations:
            renpy.store.current_message[chat_name] = min(
                renpy.store.current_message[chat_name],
                len(renpy.store.conversations[chat_name]) - 1
            )
        else:
            print(f"[Warning] Attempted to reset current_message for invalid chat: {chat_name}")

screen Messanger_screen():
    frame:
        xpos 1550
        ypos 100
        background "BackgroundsScreen.png"
        vbox:
            xpos 9
            ypos 100
            spacing 20  
            for name in chat_names:
                hbox box_wrap True: 
                    xsize 1000  
                    ysize 50 
                    spacing 20
                    # Using a dynamic index for chat photo, assuming chat_names and photos have a matching order
                    $ chat_index = chat_names.index(name)
                    imagebutton:  
                        idle im.AlphaMask(im.Scale("MessangerIcons/ChatImage_{}_Idle.png".format(name), 80, 80), im.Scale("circle_mask.png", 80, 80))
                        action [
                            SetVariable("selected_chat", name), 
                            SetVariable("ShowConversationScreen", True), 
                            SetVariable("Messanger", False)
                        ]
                    vbox:
                        text name color "#FFFFFF" size 25 
                        if name in conversations and conversations[name]:  # Access conversations by name
                            $ last_loaded_message_index = min(
                                current_message.get(name, 0), len(conversations[name]) - 1
                            )
                            $ last_loaded_message = conversations[name][last_loaded_message_index]
                            if 'text' in last_loaded_message and last_loaded_message['text'] is not None:
                                $ display_text = truncate_message(last_loaded_message['text'])
                                text display_text size 15 color "#FFFFFF"
                            elif 'image' in last_loaded_message and last_loaded_message['image'] is not None:
                                text "Image" size 15 color "#FFFFFF"  # Display a placeholder for image messages

        text "Chats":
            xpos 15
            ypos 25 
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