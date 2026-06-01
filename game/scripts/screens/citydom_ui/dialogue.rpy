init offset = 20

screen say(who, what):
    zorder 10
    $ _display_who = renpy.filter_text_tags(str(who).upper(), allow=[]) if who is not None else None
    $ _display_what = renpy.filter_text_tags(str(what), allow=[])

    fixed:
        xalign 0.5
        ypos 872
        xysize (900, 152)
        at citydom_dialogue_panel_show
        add Frame(citydom_ui_asset("dialogue_glass_panel"), 6, 6, 6, 6)

        fixed:
            xysize (900, 152)

            hbox:
                xpos 392
                ypos 16
                spacing 15

                textbutton _("Back").upper() action Rollback() style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("History").upper() action ShowMenu("history") style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Skip").upper() action Skip() alternate Skip(fast=True, confirm=True) style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Auto").upper() action Preference("auto-forward", "toggle") style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Save").upper() action ShowMenu("save") style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Q.Save").upper() action QuickSave() style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Q.Load").upper() action QuickLoad() style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Settings").upper() action ShowMenu("preferences") style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"
                textbutton _("Hide").upper() action HideInterface() style "citydom_dialogue_quick_button" text_style "citydom_dialogue_quick_button_text"

            if who is not None:
                text who id "who":
                    xpos -2000
                    ypos -2000
                    xsize 1
                    at citydom_dialogue_engine_text_hidden

                text _display_who:
                    style "new_ui_name_text"
                    xpos 36
                    ypos 28
                    xsize 430

                add citydom_dialogue_gradient_name(_display_who):
                    xpos 36
                    ypos 28

                add citydom_ui_asset("dialogue_header_rule"):
                    xpos 36
                    ypos 55

                text what id "what":
                    xpos -2000
                    ypos -2000
                    xsize 1
                    at citydom_dialogue_engine_text_hidden

                text _display_what:
                    style "new_ui_dialogue_text"
                    xpos 36
                    ypos 75
                    xsize 828
                    ysize 44
            else:
                text what id "what":
                    xpos -2000
                    ypos -2000
                    xsize 1
                    at citydom_dialogue_engine_text_hidden

                text _display_what:
                    style "new_ui_dialogue_text"
                    xpos 36
                    ypos 36
                    xsize 828
                    ysize 62

            hbox:
                xpos 760
                ypos 112
                spacing 8
                text _("Continue").upper():
                    style "citydom_dialogue_continue_text"
                add citydom_ui_asset("dialogue_continue_chevron"):
                    ypos 0

screen input(prompt):
    zorder 10
    $ _display_prompt = renpy.filter_text_tags(str(prompt), allow=[])

    fixed:
        xalign 0.5
        ypos 872
        xysize (900, 152)
        at citydom_dialogue_panel_show
        add Frame(citydom_ui_asset("dialogue_glass_panel"), 6, 6, 6, 6)

        fixed:
            xysize (900, 152)

            text _display_prompt.upper():
                style "new_ui_name_text"
                xpos 36
                ypos 28
                xsize 430

            add citydom_dialogue_gradient_name(_display_prompt.upper()):
                xpos 36
                ypos 28

            add citydom_ui_asset("dialogue_header_rule"):
                xpos 36
                ypos 55

            input:
                id "input"
                style "citydom_dialogue_input_text"
                xpos 36
                ypos 76
                xsize 828
                length 24

screen choice(items):
    zorder 20
    default citydom_choice_hover = None

    $ _two_col = len(items) >= 4
    $ _pairs_count = len(items) - (1 if (_two_col and len(items) % 2 == 1) else 0)

    if not _two_col:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            for index, i in enumerate(items):
                use citydom_choice_button(i.caption, i.action, index, citydom_choice_hover, index * 0.06)
    else:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            grid 2 int(_pairs_count / 2):
                spacing 10
                for index, i in enumerate(items[:_pairs_count]):
                    use citydom_choice_button(i.caption, i.action, index, citydom_choice_hover, index * 0.05)

            if _pairs_count < len(items):
                hbox:
                    xalign 0.5
                    use citydom_choice_button(items[-1].caption, items[-1].action, _pairs_count, citydom_choice_hover, _pairs_count * 0.05)

screen citydom_choice_button(caption, action, index, current_hover, delay=0.0):
    $ _hovered = current_hover == index
    $ _choice_color = citydom_color_text_bright if _hovered else citydom_color_text_muted
    button:
        xysize (500, 56)
        background Frame(citydom_ui_asset("choice_glass_hover") if _hovered else citydom_ui_asset("choice_glass_idle"), 6, 6, 6, 6)
        hover_background Frame(citydom_ui_asset("choice_glass_hover"), 6, 6, 6, 6)
        hovered SetScreenVariable("citydom_choice_hover", index)
        unhovered SetScreenVariable("citydom_choice_hover", None)
        action action
        at citydom_choice_button_show(delay)

        text caption:
            xpos 28
            yalign 0.5
            xsize 420
            font citydom_dialogue_font_ui
            size 20
            color _choice_color
            outlines [ (1, citydom_color_shadow, 0, 1) ]

        if _hovered:
            add citydom_ui_asset("dialogue_continue_chevron"):
                xpos 466
                yalign 0.5
