screen MedicRoomFrontScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/MedicRoomFront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/MedicRoomDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/SchoolLibraryDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/BioClassDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/MedicRoomFront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/MedicRoomDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/SchoolLibraryDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/BioClassDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/MedicRoomFront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/MedicRoomDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/SchoolLibraryDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover make_tinted_hover_displayable("SchoolDoors/BioClassDoor_idle.png", OBJECT_HOVER_TINT)
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True