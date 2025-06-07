# logic_data.rpy

# Default variables — MUST come before init python!
default background_buttons = {
    "DefaultBackground": "BackgroundButton_Default_Idle"
}
default background_previews = {}
default typing_indicator = False
default delay_selected_chat = None
default message_in_progress = False
default displayed_text = ""
default message_complete = False
default typebar_focused = False
default typebar_placeholder = "Type your message"
# default selected_chat = ""
# default current_message = {}R

init python:

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
            if key not in background_buttons:
                background_buttons[key] = "BackgroundButton_Default_Idle"

    def update_current_message():
        for name in get_chat_names():
            if name not in current_message:
                current_message[name] = 0

    def handleBackgroundPreview(chat_name):
        global previewImage, showWallpaperPreview, canDownload, saveAsBackgroundCheck, backFromBackgroundSave

        previews = get_wallpaper_previews()
        background_key = chat_name + "Background"

        button_unlocked = background_buttons.get(background_key, False)
        preview_image = previews.get(chat_name, "")

        previewImage = preview_image if preview_image else "WallpaperPreview_Default.png"

        showWallpaperPreview = True
        canDownload = True
        saveAsBackgroundCheck = False
        backFromBackgroundSave = True

        renpy.store.previewImage = previewImage
        renpy.store.showWallpaperPreview = showWallpaperPreview
        renpy.store.canDownload = canDownload
        renpy.store.saveAsBackgroundCheck = saveAsBackgroundCheck
        renpy.store.backFromBackgroundSave = backFromBackgroundSave

    def clear_typing_state():
        renpy.store.displayed_text = ""
        renpy.store.message_complete = False

    def set_typing_state(is_typing, selected_chat=None):
        renpy.store.typing_indicator = is_typing
        renpy.store.message_in_progress = is_typing
        renpy.store.delay_selected_chat = selected_chat if is_typing else None

    def handle_message_advance(selected_chat, is_player=False):
        current_index = renpy.store.current_message[selected_chat]
        messages = get_conversations().get(selected_chat, [])

        if current_index < len(messages) - 1:
            if is_player and messages[current_index + 1].get("speaker") == "right":
                renpy.store.current_message[selected_chat] += 1
            elif not is_player:
                renpy.store.current_message[selected_chat] += 1
            set_typing_state(False)
        else:
            print(f"[Log] End of chat reached for {selected_chat}")
        
        update_no_messages_state(selected_chat)

    def calculate_delay(message_text):
        typing_speed_chars_per_sec = 7
        delay = len(message_text) / typing_speed_chars_per_sec
        return min(6.0, max(1.0, delay))

    def advance_typing_message():
        selected_chat = renpy.store.selected_chat
        current_index = renpy.store.current_message[selected_chat]
        messages = get_conversations().get(selected_chat, [])

        if renpy.store.message_complete:
            return

        if current_index < len(messages) - 1:
            next_message = messages[current_index + 1]
            if next_message.get("speaker") == "right":
                message_text = next_message["text"]
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
        messages = get_conversations().get(selected_chat, [])
        
        if renpy.store.current_message[selected_chat] >= len(messages) - 1:
            renpy.store.message_in_progress = False
            renpy.store.message_complete = True
            renpy.store.typing_indicator = False
            return
        
        renpy.store.displayed_text = ""
        renpy.store.message_complete = False
        handle_message_advance(selected_chat, is_player=True)

    def update_no_messages_state(selected_chat):
        messages = get_conversations().get(selected_chat, [])
        if renpy.store.current_message[selected_chat] >= len(messages):
            renpy.store.message_complete = True
            renpy.store.message_in_progress = False
            renpy.store.typing_indicator = False
            renpy.restart_interaction()
        else:
            renpy.store.message_complete = False
            renpy.store.typing_indicator = False
