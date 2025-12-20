screen JenniferMorningScreen14():
    add "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Screen1.png"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_idle.png"
            hover "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_hover.png"
            xpos 927
            ypos 361
            action [Hide("JenniferMorningScreen14"), Jump("JenniferMorningEvent14")]