init offset = 20

screen preferences():
    tag menu

    $ _outer_pad = 48
    $ _panel_gap = 20
    $ _panel_w = int((1920 - (_outer_pad * 2 + _panel_gap)) / 2)
    $ _inner_pad = 24
    $ _control_w = _panel_w - (_inner_pad * 2)
    $ _left_x = _outer_pad
    $ _right_x = _left_x + _panel_w + _panel_gap
    $ _top_y = 155
    $ _bottom_y = 355

    use citydom_menu_backdrop()

    text _("Settings").upper():
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

        use citydom_settings_panel(_left_x, _top_y, _panel_w, 160)
        use citydom_settings_panel(_right_x, _top_y, _panel_w, 160)
        use citydom_settings_panel(_left_x, _bottom_y, _panel_w, 190)
        use citydom_settings_panel(_right_x, _bottom_y, _panel_w, 190)

        text _("Display").upper() xpos (_left_x + _inner_pad) ypos (_top_y + 24) style "citydom_settings_section_text"
        use citydom_settings_radio(_left_x + _inner_pad, _top_y + 62, _("Window"), Preference("display", "window"), "monitor")
        use citydom_settings_radio(_left_x + _inner_pad, _top_y + 102, _("Fullscreen"), Preference("display", "fullscreen"), "maximize_2")

        text _("Skip").upper() xpos (_right_x + _inner_pad) ypos (_top_y + 24) style "citydom_settings_section_text"
        use citydom_settings_check(_right_x + _inner_pad, _top_y + 50, _("Unseen Text"), Preference("skip", "toggle"))
        use citydom_settings_check(_right_x + _inner_pad, _top_y + 82, _("After Choices"), Preference("after choices", "toggle"))
        use citydom_settings_check(_right_x + _inner_pad, _top_y + 114, _("Transitions"), InvertSelected(Preference("transitions", "toggle")))

        use citydom_settings_slider(_left_x + _inner_pad, _bottom_y + 34, _("Text Speed"), Preference("text speed"), "type", _control_w)
        use citydom_settings_slider(_left_x + _inner_pad, _bottom_y + 110, _("Auto-Forward Time"), Preference("auto-forward time"), "fast_forward", _control_w)

        if config.has_music:
            use citydom_settings_slider(_right_x + _inner_pad, _bottom_y + 30, _("Music"), Preference("music volume"), "volume_2", _control_w)

        if config.has_sound:
            use citydom_settings_slider(_right_x + _inner_pad, _bottom_y + 88, _("Sound"), Preference("sound volume"), "volume_2", _control_w)

        add Solid(citydom_color_settings_divider, xysize=(_control_w, 1)) xpos (_right_x + _inner_pad) ypos (_bottom_y + 142)
        use citydom_settings_switch(_right_x + _inner_pad, _bottom_y + 150, _("Mute All"), Preference("all mute", "toggle"), "volume_x", _control_w)

        add Transform(citydom_ui_asset("settings_icon_skip_forward_muted"), xysize=(16, 16)) xpos 700 ypos 596
        text _("Changes apply immediately - No restart required"):
            xpos 724
            ypos 596
            style "citydom_settings_note_text"

    use citydom_file_bottom_nav("settings")
