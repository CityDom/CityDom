screen LilSisMorningScreen14():
    add "ScenesScreens/LilSisSceneScreens/LilSis14MorningScreen/LilSisMorning14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis14MorningScreen/LilSisMorning14Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis14MorningScreen/LilSisMorning14Button1_hover.png"
            xpos 720
            ypos 331
            action [Hide("LilSisMorningScreen14"), Jump("LilSisMorningEvent14")]