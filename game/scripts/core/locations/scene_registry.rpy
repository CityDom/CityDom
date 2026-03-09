default HOUSE_SCENE_HISTORY = {}
default scene_rotation_max_repeats = 2
default scene_rotation_recent_window = 5

init python:
    import random

    def get_scene_history(key):
        history = HOUSE_SCENE_HISTORY.get(key)
        if history is None:
            history = []
            HOUSE_SCENE_HISTORY[key] = history
        return history

    def choose_scene_from_history(scenes, scene_history):
        if not scenes:
            renpy.say("Error", "No scenes available! Check your scene setup.")
            return None

        scene_counts = {scene: scene_history.count(scene) for scene in scenes}
        never_played = [scene for scene in scenes if scene_counts[scene] == 0]

        if never_played:
            chosen_scene = random.choice(never_played)
        else:
            if len(scene_history) >= scene_rotation_max_repeats:
                last_scene = scene_history[-1]
                repeated = scene_history[-scene_rotation_max_repeats:]
                if repeated == [last_scene] * scene_rotation_max_repeats:
                    scenes = [scene for scene in scenes if scene != last_scene] or scenes

            recent_window = scene_history[-scene_rotation_recent_window:]
            filtered = [scene for scene in scenes if scene not in recent_window]
            chosen_scene = random.choice(filtered) if filtered else random.choice(scenes)

        scene_history.append(chosen_scene)

        if len(scene_history) > scene_rotation_recent_window:
            scene_history.pop(0)

        return chosen_scene

    def choose_housefront_scene(housefront_scenes, scene_history):
        return choose_scene_from_history(housefront_scenes, scene_history)

    def choose_scene_with_history(key, scenes):
        return choose_scene_from_history(scenes, get_scene_history(key))
