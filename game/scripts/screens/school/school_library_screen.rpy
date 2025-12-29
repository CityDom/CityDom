screen SchoolLibraryScreen():
    if are_girls_in_break():
        add "SchoolSubplace/SchoolLibrary.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/SchoolLibrarian_idle.png"
                hover "SchoolCharButtons/SchoolLibrarian_hover.png"
                xpos 922
                ypos 298
                action Function(show_work_in_progress)
            imagebutton:
                idle "SchoolFirstPause/DorothyEventScene/DorothyButton_idle.png"
                hover "SchoolFirstPause/DorothyEventScene/DorothyButton_hover.png"
                xpos 549
                ypos 165
                action Function(start_event_from_screen, "SchoolSubplace/SchoolLibrary.png", "DorothyFirstPauseScene")
    elif is_day_hour(calendar.Hours):
        add "SchoolSubplace/SchoolLibrary.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/SchoolLibrarian_idle.png"
                hover "SchoolCharButtons/SchoolLibrarian_hover.png"
                xpos 922
                ypos 298
                action Function(show_work_in_progress)
    else:
        add "SchoolSubplace/SchoolLibrary evening.png"
    # if is_night_hour(calendar.Hours):
    #     add "SchoolSubplace/SchoolLibrary night.png"
