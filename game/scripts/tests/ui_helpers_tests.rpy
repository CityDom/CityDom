testsuite ui_helpers_tests:
    description "UI helper tests."

    before testcase:
        python:
            renpy.store._test_ui_state = (
                renpy.store.MapScreenShown,
                renpy.store.StatsScreenShown,
            )

    after testcase:
        python:
            (
                renpy.store.MapScreenShown,
                renpy.store.StatsScreenShown,
            ) = renpy.store._test_ui_state
            del renpy.store._test_ui_state

    testcase should_show_room_buttons_flag:
        description "Room button visibility respects map/stats flags."
        python:
            renpy.store.MapScreenShown = False
            renpy.store.StatsScreenShown = False
            test_expect_equal(
                renpy.store.should_show_room_buttons(),
                True,
                "Expected buttons to show when map/stats are hidden."
            )
            renpy.store.MapScreenShown = True
            test_expect_equal(
                renpy.store.should_show_room_buttons(),
                False,
                "Expected buttons to hide when map is shown."
            )
            renpy.store.MapScreenShown = False
            renpy.store.StatsScreenShown = True
            test_expect_equal(
                renpy.store.should_show_room_buttons(),
                False,
                "Expected buttons to hide when stats are shown."
            )
