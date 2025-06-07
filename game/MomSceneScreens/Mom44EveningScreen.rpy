screen MomEveningScreen44():
    add "ScenesScreens/MomSceneScreens/Mom44EveningScreen/MomEvening44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom44EveningScreen/MomEvening44Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom44EveningScreen/MomEvening44Button1_hover.png"
            xpos 923
            ypos 274
            action [Hide("MomEveningScreen44"), Jump("MomEveningEvent44")]