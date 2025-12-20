screen TeacherHallScreen():
    if 0 <= calendar.Hours <= 11:
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
                action [Hide("TeacherHallScreen"), Jump("PrincipalOffice")]
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]
    if 12 <= calendar.Hours <= 15:
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
                action [Hide("TeacherHallScreen"), Jump("PrincipalOffice")]
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]
    if 16 <= calendar.Hours <= 24:
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
                action [Hide("TeacherHallScreen"), Jump("PrincipalOffice")]
            imagebutton:
                idle "SchoolDoors/TeachersLoungeDoor_idle.png"
                hover "SchoolDoors/TeachersLoungeDoor_hover.png"
                xpos 1508
                ypos 310
                action [Return("TeachersLounge"), Hide("TeacherHallScreen")]