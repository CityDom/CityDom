screen BackYardScreen():
    if (not school_clock.IsBreak and school_clock.period < 11) or school_clock.period == 7 or school_clock.period == 9:
        add "SchoolSubplace/BackYard.png"
    elif school_clock.IsBreak and school_clock.hour < 15 and school_clock.period < 7:
        add "SchoolSubplace/BackYard1.png"
        imagebutton:
            idle "SchoolFirstPause/MariaEventScene/Maria_Button_idle.png"
            hover "SchoolFirstPause/MariaEventScene/Maria_Button_hover.png"
            xpos 812
            ypos 325
            action [Hide("BackYardScreen"),Jump("MariaFirstPauseScene")]
            focus_mask True