testsuite registry_tests:
    description "Registry integrity tests."

    testcase location_screens_exist:
        description "All registered location screens exist."
        python:
            for screen_name in renpy.store.get_all_location_screen_names():
                test_expect(
                    renpy.has_screen(screen_name),
                    "Expected screen to exist: " + screen_name
                )

    testcase event_screens_unique:
        description "ALL_EVENT_SCREENS has no duplicates."
        python:
            screens = list(renpy.store.ALL_EVENT_SCREENS)
            test_expect_equal(
                len(screens),
                len(set(screens)),
                "Expected ALL_EVENT_SCREENS to be unique."
            )

    testcase event_blocks_have_labels_when_auto:
        description "Auto-trigger events without screens should have labels."
        python:
            for event in renpy.store.EVENTS.values():
                if event.auto_trigger and not event.screen_name:
                    test_expect(
                        renpy.has_label(event.block),
                        "Expected label for auto-trigger event: " + event.block
                    )
