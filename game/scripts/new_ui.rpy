init offset = 20

define new_ui_font_menu = "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
define new_ui_font_text = "fonts/citydom_ui/Raleway.ttf"
define new_ui_font_title = "fonts/citydom_ui/CinzelDecorative-Bold.ttf"
define citydom_font_logo = "fonts/citydom_ui/CinzelDecorative-Bold.ttf"
define citydom_font_serif = "fonts/citydom_ui/CormorantInfant.ttf"
define citydom_font_serif_italic = "fonts/citydom_ui/CormorantInfant-Italic.ttf"
define citydom_font_ui = "fonts/citydom_ui/Raleway.ttf"
define citydom_dialogue_font_name = "fonts/citydom_dialogue/Cinzel.ttf"
define citydom_dialogue_font_body = "fonts/citydom_dialogue/Lora.ttf"
define citydom_dialogue_font_ui = "fonts/citydom_dialogue/Outfit.ttf"
define new_ui_scale = 0.24

default citydom_bottom_nav_previous_id = "save"
default citydom_history_scene_id = None

init python:
    def _citydom_cubic_bezier_value(a, b, t):
        return (3.0 * a * (1.0 - t) * (1.0 - t) * t) + (3.0 * b * (1.0 - t) * t * t) + (t * t * t)

    def _citydom_cubic_bezier_slope(a, b, t):
        return (3.0 * a * (1.0 - t) * (1.0 - t)) + (6.0 * (b - a) * (1.0 - t) * t) + (3.0 * (1.0 - b) * t * t)

    def citydom_menu_curve(t):
        guess = t
        for _i in range(5):
            slope = _citydom_cubic_bezier_slope(0.25, 0.45, guess)
            if abs(slope) < 0.001:
                break
            guess -= (_citydom_cubic_bezier_value(0.25, 0.45, guess) - t) / slope
            guess = max(0.0, min(1.0, guess))
        return _citydom_cubic_bezier_value(0.46, 0.94, guess)

    def citydom_settings_slider_fraction(value):
        try:
            adjustment = value.get_adjustment()
            range_value = float(adjustment.range)
            if range_value <= 0.0:
                return 0.0
            return min(1.0, max(0.0, float(adjustment.value) / range_value))
        except Exception:
            pass
        return 0.0

    def citydom_action_selected(action):
        try:
            if isinstance(action, (list, tuple)):
                return any(citydom_action_selected(item) for item in action)
            return bool(action.get_selected())
        except Exception:
            return False

    def citydom_dialogue_gradient_name(name):
        return AlphaMask(
            "gui/citydom_ui_v2/dialogue_name_gradient.png",
            Text(name, style="new_ui_name_text_mask")
        )

    def citydom_history_current_scene_id():
        try:
            filename, _line = renpy.get_filename_line()
            if filename and filename != "unknown":
                return filename
        except Exception:
            pass
        return citydom_history_scene_id

    def citydom_history_tag_entry(entry):
        scene_id = citydom_history_current_scene_id()
        entry.citydom_scene_id = scene_id
        renpy.store.citydom_history_scene_id = scene_id

    if citydom_history_tag_entry not in config.history_callbacks:
        config.history_callbacks.append(citydom_history_tag_entry)

style new_ui_menu_text is default:
    font new_ui_font_menu
    size 44
    color "#ebd2ffd1"
    hover_color "#ffb9e1f2"
    selected_color "#ffb9e1f2"
    outlines [ (1, "#000000e6", 1, 1) ]

style new_ui_return_text is new_ui_menu_text:
    size 70

style new_ui_title_text is default:
    font new_ui_font_title
    size 58
    color "#ffc8f0"
    outlines [ (1, "#00000099", 1, 1) ]
    kerning 12

style new_ui_label_text is default:
    font citydom_font_ui
    size 18
    color "#c084d480"
    outlines [ ]
    kerning 3

style new_ui_small_text is default:
    font citydom_font_ui
    size 22
    color "#e6beffe6"
    outlines [ ]

style citydom_ui_title_text is default:
    font new_ui_font_title
    size 58
    color "#ffd2f4"
    kerning 12
    outlines [ (1, "#00000099", 1, 1) ]

style citydom_ui_slot_text is default:
    font citydom_font_ui
    size 18
    color "#d8b6f0c9"
    outlines [ ]

style citydom_ui_slot_name_text is citydom_ui_slot_text:
    font citydom_font_serif_italic
    size 26
    color "#e8d4fce0"

style citydom_ui_slot_date_text is citydom_ui_slot_text:
    color "#d8b6f0d9"

style citydom_ui_card_chip_text is default:
    font citydom_font_ui
    size 12
    color "#e879a0d9"
    kerning 2
    outlines [ ]

style citydom_settings_section_text is default:
    font citydom_font_ui
    size 12
    color "#ff8df8f2"
    kerning 4
    outlines [ (1, "#7d1bb366", 0, 0) ]

style citydom_settings_option_text is default:
    font citydom_font_ui
    size 16
    color "#f1c4ffff"
    kerning 1
    outlines [ (1, "#8b28c866", 0, 0) ]

style citydom_settings_value_text is default:
    font citydom_font_ui
    size 12
    color "#ff9df8ff"
    outlines [ (1, "#7d1bb366", 0, 0) ]

style citydom_settings_note_text is default:
    font citydom_font_ui
    size 12
    color "#ff9df8ff"
    kerning 3
    outlines [ (1, "#7d1bb366", 0, 0) ]

transform citydom_card_idle:
    zoom 1.0
    yoffset 0

transform citydom_card_hover:
    zoom 1.025
    yoffset -3

transform citydom_card_pop:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        easein 0.16 zoom 1.0
    on hover:
        easeout 0.22 zoom 1.025

transform citydom_confirm_button_pop:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        easein 0.16 zoom 1.0
    on hover:
        easeout 0.22 zoom 1.045

transform citydom_confirm_overlay_fade:
    on show:
        alpha 0.0
        linear 0.28 alpha 1.0
    on hide:
        linear 0.24 alpha 0.0

transform citydom_confirm_panel_show:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        alpha 0.0
        zoom 0.96
        yoffset 12
        easeout 0.32 alpha 1.0 zoom 1.0 yoffset 0
    on hide:
        easein 0.24 alpha 0.0 zoom 0.98 yoffset 12

transform citydom_file_content_show:
    subpixel True
    on show:
        alpha 0.0
        yoffset 14
        easeout 0.24 alpha 1.0 yoffset 0
    on hide:
        easein 0.18 alpha 0.0 yoffset -10

transform citydom_main_bg_fade:
    on show:
        alpha 0.0
        linear 1.4 alpha 1.0

transform citydom_main_menu_item_motion(delay=0.0):
    subpixel True
    on show:
        alpha 0.0
        xoffset -16
        pause delay
        warp citydom_menu_curve 0.45 alpha 1.0 xoffset 0
    on idle:
        warp citydom_menu_curve 0.45 xoffset 0 zoom 1.0
    on hover:
        warp citydom_menu_curve 0.45 xoffset 10 zoom 1.0

transform citydom_main_delayed_show(delay=0.0):
    subpixel True
    on show:
        alpha 0.0
        yoffset 8
        pause delay
        easeout 0.40 alpha 1.0 yoffset 0

transform citydom_main_dust(opacity=0.3, drift=16, duration=4.0):
    alpha opacity
    yoffset 0
    block:
        linear (duration / 2.0) alpha (opacity * 0.25) yoffset -drift
        linear (duration / 2.0) alpha opacity yoffset 0
        repeat

transform citydom_settings_option_motion:
    subpixel True
    on idle:
        easein 0.16 xoffset 0 zoom 1.0
    on hover:
        easeout 0.16 xoffset 2 zoom 1.0
    on selected_idle:
        easein 0.16 xoffset 0 zoom 1.0
    on selected_hover:
        easeout 0.16 xoffset 2 zoom 1.0

transform citydom_bottom_nav_active_motion(start_x=0, end_x=0):
    subpixel True
    xpos start_x
    on show:
        alpha 1.0
        warp citydom_menu_curve 0.30 xpos end_x
    on replace:
        warp citydom_menu_curve 0.30 xpos end_x

style citydom_settings_slider_hitbox is bar:
    left_bar Solid("#00000000")
    right_bar Solid("#00000000")
    hover_left_bar Solid("#00000000")
    hover_right_bar Solid("#00000000")
    thumb "gui/new_ui/menu/transparent_thumb.png"
    thumb_offset 0

screen citydom_settings_panel(x, y, w=695, h=170):
    add Frame("gui/citydom_ui_v2/panel_bg_opaque.png", 12, 12):
        xpos x
        ypos y
        xysize (w, h)
    add Frame("gui/citydom_ui_v2/panel_bg.png", 12, 12):
        xpos x
        ypos y
        xysize (w, h)

screen citydom_menu_backdrop():
    if main_menu:
        add "gui/citydom_ui_v2/main_bg_3.png"

    add Solid("#07020e78")
    add Solid("#2b0a4552")
    add Transform("gui/citydom_ui_v2/card_empty_base.png", xysize=(1920, 1080), alpha=0.22)
    add Solid("#7c1fb926")
    add Solid("#e879a012")

screen citydom_settings_radio(x, y, label, action, icon_name):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (270, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add ("gui/citydom_ui_v2/radio_on.png" if _selected else "gui/citydom_ui_v2/radio_off.png") xpos 0 ypos 6
        add Transform("gui/citydom_ui_v2/settings_icon_%s_%s.png" % (icon_name, "active" if _selected else "idle"), xysize=(16, 16)) xpos 34 ypos 8

        text label:
            xpos 62
            ypos 6
            style "citydom_settings_option_text"
            color ("#e6beffe6" if _selected else "#a078c880")

screen citydom_settings_check(x, y, label, action):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (300, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add ("gui/citydom_ui_v2/check_on.png" if _selected else "gui/citydom_ui_v2/check_off.png") xpos 0 ypos 6

        text label:
            xpos 34
            ypos 6
            style "citydom_settings_option_text"
            color ("#e6beffe6" if _selected else "#a078c880")

screen citydom_settings_slider(x, y, label, value, icon_name, bar_w=650):
    $ _fraction = citydom_settings_slider_fraction(value)
    $ _percent = int(round(_fraction * 100))
    $ _fill_w = int(bar_w * _fraction)

    add Transform("gui/citydom_ui_v2/settings_icon_%s_muted.png" % icon_name, xysize=(16, 16)) xpos x ypos y + 2

    text label.upper():
        xpos x + 32
        ypos y + 2
        style "citydom_settings_section_text"
        kerning 3

    text "%d%%" % _percent:
        xpos x + bar_w - 45
        ypos y + 2
        xsize 45
        text_align 1.0
        style "citydom_settings_value_text"

    add Transform("gui/citydom_ui_v2/slider_empty.png", xysize=(bar_w, 8)):
        xpos x
        ypos y + 36

    if _fill_w > 0:
        add Crop((0, 0, _fill_w, 8), Transform("gui/citydom_ui_v2/slider_full.png", xysize=(bar_w, 8))):
            xpos x
            ypos y + 36

    add "gui/citydom_ui_v2/slider_thumb.png":
        xpos int(x + (_fraction * bar_w) - 10)
        ypos y + 30

    bar:
        xpos x
        ypos y + 28
        xysize (bar_w, 24)
        style "citydom_settings_slider_hitbox"
        value value

screen citydom_settings_switch(x, y, label, action, icon_name, row_w=650):
    $ _selected = citydom_action_selected(action)
    button:
        xpos x
        ypos y
        xysize (row_w, 32)
        background None
        hover_background None
        action action
        at citydom_settings_option_motion

        add Transform("gui/citydom_ui_v2/settings_icon_%s_muted.png" % icon_name, xysize=(16, 16)) xpos -4 ypos 2

        text label.upper():
            xpos 27
            ypos 1
            style "citydom_settings_section_text"
            kerning 3

        add ("gui/citydom_ui_v2/switch_on.png" if _selected else "gui/citydom_ui_v2/switch_off.png") xpos (row_w - 36) ypos 2

style new_ui_transparent_button is button:
    background None
    hover_background "#ffffff12"
    selected_background "#ffffff0d"

style citydom_ui_clear_button is button:
    background None
    hover_background None
    selected_background None

style citydom_ui_card_button is button:
    background None
    hover_background None
    selected_background None
    padding (0, 0, 0, 0)
    xpadding 0
    ypadding 0
    margin (0, 0, 0, 0)

style new_ui_dialogue_text is default:
    font citydom_dialogue_font_body
    size 23
    color "#ffffffcc"
    outlines [ (1, "#00000099", 0, 1) ]
    line_spacing 6

style new_ui_name_text is default:
    font citydom_dialogue_font_name
    size 20
    color "#d864ff55"
    outlines [ (1, "#d864ff55", 0, 0), (1, "#00000080", 0, 1) ]
    kerning 5
    layout "nobreak"

style new_ui_name_text_mask is default:
    font citydom_dialogue_font_name
    size 20
    color "#ffffff"
    outlines [ ]
    kerning 5
    layout "nobreak"

style citydom_dialogue_hidden_text is default:
    size 1
    color "#00000000"
    outlines [ ]

style citydom_dialogue_continue_text is default:
    font citydom_dialogue_font_ui
    size 10
    bold True
    color "#f472b68a"
    outlines [ ]
    kerning 3

style citydom_dialogue_quick_button is button:
    background None
    hover_background None
    selected_background None
    padding (0, 0, 0, 0)
    xpadding 0
    ypadding 0

style citydom_dialogue_quick_button_text is button_text:
    font citydom_dialogue_font_ui
    size 11
    color "#c4a1d280"
    hover_color "#ff9bd9f2"
    selected_color "#ff9bd9f2"
    outlines [ ]
    kerning 0
    xalign 0.5
    yalign 0.5

style citydom_history_title_text is default:
    font citydom_dialogue_font_name
    size 42
    color "#ff9bd9f2"
    outlines [ (1, "#8d36c080", 0, 0), (1, "#00000099", 0, 1) ]
    kerning 13

style citydom_history_name_text is default:
    font citydom_dialogue_font_name
    size 14
    color "#ff6c9dcc"
    outlines [ ]
    kerning 4

style citydom_history_body_text is default:
    font citydom_dialogue_font_body
    size 18
    color "#e9ddf2d9"
    outlines [ (1, "#00000099", 0, 1) ]
    line_spacing 4

style citydom_history_empty_text is citydom_history_body_text:
    color "#c6a5d18c"
    text_align 0.5

style citydom_history_narration_text is default:
    font citydom_dialogue_font_ui
    size 16
    color "#c08cc98a"
    outlines [ ]
    kerning 5
    text_align 0.5

style citydom_history_footer_button is button:
    xsize 92
    ysize 46
    background None
    hover_background Frame("gui/citydom_ui_v2/history_footer_button_hover.png", 8, 8, 8, 8)
    padding (0, 0, 0, 0)

style citydom_history_footer_button_text is button_text:
    font citydom_dialogue_font_ui
    size 10
    color "#c79bd985"
    hover_color "#ff9bd9f2"
    outlines [ ]
    kerning 1
    xalign 0.5
    yalign 0.5

style new_ui_choice_button is button:
    xsize 500
    ysize 56
    background Frame("gui/citydom_ui_v2/choice_glass_idle.png", 6, 6, 6, 6)
    hover_background Frame("gui/citydom_ui_v2/choice_glass_hover.png", 6, 6, 6, 6)
    padding (0, 0, 0, 0)

style new_ui_choice_button_text is button_text:
    font citydom_dialogue_font_ui
    size 20
    color "#ffffff99"
    hover_color "#fffffff2"
    selected_color "#fffffff2"
    xalign 0.0
    yalign 0.5
    xoffset 28
    outlines [ (1, "#00000099", 0, 1) ]

transform citydom_dialogue_panel_show:
    subpixel True
    alpha 0.0
    yoffset 16
    warp citydom_hud_curve 0.40 alpha 1.0 yoffset 0

transform citydom_dialogue_engine_text_hidden:
    alpha 0.0

transform citydom_choice_button_show(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset 6
    pause delay
    warp citydom_hud_curve 0.26 alpha 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.16 xoffset 3
    on idle:
        warp citydom_hud_curve 0.16 xoffset 0

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
        add Solid("#f9a8d4", xysize=(_dust_size, _dust_size)) xpos _dust_x ypos _dust_y at citydom_main_dust(_dust_alpha, 16, _dust_duration)

    text "City":
        xpos 56
        ypos 76
        font citydom_font_logo
        size 88
        color "#d77dff"
        outlines [ (1, "#000000cc", 2, 2) ]

    text "dom":
        xpos 318
        ypos 119
        font citydom_font_serif_italic
        size 48
        color "#cd96ffa6"
        kerning 4
        outlines [ (1, "#000000aa", 1, 1) ]

    use new_ui_main_button("play", 64, 710, _("Play"), [ With(citydom_soft_game_transition), Start() ], new_ui_main_hover, delay=0.10)
    use new_ui_main_button("continue", 64, 775, _("Continue"), Continue(confirm=False), new_ui_main_hover, sub=_("last save"), delay=0.18)
    use new_ui_main_button("load", 64, 840, _("Load"), ShowMenu("load"), new_ui_main_hover, delay=0.26)
    use new_ui_main_button("settings", 64, 905, _("Settings"), ShowMenu("preferences"), new_ui_main_hover, delay=0.34)
    use new_ui_main_button("quit", 64, 970, _("Quit"), ShowMenu("custom_quit_screen"), new_ui_main_hover, delay=0.42)

    button:
        xpos 1625
        ypos 1012
        xysize (240, 45)
        background "#140626a6"
        hover_background "#28104ccc"
        action Show("thank_you_screen")
        at citydom_main_delayed_show(0.60)
        text _("Thank you Patreons"):
            font citydom_font_ui
            size 14
            color "#c89bf0b3"
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
            color ("#ffb9e1f2" if current_hover == hover_name else "#ebd2ffd1")

        if sub:
            text sub:
                xpos 270
                ypos 28
                font citydom_font_ui
                size 11
                color "#b482dc80"
                kerning 4

screen new_ui_menu_base(selected="load"):
    if main_menu:
        add "gui/new_ui/menu/main_menu_base.png"

    add "gui/new_ui/menu/menu_base.png"

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
            background Transform("gui/new_ui/menu/left_selected.png", xysize=(497, 137))
        else:
            background None
        hover_background Transform("gui/new_ui/menu/left_selected.png", xysize=(497, 137))
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

screen say(who, what):
    zorder 10
    $ _display_who = renpy.filter_text_tags(str(who).upper(), allow=[]) if who is not None else None
    $ _display_what = renpy.filter_text_tags(str(what), allow=[])

    fixed:
        xalign 0.5
        ypos 872
        xysize (900, 152)
        at citydom_dialogue_panel_show
        add Frame("gui/citydom_ui_v2/dialogue_glass_panel.png", 6, 6, 6, 6)

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

                add "gui/citydom_ui_v2/dialogue_header_rule.png":
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
                add "gui/citydom_ui_v2/dialogue_continue_chevron.png":
                    ypos 0

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
    $ _choice_color = "#fffffff2" if _hovered else "#ffffff99"
    button:
        xysize (500, 56)
        background Frame("gui/citydom_ui_v2/choice_glass_hover.png" if _hovered else "gui/citydom_ui_v2/choice_glass_idle.png", 6, 6, 6, 6)
        hover_background Frame("gui/citydom_ui_v2/choice_glass_hover.png", 6, 6, 6, 6)
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
            outlines [ (1, "#00000099", 0, 1) ]

        if _hovered:
            add "gui/citydom_ui_v2/dialogue_continue_chevron.png":
                xpos 466
                yalign 0.5

screen history():
    tag menu
    predict False
    default citydom_history_adjustment = ui.adjustment()
    $ _current_history_scene = citydom_history_scene_id
    $ _history_items = [h for h in _history_list if getattr(h, "citydom_scene_id", None) == _current_history_scene]

    add "gui/citydom_ui_v2/main_bg_3.png"
    add Solid("#160023b8")
    add Solid("#50106f5c")
    add "gui/citydom_ui_v2/history_pattern_overlay.png"

    text _("History").upper():
        xalign 0.5
        ypos 42
        style "citydom_history_title_text"

    add "gui/citydom_ui_v2/chain_divider.png":
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
                    $ _who_color = h.who_args.get("color", "#ff6c9dcc") if h.who else "#ff6c9dcc"

                    if _who:
                        frame:
                            xsize 860
                            yminimum 62
                            background Frame("gui/citydom_ui_v2/history_entry_bg.png", 6, 6, 6, 6)
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
                        add "gui/citydom_ui_v2/history_dots.png":
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
        add "gui/citydom_ui_v2/history_footer_bg.png"

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

    add "gui/citydom_ui_v2/chain_divider.png":
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
        foreground "gui/citydom_ui_v2/card_border_default.png"
        hover_foreground "gui/citydom_ui_v2/card_border_hover.png"
        action FileAction(slot)
        key "save_delete" action FileDelete(slot)
        hovered SetScreenVariable("citydom_slot_hovered", True)
        unhovered SetScreenVariable("citydom_slot_hovered", False)
        at citydom_card_pop

        if has_save:
            add "gui/citydom_ui_v2/card_empty_base_opaque.png"
            add AlphaMask(Transform(FileScreenshot(slot), xysize=(568, 320)), "gui/citydom_ui_v2/card_screenshot_mask.png")
            add Transform("gui/citydom_ui_v2/card_overlay_default.png", alpha=0.82)
            add "gui/citydom_ui_v2/card_shadow.png"

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
            add "gui/citydom_ui_v2/card_empty_base_opaque.png"
            add "gui/citydom_ui_v2/card_shadow.png"

            text _("Empty Slot"):
                xalign 0.5
                yalign 0.5
                style "citydom_ui_slot_text"

        if citydom_slot_hovered:
            add "gui/citydom_ui_v2/card_hover_chip.png":
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
        add ("gui/citydom_ui_v2/page_heart_prev_disabled.png" if _page_at_first else "gui/citydom_ui_v2/page_heart_prev_idle.png") xalign 0.5 yalign 0.5

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
                add "gui/citydom_ui_v2/page_active_bg.png" xalign 0.5 yalign 0.5

            add "gui/citydom_ui_v2/page_label_%s_%s.png" % (_page_asset_key, "active" if _page_active else "idle"):
                xalign 0.5
                yalign 0.5

    button:
        xpos _page_start_x + (len(_page_items) - 1) * _page_gap + 25
        ypos _page_center_y - 16
        xysize (32, 32)
        style "citydom_ui_clear_button"
        action FilePageNext()
        add "gui/citydom_ui_v2/page_heart_next_idle.png" xalign 0.5 yalign 0.5

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

    add "gui/citydom_ui_v2/bottom_nav_base.png" xpos _nav_x ypos _nav_y
    add "gui/citydom_ui_v2/nav_item_active_glow.png" ypos _nav_y at citydom_bottom_nav_active_motion(_indicator_start_x, _indicator_end_x)

    if citydom_bottom_nav_previous_id != slot_section:
        timer 0.32 action SetVariable("citydom_bottom_nav_previous_id", slot_section)

    for _divider_index in range(1, len(_nav_items)):
        add "gui/citydom_ui_v2/nav_divider.png" xpos (_nav_x + _divider_index * _nav_cell_w - 6) ypos (_nav_y + 18)

    for _idx, (_nav_id, _label, _action, _text_size) in enumerate(_nav_items):
        $ _active = (_nav_id == slot_section)
        $ _item_x = _nav_x + _idx * _nav_cell_w

        add "gui/citydom_ui_v2/nav_icon_%s_%s.png" % (_nav_id, "active" if _active else "idle"):
            xpos _item_x + 63
            ypos _nav_y + 16

        text _label.upper():
            xcenter _item_x + int(_nav_cell_w / 2)
            ypos _nav_y + 44
            font citydom_font_ui
            size _text_size
            kerning 0
            color ("#e879a0d9" if _active else "#a06ec861")

        button:
            xpos _item_x
            ypos _nav_y
            xysize (_nav_cell_w, 72)
            background None
            action _action

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

    add "gui/citydom_ui_v2/chain_divider.png":
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

        add Solid("#c084d414", xysize=(_control_w, 1)) xpos (_right_x + _inner_pad) ypos (_bottom_y + 142)
        use citydom_settings_switch(_right_x + _inner_pad, _bottom_y + 150, _("Mute All"), Preference("all mute", "toggle"), "volume_x", _control_w)

        add Transform("gui/citydom_ui_v2/settings_icon_skip_forward_muted.png", xysize=(16, 16)) xpos 700 ypos 596
        text _("Changes apply immediately - No restart required"):
            xpos 724
            ypos 596
            style "citydom_settings_note_text"

    use citydom_file_bottom_nav("settings")

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    use new_ui_menu_base("load")

    frame:
        background None
        xpos 540
        ypos 155
        xsize 1300
        ysize 850

        if scroll == "viewport":
            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                transclude
        elif scroll == "vpgrid":
            vpgrid:
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                transclude
        else:
            transclude

screen custom_quit_screen():
    tag menu

    add "gui/new_ui/quit.png"

    button:
        xpos 940
        ypos 945
        xysize (230, 80)
        background None
        hover_background "#ffffff10"
        action Return()

    button:
        xpos 1380
        ypos 945
        xysize (230, 80)
        background None
        hover_background "#ffffff10"
        action Quit(confirm=False)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    default new_ui_confirm_hover = None

    add Solid("#04010c8c") at citydom_confirm_overlay_fade

    fixed:
        xcenter 960
        ycenter 540
        xysize (600, 300)
        at citydom_confirm_panel_show

        add "gui/citydom_ui_v2/dialog_bg.png"

        add "gui/citydom_ui_v2/dialog_heart.png":
            xalign 0.5
            ypos 60

        text message:
            xalign 0.5
            ypos 118
            xsize 500
            text_align 0.5
            font citydom_font_serif_italic
            size 26
            color "#f0dcffe6"
            line_spacing 4
            outlines [ ]

        button:
            style "citydom_ui_card_button"
            xcenter 210
            ycenter 214
            xysize (140, 48)
            idle_background "gui/citydom_ui_v2/dialog_button_yes_idle.png"
            hover_background "gui/citydom_ui_v2/dialog_button_yes_hover.png"
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
                color "#ffc3e1f2"
                outlines [ ]

        button:
            style "citydom_ui_card_button"
            xcenter 390
            ycenter 214
            xysize (140, 48)
            idle_background "gui/citydom_ui_v2/dialog_button_no_idle.png"
            hover_background "gui/citydom_ui_v2/dialog_button_no_hover.png"
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
                color ("#d8aee8d9" if new_ui_confirm_hover == "no" else "#a078c3a6")
                outlines [ ]

    key "game_menu" action no_action
