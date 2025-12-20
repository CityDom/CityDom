screen ClaireEveningScreen34():
    add "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_hover.png"
            xpos 1012
            ypos 264
            action [Hide("ClaireEveningScreen34"), Jump("ClaireEveningEvent34")]