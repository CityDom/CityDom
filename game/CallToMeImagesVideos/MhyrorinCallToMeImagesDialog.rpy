init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("MhyrorinScene", "CallToMeScenes/MhyrorinScenes", "MhyrorinScene", 100)

    def define_videos(variable_prefix, folder, video_prefix, count, loop=False, group_name="pov_group"):
        
        for i in range(1, count + 1):
            video_id = f"{variable_prefix}{i}"
            video_path = f"{folder}/{video_prefix}{i}.webm"
            renpy.image(video_id, Movie(play=video_path, loop=loop, group=group_name))

    define_videos("MhyrorinVideo", "images/CallToMeScenes/MhyrorinVideos", "MhyrorinVideo", 30, loop=True)