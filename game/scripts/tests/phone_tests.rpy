testsuite phone_tests:
    description "Phone UI and chat tests."

    before testcase:
        python:
            if not hasattr(renpy.store, "_test_restart_interaction_orig"):
                renpy.store._test_restart_interaction_orig = renpy.restart_interaction
            renpy.restart_interaction = lambda *args, **kwargs: None
        $ renpy.store.selected_chat = ""
        $ renpy.store.displayed_text = ""
        $ renpy.store.message_complete = False
        $ renpy.store.message_in_progress = False
        $ renpy.store.typing_indicator = False
        $ renpy.store.delay_selected_chat = None
        python:
            for name in renpy.store.current_message:
                renpy.store.current_message[name] = 0
        run Hide("Messanger_screen")
        run Hide("Conversation_screen")

    after testcase:
        python:
            if hasattr(renpy.store, "_test_restart_interaction_orig"):
                renpy.restart_interaction = renpy.store._test_restart_interaction_orig
                del renpy.store._test_restart_interaction_orig

    testcase phone_chat_list_shows_chats:
        description "Chat list shows the default chats."
        run Show("Messanger_screen")
        python:
            test_expect(renpy.get_screen("Messanger_screen") is not None,
                "Expected Messanger_screen to be shown.")
            test_expect("Jennifer" in get_chat_names(),
                "Expected Jennifer in chat list.")
            test_expect("Isabella" in get_chat_names(),
                "Expected Isabella in chat list.")
            test_expect("Claire" in get_chat_names(),
                "Expected Claire in chat list.")

    testcase phone_conversation_initial_message:
        description "Conversation screen shows the first message."
        $ renpy.store.selected_chat = "Isabella"
        run Show("Conversation_screen")
        python:
            test_expect(renpy.get_screen("Conversation_screen") is not None,
                "Expected Conversation_screen to be shown.")
            test_expect("Isabella" in renpy.store.conversations,
                "Expected Isabella conversation to exist.")
            test_expect(len(renpy.store.conversations["Isabella"]) > 0,
                "Expected Isabella conversation to have messages.")
            test_expect("big brother" in renpy.store.conversations["Isabella"][0].get("text", ""),
                "Expected Isabella first message to mention 'big brother'.")

    testcase phone_typing_advances_message:
        description "Typing advances the next right-side message."
        $ renpy.store.selected_chat = "Isabella"
        $ renpy.store.current_message["Isabella"] = 0
        $ renpy.store.displayed_text = ""
        $ renpy.store.message_complete = False
        run Show("Conversation_screen")
        python:
            for _ in range(200):
                if renpy.store.message_complete:
                    break
                advance_typing_message()
            test_expect(renpy.store.message_complete,
                "Expected typing to complete the next right-side message.")
            test_expect_equal(renpy.store.displayed_text, "What do u want?",
                "Expected typed text to match the next message.")

    testcase phone_reset_typing_advances_index:
        description "Reset typing advances the current message index."
        $ renpy.store.selected_chat = "Isabella"
        $ renpy.store.current_message["Isabella"] = 0
        run Function(reset_typing)
        python:
            test_expect_equal(renpy.store.current_message["Isabella"], 1,
                "Expected reset_typing to advance current_message by 1.")
