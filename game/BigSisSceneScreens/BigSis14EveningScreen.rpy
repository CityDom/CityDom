screen BigSisEveningScreen14():
    add "ScenesScreens/BigSisSceneScreens/BigSis14EveningScreen/BigSisEvening14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis14EveningScreen/BigSisEvening14Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis14EveningScreen/BigSisEvening14Button1_hover.png"
            xpos 1302
            ypos 379
            action [Hide("BigSisEveningScreen14"), Jump("BigSisEveningEvent14")]