screen LilSisNightScreen44():
    add "ScenesScreens/LilSisSceneScreens/LilSis44NightScreen/LilSisNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis44NightScreen/LilSisNight44Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis44NightScreen/LilSisNight44Button1_hover.png"
            xpos 753
            ypos 398
            action [Hide("LilSisNightScreen44"), Jump("LilSisNightEvent44")]