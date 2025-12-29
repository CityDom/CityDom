default HOUSE_SCENE_HISTORY = {}

init python:
    def get_scene_history(key):
        history = HOUSE_SCENE_HISTORY.get(key)
        if history is None:
            history = []
            HOUSE_SCENE_HISTORY[key] = history
        return history

    def choose_scene_with_history(key, scenes):
        return choose_housefront_scene(scenes, get_scene_history(key))
