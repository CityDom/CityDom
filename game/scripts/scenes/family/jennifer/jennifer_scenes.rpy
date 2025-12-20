init python:
    # Jennifer's morning scene'
    define_images("Jennifer_morning14_", "JenniferAllScenes/JenniferMorning14", "Jennifer_morning14_", 30, start=1)
    define_images("Jennifer_morning24_", "JenniferAllScenes/JenniferMorning24", "Jennifer_morning24_", 30, start=1)
    define_images("Jennifer_morning34_", "JenniferAllScenes/JenniferMorning34", "Jennifer_morning34_", 25, start=0)
    define_images("Jennifer_morning44_", "JenniferAllScenes/JenniferMorning44", "Jennifer_morning44_", 44, start=0)

    # Jennifer's evening scene'
    define_images("Jennifer_evening24_", "JenniferAllScenes/JenniferEvening24", "Jennifer_evening24_", 70, start=0)
    define_images("Jennifer_evening34_", "JenniferAllScenes/JenniferEvening34", "Jennifer_evening34_", 26, start=0)
    define_images("Jennifer_evening44_", "JenniferAllScenes/JenniferEvening44", "Jennifer_evening44_", 44, start=0)

    # Jennifer's night scene'
    define_images("Jennifer_night24_", "JenniferAllScenes/JenniferNight24", "Jennifer_night24_", 3, start=0)
    define_images("Jennifer_night34_", "JenniferAllScenes/JenniferNight34", "Jennifer_night34_", 27, start=1)
    define_images("Jennifer_night44_", "JenniferAllScenes/JenniferNight44", "Jennifer_night44_", 44, start=1)

label JenniferScenes:
    return

init python:
    define_videos("Jennifer14AMVideos", "Images/JenniferAllScenes/JenniferMorning14", "Jennifer14AMVideos", 10, loop=False)
