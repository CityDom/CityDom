screen MannersClassScreen():
    if not (school_clock.hour == 14 and school_clock.period == 4) and calendar.Hours < 12:
        add "SchoolSubplace/MannersClass.png"
    # elif school_clock.hour == 14 and school_clock.period == 4:
    #     $ renpy.hide_screen("MannersClassScreen")
    #     $ renpy.jump("MannersClassEvent")
    elif not (school_clock.hour == 14 and school_clock.period == 4):
        add "SchoolSubplace/MannersClass evening.png"
