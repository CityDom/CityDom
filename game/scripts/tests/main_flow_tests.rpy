testsuite main_flow_tests:
    description "Main flow sanity tests."

    testcase main_flow_labels_exist:
        description "Core labels exist."
        python:
            test_expect(
                renpy.has_label("start"),
                "Expected 'start' label to exist."
            )
            test_expect(
                renpy.has_label("GameLoop"),
                "Expected 'GameLoop' label to exist."
            )
