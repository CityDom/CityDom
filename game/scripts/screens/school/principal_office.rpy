screen PrincipalOfficeScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/PrincipalOffice.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolCharButtons/PrincipalButton_idle.png"
                hover make_tinted_hover_displayable("SchoolCharButtons/PrincipalButton_idle.png", CHARACTER_HOVER_TINT)
                xpos 879
                ypos 232
                action Function(show_work_in_progress)
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/PrincipalOffice evening.png"
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/PrincipalOffice night.png"
