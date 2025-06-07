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
            action [Hide("MainClassroomScreen"), Jump("DetentionClass_Sandra_Scene")]
            focus_mask True

        imagebutton:
            idle "DetentionClass/DetentionClass_Maria_Button_idle.png"
            hover "DetentionClass/DetentionClass_Maria_Button_hover.png"
            xpos 1376
            ypos 408
            action [Hide("MainClassroomScreen"), Jump("DetentionClass_Maria_Scene")]
            focus_mask True
        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos 1050
            ypos 350
            action [Hide("MainClassroomScreen"), Jump("DetentionClass_Scene")]
            at rootateDown
            focus_mask True
    elif is_english_class_hour():
        add "SchoolSubplace/MainClassroom.png"

        imagebutton:
            idle "ClassRoomButtons/JanniceButton_idle.png"
            hover "ClassRoomButtons/JanniceButton_hover.png"
            xpos 1272
            ypos 483
            action [Hide("MainClassroomScreen"), Jump("JanniceClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/DorothyButton_idle.png"
            hover "ClassRoomButtons/DorothyButton_hover.png"
            xpos 340
            ypos 367
            action [Hide("MainClassroomScreen"), Jump("DorothyClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/HelenaButton_idle.png"
            hover "ClassRoomButtons/HelenaButton_hover.png"
            xpos 557
            ypos 276
            action [Hide("MainClassroomScreen"), Jump("HelenaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/AlisButton_idle.png"
            hover "ClassRoomButtons/AlisButton_hover.png"
            xpos 336
            ypos 215
            action [Hide("MainClassroomScreen"), Jump("AlisClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/SophieButton_idle.png"
            hover "ClassRoomButtons/SophieButton_hover.png"
            xpos 538
            ypos 232
            action [Hide("MainClassroomScreen"), Jump("SophieClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/AnnaEmmaButton_idle.png"
            hover "ClassRoomButtons/AnnaEmmaButton_hover.png"
            xpos 255
            ypos 165
            action [Hide("MainClassroomScreen"), Jump("AnnaEmmaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/SelinaButton_idle.png"
            hover "ClassRoomButtons/SelinaButton_hover.png"
            xpos 1035
            ypos 305
            action [Hide("MainClassroomScreen"), Jump("SelinaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/GretaButton_idle.png"
            hover "ClassRoomButtons/GretaButton_hover.png"
            xpos 1205
            ypos 270
            action [Hide("MainClassroomScreen"), Jump("GretaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/LeyaButton_idle.png"
            hover "ClassRoomButtons/LeyaButton_hover.png"
            xpos 865
            ypos 190
            action [Hide("MainClassroomScreen"), Jump("LeyaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/LolaButton_idle.png"
            hover "ClassRoomButtons/LolaButton_hover.png"
            xpos 1047
            ypos 173
            action [Hide("MainClassroomScreen"), Jump("LolaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/IsabellaButton_idle.png"
            hover "ClassRoomButtons/IsabellaButton_hover.png"
            xpos 767
            ypos 136
            action [Hide("MainClassroomScreen"), Jump("IsabellaClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/CrissButton_idle.png"
            hover "ClassRoomButtons/CrissButton_hover.png"
            xpos 913
            ypos 97
            action [Hide("MainClassroomScreen"), Jump("CrissClassroomScene")]
            focus_mask True

        imagebutton:
            idle "ClassRoomButtons/MariaButton_idle.png"
            hover "ClassRoomButtons/MariaButton_hover.png"
            xpos 832
            ypos 130
            action [Hide("MainClassroomScreen"), Jump("MariaClassroomScene")]
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
            hover "ClassRoomButtons/GretaButton_hover.png"
            xpos 1205
            ypos 270
            action [Hide("MainClassroomScreen"), Jump("GretaFirstPauseScene")]
            focus_mask True

    elif school_clock.period < 11:
        add "SchoolSubplace/MainClassroom.png"
    else:
        add "SchoolSubplace/MainClassroom evening1.png"
    # if 16 <= calendar.Hours <= 24:
    #     add "SchoolSubplace/MainClassroom night.png"
transform ClassRoomButtonLookDown:
    rotate 45
    on hover:
        linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
    on idle:
        linear 0.1 zoom 1.0
