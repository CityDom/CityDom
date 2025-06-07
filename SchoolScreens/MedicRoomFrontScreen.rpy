screen MedicRoomFrontScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/MedicRoomFront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover "SchoolDoors/MedicRoomDoor_hover.png"
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover "SchoolDoors/SchoolLibraryDoor_hover.png"
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover "SchoolDoors/BioClassDoor_hover.png"
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/MedicRoomFront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover "SchoolDoors/MedicRoomDoor_hover.png"
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover "SchoolDoors/SchoolLibraryDoor_hover.png"
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover "SchoolDoors/BioClassDoor_hover.png"
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/MedicRoomFront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/MedicRoomDoor_idle.png"
                hover "SchoolDoors/MedicRoomDoor_hover.png"
                xpos 1542
                ypos 294
                action [Return("NurseRoom"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/SchoolLibraryDoor_idle.png"
                hover "SchoolDoors/SchoolLibraryDoor_hover.png"
                xpos 119
                ypos 227
                action [Return("SchoolLibrary"), Hide("MedicRoomFrontScreen")]
            imagebutton:
                idle "SchoolDoors/BioClassDoor_idle.png"
                hover "SchoolDoors/BioClassDoor_hover.png"
                xpos 1357
                ypos 295
                action [Return("BioClass"), Hide("MedicRoomFrontScreen")]
                focus_mask True