testsuite room_screen_tests:
    description "Room screen scene selection smoke tests."

    testcase jennifer_weekday_event_at_6am:
        description "Jennifer weekday 6 AM should return the event scene."
        python:
            scene_def = renpy.store.select_room_scene(
                renpy.store.HOUR_6AM,
                renpy.store.JENNIFER_ROOM_WEEKDAY_EVENTS,
                "day",
                "evening",
                "night",
            )
            test_expect_equal(
                scene_def["button"]["jump"],
                "JenniferMorningEvent14",
                "Expected Jennifer 6 AM event jump."
            )

    testcase jennifer_weekday_day_background:
        description "Jennifer weekday day hours should return day background."
        python:
            scene_def = renpy.store.select_room_scene(
                renpy.store.HOUR_3PM,
                renpy.store.JENNIFER_ROOM_WEEKDAY_EVENTS,
                "day",
                "evening",
                "night",
            )
            test_expect_equal(
                scene_def["bg"],
                "day",
                "Expected day background for afternoon hours."
            )

    testcase isabella_weekend_event_at_6am:
        description "Isabella weekend 6 AM should return the event scene."
        python:
            scene_def = renpy.store.select_room_scene(
                renpy.store.HOUR_6AM,
                renpy.store.ISABELLA_ROOM_WEEKEND_EVENTS,
                "day",
                "evening",
                "night",
            )
            test_expect_equal(
                scene_def["button"]["jump"],
                "Isabella_weekend_6AM",
                "Expected Isabella weekend 6 AM event jump."
            )
