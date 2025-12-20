init python:
    import renpy.ui as ui

    typing_keys = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "K_SPACE", "K_RETURN", "K_BACKSPACE"
    ]

    char_limit_per_line = 21

    def get_conversations():
        return renpy.store.conversations

    def get_chat_names():
        return list(renpy.store.conversations.keys())

    def get_wallpaper_previews():
        return {
            "Default": "WallpaperPreview_Default.png",
            "Jennifer": "WallpaperPreview_Jennifer.png",
            "Isabella": "WallpaperPreview_Isabella.png",
            "Claire": "WallpaperPreview_Claire.png",
            "Mhyrorin": "WallpaperPreview_Mhyrorin.png",
            "Maria": "WallpaperPreview_Maria.png",
            "Scarlet": "WallpaperPreview_Scarlet.png",
            "ScarletLingerie": "WallpaperPreview_Lingerie_Scarlet.png",
        }

    def init_background_buttons():
        for name in get_wallpaper_previews().keys():
            key = name + "Background"
            if key not in renpy.store.background_buttons:
                renpy.store.background_buttons[key] = "BackgroundButton_Default_Idle"

    def update_current_message():
        for name in get_chat_names():
            if name not in renpy.store.current_message:
                renpy.store.current_message[name] = 0

    def handleBackgroundPreview(chat_name):
        previews = get_wallpaper_previews()
        background_key = chat_name + "Background"

        button_unlocked = renpy.store.background_buttons.get(background_key, False)
        preview_image = previews.get(chat_name, "")

        renpy.store.previewImage = preview_image if preview_image else "WallpaperPreview_Default.png"

        renpy.store.showWallpaperPreview = True
        renpy.store.canDownload = True
        renpy.store.saveAsBackgroundCheck = False
        renpy.store.backFromBackgroundSave = True

    def clear_typing_state():
        renpy.store.displayed_text = ""
        renpy.store.message_complete = False

    def set_typing_state(is_typing, selected_chat=None):
        renpy.store.typing_indicator = is_typing
        renpy.store.message_in_progress = is_typing
        renpy.store.delay_selected_chat = selected_chat if is_typing else None

    def handle_message_advance(selected_chat, is_player=False):
        if selected_chat not in get_conversations():
            renpy.notify(f"Invalid chat: {selected_chat}")
            return

        current_index = renpy.store.current_message.get(selected_chat, 0)
        messages = get_conversations().get(selected_chat, [])

        if current_index < len(messages) - 1:
            if is_player and messages[current_index + 1].get("speaker") == "right":
                renpy.store.current_message[selected_chat] += 1
            elif not is_player:
                renpy.store.current_message[selected_chat] += 1
            set_typing_state(False)
        else:
            renpy.log(f"[Log] End of chat reached for {selected_chat}")

        if renpy.store.current_message.get(selected_chat, 0) >= len(messages):
            renpy.store.message_complete = True
            renpy.store.message_in_progress = False
            renpy.store.typing_indicator = False
            renpy.restart_interaction()
        else:
            renpy.store.message_complete = False
            renpy.store.typing_indicator = False

    def calculate_delay(message_text):
        typing_speed_chars_per_sec = 10
        delay = len(message_text) / typing_speed_chars_per_sec
        return min(6.0, max(1.0, delay)) + renpy.random.uniform(-0.5, 0.5)

    def advance_typing_message():
        selected_chat = renpy.store.selected_chat
        if selected_chat not in get_conversations() or renpy.store.message_complete:
            return

        current_index = renpy.store.current_message.get(selected_chat, 0)
        messages = get_conversations().get(selected_chat, [])
        next_message = messages[current_index + 1]
        if next_message.get("speaker") == "right":
            message_text = next_message.get("text", "")
            next_char_index = len(renpy.store.displayed_text)

            if next_char_index < len(message_text):
                renpy.store.displayed_text += message_text[next_char_index]
                lines = renpy.store.displayed_text.splitlines()
                renpy.store.displayed_text = "\n".join(lines[-3:])
                renpy.restart_interaction()
            else:
                renpy.store.message_complete = True

    def reset_typing():
        selected_chat = renpy.store.selected_chat
        if selected_chat not in get_conversations():
            return

        messages = get_conversations().get(selected_chat, [])

        if renpy.store.current_message.get(selected_chat, 0) >= len(messages) - 1:
            renpy.store.message_in_progress = False
            renpy.store.message_complete = True
            renpy.store.typing_indicator = False
            return

        renpy.store.displayed_text = ""
        renpy.store.message_complete = False
        handle_message_advance(selected_chat, is_player=True)

    def setup_auto_advance(selected_chat):
        messages = get_conversations().get(selected_chat, [])
        current_index = current_message.get(selected_chat, 0)
        if current_index >= len(messages) - 1 or renpy.store.message_in_progress:
            return {'should_setup': False}
        next_message = messages[current_index + 1]
        if next_message.get('speaker') == 'left':
            if 'emoji' in next_message or 'image' in next_message:
                delay = 2.0
            else:
                delay = calculate_delay(next_message.get('text', ''))
            set_typing_state(True, selected_chat)
            actions = [Function(handle_message_advance, selected_chat), Function(renpy.restart_interaction)]
            return {'should_setup': True, 'delay': delay, 'actions': actions}
        return {'should_setup': False}

    def is_next_right_image_or_emoji(messages, current_index):
        if current_index < len(messages) - 1:
            next_message = messages[current_index + 1]
            return next_message.get("speaker") == "right" and ('emoji' in next_message or 'image' in next_message)
        return False

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

    def unlockBackground():
        global previewImage

        previewImageFilename = previewImage.split("/")[-1]

        matchedKey = None
        for key, value in get_wallpaper_previews().items():
            if value == previewImageFilename:
                matchedKey = key + "Background"
                break

        if matchedKey:
            background_buttons[matchedKey] = True
            renpy.store.showWallpaperPreview = False
            renpy.store.showWallpaperScreen = True
            renpy.store.canDownload = False
            renpy.redraw(None, 0)
        else:
            renpy.error("Preview image does not match any known backgrounds: " + previewImageFilename)

    def toggle_schedule():
        global is_weekend_schedule
        is_weekend_schedule = not is_weekend_schedule

    def get_field(character, field):
        return renpy.store.__dict__.get("Show{}{}".format(character, field), False)

    def calculate_progress(character):
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)

        total_progress = love + obedience + corruption
        max_progress = 60
        progress_percentage = (total_progress / max_progress) * 100
        return progress_percentage

    def toggle_char_tab():
        global current_char_tab
        if current_char_tab == 1:
            current_char_tab = 2
        else:
            current_char_tab = 1

    def check_and_update_character_stats(character):
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)

        if love > 20:
            renpy.store.__dict__[character + "_love"] = 20
        if obedience > 20:
            renpy.store.__dict__[character + "_Obedience"] = 20
        if corruption > 20:
            renpy.store.__dict__[character + "_Corruption"] = 20

        if love < 0:
            renpy.store.__dict__[character + "_love"] = 0
        if obedience < 0:
            renpy.store.__dict__[character + "_Obedience"] = 0
        if corruption < 0:
            renpy.store.__dict__[character + "_Corruption"] = 0

    def add_chat(name):
        """
        Add a new chat with an empty conversation if it doesn't already exist'
        """
        if name not in renpy.store.conversations:
            renpy.store.conversations[name] = []
        if name not in renpy.store.chat_names:
            renpy.store.chat_names.append(name)
        if name not in renpy.store.current_message:
            renpy.store.current_message[name] = 0

    def Maria_ScarletPhoto_Lingerie():
        """
        Add Maria's Scarlet photo lingerie conversation chunk'
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'left', 'text': 'Just send me that damn image already...'},
            {'speaker': 'right', 'text': 'New phone, who s this?'},
            {'speaker': 'left', 'text': 'Stop playing dumb and send me that shit'},
            {'speaker': 'left', 'text': 'I made that whole scene for nothing...'},
            {'speaker': 'right', 'image': 'images/ArtClass/DuringClass_Scene/DuringArtClass_Scene202.webp'},
            {'speaker': 'left', 'emoji': '{image=noway_face_emoji}'},
            {'speaker': 'left', 'text': 'Wait what'},
            {'speaker': 'right', 'text': 'What?'},
            {'speaker': 'left', 'text': 'How tf did you get such a good shot?'},
            {'speaker': 'left', 'text': 'It looks like you re in there with her'},
            {'speaker': 'right', 'text': 'I have my own secrets'},
            {'speaker': 'left', 'text': '...'},
        ])

    def Maria_ScarletPhoto_Naked():
        """
        Add Maria's Scarlet photo naked conversation chunk'
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'left', 'text': 'Gimme'},
            {'speaker': 'right', 'text': 'What?'},
            {'speaker': 'left', 'text': 'what I worked for'},
            {'speaker': 'right', 'text': 'oh right, mb'},
            {'speaker': 'right', 'image': 'images/ArtClass/DuringClass_Scene/photo.png'},
            {'speaker': 'right', 'text': 'ummmm'},
            {'speaker': 'right', 'text': 'are you still there?'},
            {'speaker': 'right', 'text': 'no reaction at all?'},
            {'speaker': 'left', 'text': '{image=noway_face_emoji}{image=noway_face_emoji}{image=noway_face_emoji}'},
            {'speaker': 'left', 'text': 'Don\'t send this to anyone else'},
            {'speaker': 'left', 'text': 'I\'m pretty sure you can get to prison or some shit like that for this'},
            {'speaker': 'right', 'text': 'Of course I won\'t, you think I\'m dumb?'},
            {'speaker': 'left', 'text': '....'},
            {'speaker': 'left', 'text': 'yes'},
            {'speaker': 'right', 'text': 'So? You didn\'t tell me, do u like the picture?'},
            {'speaker': 'left', 'text': 'hoyl fk, are u stupid? It\'s hot af!'},
            {'speaker': 'left', 'text': 'She did\'t see you, right?'},
            {'speaker': 'right', 'text': 'She did while I was checking out the photo to see that it was alright'},
            {'speaker': 'right', 'text': 'But she doesn\'t know I took it.'},
            {'speaker': 'left', 'text': 'SHE DID?!'},
            {'speaker': 'left', 'text': 'Didn\'t she go nuts on you?'},
            {'speaker': 'right', 'text': 'Ofc she did, but I was just "staying there"'},
            {'speaker': 'right', 'text': 'so it\'s not my fault'},
            {'speaker': 'right', 'text': 'but she started yelling and goingn nuts while still naked, like face to face with me'},
            {'speaker': 'left', 'text': 'WHAT?'},
            {'speaker': 'right', 'text': 'yeah, that\'s what I\'m saying'},
            {'speaker': 'right', 'text': 'she didn\'t even realize we were face to face, she told me to turn around after a bit'},
            {'speaker': 'right', 'text': 'I\'m telling you, that + changing in the room right next to us'},
            {'speaker': 'right', 'text': 'She has to be some kind of nympho'},
            {'speaker': 'left', 'text': 'wtf is a nympho'},
            {'speaker': 'right', 'text': '.....'},
            {'speaker': 'right', 'text': 'ummm, a girl that likes to be naked in public... I think'},
            {'speaker': 'left', 'text': 'hmmm, idk, she might be I guess...'},
            {'speaker': 'left', 'text': 'It is a bit weird to be changing like that, now that I think about it'},
            {'speaker': 'right', 'text': 'What do u say? Do u think we could black mail her with the image?'},
            {'speaker': 'left', 'text': 'Are you fucking stupid? Shut the fuck up!'},
            {'speaker': 'left', 'text': 'Don\'t talk about shit like that in messages'},
            {'speaker': 'right', 'text': 'Geez, ok, chill, you\'re such a scaredy cat'},
            {'speaker': 'left', 'text': 'I gotta go, don\'t do anything dumb with that photo, okay?'},
            {'speaker': 'right', 'text': 'Ummm...'},
            {'speaker': 'left', 'text': '!!!!!!!!!!!!!'},
            {'speaker': 'left', 'text': 'Beat your dick all u want on it, just don\'t share it, UDNERSTOOD?'},
            {'speaker': 'right', 'text': 'Udnerstood, udnerstood'},
            {'speaker': 'left', 'text': '...'},
        ])

    def Maria_AddToGroupChat():
        """
        Add Maria's group chat conversation chunk'
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'right', 'text': 'We are waiting for you!'},
            {'speaker': 'right', 'text': 'Don\'t keep us waiting too long!'},
        ])
