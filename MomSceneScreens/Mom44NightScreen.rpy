screen MomNightScreen44():
    add "ScenesScreens/MomSceneScreens/Mom44NightScreen/MomNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom44NightScreen/MomNight44Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom44NightScreen/MomNight44Button1_hover.png"
            xpos 1080
            ypos 457
            action [Hide("MomNightScreen44"), Jump("MomNightEvent44")]