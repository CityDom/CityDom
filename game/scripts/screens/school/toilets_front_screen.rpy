screen ToiletsFrontScreen():
    if (not school_clock.IsBreak and school_clock.period < 11) or school_clock.period == 7 or school_clock.period == 9:
        add "SchoolSubplace/ToiletsFront1.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/GirlsToiletsDoor_idle.png"
                hover "SchoolDoors/GirlsToiletsDoor_hover.png"
                xpos 928
                ypos 237
                action [Return("WomansToilet"), Hide("SchoolEntranceScreen")]
            imagebutton:
                idle "SchoolDoors/BoysToiletsDoor_idle.png"
                hover "SchoolDoors/BoysToiletsDoor_hover.png"
                xpos 297
                ypos 240
                action [Return("MansToilet"), Hide("SchoolEntranceScreen")]
            imagebutton:
                auto "MoveRightArrow_%s.png"
                xpos 1760
                ypos 500
                action [Return("SchoolEntrance"), Hide("SchoolEntranceScreen")]
                at buttonScale
    elif school_clock.IsBreak and school_clock.hour < 15 and school_clock.period < 7:
        add "SchoolSubplace/ToiletsFront1.png"
        imagebutton:
            idle "SchoolFirstPause/SelinaEventScene/Selina_Button_idle.png"
            hover "SchoolFirstPause/SelinaEventScene/Selina_Button_hover.png"
            xpos 488
            ypos 370
            action Function(start_event_from_screen, "SchoolSubplace/ToiletsFront1.png", "SelinaFirstPauseScene")
            focus_mask True
        imagebutton:
            idle "SchoolDoors/GirlsToiletsDoor_idle.png"
            hover "SchoolDoors/GirlsToiletsDoor_hover.png"
            xpos 928
            ypos 237
            action [Return("WomansToilet"), Hide("SchoolEntranceScreen")]
        imagebutton:
            idle "SchoolDoors/BoysToiletsDoor_idle.png"
            hover "SchoolDoors/BoysToiletsDoor_hover.png"
            xpos 297
            ypos 240
            action [Return("MansToilet"), Hide("SchoolEntranceScreen")]
        imagebutton:
            auto "MoveRightArrow_%s.png"
            xpos 1760
            ypos 500
            action [Return("SchoolEntrance"), Hide("SchoolEntranceScreen")]
            at buttonScale
    else:
        add "SchoolSubplace/ToiletsFront evening.png"
