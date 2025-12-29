screen ArtClassScreen():
    # if not school_clock.IsBreak and school_clock.hour == 12 and school_clock.period == 1:
    #     add "SchoolSubplace/ArtClass.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             idle "SchoolCharButtons/ArtTeacherButton_idle.png"
    #             hover "SchoolCharButtons/ArtTeacherButton_hover.png"
    #             xpos 936
    #             ypos 228
    #             action Function(show_work_in_progress)
    if is_art_class_hour():
        add "ArtClass/ArtClass.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 950
                ypos 550
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "DuringArtClassScene")
                at ClassRoomButtonLookDown
                focus_mask True
            imagebutton:
                idle "ArtClass/Maria_idle.png"
                hover "ArtClass/Maria_hover.png"
                xpos 725
                ypos 512
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_Maria_Scene")
                focus_mask True
            imagebutton:
                idle "ArtClass/Isa_Criss_idle.png"
                hover "ArtClass/Isa_Criss_hover.png"
                xpos 1190
                ypos 173
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_IsabellaCriss_Scene")
                focus_mask True
            imagebutton:
                idle "ArtClass/Emma_Anna_idle.png"
                hover "ArtClass/Emma_Anna_hover.png"
                xpos 330
                ypos 240
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_AnnaEmma_Scene")
                focus_mask True
            imagebutton:
                idle "ArtClass/Sophie_Alis_idle.png"
                hover "ArtClass/Sophie_Alis_hover.png"
                xpos 606
                ypos 120
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_SophieAlis_Scene")
                focus_mask True
            imagebutton:
                idle "ArtClass/Lola_Leya_Dorothy_Helena_idle.png"
                hover "ArtClass/Lola_Leya_Dorothy_Helena_hover.png"
                xpos 1518
                ypos 199
                action Function(show_work_in_progress)
                focus_mask True
            imagebutton:
                idle "ArtClass/Selina_Greta_idle.png"
                hover "ArtClass/Selina_Greta_hover.png"
                xpos 48
                ypos 343
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_SelinaGreta_Scene")
                focus_mask True
            imagebutton:
                idle "ArtClass/Scarlet_idle.png"
                hover "ArtClass/Scarlet_hover.png"
                xpos 997
                ypos 114
                action Function(start_event_from_screen, "ArtClass/ArtClass.png", "ArtClass_Scarlet_Scene")
                focus_mask True
    else:
        add "SchoolSubplace/ArtClass.png"
        # if not MapScreenShown and not StatsScreenShown:
        #     if school_clock.period == 3:
        #         imagebutton:
        #             idle "ArtClass/backroom_door_idle.png"
        #             hover "ArtClass/backroom_door_hover.png"
        #             xpos 1443
        #             ypos 23
        #             action [Hide("ArtClassScreen"), Jump("AfterArtClassScene")]
        #     else:
        #         imagebutton:
        #             idle "ArtClass/backroom_door_idle.png"
        #             hover "ArtClass/backroom_door_hover.png"
        #             xpos 1443
        #             ypos 23
        #             action Function(show_work_in_progress)
