label start:
    $ GameIsRunning = True

    jump GameIntro
    # Game is running

    while GameIsRunning:
        label GameLoop:
            
            # Reset variables
            $ BlockToCall, clickType = "", ""
            
            # Check for events in the current location
            $ current_location = str(Location).lower()
            python:
                for event in EVENTS.values():
                    if event.is_active and event.date_check(calendar) and event.location.lower() == current_location:
                        BlockToCall = event.block

            if BlockToCall:
                $ screen_name = f"{BlockToCall.replace('Event', 'Screen')}"
                # Check if the screen exists before attempting to show it
                if renpy.has_screen(screen_name):
                    $ renpy.show_screen(screen_name)
                else:
                    # If there's no specific screen for the event, call the event block directly
                    # This assumes you have a label or function setup for handling the event by its name
                    $ renpy.call(BlockToCall)

            # Change location image if it exists
            python:
                if calendar.period_index == 1:
                    Location_img = str(Location).lower() + " evening"
                elif calendar.period_index == 2:
                    Location_img = str(Location).lower() + " night"
                else:
                    Location_img = str(Location).lower()
            if renpy.has_image(Location_img, exact=True):
                scene expression Location_img

            # ! Sad isolate event. Will look for a better solution
            if is_before_gym_swim_class() and (calendar.Day == 1 or calendar.Day == 3 or calendar.Day == 5) and Location == "GirlsLockerRoom":
                $ renpy.hide_screen("GirlsLockerRoomScreen")
                $ renpy.jump("BeforeGymClass_FromInside_Scene")
            # ! Sad isolate event. Will look for a better solution

            # Check for location change and update the location if changed
            $ new_location = renpy.call_screen("MainHud", _layer="screens")
            if new_location != Location:
                # Assuming Location is the variable holding the current location name
                $ Location = new_location

                # Hide all screens from the previous location
                python:
                    for screen_name in ALL_EVENT_SCREENS:
                        renpy.hide_screen(screen_name)

                # Then show the new location's screen
                $ new_location_screen = f"{Location}_Screen"
                if renpy.has_screen(new_location_screen):
                    $ renpy.show_screen(new_location_screen)
                else:
                    scene expression Location_img

            # Update last location
            $ LastLocation = Location
        

