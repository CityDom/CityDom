init:
    # Define a transform that rotates an image by 45 degrees
    transform rotateUpRight:
        rotate -30
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0
    transform rootateDown:
        rotate -270
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0
    transform bump:
        on hover:
            linear 0.1 zoom 1.1 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0

screen ArtClassFrontScreen():
    if (not school_clock.IsBreak and school_clock.period < 11) or school_clock.period == 7 or school_clock.period == 9:
        add "SchoolSubplace/ArtClassFront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 1750
                ypos 700
                action [Return("MedicRoomFront"), Hide("ArtClassFrontScreen")]
                at rotateUpRight
            imagebutton:
                idle "SchoolDoors/ArtClassDoor_idle.png"
                hover "SchoolDoors/ArtClassDoor_hover.png"
                xpos 1622
                ypos 318
                action [Return("ArtClass"), Hide("ArtClassScreen")]
            imagebutton:
                idle "SchoolDoors/ClassRoomDoor_idle.png"
                hover "SchoolDoors/ClassRoomDoor_hover.png"
                xpos 39
                ypos 230
                action [Return("MainClassroom"), Hide("SchoolEntranceScreen")]
    elif are_girls_in_break():
        add "SchoolFirstPause/HelenaAndSophieEventScene/HelenaAndSophieScreen.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 1750
                ypos 700
                action [Return("MedicRoomFront"), Hide("ArtClassFrontScreen")]
                at rotateUpRight
            imagebutton:
                idle "SchoolDoors/ArtClassDoor_idle.png"
                hover "SchoolDoors/ArtClassDoor_hover.png"
                xpos 1622
                ypos 318
                action [Return("ArtClass"), Hide("ArtClassScreen")]
            imagebutton:
                idle "SchoolDoors/ClassRoomDoor_idle.png"
                hover "SchoolDoors/ClassRoomDoor_hover.png"
                xpos 39
                ypos 230
                action [Return("MainClassroom"), Hide("SchoolEntranceScreen")]
            imagebutton:
                idle "SchoolFirstPause/HelenaAndSophieEventScene/SophieAndHelenaButton_idle.png"
                hover "SchoolFirstPause/HelenaAndSophieEventScene/SophieAndHelenaButton_hover.png"
                xpos 1065
                ypos 379
                action Function(start_event_from_screen, "SchoolFirstPause/HelenaAndSophieEventScene/HelenaAndSophieScreen.png", "HelenaAndSophieFirstPauseScene")
                focus_mask True
