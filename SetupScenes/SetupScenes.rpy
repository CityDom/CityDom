init python:
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
        vm = video_manager  # Short-hand reference
        vm["sequence"] = video_ids
        vm["index"] = 0  # Start with the first video
        vm["current"] = video_ids[0] if video_ids else None

    def switch_video():
        """
        Switches to the next video in the sequence, ensuring that the sequence is not empty.
        """
        vm = video_manager
        sequence_length = len(vm["sequence"])
        if sequence_length == 0:
            return  
        vm["index"] = (vm["index"] + 1) % sequence_length
        vm["current"] = vm["sequence"][vm["index"]]
        
        # Assuming renpy.hide and renpy.show should only be called if there's a valid video
        renpy.hide(vm["current"])  # Hide the current (now previous) video
        renpy.show(vm["current"])  # Show the next video
    def get_current_video_id():
        """
        Returns the ID of the currently playing video.
        """
        return video_manager["sequence"][video_manager["index"]] if video_manager["sequence"] else None

    def show_current_video():
        """
        Shows the current video from the sequence.
        """
        vm = video_manager
        if vm["sequence"]:
            vm["current"] = vm["sequence"][vm["index"]]
            renpy.show(vm["current"])
        else:
            pass  # Consider handling the case when there's no video to show

    def play_video_sequence(video_ids):
        """
        Sets up and plays a given sequence of videos.
        """
        setup_video_sequence(video_ids)
        show_current_video()
        renpy.show_screen("switch_pov_videos")

screen switch_pov_videos():
    if ShouldSeeSwitchSceneButton:  # Simplified condition check
        imagebutton:
            idle "images/Switch_POV.png"
            action [Function(switch_video)]
            xalign 1.0  
            yalign 0.0 
