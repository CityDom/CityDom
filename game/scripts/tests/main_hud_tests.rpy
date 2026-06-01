testsuite main_hud_logic_tests:
    description "Main HUD helper logic tests."

    before testcase:
        python:
            renpy.store._test_mainhud_state = (
                renpy.store.LocationID,
                renpy.store.calendar.Hours,
                renpy.store.calendar.Day,
                renpy.store.ShowPhone,
                renpy.store.ShowInventory,
                renpy.store.ShowCallForSidebar,
                renpy.store.Messanger,
                renpy.store.ShowConversationScreen,
                renpy.store.showWallpaperScreen,
                renpy.store.showWallpaperPreview,
            )

    after testcase:
        python:
            (
                renpy.store.LocationID,
                renpy.store.calendar.Hours,
                renpy.store.calendar.Day,
                renpy.store.ShowPhone,
                renpy.store.ShowInventory,
                renpy.store.ShowCallForSidebar,
                renpy.store.Messanger,
                renpy.store.ShowConversationScreen,
                renpy.store.showWallpaperScreen,
                renpy.store.showWallpaperPreview,
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
            renpy.store.calendar.Day = 1
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
            renpy.store.calendar.Day = 6
            renpy.store.calendar.Hours = 6
            test_expect_equal(
                renpy.store.is_in_school_hours(),
                False,
                "Expected is_in_school_hours to be False on weekend."
            )

    testcase main_hud_school_hours_minusone:
        description "is_in_school_hours_minusONE boundaries."
        python:
            renpy.store.calendar.Day = 1
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

    testcase main_hud_panel_toggle_resets_other_panels:
        description "Panel toggles should reset competing HUD panels."
        python:
            renpy.store.set_hud_panels(
                ShowInventory=True,
                ShowCallForSidebar=True,
                Messanger=True,
            )
            renpy.store.toggle_hud_panel("ShowPhone")
            test_expect_equal(
                renpy.store.ShowPhone,
                True,
                "Expected phone panel to be enabled after toggle."
            )
            test_expect_equal(
                renpy.store.ShowInventory,
                False,
                "Expected inventory panel to be cleared by phone toggle."
            )
            test_expect_equal(
                renpy.store.ShowCallForSidebar,
                False,
                "Expected sidebar panel to be cleared by phone toggle."
            )
            test_expect_equal(
                renpy.store.Messanger,
                False,
                "Expected messenger panel to be cleared by phone toggle."
            )

    testcase main_hud_hotspots_blocked_by_overlay_panels:
        description "HUD room hotspots should be disabled while overlays are open."
        python:
            renpy.store.set_hud_panels()
            test_expect_equal(
                renpy.store.can_use_hud_hotspots(),
                True,
                "Expected HUD hotspots to be available with no overlays."
            )
            renpy.store.set_hud_panels(ShowPhone=True)
            test_expect_equal(
                renpy.store.can_use_hud_hotspots(),
                False,
                "Expected HUD hotspots to be blocked while the phone is open."
            )
