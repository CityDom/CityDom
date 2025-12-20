default manners_event_triggered = False  # Global flag if not already

screen MannersClassScreen():
    if calendar.Hours < 12:
        add "SchoolSubplace/MannersClass.png"
    else:
        add "SchoolSubplace/MannersClass evening.png"

    on "show":
        if school_clock.hour == 14 and school_clock.period == 4 and not manners_event_triggered:
            action If(not renpy.in_rollback(), [SetVariable("manners_event_triggered", True), Hide("MannersClassScreen"), Call("MannersClassWrapper")])
label MannersClassWrapper:
    if seenSandraBackstory:
        call MannersClass_FromInside_Scene
    else:
        call MannersClassScene
    
    $ renpy.checkpoint()
    return