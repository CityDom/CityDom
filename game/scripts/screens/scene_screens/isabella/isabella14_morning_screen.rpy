screen IsabellaMorningScreen14():
    add "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_hover.png"
            xpos 720
            ypos 331
            action [Hide("IsabellaMorningScreen14"), Jump("IsabellaMorningEvent14")]