# Shared state for phone screens.

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

default selected_chat = ""
default chat_names = ["Jennifer", "Isabella", "Claire"]
default current_message = {name: 0 for name in chat_names}

# Character selection tabs.
default characters_tab1 = ["Jennifer", "Isabella", "Claire", "Maria", "Alis", "Sophie", "Lola", "Selina", "Helena", "Dorothy", "Leya", "Greta", "Jannice", "Criss"]
default characters_tab2 = ["Luna", "Asako", "Angeline", "Scarlet", "Tanya", "Anna", "Emma"]
default current_char_tab = 1

# Stats/overview toggles.
default ShowCharOverviewScreen = False
default CharacterSelectionIsShowing = False
default selected_character = "Jennifer"

# Schedule toggle.
default is_weekend_schedule = False
