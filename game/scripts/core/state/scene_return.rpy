init python:
    def get_return_location_image(location, period_index, current_img):
        desired = get_location_image_key(location, period_index)
        return desired if desired != current_img else current_img

label ReturnToLocation:
    python:
        for screen_name in ALL_EVENT_SCREENS:
            renpy.hide_screen(screen_name)
    $ Location_img = get_return_location_image(Location, calendar.period_index, Location_img)
    if renpy.has_image(Location_img, exact=True):
        scene expression Location_img
    $ renpy.call("GameLoop")
    return
