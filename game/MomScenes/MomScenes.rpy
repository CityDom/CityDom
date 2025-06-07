label MomScenes:
    init python:
        def define_images(variable_prefix, folder, image_prefix, start, count):
            for i in range(start, count + 1):
                variable_name = f"{variable_prefix}{i}"
                image_path = f"{folder}/{image_prefix}{i}.webp"
                renpy.image(variable_name, image_path)

        # Mom's morning scenes
        define_images("MOM", "MomAllScenes/MomMorning14", "MOM", 1, 30)
        define_images("MORNINGS24MOM", "MomAllScenes/MomMorning24", "MomMorning", 1, 30)
        define_images("MORNINGS34MOM", "MomAllScenes/MomMorning34", "MomMorning", 0, 25)
        define_images("MORNINGS44MOM", "MomAllScenes/MomMorning44", "MomMorning", 0, 44)

        # Mom's evening scenes
        define_images("EVENINGS24MOM", "MomAllScenes/MomEvening24", "MomEvening", 0, 70)
        define_images("EVENINGS34MOM", "MomAllScenes/MomEvening34", "MomEvening", 0, 26)
        define_images("EVENINGS44MOM", "MomAllScenes/MomEvening44", "MomEvening", 0, 44)

        # Mom's night scenes
        define_images("NIGHT24MOM", "MomAllScenes/MomNight24", "MomNight", 0, 3)
        define_images("NIGHT34MOM", "MomAllScenes/MomNight34", "MomNight", 1, 27)
        define_images("NIGHT44MOM", "MomAllScenes/MomNight44", "MomNight", 1, 44)

init python:
    def define_videos(variable_prefix, folder, video_prefix, count, loop=False, group_name="pov_group"):
        
        for i in range(1, count + 1):
            video_id = f"{variable_prefix}{i}"
            video_path = f"{folder}/{video_prefix}{i}.webm"
            renpy.image(video_id, Movie(play=video_path, loop=loop, group=group_name))

    define_videos("Mom14AMVideos", "Images/MomAllScenes/MomMorning14", "Mom14AMVideos", 10, loop=False)