init -1 python:
    def define_images(variable_prefix, folder, image_prefix, count, start=1):
        for i in range(start, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    def define_videos(variable_prefix, folder, video_prefix, count, loop=False, group_name="pov_group"):
        for i in range(1, count + 1):
            video_id = f"{variable_prefix}{i}"
            video_path = f"{folder}/{video_prefix}{i}.webm"
            renpy.image(video_id, Movie(play=video_path, loop=loop, group=group_name))
