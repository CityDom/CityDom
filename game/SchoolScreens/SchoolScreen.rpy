init:
    # Define a transform that rotates an image by 45 degrees
    transform rotateUpLeft:
        rotate 30
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0

screen SchoolScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/School.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolDoors/SchoolDoor_Idle.png"
                hover "SchoolDoors/SchoolDoor_hover.png"
                xpos 363
                ypos 196
                action [Return("SchoolEntrance"), Hide("SchoolScreen")]
            imagebutton:
                auto "MoveLeftArrow_%s.png"
                xpos 20
                ypos 500
                action [Return("SchoolGymFront"), Hide("SchoolScreen")]
                at rotateUpLeft
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/School evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/School night.png"
