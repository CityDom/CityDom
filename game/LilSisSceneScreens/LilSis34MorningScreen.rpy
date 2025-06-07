screen LilSisMorningScreen34():
    add "ScenesScreens/LilSisSceneScreens/LilSis34MorningScreen/LilSisMorning34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis34MorningScreen/LilSisMorning34Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis34MorningScreen/LilSisMorning34Button1_hover.png"
            xpos 662
            ypos 340
            action [Hide("LilSisMorningScreen34"), Jump("LilSisMorningEvent34")]