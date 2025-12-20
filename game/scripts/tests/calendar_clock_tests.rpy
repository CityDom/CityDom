testsuite calendar_clock_tests:
    description "Calendar and school clock tests."

    before testcase:
        python:
            renpy.store._test_calendar_state = (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
                renpy.store.school_clock.hour,
                renpy.store.school_clock.period,
                renpy.store.LocationID,
            )

    after testcase:
        python:
            (
                renpy.store.calendar.Day,
                renpy.store.calendar.Hours,
                renpy.store.calendar.period_index,
                renpy.store.school_clock.hour,
                renpy.store.school_clock.period,
                renpy.store.LocationID,
            ) = renpy.store._test_calendar_state
            del renpy.store._test_calendar_state

    testcase calendar_output_format:
        description "Calendar Output uses weekday and zero-padded hour."
        python:
            renpy.store.calendar.Day = 1
            renpy.store.calendar.Hours = 6
            test_expect_equal(
                renpy.store.calendar.Output,
                "Monday 06:00",
                "Expected calendar Output to use weekday and zero-padded hour."
            )

    testcase calendar_period_index_morning:
        description "Calendar period_index is 0 before noon."
        python:
            renpy.store.calendar.Hours = 10
            renpy.store.calendar.update_sub_place_data()
            test_expect_equal(
                renpy.store.calendar.period_index,
                0,
                "Expected period_index to be 0 before noon."
            )

    testcase calendar_period_index_afternoon:
        description "Calendar period_index is 1 during 12-15."
        python:
            renpy.store.calendar.Hours = 13
            renpy.store.calendar.update_sub_place_data()
            test_expect_equal(
                renpy.store.calendar.period_index,
                1,
                "Expected period_index to be 1 during 12-15."
            )

    testcase calendar_period_index_evening:
        description "Calendar period_index is 2 after 16:00."
        python:
            renpy.store.calendar.Hours = 17
            renpy.store.calendar.update_sub_place_data()
            test_expect_equal(
                renpy.store.calendar.period_index,
                2,
                "Expected period_index to be 2 after 16:00."
            )

    testcase school_clock_output_and_break:
        description "School clock output and break flag."
        python:
            renpy.store.school_clock.hour = 12
            renpy.store.school_clock.period = 0
            test_expect_equal(
                renpy.store.school_clock.Output,
                "12:00",
                "Expected school clock output at 12:00 for period 0."
            )
            test_expect_equal(
                renpy.store.school_clock.IsBreak,
                False,
                "Expected IsBreak to be False at period 0."
            )
            renpy.store.school_clock.period = 1
            test_expect_equal(
                renpy.store.school_clock.Output,
                "12:50",
                "Expected school clock output at 12:50 for period 1."
            )
            test_expect_equal(
                renpy.store.school_clock.IsBreak,
                True,
                "Expected IsBreak to be True at period 1."
            )
            renpy.store.school_clock.hour = 13
            renpy.store.school_clock.period = 2
            test_expect_equal(
                renpy.store.school_clock.Output,
                "1:00",
                "Expected school clock output at 1:00 for period 2."
            )
            test_expect_equal(
                renpy.store.school_clock.IsBreak,
                False,
                "Expected IsBreak to be False at period 2."
            )

    testcase school_clock_addtime_at_school:
        description "School clock AddTime increments period/hour at school."
        python:
            renpy.store.school_clock.hour = 12
            renpy.store.school_clock.period = 0
            renpy.store.school_clock.AddTime(at_school=True)
            test_expect_equal(
                renpy.store.school_clock.hour,
                12,
                "Expected hour to remain 12 after first at_school tick."
            )
            test_expect_equal(
                renpy.store.school_clock.period,
                1,
                "Expected period to advance to 1 after first at_school tick."
            )
            renpy.store.school_clock.AddTime(at_school=True)
            test_expect_equal(
                renpy.store.school_clock.hour,
                13,
                "Expected hour to advance to 13 after second at_school tick."
            )
            test_expect_equal(
                renpy.store.school_clock.period,
                2,
                "Expected period to advance to 2 after second at_school tick."
            )

    testcase school_clock_addtime_not_at_school:
        description "School clock AddTime skips periods when not at school."
        python:
            renpy.store.school_clock.hour = 12
            renpy.store.school_clock.period = 0
            renpy.store.school_clock.AddTime(at_school=False)
            test_expect_equal(
                renpy.store.school_clock.hour,
                13,
                "Expected hour to advance to 13 after not_at_school tick."
            )
            test_expect_equal(
                renpy.store.school_clock.period,
                2,
                "Expected period to skip to 2 after not_at_school tick."
            )
