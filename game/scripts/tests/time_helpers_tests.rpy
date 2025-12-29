testsuite time_helpers_tests:
    description "Time helper and mapping tests."

    testcase time_to_real_hour_mapping:
        description "Game hour mapping converts to real hours."
        python:
            test_expect_equal(
                renpy.store.to_real_hour(renpy.store.HOUR_6AM),
                6,
                "Expected HOUR_6AM to map to real 6."
            )
            test_expect_equal(
                renpy.store.to_real_hour(renpy.store.HOUR_2PM),
                14,
                "Expected HOUR_2PM to map to real 14."
            )
            test_expect_equal(
                renpy.store.from_real_hour(14),
                renpy.store.HOUR_2PM,
                "Expected real 14 to map back to HOUR_2PM."
            )

    testcase time_windows:
        description "Window helper handles exclusive and inclusive ranges."
        python:
            test_expect_equal(
                renpy.store.is_in_window(renpy.store.HOUR_6AM, renpy.store.HOUR_6AM, renpy.store.HOUR_8AM),
                True,
                "Expected inclusive start to pass for HOUR_6AM."
            )
            test_expect_equal(
                renpy.store.is_in_window(renpy.store.HOUR_8AM, renpy.store.HOUR_6AM, renpy.store.HOUR_8AM),
                False,
                "Expected exclusive end to block HOUR_8AM."
            )
            test_expect_equal(
                renpy.store.is_in_window(renpy.store.HOUR_8AM, renpy.store.HOUR_6AM, renpy.store.HOUR_8AM, inclusive_end=True),
                True,
                "Expected inclusive end to allow HOUR_8AM."
            )

    testcase time_of_day_helpers:
        description "Day/evening/night helpers match thresholds."
        python:
            test_expect_equal(
                renpy.store.is_day_hour(renpy.store.HOUR_11AM),
                True,
                "Expected day hour before 2 PM."
            )
            test_expect_equal(
                renpy.store.is_evening_hour(renpy.store.HOUR_6PM),
                True,
                "Expected evening hour at 6 PM."
            )
            test_expect_equal(
                renpy.store.is_night_hour(renpy.store.HOUR_10PM),
                True,
                "Expected night hour after 10 PM."
            )
