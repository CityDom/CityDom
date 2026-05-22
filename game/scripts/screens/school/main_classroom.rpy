transform transparent_idle:
    alpha 0.0

screen MainClassroomScreen():
    if is_detention_class_hour():
        add "DetentionClass/DetentionClass.png"
        imagebutton:
            idle "DetentionClass/DetentionClass_Sandra_Button_idle.png"
            hover "DetentionClass/DetentionClass_Sandra_Button_hover.png"
            xpos 251
            ypos 157
            action Function(start_event_from_screen, "DetentionClass/DetentionClass.png", "DetentionClass_Sandra_Scene")
            focus_mask True

        imagebutton:
            idle "DetentionClass/DetentionClass_Maria_Button_idle.png"
            hover "DetentionClass/DetentionClass_Maria_Button_hover.png"
            xpos 1376
            ypos 408
            action Function(start_event_from_screen, "DetentionClass/DetentionClass.png", "DetentionClass_Maria_Scene")
            focus_mask True
        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos 1050
            ypos 350
            action Function(start_event_from_screen, "DetentionClass/DetentionClass.png", "DetentionClass_Scene")
            at rootateDown
            focus_mask True
    elif is_english_class_hour():
        add "SchoolSubplace/MainClassroom.png"

        imagebutton:
            idle "ClassRoomButtons/JanniceButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/JanniceButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 1272
            ypos 483
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "JanniceClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/DorothyButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/DorothyButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 340
            ypos 367
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "DorothyClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/HelenaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/HelenaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 557
            ypos 276
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "HelenaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/AlisButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/AlisButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 336
            ypos 215
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "AlisClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/SophieButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/SophieButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 538
            ypos 232
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "SophieClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/AnnaEmmaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/AnnaEmmaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 255
            ypos 165
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "AnnaEmmaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/SelinaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/SelinaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 1035
            ypos 305
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "SelinaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/GretaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/GretaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 1205
            ypos 270
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "GretaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/LeyaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/LeyaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 865
            ypos 190
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "LeyaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/LolaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/LolaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 1047
            ypos 173
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "LolaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/IsabellaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/IsabellaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 767
            ypos 136
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "IsabellaClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/CrissButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/CrissButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 913
            ypos 97
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "CrissClassroomScene")
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/MariaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/MariaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 832
            ypos 130
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "MariaClassroomScene")
            focus_mask True

        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos 580
            ypos 50
            action [Hide("MainClassroomScreen"), Hide("MainHud"), Show("EnglishLessonScreen")]
            at ClassRoomButtonLookDown
            focus_mask True

    elif are_girls_in_break():
        add "SchoolSubplace/MainClassroom.png"
        imagebutton:
            idle "ClassRoomButtons/GretaButton_idle.png"
            hover make_tinted_hover_displayable("ClassRoomButtons/GretaButton_idle.png", CHARACTER_HOVER_TINT)
            xpos 1205
            ypos 270
            action Function(start_event_from_screen, "SchoolSubplace/MainClassroom.png", "GretaFirstPauseScene")
            focus_mask True

    elif school_clock.period < 11:
        add "SchoolSubplace/MainClassroom.png"
    else:
        add "SchoolSubplace/MainClassroom evening1.png"
    # if is_night_hour(calendar.Hours):
    #     add "SchoolSubplace/MainClassroom night.png"
transform ClassRoomButtonLookDown:
    rotate 45
    on hover:
        linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
    on idle:
        linear 0.1 zoom 1.0
