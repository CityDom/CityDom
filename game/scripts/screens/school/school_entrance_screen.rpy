init:
    # Define a transform that rotates an image by 45 degrees
    transform rotate_Minus35:
        rotate -140
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0
    transform rotate_180:
        rotate 180

screen SchoolEntranceScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/SchoolEntrance.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                auto "MoveLeftArrow_%s.png"
                xpos 20
                ypos 500
                action [Return("ToiletsFront"), Hide("SchoolEntranceScreen")]
                at buttonScale
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 220
                ypos 230
                action [Return("UpTheStairs"), Hide("SchoolEntranceScreen")]
                at rotate_Minus35
            imagebutton:
                idle "SchoolDoors/MannersClassDoor_idle.png"
                hover "SchoolDoors/MannersClassDoor_hover.png"
                xpos 1146
                ypos 390
                action [Return("MannersClass"), Hide("SchoolEntranceScreen")]
    else:
        add "SchoolSubplace/SchoolEntrance evening.png"
