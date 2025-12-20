screen ClaireNightScreen44():
    add "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Button1_hover.png"
            xpos 1160
            ypos 366
            action [Hide("ClaireNightScreen44"), Jump("ClaireNightEvent44")]