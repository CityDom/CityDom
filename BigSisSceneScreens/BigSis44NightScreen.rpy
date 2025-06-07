screen BigSisNightScreen44():
    add "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Button1_hover.png"
            xpos 1160
            ypos 366
            action [Hide("BigSisNightScreen44"), Jump("BigSisNightEvent44")]