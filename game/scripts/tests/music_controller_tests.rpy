testsuite music_controller_tests:
    description "Music controller selection tests."

    before testcase:
        python:
            renpy.store._test_music_state = (
                getattr(renpy.store, "main_menu", None),
                getattr(renpy.store, "force_music_in_tests", None),
                renpy.store.calendar.Hours,
            )

    after testcase:
        python:
            (
                renpy.store.main_menu,
                renpy.store.force_music_in_tests,
                renpy.store.calendar.Hours,
            ) = renpy.store._test_music_state
            del renpy.store._test_music_state

    testcase music_track_by_time:
        description "Music selection matches morning/afternoon/night."
        python:
            renpy.store.main_menu = False
            renpy.store.force_music_in_tests = True
            renpy.store.calendar.Hours = renpy.store.HOUR_6AM
            test_expect_equal(
                renpy.store._get_time_music_track(),
                renpy.store.MUSIC_TRACKS[0],
                "Expected morning track at 6 AM."
            )
            renpy.store.calendar.Hours = renpy.store.HOUR_2PM
            test_expect_equal(
                renpy.store._get_time_music_track(),
                renpy.store.MUSIC_TRACKS[1],
                "Expected afternoon track at 2 PM."
            )
            renpy.store.calendar.Hours = renpy.store.HOUR_6PM
            test_expect_equal(
                renpy.store._get_time_music_track(),
                renpy.store.MUSIC_TRACKS[2],
                "Expected night track at 6 PM."
            )

    testcase music_disabled_on_main_menu:
        description "Main menu disables background music selection."
        python:
            renpy.store.main_menu = True
            renpy.store.force_music_in_tests = False
            renpy.store.calendar.Hours = renpy.store.HOUR_6AM
            test_expect_equal(
                renpy.store._get_time_music_track(),
                None,
                "Expected no track on main menu."
            )
