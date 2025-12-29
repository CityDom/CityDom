default manners_event_last_time = None

screen MannersClassScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/MannersClass.png"
    else:
        add "SchoolSubplace/MannersClass evening.png"
label MannersClassWrapper:
    $ manners_event_last_time = (calendar.Day, calendar.Hours)
    $ from_inside = True
    if LocationEntryFrom is not None and LocationEntryTime == (calendar.Day, calendar.Hours):
        $ from_inside = normalize_location_key(LocationEntryFrom) == normalize_location_key("MannersClass")
    if from_inside and seenSandraBackstory:
        call MannersClass_FromInside_Scene
    else:
        call MannersClassScene
    
    $ renpy.checkpoint()
    return
