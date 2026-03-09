testsuite sleep_event_tests:
    description "Sleep event location gating tests."

    before testcase:
        python:
            renpy.store._test_sleep_location = renpy.store.Location

    after testcase:
        python:
            renpy.store.Location = renpy.store._test_sleep_location
            del renpy.store._test_sleep_location

    testcase sleep_allowed_in_mc_room:
        description "Sleep button should accept the normalized MC room location."
        python:
            renpy.store.Location = "My room"
            test_expect_equal(
                renpy.store.can_sleep_in_current_room(),
                True,
                "Expected sleep to be allowed in the MC room."
            )

    testcase sleep_blocked_outside_mc_room:
        description "Sleep button should reject other locations."
        python:
            renpy.store.Location = "Entrance"
            test_expect_equal(
                renpy.store.can_sleep_in_current_room(),
                False,
                "Expected sleep to be blocked outside the MC room."
            )
