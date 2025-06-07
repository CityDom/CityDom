screen MomEveningScreen24():
    add "ScenesScreens/MomSceneScreens/Mom24EveningScreen/MomEvening24Screen1.png"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom24EveningScreen/MomEvening24Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom24EveningScreen/MomEvening24Button1_hover.png"
            xpos 1293
            ypos 360
            action [Hide("MomEveningScreen24"), Jump("MomEveningEvent24")]