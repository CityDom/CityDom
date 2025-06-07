screen MomMorningScreen24():
    add "ScenesScreens/MomSceneScreens/Mom24MorningScreen/MomMorning24Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom24MorningScreen/MomMorning24Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom24MorningScreen/MomMorning24Button1_hover.png"
            xpos 952
            ypos 233
            action [Hide("MomMorningScreen24"), Jump("MomMorningEvent24")]