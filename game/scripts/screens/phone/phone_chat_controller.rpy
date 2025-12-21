init python:
    import renpy.ui as ui

    typing_keys = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "K_SPACE", "K_BACKSPACE"
    ]

    char_limit_per_line = 21

    def get_conversations():
        return renpy.store.conversations

    def sync_chat_state():
        names = list(renpy.store.conversations.keys())
        renpy.store.chat_names = names
        for name in names:
            if name not in renpy.store.current_message:
                renpy.store.current_message[name] = 0
        for name in list(renpy.store.current_message.keys()):
            if name not in names:
                del renpy.store.current_message[name]

    def get_chat_names():
        sync_chat_state()
        return list(renpy.store.chat_names)

    def update_current_message():
        sync_chat_state()

    def commit_chat_progress():
        if renpy.in_rollback():
            return
        renpy.retain_after_load()
        renpy.checkpoint()

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

        commit_chat_progress()

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
        if current_index >= len(messages) - 1:
            renpy.store.message_complete = True
            renpy.store.message_in_progress = False
            renpy.store.typing_indicator = False
            return
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
        current_index = renpy.store.current_message.get(selected_chat, 0)
        if current_index >= len(messages) - 1 or renpy.store.message_in_progress:
            return {"should_setup": False}
        next_message = messages[current_index + 1]
        if next_message.get("speaker") == "left":
            if "emoji" in next_message or "image" in next_message:
                delay = 2.0
            else:
                delay = calculate_delay(next_message.get("text", ""))
            set_typing_state(True, selected_chat)
            actions = [Function(handle_message_advance, selected_chat), Function(renpy.restart_interaction)]
            return {"should_setup": True, "delay": delay, "actions": actions}
        return {"should_setup": False}

    def is_next_right_image_or_emoji(messages, current_index):
        if current_index < len(messages) - 1:
            next_message = messages[current_index + 1]
            return next_message.get("speaker") == "right" and ("emoji" in next_message or "image" in next_message)
        return False

    def truncate_message(text, max_length=20):
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text

    def reset_current_message(chat_name):
        if chat_name in renpy.store.conversations:
            renpy.store.current_message[chat_name] = min(
                renpy.store.current_message[chat_name],
                len(renpy.store.conversations[chat_name]) - 1
            )
        else:
            print(f"[Warning] Attempted to reset current_message for invalid chat: {chat_name}")

    def _ensure_chat(chat_name):
        if chat_name not in renpy.store.conversations:
            renpy.store.conversations[chat_name] = []
        sync_chat_state()

    def add_chat(chat_name, initial_messages=None):
        _ensure_chat(chat_name)
        if initial_messages:
            renpy.store.conversations[chat_name].extend(initial_messages)
            commit_chat_progress()

    def append_chat_messages(chat_name, messages):
        if not messages:
            return
        _ensure_chat(chat_name)
        renpy.store.conversations[chat_name].extend(messages)
        commit_chat_progress()

    def Maria_ScarletPhoto_Lingerie():
        append_chat_messages("Maria", maria_scarlet_photo_lingerie_messages())

    def Maria_ScarletPhoto_Naked():
        append_chat_messages("Maria", maria_scarlet_photo_naked_messages())

    def Maria_AddToGroupChat():
        append_chat_messages("Maria", maria_add_to_group_chat_messages())
