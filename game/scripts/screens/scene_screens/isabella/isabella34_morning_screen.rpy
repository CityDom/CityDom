screen IsabellaMorningScreen34():
    add "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_hover.png"
            xpos 662
            ypos 340
            action [Hide("IsabellaMorningScreen34"), Jump("IsabellaMorningEvent34")]