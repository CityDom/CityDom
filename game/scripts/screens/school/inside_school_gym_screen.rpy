screen InsideSchoolGymScreen():
    if (school_clock.period == 8 and (calendar.Day == 1 or calendar.Day == 3 or calendar.Day == 5) and Watched_FirstTime_GymClass == False):
        add "SchoolSubplace/InsideSchoolGym.png"
        imagebutton:
            idle "SchoolDoors/GymDoor_idle.png"
            hover "SchoolDoors/GymDoor_hover.png"
            xpos 206
            ypos 219
            action [Hide("InsideSchoolGymScreen"), Jump("FirstTimeGym_Scene")]
            focus_mask True
        imagebutton:
            auto "MoveRightArrow_%s.png"
            xpos 1400
            ypos 300
            action [Return("GymLockerRoomFront"), Hide("InsideSchoolGymScreen")]
            at rotateUpRight
    elif 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/InsideSchoolGym.png"
        imagebutton:
            idle "SchoolDoors/GymDoor_idle.png"
            hover "SchoolDoors/GymDoor_hover.png"
            xpos 206
            ypos 219
            action [Return("Gym"), Hide("InsideSchoolGymScreen")]
            focus_mask True
        imagebutton:
            auto "MoveRightArrow_%s.png"
            xpos 1400
            ypos 300
            action [Return("GymLockerRoomFront"), Hide("InsideSchoolGymScreen")]
            at rotateUpRight
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/InsideSchoolGym evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/InsideSchoolGym night.png"