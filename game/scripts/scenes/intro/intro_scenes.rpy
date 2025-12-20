init python:
    define_videos("IntroVideo", "Images/IntroVideos", "IntroVideo", 40, loop=True)


label IntroScenes:
    init python:
        define_images("IntroScene", "IntroScenes", "IntroScene", 300)

        
        renpy.image("IntroVideo33", Movie(play="Images/IntroVideos/IntroVideo33.webm", loop=False, group="pov_group"))