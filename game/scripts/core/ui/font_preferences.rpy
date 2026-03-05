default persistent.selected_game_font = "Chococooky.ttf"

init -1 python:
    AVAILABLE_GAME_FONTS = (
        ("Chococooky", "Chococooky.ttf"),
        ("Arial", "arial.ttf"),
        ("Arial Unicode", "arial_unicode_ms.ttf"),
        ("DejaVu Sans Oblique", "dejavu_sans_oblique.ttf"),
        ("DS-DIGI", "DS-DIGI.TTF"),
    )

    _DEFAULT_GAME_FONT = "Chococooky.ttf"
    _GAME_FONT_PATHS = set(font_path for _, font_path in AVAILABLE_GAME_FONTS)
    _FONT_STYLE_TARGETS = (
        "default",
        "input",
        "gui_text",
        "label_text",
        "prompt_text",
        "say_label",
        "say_dialogue",
        "namebox_label",
        "input_prompt",
        "choice_button_text",
        "quick_button_text",
        "navigation_button_text",
        "page_button_text",
        "slot_button_text",
        "radio_button_text",
        "check_button_text",
        "slider_button_text",
        "help_button_text",
        "confirm_button_text",
        "nvl_button_text",
        "history_text",
        "history_name_text",
        "history_label_text",
        "help_text",
        "help_label_text",
        "main_menu_title",
        "main_menu_version",
        "notify_text",
        "confirm_prompt",
    )

    def _register_font_style_preferences():
        for _, font_path in AVAILABLE_GAME_FONTS:
            for style_name in _FONT_STYLE_TARGETS:
                try:
                    renpy.register_style_preference("game_font", font_path, style_name, "font", font_path)
                except Exception:
                    continue

    def get_selected_game_font():
        selected = getattr(persistent, "selected_game_font", _DEFAULT_GAME_FONT)
        if selected not in _GAME_FONT_PATHS:
            selected = _DEFAULT_GAME_FONT
            persistent.selected_game_font = selected
        return selected

    def is_game_font_selected(font_path):
        return get_selected_game_font() == font_path

    def apply_selected_game_font(restart=False):
        selected = get_selected_game_font()
        changed = gui.text_font != selected

        gui.text_font = selected
        gui.name_text_font = selected
        gui.interface_text_font = selected
        gui.button_text_font = selected
        gui.choice_button_text_font = selected

        if persistent._style_preferences.get("game_font") != selected:
            persistent._style_preferences["game_font"] = selected
            renpy.style.rebuild()

        if restart or changed:
            renpy.restart_interaction()

    def set_game_font(font_path):
        if font_path not in _GAME_FONT_PATHS:
            return
        persistent.selected_game_font = font_path
        renpy.set_style_preference("game_font", font_path)
        apply_selected_game_font(restart=True)

init 1 python:
    _register_font_style_preferences()
    apply_selected_game_font()
