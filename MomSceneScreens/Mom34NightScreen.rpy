screen MomNightScreen34():
    add "ScenesScreens/MomSceneScreens/Mom34NightScreen/MomNight34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/MomSceneScreens/Mom34NightScreen/MomNight34Button1_idle.png"
            hover "ScenesScreens/MomSceneScreens/Mom34NightScreen/MomNight34Button1_hover.png"
            xpos 995
            ypos 285
            action [Hide("MomNightScreen34"), Jump("MomNightEvent34")]