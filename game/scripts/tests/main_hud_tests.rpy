testsuite main_hud_logic_tests:
    description "Main HUD helper logic tests."

    before testcase:
        python:
            renpy.store._test_mainhud_state = (
                renpy.store.LocationID,
                renpy.store.calendar.Hours,
            )

    after testcase:
        python:
            (
                renpy.store.LocationID,
                renpy.store.calendar.Hours,
            ) = renpy.store._test_mainhud_state
            del renpy.store._test_mainhud_state

    testcase main_hud_is_in_school:
        description "is_in_school reflects LocationID."
        python:
            renpy.store.LocationID = 1
            test_expect_equal(
                renpy.store.is_in_school(renpy.store.LocationID),
                True,
                "Expected is_in_school to be True when LocationID is 1."
            )
            renpy.store.LocationID = 0
            test_expect_equal(
                renpy.store.is_in_school(renpy.store.LocationID),
                False,
                "Expected is_in_school to be False when LocationID is 0."
            )

    testcase main_hud_school_hours:
        description "is_in_school_hours boundaries."
        python:
            renpy.store.calendar.Hours = 6
            test_expect_equal(
                renpy.store.is_in_school_hours(),
                True,
                "Expected is_in_school_hours to be True at 6."
            )
            renpy.store.calendar.Hours = 11
            test_expect_equal(
                renpy.store.is_in_school_hours(),
                True,
                "Expected is_in_school_hours to be True at 11."
            )
            renpy.store.calendar.Hours = 5
            test_expect_equal(
                renpy.store.is_in_school_hours(),
                False,
                "Expected is_in_school_hours to be False at 5."
            )
            renpy.store.calendar.Hours = 12
            test_expect_equal(
                renpy.store.is_in_school_hours(),
                False,
                "Expected is_in_school_hours to be False at 12."
            )

    testcase main_hud_school_hours_minusone:
        description "is_in_school_hours_minusONE boundaries."
        python:
            renpy.store.calendar.Hours = 10
            test_expect_equal(
                renpy.store.is_in_school_hours_minusONE(),
                True,
                "Expected is_in_school_hours_minusONE to be True at 10."
            )
            renpy.store.calendar.Hours = 11
            test_expect_equal(
                renpy.store.is_in_school_hours_minusONE(),
                False,
                "Expected is_in_school_hours_minusONE to be False at 11."
            )
