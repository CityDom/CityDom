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

    testcase housefront_8pm_uses_dedicated_history_bucket:
        description "Housefront 8 PM should not reuse the 7 AM rotation history."
        python:
            scene_def = renpy.store.get_housefront_scene(renpy.store.HOUR_8PM)
            button = scene_def["buttons"][0]
            test_expect_equal(
                button["history_key"],
                "housefront_8PM",
                "Expected 8 PM housefront scene rotation to use its own history key."
            )

    testcase livingroom_midnight_uses_midnight_history:
        description "Living room midnight rotation should use the 12 AM history bucket."
        python:
            scene_def = renpy.store.get_livingroom_scene(1, renpy.store.HOUR_12AM)
            button = scene_def["buttons"][0]
            test_expect_equal(
                button["history_key"],
                "livingroom_12AM",
                "Expected midnight living room scene rotation to use the 12 AM history key."
            )

    testcase livingroom_weekend_uses_time_background:
        description "Weekend living room fallback should respect time of day."
        python:
            scene_def = renpy.store.get_livingroom_scene(6, renpy.store.HOUR_9PM)
            test_expect_equal(
                scene_def["bg"],
                "HomeSubplace/LivingRoom evening.png",
                "Expected weekend fallback background to use the evening variant."
            )
