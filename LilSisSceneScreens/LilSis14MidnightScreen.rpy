screen LilSisMidnightScreen14():
    add "ScenesScreens/LilSisSceneScreens/LilSis14MidnightScreen/LilSisMidnight14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis14MidnightScreen/LilSisMidnight14Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis14MidnightScreen/LilSisMidnight14Button1_hover.png"
            xpos 823
            ypos 401
            action [Hide("LilSisMidnightScreen14"), Jump("LilSisMidnightEvent14")]