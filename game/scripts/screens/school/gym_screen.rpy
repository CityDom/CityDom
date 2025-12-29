screen GymScreen():
    if is_gym_swim_class_hour() and (calendar.Day == 1 or calendar.Day == 3 or calendar.Day == 5):
        add "SchoolSubplace/Gym.png"
        imagebutton:
            idle "GymClass/Isa_Team_Button_idle.png"
            hover "GymClass/Isa_Team_Button_hover.png"
            xpos 1267
            ypos 302
            action Function(start_event_from_screen, "SchoolSubplace/Gym.png", "Isa_Team_Scene")
            focus_mask True
        imagebutton:
            idle "GymClass/Lola_Team_Button_idle.png"
            hover "GymClass/Lola_Team_Button_hover.png"
            xpos 162
            ypos 372
            action Function(start_event_from_screen, "SchoolSubplace/Gym.png", "Lola_Team_Scene")
            focus_mask True
        imagebutton:
            idle "GymClass/Tanya_Button_idle.png"
            hover "GymClass/Tanya_Button_hover.png"
            xpos 898
            ypos 116
            action Function(start_event_from_screen, "SchoolSubplace/Gym.png", "GymClass_Tanya")
            focus_mask True
        imagebutton:
            auto "MoveRightArrow_%s.png"
            xpos 898
            ypos 600
            action Function(show_work_in_progress)
            at rootateDown
    elif is_day_hour(calendar.Hours):
        add "SchoolSubplace/Gym empty.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/Gym evening.png"
