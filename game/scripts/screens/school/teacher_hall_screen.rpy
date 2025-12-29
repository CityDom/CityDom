screen TeacherHallScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/TeacherHall.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/TeachersToiletDoor_idle.png"
                hover "SchoolDoors/TeachersToiletDoor_hover.png"
                xpos 301
                ypos 292
                action [Return("TeachersBathroom"), Hide("TeacherHallScreen")]
            imagebutton:
                idle "SchoolDoors/PrincipalDoor_idle.png"
                hover "SchoolDoors/PrincipalDoor_hover.png"
                xpos 875
                ypos 392
                action Function(start_event_from_screen, "SchoolSubplace/TeacherHall.png", "PrincipalOffice")
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/TeacherHall evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/TeachersToiletDoor_idle.png"
                hover "SchoolDoors/TeachersToiletDoor_hover.png"
                xpos 301
                ypos 292
                action [Return("TeachersBathroom"), Hide("TeacherHallScreen")]
            imagebutton:
                idle "SchoolDoors/PrincipalDoor_idle.png"
                hover "SchoolDoors/PrincipalDoor_hover.png"
                xpos 875
                ypos 392
                action Function(start_event_from_screen, "SchoolSubplace/TeacherHall evening.png", "PrincipalOffice")
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/TeacherHall night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/TeachersToiletDoor_idle.png"
                hover "SchoolDoors/TeachersToiletDoor_hover.png"
                xpos 301
                ypos 292
                action [Return("TeachersBathroom"), Hide("TeacherHallScreen")]
            imagebutton:
                idle "SchoolDoors/PrincipalDoor_idle.png"
                hover "SchoolDoors/PrincipalDoor_hover.png"
                xpos 875
                ypos 392
                action Function(start_event_from_screen, "SchoolSubplace/TeacherHall night.png", "PrincipalOffice")
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]
