screen BigSisEveningScreen34():
    add "ScenesScreens/BigSisSceneScreens/BigSis34EveningScreen/BigSisEvening34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis34EveningScreen/BigSisEvening34Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis34EveningScreen/BigSisEvening34Button1_hover.png"
            xpos 1012
            ypos 264
            action [Hide("BigSisEveningScreen34"), Jump("BigSisEveningEvent34")]