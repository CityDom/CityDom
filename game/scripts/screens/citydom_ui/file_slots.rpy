init offset = 20

screen save():
    tag menu
    use file_slots(_("Save"), "save")

screen load():
    tag menu
    use file_slots(_("Load"), "load")

screen file_slots(title, slot_section):
    $ slot_origin_x = 64
    $ slot_origin_y = 185
    $ slot_gap_x = 612
    $ slot_gap_y = 348
    $ slot_columns = 3
    $ slot_count = 6

    use citydom_menu_backdrop()

    text title.upper():
        xalign 0.5
        ypos 54
        style "citydom_ui_title_text"

    add citydom_ui_asset("chain_divider"):
        xalign 0.5
        ypos 128

    fixed:
        xpos 0
        ypos 0
        at citydom_file_content_show

        for i in range(slot_count):
            $ slot = i + 1
            $ slot_x = slot_origin_x + (i % slot_columns) * slot_gap_x
            $ slot_y = slot_origin_y + int(i / slot_columns) * slot_gap_y
            use citydom_file_slot(slot, slot_x, slot_y, slot_section)

    use citydom_file_pagination()
    use citydom_file_bottom_nav(slot_section)

screen citydom_file_slot(slot, slot_x, slot_y, slot_section):
    default citydom_slot_hovered = False
    $ has_save = FileLoadable(slot)
    $ card_cx = slot_x + 284
    $ card_cy = slot_y + 160

    button:
        style "citydom_ui_card_button"
        xcenter card_cx
        ycenter card_cy
        xysize (568, 320)
        foreground citydom_ui_asset("card_border_default")
        hover_foreground citydom_ui_asset("card_border_hover")
        action FileAction(slot)
        key "save_delete" action FileDelete(slot)
        hovered SetScreenVariable("citydom_slot_hovered", True)
        unhovered SetScreenVariable("citydom_slot_hovered", False)
        at citydom_card_pop

        if has_save:
            add citydom_ui_asset("card_empty_base_opaque")
            add AlphaMask(Transform(FileScreenshot(slot), xysize=(568, 320)), citydom_ui_asset("card_screenshot_mask"))
            add Transform(citydom_ui_asset("card_overlay_default"), alpha=0.82)
            add citydom_ui_asset("card_shadow")

            text FileSaveName(slot):
                xpos 34
                ypos 224
                xsize 500
                style "citydom_ui_slot_name_text"

            text FileTime(slot, format=_("{#file_time}%a, %d %b - %H:%M"), empty=""):
                xpos 24
                ypos 292
                xsize 500
                style "citydom_ui_slot_date_text"
        else:
            add citydom_ui_asset("card_empty_base_opaque")
            add citydom_ui_asset("card_shadow")

            text _("Empty Slot"):
                xalign 0.5
                yalign 0.5
                style "citydom_ui_slot_text"

        if citydom_slot_hovered:
            add citydom_ui_asset("card_hover_chip"):
                xpos 446
                ypos 10

            text (_("Save here") if slot_section == "save" else _("Load save")):
                xpos 446
                ypos 15
                xsize 112
                text_align 0.5
                style "citydom_ui_card_chip_text"

screen citydom_file_pagination():
    $ _page_y = 918
    $ _page_center_y = _page_y + 17
    $ _page_items = [("auto", FilePage("auto")), ("quick", FilePage("quick"))] + [(str(page), FilePage(page)) for page in range(1, 10)]
    $ _page_gap = 53
    $ _page_strip_w = (len(_page_items) - 1) * _page_gap
    $ _page_start_x = int((1920 - _page_strip_w) / 2)
    $ _page_at_first = str(persistent._file_page) == "auto"

    button:
        xpos _page_start_x - 57
        ypos _page_center_y - 16
        xysize (32, 32)
        style "citydom_ui_clear_button"
        action FilePagePrevious()
        add (citydom_ui_asset("page_heart_prev_disabled") if _page_at_first else citydom_ui_asset("page_heart_prev_idle")) xalign 0.5 yalign 0.5

    for _idx, (_page_key, _page_action) in enumerate(_page_items):
        $ _page_cx = _page_start_x + _idx * _page_gap
        $ _page_active = str(persistent._file_page) == _page_key
        $ _page_asset_key = "auto" if _page_key == "auto" else ("quick" if _page_key == "quick" else _page_key)

        button:
            xpos _page_cx - 20
            ypos _page_center_y - 17
            xysize (40, 34)
            style "citydom_ui_clear_button"
            action _page_action

            if _page_active:
                add citydom_ui_asset("page_active_bg") xalign 0.5 yalign 0.5

            add citydom_ui_asset("page_label_%s_%s" % (_page_asset_key, "active" if _page_active else "idle")):
                xalign 0.5
                yalign 0.5

    button:
        xpos _page_start_x + (len(_page_items) - 1) * _page_gap + 25
        ypos _page_center_y - 16
        xysize (32, 32)
        style "citydom_ui_clear_button"
        action FilePageNext()
        add citydom_ui_asset("page_heart_next_idle") xalign 0.5 yalign 0.5

screen citydom_file_bottom_nav(slot_section):
    $ _nav_w = 900
    $ _nav_cell_w = 150
    $ _nav_x = int((1920 - _nav_w) / 2)
    $ _nav_y = 987
    $ _nav_items = [
        ("save", _("Save"), ShowMenu("save"), 14),
        ("load", _("Load"), ShowMenu("load"), 14),
        ("settings", _("Settings"), ShowMenu("preferences"), 14),
        ("main_menu", _("Main Menu"), Return() if main_menu else MainMenu(), 12),
        ("quit", _("Quit"), ShowMenu("custom_quit_screen"), 14),
        ("return", _("Return"), Return(), 14),
    ]
    $ _nav_ids = [item[0] for item in _nav_items]
    $ _active_index = _nav_ids.index(slot_section) if slot_section in _nav_ids else 0
    $ _previous_index = _nav_ids.index(citydom_bottom_nav_previous_id) if citydom_bottom_nav_previous_id in _nav_ids else _active_index
    $ _indicator_start_x = _nav_x + _previous_index * _nav_cell_w
    $ _indicator_end_x = _nav_x + _active_index * _nav_cell_w

    add citydom_ui_asset("bottom_nav_base") xpos _nav_x ypos _nav_y
    add citydom_ui_asset("nav_item_active_glow") ypos _nav_y at citydom_bottom_nav_active_motion(_indicator_start_x, _indicator_end_x)

    if citydom_bottom_nav_previous_id != slot_section:
        timer 0.32 action SetVariable("citydom_bottom_nav_previous_id", slot_section)

    for _divider_index in range(1, len(_nav_items)):
        add citydom_ui_asset("nav_divider") xpos (_nav_x + _divider_index * _nav_cell_w - 6) ypos (_nav_y + 18)

    for _idx, (_nav_id, _label, _action, _text_size) in enumerate(_nav_items):
        $ _active = (_nav_id == slot_section)
        $ _item_x = _nav_x + _idx * _nav_cell_w

        add citydom_ui_asset("nav_icon_%s_%s" % (_nav_id, "active" if _active else "idle")):
            xpos _item_x + 63
            ypos _nav_y + 16

        text _label.upper():
            xcenter _item_x + int(_nav_cell_w / 2)
            ypos _nav_y + 44
            font citydom_font_ui
            size _text_size
            kerning 0
            color (citydom_color_primary_muted if _active else citydom_color_nav_idle)

        button:
            xpos _item_x
            ypos _nav_y
            xysize (_nav_cell_w, 72)
            background None
            action _action
