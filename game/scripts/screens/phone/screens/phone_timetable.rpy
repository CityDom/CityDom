default citydom_calendar_closing = False
default citydom_schedule_selected_day = "Fri"

init python:
    CITYDOM_SCHEDULE_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")
    CITYDOM_SCHEDULE_PERIODS = (
        ("12pm", "12pm"),
        ("1pm", "1pm"),
        ("2pm", "2pm"),
        ("3pm", "3pm"),
        ("4pm", "4pm"),
        ("5pm", "5pm"),
    )
    CITYDOM_SCHEDULE_CLASSES = {
        "English": {"abbr": "Eng", "color": "#82a0ff", "asset": "english"},
        "Art": {"abbr": "Art", "color": "#ffb946", "asset": "art"},
        "Manners": {"abbr": "Man", "color": "#e879a0", "asset": "manners"},
        "Biology": {"abbr": "Bio", "color": "#50d28c", "asset": "biology"},
        "Gym": {"abbr": "Gym", "color": "#3cd2d2", "asset": "gym"},
        "Pool": {"abbr": "Pool", "color": "#50aaff", "asset": "pool"},
        "Detention": {"abbr": "Det", "color": "#e65a5a", "asset": "detention"},
    }
    CITYDOM_WEEKLY_SCHEDULE = {
        "Mon": {"12pm": "English", "1pm": "Art", "2pm": "Manners", "3pm": "Biology", "4pm": "Gym", "5pm": "Detention"},
        "Tue": {"12pm": "English", "1pm": "Art", "2pm": "Manners", "3pm": "Biology", "4pm": "Pool", "5pm": "Detention"},
        "Wed": {"12pm": "English", "1pm": "Art", "2pm": "Manners", "3pm": "Biology", "4pm": "Gym", "5pm": "Detention"},
        "Thu": {"12pm": "English", "1pm": "Art", "2pm": "Manners", "3pm": "Biology", "4pm": "Pool", "5pm": "Detention"},
        "Fri": {"12pm": "English", "1pm": "Art", "2pm": "Manners", "3pm": "Biology", "4pm": "Gym", "5pm": "Detention"},
    }

    def citydom_schedule_today_key():
        day_index = int(getattr(store.calendar, "Day", 5))
        return {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri"}.get(day_index, "Fri")

    def citydom_schedule_class(day, period):
        class_name = CITYDOM_WEEKLY_SCHEDULE.get(day, {}).get(period)
        if not class_name:
            return None
        data = CITYDOM_SCHEDULE_CLASSES[class_name].copy()
        data["subject"] = class_name
        return data

    def citydom_calendar_back_to_phone():
        store.ShowPhone = True
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_home_returning = True
        store.citydom_calendar_closing = True
        renpy.restart_interaction()

    def citydom_calendar_finish_close():
        store.ShowCalendarScreen = False
        store.citydom_calendar_closing = False
        renpy.restart_interaction()

transform citydom_calendar_screen_show:
    subpixel True
    alpha 0.0
    xoffset 340
    warp citydom_hud_curve 0.32 alpha 1.0 xoffset 0

transform citydom_calendar_screen_hide:
    subpixel True
    alpha 1.0
    xoffset 0
    warp citydom_hud_curve 0.30 alpha 0.0 xoffset 340

transform citydom_calendar_row_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        xoffset -10
        pause 0.05 + (index * 0.04)
        warp citydom_hud_curve 0.22 alpha 1.0 xoffset 0

style citydom_schedule_title_text is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 18
    color "#ffe6fb"
    outlines [ (1, "#ff5bd680", 0, 0) ]
    kerning 8

style citydom_schedule_label_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 10
    bold True
    color "#e6d0f7e6"
    outlines [ (1, "#06001080", 0, 0) ]
    kerning 2

style citydom_schedule_small_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 9
    bold True
    color "#d9c1efdd"
    outlines [ (1, "#06001080", 0, 0) ]

screen citydom_schedule_day_tab(day, index, today):
    $ _selected = citydom_schedule_selected_day == day
    $ _bg = "gui/citydom_ui_v2/phone_schedule_day_active.png" if _selected else "gui/citydom_ui_v2/phone_schedule_day_idle.png"
    $ _day_color = "#b4cdfff2" if _selected else "#a0aadca6"
    button:
        xpos 19 + (index * 61)
        ypos 134
        xysize (52, 34)
        background _bg
        hover_background "gui/citydom_ui_v2/phone_schedule_day_active.png"
        action SetVariable("citydom_schedule_selected_day", day)
        text day:
            xalign 0.5
            yalign 0.5
            style "citydom_schedule_label_text"
            size 9
            color _day_color

screen citydom_schedule_grid(today):
    $ _selected_index = CITYDOM_SCHEDULE_DAYS.index(citydom_schedule_selected_day) if citydom_schedule_selected_day in CITYDOM_SCHEDULE_DAYS else 4
    $ _grid_cols = ((36, 52), (88, 53), (141, 53), (194, 53), (247, 53))
    $ _grid_rows = ((25, 32), (57, 32), (89, 32), (121, 32), (153, 32), (185, 29))
    fixed:
        xpos 20
        ypos 192
        xysize (300, 214)
        add "gui/citydom_ui_v2/phone_schedule_grid_bg.png"
        add Solid("#ff5bd620", xysize=(_grid_cols[_selected_index][1], 194)):
            xpos _grid_cols[_selected_index][0]
            ypos 20

        for day_index, day in enumerate(CITYDOM_SCHEDULE_DAYS):
            $ _header_color = "#e879a0e6" if today == day else ("#b4cdffe6" if citydom_schedule_selected_day == day else "#8291be99")
            fixed:
                xpos _grid_cols[day_index][0]
                ypos 0
                xysize (_grid_cols[day_index][1], 20)
                text day:
                    xalign 0.5
                    yalign 0.5
                    style "citydom_schedule_small_text"
                    size 8
                    color _header_color

        for period_index, (period_id, period_label) in enumerate(CITYDOM_SCHEDULE_PERIODS):
            $ _row_y = _grid_rows[period_index][0]
            $ _row_h = _grid_rows[period_index][1]
            fixed:
                xpos 0
                ypos _row_y
                xysize (36, _row_h)
                text period_label:
                    xalign 0.5
                    yalign 0.5
                    style "citydom_schedule_small_text"
                    size 8
                    color "#d9c1efc8"
            for day_index, day in enumerate(CITYDOM_SCHEDULE_DAYS):
                $ _slot = citydom_schedule_class(day, period_id)
                if _slot:
                    fixed:
                        xpos _grid_cols[day_index][0]
                        ypos _row_y
                        xysize (_grid_cols[day_index][1], _row_h)
                        add "gui/citydom_ui_v2/phone_schedule_mini_%s.png" % _slot["asset"]:
                            xalign 0.5
                            yalign 0.5
                        text _slot["abbr"]:
                            xalign 0.5
                            yalign 0.5
                            style "citydom_schedule_small_text"
                            size 8
                            color _slot["color"]

screen citydom_schedule_row(period_id, period_label, class_name, index):
    $ _class = CITYDOM_SCHEDULE_CLASSES[class_name]
    button:
        xpos 0
        ypos index * 54
        xysize (300, 44)
        background "gui/citydom_ui_v2/phone_schedule_row_%s.png" % _class["asset"]
        hover_background "gui/citydom_ui_v2/phone_schedule_row_%s.png" % _class["asset"]
        at citydom_calendar_row_motion(index)
        action NullAction()
        text period_label:
            xpos 12
            yalign 0.5
            xsize 44
            text_align 1.0
            style "citydom_schedule_label_text"
            size 9
            color "#e6d0f7e6"
        add Solid(citydom_details_hex_rgba(_class["color"], 0.42), xysize=(1, 24)):
            xpos 66
            ypos 10
        text class_name:
            xpos 82
            yalign 0.5
            xsize 170
            style "citydom_schedule_label_text"
            size 12
            color _class["color"]
        add Solid(citydom_details_hex_rgba(_class["color"], 0.65), xysize=(6, 6)):
            xpos 274
            ypos 19

screen TimeTableScreen():
    $ _today = citydom_schedule_today_key()
    $ _schedule = CITYDOM_WEEKLY_SCHEDULE.get(citydom_schedule_selected_day, {})

    if citydom_calendar_closing:
        timer 0.32 action Function(citydom_calendar_finish_close)

    if not ShowPhone:
        fixed:
            at citydom_phone_overlay_static
            add "gui/citydom_ui_v2/phone_overlay_dim.png"

    fixed:
        xpos CITYDOM_PHONE_X + (CITYDOM_PHONE_W // 2)
        ypos CITYDOM_PHONE_Y + (CITYDOM_PHONE_H // 2)
        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
        at citydom_phone_frame_static

        viewport:
            xpos 0
            ypos 0
            xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
            draggable False
            mousewheel False
            scrollbars None
            child_size (CITYDOM_PHONE_W, CITYDOM_PHONE_H)

            fixed:
                xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                if citydom_calendar_closing:
                    at citydom_calendar_screen_hide
                else:
                    at citydom_calendar_screen_show

                add "gui/citydom_ui_v2/phone_inventory_bg.png"

                imagebutton:
                    idle "gui/citydom_ui_v2/phone_inventory_back_idle.png"
                    hover "gui/citydom_ui_v2/phone_inventory_back_hover.png"
                    xpos 20
                    ypos 54
                    action Function(citydom_calendar_back_to_phone)

                text _("Schedule"):
                    xcenter 170
                    ypos 56
                    style "citydom_schedule_title_text"

                add "gui/citydom_ui_v2/chain_divider_phone.png":
                    xcenter 170
                    ypos 104

                for index, day in enumerate(CITYDOM_SCHEDULE_DAYS):
                    use citydom_schedule_day_tab(day, index, _today)

                use citydom_schedule_grid(_today)

                fixed:
                    xpos 20
                    ypos 422
                    xysize (300, 22)
                    add Solid("#c084d44a", xysize=(95, 1)):
                        xpos 0
                        ypos 10
                    text ("TODAY" if citydom_schedule_selected_day == _today else citydom_schedule_selected_day.upper()):
                        xcenter 150
                        ypos 3
                        style "citydom_schedule_label_text"
                        size 8
                        color "#ff8df8cc"
                    add Solid("#c084d44a", xysize=(95, 1)):
                        xpos 205
                        ypos 10

                viewport:
                    xpos 20
                    ypos 452
                    xysize (300, 196)
                    mousewheel True
                    draggable True
                    scrollbars None

                    fixed:
                        xysize (300, 324)
                        for row_index, (period_id, period_label) in enumerate(CITYDOM_SCHEDULE_PERIODS):
                            if period_id in _schedule:
                                use citydom_schedule_row(period_id, period_label, _schedule[period_id], row_index)

        add "gui/citydom_ui_v2/phone_dynamic_island.png":
            xpos 126
            ypos 14

        add "gui/citydom_ui_v2/phone_status_pill.png":
            xpos 20
            ypos 8

        text citydom_phone_time_text():
            xpos 31
            ypos 13
            style "citydom_phone_status_text"

        add "gui/citydom_ui_v2/phone_status_icons_pill.png":
            xpos 248
            ypos 8
