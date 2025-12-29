screen SchoolGymFrontScreen():

    if (not school_clock.IsBreak and school_clock.period < 11) or school_clock.period == 7 or school_clock.period == 9:
        add "SchoolSubplace/SchoolGymFront.png"
        imagebutton:
            idle "SchoolDoors/GymRoomDoor_idle.png"
            hover "SchoolDoors/GymRoomDoor_hover.png"
            xpos 881
            ypos 269
            action [Return("InsideSchoolGym"), Hide("SchoolGymFrontScreen")]
        imagebutton:
            auto "MoveRightArrow_%s.png"
            xpos 1760
            ypos 400
            action [Return("BackYard"), Hide("SchoolGymFrontScreen")]
            at rotateUpRight
        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos -40
            ypos 400
            action [Return("schoolpool"), Hide("SchoolGymFrontScreen")]
            at rotate_upLeft
    elif school_clock.IsBreak and school_clock.hour < 15 and school_clock.period < 7:
        add "SchoolFirstPause/LolaAndDorothyEventScene/SchoolGymFront_LolaAndDorothy.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/GymRoomDoor_idle.png"
                hover "SchoolDoors/GymRoomDoor_hover.png"
                xpos 881
                ypos 269
                action [Return("InsideSchoolGym"), Hide("SchoolGymFrontScreen")]
            imagebutton:
                auto "MoveRightArrow_%s.png"
                xpos 1760
                ypos 400
                action [Return("backyard"), Hide("SchoolGymFrontScreen")]
                at rotateUpRight
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos -40
                ypos 400
                action [Return("schoolpool"), Hide("SchoolGymFrontScreen")]
                at rotate_upLeft
            imagebutton:
                idle "SchoolFirstPause/LolaAndDorothyEventScene/LolaAndDorothyButton_idle.png"
                hover "SchoolFirstPause/LolaAndDorothyEventScene/LolaAndDorothyButton_hover.png"
                xpos 210
                ypos 350
                action Function(start_event_from_screen, "SchoolFirstPause/LolaAndDorothyEventScene/SchoolGymFront_LolaAndDorothy.png", "LolaAndDorothyFirstPauseScene")
                focus_mask True
    else:
        add "SchoolSubplace/SchoolGymFront evening.png"
