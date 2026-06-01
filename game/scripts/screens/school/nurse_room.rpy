screen NurseRoomScreen():
    if school_clock.period == 6 or school_clock.period == 7:
        add "SchoolSubplace/NurseRoom empty.png"
    elif is_day_hour(calendar.Hours):
        add "SchoolSubplace/NurseRoom.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/SchoolMedicButton_idle.png"
                hover make_tinted_hover_displayable("SchoolCharButtons/SchoolMedicButton_idle.png", CHARACTER_HOVER_TINT)
                xpos 1023
                ypos 302
                action Function(start_event_from_screen, "SchoolSubplace/NurseRoom.png", "NurseScene")
                focus_mask True
    else:
        add "SchoolSubplace/NurseRoom evening.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             idle "SchoolCharButtons/SchoolMedicButton_idle.png"
    #             hover make_tinted_hover_displayable("SchoolCharButtons/SchoolMedicButton_idle.png", CHARACTER_HOVER_TINT)
    #             xpos 900
    #             ypos 226
    #             action Function(show_work_in_progress)
    # # if is_night_hour(calendar.Hours):
    #     add "SchoolSubplace/NurseRoom night.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             idle "SchoolCharButtons/SchoolMedicButton_idle.png"
    #             hover make_tinted_hover_displayable("SchoolCharButtons/SchoolMedicButton_idle.png", CHARACTER_HOVER_TINT)
    #             xpos 900
    #             ypos 226
    #             action Function(show_work_in_progress)
