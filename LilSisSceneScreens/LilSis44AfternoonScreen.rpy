screen LilSisAfterNoonScreen44():
    add "ScenesScreens/LilSisSceneScreens/LilSis44AfternoonScreen/LilSisAfternoon44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis44AfternoonScreen/LilSisAfternoon44Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis44AfternoonScreen/LilSisAfternoon44Button1_hover.png"
            xpos 1263
            ypos 339
            action [Hide("LilSisAfterNoonScreen44"), Jump("LilSisAfterNoonEvent44")]