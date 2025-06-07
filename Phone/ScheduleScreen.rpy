default is_weekend_schedule = False

init python:
    def toggle_schedule():
        global is_weekend_schedule
        is_weekend_schedule = not is_weekend_schedule

screen ScheduleScreen():
    if is_weekend_schedule:
        add "Schedules/" + selected_character + "ScheduleScreenWeekend.png"
    else:
        add "Schedules/" + selected_character + "Schedule.png"

    imagebutton:
        xpos 1780
        ypos 903
        auto "Arrow_%s.png"
        action Function(toggle_schedule)

    imagebutton:
        xpos 1780
        ypos 1003
        auto "Exit_%s.png"
        action [Hide("ScheduleScreen"),
                SetVariable("StatsButtonsAreActive", True),
                SetVariable("CharacterSelectionIsShowing", True)]