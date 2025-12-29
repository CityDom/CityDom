screen GymLockerRoomFrontScreen():
    if is_before_gym_swim_class() and (calendar.Day == 1 or calendar.Day == 3 or calendar.Day == 5):
        add "SchoolSubplace/GymLockerRoomFront.png"
        imagebutton:
            idle "SchoolDoors/GirlsLockerRoomDoor_idle.png"
            hover "SchoolDoors/GirlsLockerRoomDoor_hover.png"
            xpos 1248
            ypos 152
            action Function(start_event_from_screen, "SchoolSubplace/GymLockerRoomFront.png", "BeforeGymClass_Scene")
            focus_mask True
    elif is_day_hour(calendar.Hours):
        add "SchoolSubplace/GymLockerRoomFront.png"
        imagebutton:
            idle "SchoolDoors/GirlsLockerRoomDoor_idle.png"
            hover "SchoolDoors/GirlsLockerRoomDoor_hover.png"
            xpos 1248
            ypos 152
            action [Return("GirlsLockerRoom"), Hide("GymLockerRoomFrontScreen")]
            focus_mask True
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/GymLockerRoomFront evening.png"
