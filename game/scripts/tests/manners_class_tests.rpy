testsuite manners_class_tests:
    description "Manners class event trigger tests."

    before testcase:
        python:
            renpy.store._test_manners_state = (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
                renpy.store.school_clock.hour,
                renpy.store.school_clock.period,
                renpy.store.Location,
                renpy.store.LocationID,
                getattr(renpy.store, "manners_event_last_time", None),
            )

    after testcase:
        python:
            (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
                renpy.store.school_clock.hour,
                renpy.store.school_clock.period,
                renpy.store.Location,
                renpy.store.LocationID,
                renpy.store.manners_event_last_time,
            ) = renpy.store._test_manners_state
            del renpy.store._test_manners_state

    testcase manners_event_triggers_at_2pm:
        description "Manners class should be eligible at 2 PM with seen backstory."
        python:
            renpy.store.calendar.Day = 1
            renpy.store.calendar.Hours = 8
            renpy.store.calendar.update_period_index()
            renpy.store.school_clock.hour = 14
            renpy.store.school_clock.period = 4
            renpy.store.manners_event_last_time = None

            test_expect_equal(
                renpy.store.can_trigger_manners_event(),
                True,
                "Expected manners class to be eligible at 2 PM."
            )

    testcase manners_event_selection_prefers_wrapper:
        description "Event selection should prefer MannersClassWrapper when eligible."
        python:
            renpy.store.calendar.Day = 1
            renpy.store.calendar.Hours = 8
            renpy.store.calendar.update_period_index()
            renpy.store.school_clock.hour = 14
            renpy.store.school_clock.period = 4
            renpy.store.manners_event_last_time = None
            renpy.store.Location = "MannersClass"

            current_location = renpy.store.normalize_location_key(renpy.store.Location)
            matching_events = [
                event
                for event in renpy.store.EVENTS.values()
                if event.is_active
                and event.date_check(renpy.store.calendar)
                and event.location.lower() == current_location
                and event.condition_check()
            ]
            if matching_events:
                selected_event = max(matching_events, key=lambda e: (e.priority, e.start_hour))
            else:
                selected_event = None

            test_expect_equal(
                selected_event.block if selected_event else None,
                "MannersClassWrapper",
                "Expected MannersClassWrapper to be selected at 2 PM."
            )

    testcase manners_event_blocked_same_hour:
        description "Manners class should not re-trigger in the same hour."
        python:
            renpy.store.calendar.Day = 1
            renpy.store.calendar.Hours = 8
            renpy.store.calendar.update_period_index()
            renpy.store.school_clock.hour = 14
            renpy.store.school_clock.period = 4
            renpy.store.manners_event_last_time = (1, 8)

            test_expect_equal(
                renpy.store.can_trigger_manners_event(),
                False,
                "Expected manners class to be blocked in the same hour."
            )
