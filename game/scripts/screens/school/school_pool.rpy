screen SchoolPoolScreen():
    if (not school_clock.IsBreak and school_clock.period < 8) or school_clock.period == 9 or school_clock.period == 10:
        add "SchoolSubplace/SchoolPool.png"
    elif is_before_gym_swim_class() and (calendar.Day == 0 or calendar.Day == 2 or calendar.Day == 4 or calendar.Day == 6):
        add "SwimClass/BeforeSwimClass/BeforeSwimClass.webp"
        imagebutton:
            idle "SwimClass/BeforeSwimClass/GirlsButton_idle.png"
            hover "SwimClass/BeforeSwimClass/GirlsButton_hover.png"
            xpos 946
            ypos 250
            action Function(start_event_from_screen, "SwimClass/BeforeSwimClass/BeforeSwimClass.webp", "BeforeSwimClassScene")
            focus_mask True
    elif is_gym_swim_class_hour() and (calendar.Day == 0 or calendar.Day == 2 or calendar.Day == 4 or calendar.Day == 6) and Watched_FirstTime_GymClass == True:
        add "SwimClass/SwimClass.png"
        imagebutton:
            idle "SwimClass/Maria_idle.png"
            hover "SwimClass/Maria_hover.png"
            xpos 1467
            ypos 235
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Maria_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Sophie_Alis_idle.png"
            hover "SwimClass/Sophie_Alis_hover.png"
            xpos 1005
            ypos 234
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Helena_Alis_Sophie_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Selina_Greta_idle.png"
            hover "SwimClass/Selina_Greta_hover.png"
            xpos 378
            ypos 475
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Selina_Greta_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Isa_Criss_idle.png"
            hover "SwimClass/Isa_Criss_hover.png"
            xpos 1715
            ypos 267
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Isabella_Criss_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Emma_Anna_idle.png"
            hover "SwimClass/Emma_Anna_hover.png"
            xpos 1202
            ypos 594
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_AnnaEmma_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Lola_Leya_idle.png"
            hover "SwimClass/Lola_Leya_hover.png"
            xpos 336
            ypos 303
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Lola_Leya_Scene")
            focus_mask True
        imagebutton:
            idle "SwimClass/Dorothy_Roxanne_idle.png"
            hover "SwimClass/Dorothy_Roxanne_hover.png"
            xpos 235
            ypos 96
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Tanya_Dorothy_Scene")
            focus_mask True
        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos 850
            ypos 650
            action Function(start_event_from_screen, "SwimClass/SwimClass.png", "SwimClass_Scene")
            at ClassRoomButtonLookDown
            focus_mask True
    elif is_gym_swim_class_hour() and (calendar.Day == 0 or calendar.Day == 2 or calendar.Day == 4 or calendar.Day == 6) and Watched_FirstTime_GymClass == False:
        add "SchoolSubplace/SchoolPool.png"
        add "FirstGymRequirement.png"
    elif (is_gym_swim_class_hour() or is_before_gym_swim_class()) and not (calendar.Day == 0 or calendar.Day == 2 or calendar.Day == 4 or calendar.Day == 6):
        add "SchoolSubplace/SchoolPool.png"
    elif school_clock.hour < 15 and school_clock.period < 7:
        add "SchoolFirstPause/AnnaAndEmmaEventScene/pool.png"
        imagebutton:
            idle "SchoolFirstPause/AnnaAndEmmaEventScene/AnnaEmma_Button_Idle.png"
            hover "SchoolFirstPause/AnnaAndEmmaEventScene/AnnaEmma_Button_hover.png"
            xpos 1213
            ypos 592
            action Function(start_event_from_screen, "SchoolFirstPause/AnnaAndEmmaEventScene/pool.png", "AnnaAndEmmaFirstPauseScene")
            focus_mask True
    else:
        add "SchoolSubplace/SchoolPool evening.png"
