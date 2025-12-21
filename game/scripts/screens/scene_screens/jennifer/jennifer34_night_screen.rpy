screen JenniferNightScreen34():
    add "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_idle.png"
            hover "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_hover.png"
            xpos 995
            ypos 285
            action [Function(hideEventScreens), Jump("JenniferNightEvent34")]
