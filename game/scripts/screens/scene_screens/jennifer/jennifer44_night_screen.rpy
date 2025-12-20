screen JenniferNightScreen44():
    add "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_idle.png"
            hover "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_hover.png"
            xpos 1080
            ypos 457
            action [Hide("JenniferNightScreen44"), Jump("JenniferNightEvent44")]