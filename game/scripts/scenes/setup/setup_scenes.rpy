init python:
    # Add this for alpha management
    video_transforms = {}  # Dict to hold Transform for each video ID: {id: Transform(alpha=...)}

    # Consolidated global variables for video management
    video_manager = {
        "sequence": [],
        "index": 0,
        "current": None,
    }

    def setup_video_sequence(video_ids):
        """
        Initializes the video sequence to be played.
        """
        vm = video_manager
        vm["sequence"] = video_ids
        vm["index"] = 0
        vm["current"] = video_ids[0] if video_ids else None
        # Reset alphas: Hide all, show first
        for vid in video_ids:
            video_transforms[vid] = Transform(vid, alpha=0.0)
        if vm["current"]:
            video_transforms[vm["current"]] = Transform(vm["current"], alpha=1.0)

    def switch_video():
        """
        Switches to the next video in the sequence by updating alphas.
        """
        vm = video_manager
        sequence_length = len(vm["sequence"])
        if sequence_length == 0:
            return  
        old_current = vm["current"]
        vm["index"] = (vm["index"] + 1) % sequence_length
        vm["current"] = vm["sequence"][vm["index"]]
        
        # Apply dissolve transition (optional, 0.5 seconds)
        renpy.transition(Dissolve(0.5))
        
        # Update alphas: Hide old, show new (videos keep playing)
        if old_current:
            video_transforms[old_current] = Transform(old_current, alpha=0.0)
            renpy.show(old_current, what=video_transforms[old_current])  # Re-show with updated Transform
        video_transforms[vm["current"]] = Transform(vm["current"], alpha=1.0)
        renpy.show(vm["current"], what=video_transforms[vm["current"]])  # Re-show with updated Transform
        
        # Refresh display
        renpy.redraw(None, 0)  # Force immediate update

    def get_current_video_id():
        """
        Returns the ID of the currently playing video.
        """
        return video_manager["sequence"][video_manager["index"]] if video_manager["sequence"] else None

    def show_current_video():
        """
        Shows all videos in the sequence (with alphas controlling visibility).
        """
        vm = video_manager
        if vm["sequence"]:
            for vid in vm["sequence"]:
                renpy.show(vid, what=video_transforms[vid])  # Show with the transformed version
        else:
            pass

    def play_video_sequence(video_ids):
        """
        Sets up and plays a given sequence of videos.
        """
        setup_video_sequence(video_ids)
        show_current_video()
        renpy.show_screen("switch_pov_videos")

# Your define_videos call remains the same, e.g.:
# define_videos("MhyrorinVideo", "images/CallToMeScenes/MhyrorinVideos", "MhyrorinVideo", 30, loop=True, group_name="mhyrorin_pov")

screen switch_pov_videos():
    if ShouldSeeSwitchSceneButton:
        imagebutton:
            idle "images/Switch_POV.png"
            action [Function(switch_video)]
            xalign 1.0  
            yalign 0.0 