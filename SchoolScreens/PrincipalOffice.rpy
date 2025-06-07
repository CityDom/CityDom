screen PrincipalOfficeScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/PrincipalOffice.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/PrincipalButton_idle.png"
                hover "SchoolCharButtons/PrincipalButton_hover.png"
                xpos 879
                ypos 232
                action Function(show_work_in_progress)
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/PrincipalOffice evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/PrincipalOffice night.png"