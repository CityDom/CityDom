screen BioClassScreen():
    if not is_bio_class_hour() and is_day_hour(calendar.Hours):
        add "SchoolSubplace/BioClass empty.png"
    elif is_bio_class_hour():
        add "SchoolSubplace/BioClass.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "BioClass/Isa_Criss_Helena_idle.png"
                hover "BioClass/Isa_Criss_Helena_hover.png"
                xpos 1570
                ypos 374
                action [Hide("BioClassScreen"), Jump("BioClass_IsaCrissHelena_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Selina_Greta_idle.png"
                hover "BioClass/Selina_Greta_hover.png"
                xpos 1116
                ypos 422
                action [Hide("BioClassScreen"), Jump("BioClass_Selina_Greta_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Dorothy_idle.png"
                hover "BioClass/Dorothy_hover.png"
                xpos 743
                ypos 590
                action [Hide("BioClassScreen"), Jump("BioClass_Dorothy_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Lola_Leya_idle.png"
                hover "BioClass/Lola_Leya_hover.png"
                xpos 211
                ypos 387
                action [Hide("BioClassScreen"), Jump("BioClass_Lola_Leya_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Anna_Emma_idle.png"
                hover "BioClass/Anna_Emma_hover.png"
                xpos 485
                ypos 420
                action [Hide("BioClassScreen"), Jump("BioClass_Anna_Emma_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Sophie_Alis_idle.png"
                hover "BioClass/Sophie_Alis_hover.png"
                xpos 549
                ypos 284
                action [Hide("BioClassScreen"), Jump("BioClass_Sophie_Alis_Scene")]
                focus_mask True
            imagebutton:
                idle "BioClass/Maria_idle.png"
                hover "BioClass/Maria_hover.png"
                xpos 863
                ypos 363
                action [Hide("BioClassScreen"), Jump("BioClass_Maria_Scene")]
                focus_mask True
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 690
                ypos 290
                action [Hide("BioClassScreen"), Jump("BioClass_During_Class_Scene")]
                at ClassRoomButtonLookDown
                focus_mask True
    else:
        add "SchoolSubplace/BioClass evening.png"