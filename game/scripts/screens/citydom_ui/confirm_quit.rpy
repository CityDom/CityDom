init offset = 20

screen custom_quit_screen():
    tag menu

    add citydom_legacy_ui_asset("quit")

    button:
        xpos 940
        ypos 945
        xysize (230, 80)
        background None
        hover_background citydom_color_button_hover_soft
        action Return()

    button:
        xpos 1380
        ypos 945
        xysize (230, 80)
        background None
        hover_background citydom_color_button_hover_soft
        action Quit(confirm=False)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    default new_ui_confirm_hover = None

    add Solid(citydom_color_confirm_overlay) at citydom_confirm_overlay_fade

    fixed:
        xcenter 960
        ycenter 540
        xysize (600, 300)
        at citydom_confirm_panel_show

        add citydom_ui_asset("dialog_bg")

        add citydom_ui_asset("dialog_heart"):
            xalign 0.5
            ypos 60

        text message:
            xalign 0.5
            ypos 118
            xsize 500
            text_align 0.5
            font citydom_font_serif_italic
            size 26
            color citydom_color_confirm_message
            line_spacing 4
            outlines [ ]

        button:
            style "citydom_ui_card_button"
            xcenter 210
            ycenter 214
            xysize (140, 48)
            idle_background citydom_ui_asset("dialog_button_yes_idle")
            hover_background citydom_ui_asset("dialog_button_yes_hover")
            hovered SetScreenVariable("new_ui_confirm_hover", "yes")
            unhovered SetScreenVariable("new_ui_confirm_hover", None)
            action yes_action
            at citydom_confirm_button_pop

            text _("YES"):
                xalign 0.5
                yalign 0.5
                font citydom_font_ui
                size 15
                kerning 4
                color citydom_color_confirm_yes
                outlines [ ]

        button:
            style "citydom_ui_card_button"
            xcenter 390
            ycenter 214
            xysize (140, 48)
            idle_background citydom_ui_asset("dialog_button_no_idle")
            hover_background citydom_ui_asset("dialog_button_no_hover")
            hovered SetScreenVariable("new_ui_confirm_hover", "no")
            unhovered SetScreenVariable("new_ui_confirm_hover", None)
            action no_action
            at citydom_confirm_button_pop

            text _("NO"):
                xalign 0.5
                yalign 0.5
                font citydom_font_ui
                size 15
                kerning 4
                color (citydom_color_confirm_no_hover if new_ui_confirm_hover == "no" else citydom_color_confirm_no_idle)
                outlines [ ]

    key "game_menu" action no_action
