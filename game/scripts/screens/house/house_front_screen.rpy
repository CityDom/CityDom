default housefront_scene_history_6AM = []
default housefront_scene_history_7AM = []
default housefront_scene_history_8PM = []

default housefront_max_scene_repeats = 2
default housefront_force_scene_after_count = 5 

init python:
    import random

    def choose_housefront_scene(housefront_scenes, scene_history):
        if not housefront_scenes:
            renpy.say("Error", "No scenes available! Check your scene setup.")
            return None  

        # Count how many times each scene has been played
        scene_counts = {scene: scene_history.count(scene) for scene in housefront_scenes}

        # Prioritize scenes that have never been played
        never_played = [scene for scene in housefront_scenes if scene_counts[scene] == 0]

        if never_played:
            # Force an unplayed scene if any exist
            chosen_scene = random.choice(never_played)
        else:
            # Prevent repeating the same scene too often
            if len(scene_history) >= housefront_max_scene_repeats:
                last_scene = scene_history[-1]
                if scene_history[-housefront_max_scene_repeats:] == [last_scene] * housefront_max_scene_repeats:
                    housefront_scenes = [scene for scene in housefront_scenes if scene != last_scene] or housefront_scenes

            # Avoid scenes repeated in the last few turns
            recent_window = scene_history[-housefront_force_scene_after_count:]
            filtered = [scene for scene in housefront_scenes if scene not in recent_window]

            # Choose a scene, prioritizing filtered ones
            chosen_scene = random.choice(filtered) if filtered else random.choice(housefront_scenes)

        # Add to scene history
        scene_history.append(chosen_scene)

        # Keep scene history size reasonable
        if len(scene_history) > housefront_force_scene_after_count:
            scene_history.pop(0)

        return chosen_scene



screen HousefrontScreen():

    if calendar.Hours == 0:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_GetsHome_Claire_6AM", "MC_GetsHome_Jennifer_6AM", "MC_GetsHome_Isabella_6AM"], 
                        housefront_scene_history_6AM
                    ))
                ]
                focus_mask True

    elif calendar.Hours == 1:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_GetsHome_Claire_6AM", "MC_GetsHome_Isabella_7AM"], 
                        housefront_scene_history_7AM
                    ))
                ]
                focus_mask True

    elif calendar.Hours == 2:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Isabella_8AM")
                ]
                focus_mask True

    elif calendar.Hours == 3:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Jennifer_9AM")
                ]
                focus_mask True

    elif calendar.Hours == 4:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_All_10AM")
                ]
                focus_mask True

    elif calendar.Hours == 5:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_All_11AM")
                ]
                focus_mask True
    elif calendar.Hours == 6:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Mhyrorin_12AM")
                ]
                focus_mask True
    elif calendar.Hours == 7:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Mhyrorin_1PM")
                ]
                focus_mask True
    elif calendar.Hours == 8:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Mhyrorin_2PM")
                ]
                focus_mask True
    elif calendar.Hours == 9:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Mhyrorin_3PM")
                ]
                focus_mask True
    elif calendar.Hours == 10:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Isabella_4PM")
                ]
                focus_mask True
    elif calendar.Hours == 11:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Isabella_5PM")
                ]
                focus_mask True
    elif calendar.Hours == 12:
        add "HomeSubplace/Housefront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Claire_6PM")
                ]
                focus_mask True
    elif calendar.Hours == 13:
        add "HomeSubplace/Housefront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Jennifer_7PM")
                ]
                focus_mask True        
    elif calendar.Hours == 14:
        add "HomeSubplace/Housefront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump(choose_housefront_scene(
                        ["MC_GetsHome_Claire_8PM", "MC_GetsHome_Isabella_8PM"], 
                        housefront_scene_history_7AM
                    ))
                ]
                focus_mask True      
    elif calendar.Hours == 15:
        add "HomeSubplace/Housefront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Jennifer_9PM")
                ]
                focus_mask True 
    elif calendar.Hours == 16:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Jennifer_10PM")
                ]
                focus_mask True  
    elif calendar.Hours == 17:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Isabella_11PM")
                ]
                focus_mask True  
    elif calendar.Hours == 18:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Isabella_12PM")
                ]
                focus_mask True  
    elif calendar.Hours == 19:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Claire_1AM")
                ]
                focus_mask True 
    elif calendar.Hours == 20:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [
                    Hide("HousefrontScreen"), 
                    Jump("MC_GetsHome_Mhyrorin_2AM")
                ]
                focus_mask True 
    elif 0 <= calendar.Hours <= 11:
        add "HomeSubplace/Housefront.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [Hide("HousefrontScreen"), Return("Entrance")]
                focus_mask True
    elif 12 <= calendar.Hours <= 15:
        add "HomeSubplace/Housefront evening.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [Hide("HousefrontScreen"), Return("Entrance")]
                focus_mask True
    elif 16 <= calendar.Hours <= 24:
        add "HomeSubplace/Housefront night.png"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "EntranceScreen/EntranceDoor_idle.png"
                hover "EntranceScreen/EntranceDoor_hover.png"
                xpos 915
                ypos 199
                action [Hide("HousefrontScreen"), Return("Entrance")]
                focus_mask True