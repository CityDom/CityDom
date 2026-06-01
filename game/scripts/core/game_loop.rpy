init python:
    def select_active_event(calendar_obj, location_name):
        current_location = normalize_location_key(location_name)
        matching_events = [
            event
            for event in EVENTS.values()
            if event.is_active
            and event.date_check(calendar_obj)
            and event.location.lower() == current_location
            and event.condition_check()
        ]

        if not matching_events:
            return None

        return max(matching_events, key=lambda e: (e.priority, e.start_hour))

    def get_location_background_update(location_name, period_index, current_image):
        desired_location_img = get_location_image_key(location_name, period_index)
        should_update = desired_location_img != current_image and get_location_background_displayable(desired_location_img) is not None
        return desired_location_img, should_update

    def get_location_background_displayable(location_image):
        if renpy.has_image(location_image, exact=True):
            return location_image

        location_file = get_location_image_file(location_image)
        if location_file and renpy.loadable(location_file):
            return location_file

        return None

    def show_location_background(location_image):
        if renpy.has_image(location_image, exact=True):
            renpy.scene(layer="master")
            renpy.show(location_image, layer="master")
            return True

        location_file = get_location_image_file(location_image)
        if location_file and renpy.loadable(location_file):
            renpy.scene(layer="master")
            renpy.show("location_bg", what=renpy.display.im.Image(location_file), layer="master")
            return True

        return False

    def hide_inactive_location_screens(active_screen=None):
        for screen_name in ALL_EVENT_SCREENS:
            if screen_name != active_screen:
                renpy.hide_screen(screen_name)

    def ensure_location_screen_visible(location_name, previous_location=None):
        location_screen = get_location_screen_name(location_name)
        active_screen = location_screen if location_screen and renpy.has_screen(location_screen) else None
        hide_inactive_location_screens(active_screen)

        if active_screen:
            if previous_location != location_name or not renpy.get_screen(location_screen):
                renpy.show_screen(location_screen)

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
            $ location_changed_since_last_loop = normalize_location_key(Location) != normalize_location_key(LastLocation)

            # Keep background in sync with time-of-day before input.
            $ Location_img, should_update_bg = get_location_background_update(Location, calendar.period_index, Location_img)
            if should_update_bg or location_changed_since_last_loop:
                $ show_location_background(Location_img)
            
            # Check for events in the current location
            $ selected_event = select_active_event(calendar, Location)

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

            $ ensure_location_screen_visible(Location, LastLocation)

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

                # Trigger direct auto-events before painting the destination room,
                # so entry scenes do not briefly flash the room background.
                $ selected_event = select_active_event(calendar, Location)
                if selected_event and not selected_event.screen_name and getattr(selected_event, "auto_trigger", True):
                    python:
                        for screen_name in ALL_EVENT_SCREENS:
                            renpy.hide_screen(screen_name)
                    $ renpy.call(selected_event.block)
                else:
                    # Update background immediately for the new location.
                    $ Location_img, should_update_bg = get_location_background_update(Location, calendar.period_index, "")
                    if should_update_bg:
                        $ show_location_background(Location_img)
                    $ ensure_location_screen_visible(Location)

            # Update last location
            $ LastLocation = Location
        
