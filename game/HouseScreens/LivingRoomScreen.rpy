default Livingroom_scene_morning = []
default Livingroom_scene_12PM = []
default Livingroom_scene_1PM = []
default Livingroom_scene_2PM = []
default Livingroom_scene_3PM = []
default Livingroom_scene_4PM = []
default Livingroom_scene_5PM = []
default Livingroom_scene_6PM = []
default Livingroom_scene_9PM = []
default Livingroom_scene_2AM = []

screen LivingroomScreen():
    add "HomeSubplace/LivingRoom.png"
    if not MapScreenShown and not StatsScreenShown:
        if calendar.Hours == 0:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Jennifer_Label", "MC_Livingroom_Movie_Morning_Isabella_Label", "MC_Livingroom_Movie_Morning_Alone_Label"], 
                        Livingroom_scene_morning
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 1:
            add "ScenesScreens/BigSisSceneScreens/BigSis24MorningScreen/BigSisMorning24Screen1.png"
            imagebutton:
                idle "ScenesScreens/BigSisSceneScreens/BigSis24MorningScreen/BigSisMorning24Button1_idle.png"
                hover "ScenesScreens/BigSisSceneScreens/BigSis24MorningScreen/BigSisMorning24Button1_hover.png"
                xpos 1440
                ypos 274
                action [Hide("LivingroomScreen"), Jump("BigSisMorningEvent24")]
                focus_mask True
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump("MC_Livingroom_Movie_7AM_Claire_Label")
                ]
                focus_mask True
        elif calendar.Hours == 2:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump("MC_Livingroom_Movie_8AM_Jennifer_Label")
                ]
                focus_mask True            
        elif calendar.Hours == 3:
            add "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreen1.png"
            imagebutton:
                idle "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreenButton1_idle.png"
                hover "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreenButton1_hover.png"
                xpos 1223
                ypos 274
                action [Hide("LivingroomScreen"), Jump("DinnerGroupEvent")]
                focus_mask True
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump("MC_Livingroom_Movie_9AM_All_Label")
                ]
                focus_mask True
        elif calendar.Hours == 4:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump("MC_Livingroom_Movie_Morning_Alone_Label")
                ]
                focus_mask True
        elif calendar.Hours == 5:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump("MC_Livingroom_Movie_11AM_Jennifer_Label")
                ]
                focus_mask True
        elif calendar.Hours == 6:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_12PM_Mhyrorin_Label"], 
                        Livingroom_scene_12PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 7:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_1PM_Mhyrorin_Label"], 
                        Livingroom_scene_1PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 8:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_2PM_Mhyrorin_Label"], 
                        Livingroom_scene_2PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 9:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_3PM_Mhyrorin_Label"], 
                        Livingroom_scene_3PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 10:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_4PM_Isabella_Label"], 
                        Livingroom_scene_4PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 11:
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_5PM_Isabella_Label"], 
                        Livingroom_scene_5PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 12:
            add "HomeSubplace/LivingRoom evening.png"
            imagebutton:
                idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                xpos 975
                ypos 515
                action [
                    Hide("LivingroomScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_6PM_Isabella_Label"], 
                        Livingroom_scene_6PM
                    ))
                ]
                focus_mask True
        elif calendar.Hours == 13:
            add "ScenesScreens/LilSisSceneScreens/LilSis24EveningScreen/LilSisEvening24Screen1.png"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/LilSisSceneScreens/LilSis24EveningScreen/LilSisEvening24Button1_idle.png"
                    hover "ScenesScreens/LilSisSceneScreens/LilSis24EveningScreen/LilSisEvening24Button1_hover.png"
                    xpos 1125
                    ypos 463
                    action [Hide("LivingroomScreen"), Jump("LilSisEveningEvent24")]
                    focus_mask True
        elif calendar.Hours == 14:
            add "HomeSubplace/LivingRoom evening.png"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                    hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                    xpos 975
                    ypos 515
                    action [
                        Hide("LivingroomScreen"), 
                        Jump("MC_Livingroom_Movie_8PM_MC_Alone_Label")
                    ]
                    focus_mask True
        elif calendar.Hours == 15:
            add "MCEvents/HouseButtons/MomInTheKitchen.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                    hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                    xpos 975
                    ypos 515
                    action [
                        Hide("LivingroomScreen"), 
                        Jump(choose_housefront_scene(
                            ["MC_Livingroom_Movie_8PM_MC_Alone_Label", "MC_Livingroom_Movie_9PM_Jennifer_Label"], 
                            Livingroom_scene_9PM
                        ))
                    ]
                    focus_mask True
        elif calendar.Hours == 16:
            add "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreenButton1_idle.png"
                    hover "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreenButton1_hover.png"
                    xpos 1223
                    ypos 278
                    action [Hide("LivingroomScreen"), Jump("LunchGroupEvent")]
                    focus_mask True
                imagebutton:
                    idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                    hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                    xpos 975
                    ypos 515
                    action [
                        Hide("LivingroomScreen"), 
                        Jump("MC_Livingroom_Movie_10PM_All_Label")
                    ]
                    focus_mask True
        elif calendar.Hours == 17:
            add "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreenButton1_idle.png"
                    hover "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreenButton1_hover.png"
                    xpos 990
                    ypos 344
                    action [Hide("LivingroomScreen"), Jump("MovieNightEvent")]
        elif calendar.Hours == 18:
            add "MCEvents/HouseButtons/Livingroom_Night.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                    hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                    xpos 975
                    ypos 515
                    action [
                        Hide("LivingroomScreen"), 
                        Jump(choose_housefront_scene(
                            ["MC_Livingroom_Movie_12AM_Alone_Label", "MC_Livingroom_Movie_12AM_Isabella_Label"], 
                            Livingroom_scene_9PM
                        ))
                    ]
                    focus_mask True
        elif calendar.Hours == 19:
            add "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Screen1.png"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Button1_idle.png"
                    hover "ScenesScreens/BigSisSceneScreens/BigSis44NightScreen/BigSisNight44Button1_hover.png"
                    xpos 1187
                    ypos 364
                    action [Hide("LivingroomScreen"), Jump("BigSisNightEvent44")]
                    focus_mask True
        elif calendar.Hours == 20:
            add "MCEvents/HouseButtons/Livingroom_Night.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "MCEvents/HouseButtons/CouchButton_Evening_idle.webp"
                    hover "MCEvents/HouseButtons/CouchButton_Evening_hover.webp"
                    xpos 975
                    ypos 515
                    action [
                        Hide("LivingroomScreen"), 
                        Jump(choose_housefront_scene(
                            ["MC_Livingroom_Movie_2AM_Alone_Label", "MC_Livingroom_Movie_2AM_Isabella_Label", "MC_Livingroom_Movie_2AM_Jennifer_Label", "MC_Livingroom_Movie_2AM_Claire_Label", "MC_Livingroom_Movie_2AM_Mhyrorin_Label"], 
                            Livingroom_scene_2AM
                        ))
                    ]
                    focus_mask True