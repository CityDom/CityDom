screen NurseRoomScreen():
    if school_clock.period == 6 or school_clock.period == 7:
        add "SchoolSubplace/NurseRoom empty.png"
    elif 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/NurseRoom.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/SchoolMedicButton_idle.png"
                hover "SchoolCharButtons/SchoolMedicButton_hover.png"
                xpos 1023
                ypos 302
                action [Hide("NurseRoomScreen"), Jump("NurseScene")]
                focus_mask True
    else:
        add "SchoolSubplace/NurseRoom evening.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             idle "SchoolCharButtons/SchoolMedicButton_idle.png"
    #             hover "SchoolCharButtons/SchoolMedicButton_hover.png"
    #             xpos 900
    #             ypos 226
    #             action Function(show_work_in_progress)
    # # if 16 <= calendar.Hours <= 24:
    #     add "SchoolSubplace/NurseRoom night.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             idle "SchoolCharButtons/SchoolMedicButton_idle.png"
    #             hover "SchoolCharButtons/SchoolMedicButton_hover.png"
    #             xpos 900
    #             ypos 226
    #             action Function(show_work_in_progress)
