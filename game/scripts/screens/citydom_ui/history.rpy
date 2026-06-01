init offset = 20

screen history():
    tag menu
    predict False
    default citydom_history_adjustment = ui.adjustment()
    $ _current_history_scene = citydom_history_scene_id
    $ _history_items = [h for h in _history_list if getattr(h, "citydom_scene_id", None) == _current_history_scene]

    add citydom_ui_asset("main_bg_3")
    add Solid(citydom_color_history_overlay_dark)
    add Solid(citydom_color_history_overlay_purple)
    add citydom_ui_asset("history_pattern_overlay")

    text _("History").upper():
        xalign 0.5
        ypos 42
        style "citydom_history_title_text"

    add citydom_ui_asset("chain_divider"):
        xalign 0.5
        ypos 101

    viewport:
        id "citydom_history_viewport"
        xpos 530
        ypos 135
        xysize (860, 760)
        mousewheel True
        draggable True
        pagekeys True
        yinitial 1.0
        yadjustment citydom_history_adjustment

        vbox:
            xsize 860
            spacing 18

            if _history_items:
                for _index, h in enumerate(_history_items):
                    $ _what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    $ _who = renpy.filter_text_tags(str(h.who).upper(), allow=[]) if h.who else None
                    $ _who_color = h.who_args.get("color", citydom_color_history_name) if h.who else citydom_color_history_name

                    if _who:
                        frame:
                            xsize 860
                            yminimum 62
                            background Frame(citydom_ui_asset("history_entry_bg"), 6, 6, 6, 6)
                            padding (30, 16, 30, 16)

                            hbox:
                                spacing 22
                                yfit True
                                yalign 0.5

                                text _who:
                                    style "citydom_history_name_text"
                                    color _who_color
                                    xsize 155
                                    yalign 0.5

                                text _what:
                                    style "citydom_history_body_text"
                                    xsize 610
                                    yalign 0.5
                                    substitute False
                    else:
                        text _what:
                            xalign 0.5
                            xsize 860
                            style "citydom_history_narration_text"
                            substitute False

                    if _index < len(_history_items) - 1:
                        add citydom_ui_asset("history_dots"):
                            xalign 0.5
            else:
                null height 260
                text _("The dialogue history is empty."):
                    xalign 0.5
                    xsize 860
                    style "citydom_history_empty_text"

    fixed:
        xcenter 960
        ypos 974
        xysize (205, 72)
        add citydom_ui_asset("history_footer_bg")

        textbutton _("Top").upper():
            xpos 8
            ypos 13
            style "citydom_history_footer_button"
            text_style "citydom_history_footer_button_text"
            action Scroll("citydom_history_viewport", "vertical decrease", 1000000, delay=0.2)

        textbutton _("Return").upper():
            xpos 105
            ypos 13
            style "citydom_history_footer_button"
            text_style "citydom_history_footer_button_text"
            action Return()

    key "game_menu" action Return()
