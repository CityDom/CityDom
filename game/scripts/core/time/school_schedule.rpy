init python:
    def is_english_class_hour():
        return school_clock.hour == 12 and school_clock.period == 0 and not school_clock.period == 10

    def is_manners_class_hour():
        return school_clock.hour == 14 and school_clock.period == 4

    def can_trigger_manners_event():
        if renpy.in_rollback():
            return False
        last_time = getattr(store, "manners_event_last_time", None)
        current_time = (getattr(store.calendar, "Day", None), getattr(store.calendar, "Hours", None))
        if last_time == current_time:
            return False
        if is_manners_class_hour():
            return True
        try:
            fallback_hour = getattr(store, "AFTERNOON_START_HOUR", 8)
            return store.calendar.is_school_hours() and store.calendar.Hours == fallback_hour
        except Exception:
            return False

    def can_trigger_before_gym_class_event():
        if renpy.in_rollback():
            return False
        return is_before_gym_swim_class() and store.calendar.Day in (1, 3, 5)

    def is_art_class_hour():
        return not school_clock.IsBreak and school_clock.hour == 13 and school_clock.period == 2

    def is_detention_class_hour():
        return school_clock.period == 10

    def is_bio_class_hour():
        return school_clock.hour == 15 and school_clock.period == 6

    def is_gym_swim_class_hour():
        return school_clock.period == 8

    def is_before_gym_swim_class():
        return school_clock.period == 7

    def are_girls_in_break():
        return school_clock.IsBreak and school_clock.hour < 15 and school_clock.period < 7


