label start:
    $ GameIsRunning = True
    $ _ensure_background_music()

    jump GameIntro
    # Game is running

    while GameIsRunning:
        label GameLoop:
            
            # Reset variables
            $ selected_event, clickType = None, ""
            $ _ensure_background_music()
            $ calendar.update_period_index()
            $ LocationID = get_location_id(Location, LocationID)
            $ Location = get_location_name(Location)

            # Keep background in sync with time-of-day before input.
            $ desired_location_img = get_location_image_key(Location, calendar.period_index)
            if desired_location_img != Location_img:
                $ Location_img = desired_location_img
                if renpy.has_image(Location_img, exact=True):
                    scene expression Location_img
            
            # Check for events in the current location
            $ current_location = normalize_location_key(Location)
            python:
                matching_events = [
                    event
                    for event in EVENTS.values()
                    if event.is_active
                    and event.date_check(calendar)
                    and event.location.lower() == current_location
                    and event.condition_check()
                ]
                if matching_events:
                    selected_event = max(matching_events, key=lambda e: (e.priority, e.start_hour))

            if selected_event:
                $ screen_name = selected_event.screen_name
                # Check if the screen exists before attempting to show it
                if screen_name and renpy.has_screen(screen_name):
                    $ renpy.show_screen(screen_name)
                elif getattr(selected_event, "auto_trigger", True):
                    python:
                        for screen_name in ALL_EVENT_SCREENS:
                            renpy.hide_screen(screen_name)
                    # If there's no specific screen for the event, call the event block directly
                    # This assumes you have a label or function setup for handling the event by its name
                    $ renpy.call(selected_event.block)

            python:
                location_screen = get_location_screen_name(Location)
                if location_screen and renpy.has_screen(location_screen):
                    if LastLocation != Location or not renpy.get_screen(location_screen):
                        renpy.show_screen(location_screen)

            # Check for location change and update the location if changed
            $ previous_location_id = LocationID
            $ new_location = renpy.call_screen("MainHud", _layer="screens")
            $ location_changed = False
            if new_location != Location:
                $ location_changed = True
                $ LocationEntryFrom = Location
                $ LocationEntryTime = (calendar.Day, calendar.Hours)
                python:
                    loc_def = get_location_def(new_location)
                    if loc_def:
                        Location = loc_def.name
                        if loc_def.location_id is not None:
                            LocationID = loc_def.location_id
                    else:
                        Location = new_location

                # Hide all screens from the previous location
                python:
                    for screen_name in ALL_EVENT_SCREENS:
                        renpy.hide_screen(screen_name)

                # Leaving school: keep calendar aligned with the school clock.
                if previous_location_id == 1 and LocationID != 1:
                    $ calendar.sync_from_school_clock(round_break=True)

                # Update background immediately for the new location.
                $ Location_img = get_location_image_key(Location, calendar.period_index)
                if renpy.has_image(Location_img, exact=True):
                    scene expression Location_img
                python:
                    location_screen = get_location_screen_name(Location)
                    if location_screen and renpy.has_screen(location_screen):
                        renpy.show_screen(location_screen)

            # Update last location
            $ LastLocation = Location
        

