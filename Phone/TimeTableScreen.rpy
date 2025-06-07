screen TimeTableScreen():
    add "SchoolWeekPlanner_idle.png"

    imagebutton:
        xpos 1780
        ypos 1003
        auto "Exit_%s.png"
        action [SetVariable("ShowPhone", True), Show("MainHud"), Hide("TimeTableScreen")]
