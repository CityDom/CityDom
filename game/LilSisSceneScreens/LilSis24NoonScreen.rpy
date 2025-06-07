screen LilSisNoonScreen24():
    add "ScenesScreens/LilSisSceneScreens/LilSis24NoonScreen/LilSisNoon24Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis24NoonScreen/LilSisNoon24Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis24NoonScreen/LilSisNoon24Button1_hover.png"
            xpos 1246
            ypos 419
            action [Hide("LilSisNoonScreen24"), Jump("LilSisNoonEvent24")]