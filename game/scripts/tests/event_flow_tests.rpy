testsuite event_flow_tests:
    description "Event selection and return flow helpers."

    before testcase:
        python:
            renpy.store._test_event_flow_state = (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
            )

    after testcase:
        python:
            (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
            ) = renpy.store._test_event_flow_state
            del renpy.store._test_event_flow_state

    testcase event_priority_selects_highest:
        description "Higher priority event should win when multiple match."
        python:
            renpy.store.calendar.Day = 1
            renpy.store.calendar.Hours = 0
            renpy.store.calendar.update_period_index()
            event_low = renpy.store.Event(0, 24, -3, "Test", "LowEvent", True, priority=0)
            event_high = renpy.store.Event(0, 24, -3, "Test", "HighEvent", True, priority=10)
            matching = [
                event
                for event in (event_low, event_high)
                if event.is_active
                and event.date_check(renpy.store.calendar)
                and event.location.lower() == "test"
                and event.condition_check()
            ]
            selected = max(matching, key=lambda e: (e.priority, e.start_hour))
            test_expect_equal(
                selected.block,
                "HighEvent",
                "Expected higher priority event to be selected."
            )

    testcase return_location_image_updates:
        description "Return helper should update image when it differs."
        python:
            desired = renpy.store.get_location_image_key("Entrance", 0)
            updated = renpy.store.get_return_location_image("Entrance", 0, "old_image")
            test_expect_equal(
                updated,
                desired,
                "Expected return image helper to return desired image key."
            )

    testcase return_location_image_preserves:
        description "Return helper should preserve image when already correct."
        python:
            desired = renpy.store.get_location_image_key("Entrance", 0)
            updated = renpy.store.get_return_location_image("Entrance", 0, desired)
            test_expect_equal(
                updated,
                desired,
                "Expected return image helper to keep current image when it matches."
            )
