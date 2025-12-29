init:
    # Define a transform that rotates an image by 45 degrees
    transform rotate_down:
        rotate -230
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0
    transform rotate_left:
        xzoom -1
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0
    transform rotate_upLeft:
        rotate 50
        xzoom -1
        on hover:
            linear 0.1 zoom 1.05 #linear is speed zoom is how far you want it to zoom in/out
        on idle:
            linear 0.1 zoom 1.0

screen UpTheStairsScreen():
    if (not school_clock.IsBreak and school_clock.period < 11) or school_clock.period == 7 or school_clock.period == 9:
        add "SchoolSubplace/UpTheStairs.png"
        imagebutton:
            auto "MoveUpArrow_%s.png"
            xpos 928
            ypos 237
            action [Return("TeacherHall"), Hide("UpTheStairsScreen")]
            at rotate_down
        imagebutton:
            auto "MoveRightArrowSmaller_%s.png"
            xpos 610
            ypos 337
            action [Return("ArtClassFront"), Hide("UpTheStairsScreen")]
            at rotate_left       
            # imagebutton:
            #     auto "MoveRightArrowSmaller_%s.png"
            #     xpos 1268
            #     ypos 337
            #     action [Return("WomansToilet"), Hide("UpTheStairsScreen")]
            #     at buttonScale
    elif school_clock.IsBreak and school_clock.hour < 15 and school_clock.period < 7:
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "SchoolFirstPause/CrissAndIsabellaEventScene/CrissAndIsabella_Button_idle.png"
                hover "SchoolFirstPause/CrissAndIsabellaEventScene/CrissAndIsabella_Button_hover.png"
                xpos 385
                ypos 328
                action [Hide("UpTheStairsScreen"), Jump("CrissAndIsabellaFirstPauseScene")]
                focus_mask True     
            imagebutton:
                auto "MoveUpArrow_%s.png"
                xpos 928
                ypos 237
                action [Return("TeacherHall"), Hide("UpTheStairsScreen")]
                at rotate_down
            imagebutton:
                auto "MoveRightArrowSmaller_%s.png"
                xpos 610
                ypos 337
                action [Return("ArtClassFront"), Hide("UpTheStairsScreen")]
                at rotate_left 
    else:
        add "SchoolSubplace/UpTheStairs evening.png"
            # imagebutton:
            #     auto "MoveRightArrowSmaller_%s.png"
            #     xpos 1268
            #     ypos 337
            #     action [Return("WomansToilet"), Hide("UpTheStairsScreen")]
            #     at buttonScale
    # if is_night_hour(calendar.Hours):
    #     add "SchoolSubplace/UpTheStairs night.png"
    #     if not MapScreenShown and not StatsScreenShown:
    #         imagebutton:
    #             auto "MoveUpArrow_%s.png"
    #             xpos 928
    #             ypos 237
    #             action [Return("TeacherHall"), Hide("UpTheStairsScreen")]
    #             at rotate_down
    #         imagebutton:
    #             auto "MoveRightArrowSmaller_%s.png"
    #             xpos 610
    #             ypos 337
    #             action [Return("ArtClassFront"), Hide("UpTheStairsScreen")]
    #             at rotate_left
    #         # imagebutton:
    #         #     auto "MoveRightArrowSmaller_%s.png"
    #         #     xpos 1268
    #         #     ypos 337
    #         #     action [Return("WomansToilet"), Hide("UpTheStairsScreen")]
    #         #     at buttonScale