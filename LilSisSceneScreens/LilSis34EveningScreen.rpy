screen LilSisEveningScreen34():
    add "ScenesScreens/LilSisSceneScreens/LilSis34EveningScreen/LilSisEvening34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis34EveningScreen/LilSisEvening34Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis34EveningScreen/LilSisEvening34Button1_hover.png"
            xpos 663
            ypos 370
            action [Hide("LilSisEveningScreen34"), Jump("LilSisEveningEvent34")]