init 1 python:
    def is_weekend_day(day):
        return int(day) in (0, 6)

    def is_weekday_day(day):
        return not is_weekend_day(day)

    def select_room_scene(hour, events, day_bg, evening_bg, night_bg):
        if hour in events:
            return events[hour]
        if hour < EVENING_START_HOUR:
            return {"bg": day_bg}
        if hour < NIGHT_BG_START_HOUR:
            return {"bg": evening_bg}
        return {"bg": night_bg}

    def get_scene_buttons(scene_def):
        if not scene_def:
            return ()
        if scene_def.get("buttons"):
            return tuple(scene_def["buttons"])
        button = scene_def.get("button")
        return (button,) if button else ()

    def resolve_scene_button_action(button_def, default_bg):
        if "action" in button_def:
            return button_def["action"]
        if "return_to" in button_def:
            actions = []
            if button_def.get("hide_screen"):
                actions.append(Hide(button_def["hide_screen"]))
            actions.append(Return(button_def["return_to"]))
            return actions

        scene_bg = button_def.get("bg", default_bg)
        label = button_def.get("jump")

        if label is None and button_def.get("choices") and button_def.get("history_key"):
            label = choose_scene_with_history(button_def["history_key"], button_def["choices"])

        return Function(start_event_from_screen, scene_bg, label)


screen room_scene_buttons(scene_def):
    for button in get_scene_buttons(scene_def):
        imagebutton:
            idle button["idle"]
            hover button["hover"]
            xpos button["xpos"]
            ypos button["ypos"]
            action resolve_scene_button_action(button, scene_def.get("bg"))
            focus_mask button.get("focus_mask", True)
