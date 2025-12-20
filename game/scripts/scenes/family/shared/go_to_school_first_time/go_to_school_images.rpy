label GoToSchoolImages:
    init python:
        define_images("GoToSchoolFirstScenes", "GoToSchoolFirstScenes", "GoToSchoolFirstScenes", 211)
        renpy.image("GoToSchoolFirstMovie1", Movie(channel="movie", play="Images/GoToSchoolFirstScenes/GoToSchoolFirstMovie1.webm", loop=False, group="pov_group"))
