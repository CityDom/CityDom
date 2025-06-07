screen LeaveHomeScreen():
    add "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreenButton1_idle.png"
            hover "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreenButton1_hover.png"
            xpos 1080
            ypos 266
            action [Hide("LeaveHomeScreen"), Jump("LeaveHomeEvent")]
