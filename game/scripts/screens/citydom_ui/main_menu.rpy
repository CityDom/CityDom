init offset = 20

screen main_menu():
    tag menu
    default new_ui_main_hover = None

    add gui.main_menu_background at citydom_main_bg_fade

    for _dust_x, _dust_y, _dust_size, _dust_alpha, _dust_duration in [
        (346, 238, 2, 0.35, 4.2),
        (1421, 151, 2, 0.25, 5.1),
        (1651, 626, 3, 0.20, 3.8),
        (730, 734, 2, 0.18, 6.0),
        (1114, 108, 2, 0.28, 4.6),
        (192, 670, 2, 0.22, 5.4),
        (1248, 842, 1, 0.18, 3.5),
    ]:
        add Solid(citydom_color_main_dust, xysize=(_dust_size, _dust_size)) xpos _dust_x ypos _dust_y at citydom_main_dust(_dust_alpha, 16, _dust_duration)

    text "City":
        xpos 56
        ypos 76
        font citydom_font_logo
        size 88
        color citydom_color_logo_city
        outlines [ (1, citydom_color_black_outline_strong, 2, 2) ]

    text "dom":
        xpos 318
        ypos 119
        font citydom_font_serif_italic
        size 48
        color citydom_color_logo_dom
        kerning 4
        outlines [ (1, citydom_color_black_outline_soft, 1, 1) ]

    use new_ui_main_button("play", 64, 710, _("Play"), [ With(citydom_soft_game_transition), Start() ], new_ui_main_hover, delay=0.10)
    use new_ui_main_button("continue", 64, 775, _("Continue"), Continue(confirm=False), new_ui_main_hover, sub=_("last save"), delay=0.18)
    use new_ui_main_button("load", 64, 840, _("Load"), ShowMenu("load"), new_ui_main_hover, delay=0.26)
    use new_ui_main_button("settings", 64, 905, _("Settings"), ShowMenu("preferences"), new_ui_main_hover, delay=0.34)
    use new_ui_main_button("quit", 64, 970, _("Quit"), ShowMenu("custom_quit_screen"), new_ui_main_hover, delay=0.42)

    button:
        xpos 1625
        ypos 1012
        xysize (240, 45)
        background citydom_color_main_patreon_bg
        hover_background citydom_color_main_patreon_bg_hover
        action Show("thank_you_screen")
        at citydom_main_delayed_show(0.60)
        text _("Thank you Patreons"):
            font citydom_font_ui
            size 14
            color citydom_color_main_patreon_text
            xalign 0.5
            yalign 0.5

screen new_ui_main_button(hover_name, x, y, label, action, current_hover=None, sub=None, delay=0.0):
    button:
        xpos x
        ypos y
        xysize (360, 58)
        background None
        hover_background None
        hovered SetScreenVariable("new_ui_main_hover", hover_name)
        unhovered SetScreenVariable("new_ui_main_hover", None)
        action action
        at citydom_main_menu_item_motion(delay)

        text label:
            xpos 0
            ypos 0
            style "new_ui_menu_text"
            color (citydom_color_primary_soft if current_hover == hover_name else citydom_color_menu_idle)

        if sub:
            text sub:
                xpos 270
                ypos 28
                font citydom_font_ui
                size 11
                color citydom_color_main_subtext
                kerning 4

screen new_ui_menu_base(selected="load"):
    if main_menu:
        add citydom_legacy_menu_asset("main_menu_base")

    add citydom_legacy_menu_asset("menu_base")

    if main_menu:
        use new_ui_nav_button(_("Start"), 55, 150, [ With(citydom_soft_game_transition), Start() ], selected == "start")
    else:
        use new_ui_nav_button(_("Save"), 55, 150, ShowMenu("save"), selected == "save")
    use new_ui_nav_button(_("Load"), 55, 285, ShowMenu("load"), selected == "load")
    use new_ui_nav_button(_("Settings"), 55, 420, ShowMenu("preferences"), selected == "preferences")
    if main_menu:
        use new_ui_nav_button(_("Quit"), 55, 555, ShowMenu("custom_quit_screen"), selected == "quit")
    else:
        use new_ui_nav_button(_("Main Menu"), 55, 555, MainMenu(), selected == "main_menu")
        use new_ui_nav_button(_("Quit"), 55, 690, ShowMenu("custom_quit_screen"), selected == "quit")
    use new_ui_nav_button(_("Return"), 55, 965, Return(), selected == "return", return_button=True)

screen new_ui_nav_button(label, x, y, action, selected=False, return_button=False):
    button:
        xpos 0
        ypos y - 30
        xysize (520, 130)
        if selected:
            background Transform(citydom_legacy_menu_asset("left_selected"), xysize=(497, 137))
        else:
            background None
        hover_background Transform(citydom_legacy_menu_asset("left_selected"), xysize=(497, 137))
        action action
        if return_button:
            text label:
                style "new_ui_return_text"
                xpos x
                ypos 18
        else:
            text label:
                style "new_ui_menu_text"
                xpos x
                ypos 18
