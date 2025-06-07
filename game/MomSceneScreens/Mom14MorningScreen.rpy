screen MomMorningScreen14():
    add "ScenesScreens/MomSceneScreens/Mom14MorningScreen/MomMorning14Screen1.png"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom14MorningScreen/MomMorning14Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom14MorningScreen/MomMorning14Button1_hover.png"
            xpos 927
            ypos 361
            action [Hide("MomMorningScreen14"), Jump("MomMorningEvent14")]