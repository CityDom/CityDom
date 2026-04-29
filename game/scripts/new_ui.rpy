init offset = 20

define new_ui_font_menu = "fonts/new_ui/Euphorigenic.otf"
define new_ui_font_text = "fonts/new_ui/RomanSerif.ttf"
define new_ui_font_title = "fonts/new_ui/MB-Demonic_Tale.ttf"
define new_ui_scale = 0.24

init python:
    def new_ui_pref_slider_fraction(value):
        try:
            adjustment = value.get_adjustment()
            range_value = float(adjustment.range)
            if range_value <= 0.0:
                return 0.0
            return min(1.0, max(0.0, float(adjustment.value) / range_value))
        except Exception:
            pass
        return 0.0

style new_ui_menu_text is default:
    font new_ui_font_menu
    size 68
    color "#ffffff"
    hover_color "#f79df5"
    selected_color "#f79df5"
    outlines [ (1, "#31003d", 1, 1) ]

style new_ui_return_text is new_ui_menu_text:
    size 70

style new_ui_title_text is default:
    font new_ui_font_title
    size 110
    color "#f8a0fb"
    outlines [ (2, "#3d0047", 1, 1) ]
    kerning 8

style new_ui_label_text is default:
    font new_ui_font_menu
    size 34
    color "#ffffff"
    outlines [ (1, "#2d003a", 1, 1) ]

style new_ui_small_text is default:
    font new_ui_font_text
    size 25
    color "#ffffff"
    outlines [ (1, "#00000099", 1, 1) ]

style new_ui_page_text is default:
    font new_ui_font_menu
    size 45
    color "#ffffff"
    hover_color "#f79df5"
    selected_color "#f79df5"
    outlines [ (1, "#31003d", 1, 1) ]

style new_ui_slider is bar:
    xysize (485, 44)
    left_bar "gui/new_ui/menu/slider_full_idle_padded.png"
    right_bar "gui/new_ui/menu/slider_empty_idle_padded.png"
    hover_left_bar "gui/new_ui/menu/slider_full_hover_padded.png"
    hover_right_bar "gui/new_ui/menu/slider_empty_hover_padded.png"
    thumb "gui/new_ui/menu/transparent_thumb.png"
    thumb_offset 0

screen new_ui_pref_slider(kind, x, y, value):
    $ _fraction = new_ui_pref_slider_fraction(value)
    bar:
        xpos x
        ypos y - 12
        style "new_ui_slider"
        value value

    add Transform("gui/new_ui/menu/slider_thumb_idle.png", xysize=(36, 40)):
        xpos int(x + (_fraction * 485) - 18)
        ypos y - 10

style new_ui_transparent_button is button:
    background None
    hover_background "#ffffff12"
    selected_background "#ffffff0d"

style new_ui_dialogue_text is default:
    font new_ui_font_text
    size 30
    color "#ffffff"
    outlines [ (1, "#2d003a", 0, 0), (1, "#00000090", 2, 2) ]

style new_ui_name_text is default:
    font new_ui_font_menu
    size 45
    color "#ffffff"
    outlines [ (1, "#2d003a", 0, 0), (1, "#00000090", 2, 2) ]

style new_ui_choice_button is button:
    xsize 430
    ysize 54
    background Frame("gui/button/choice_idle_background.png", 70, 8, 70, 8)
    hover_background Frame("gui/button/choice_hover_background.png", 70, 8, 70, 8)

style new_ui_choice_button_text is button_text:
    font new_ui_font_text
    size 27
    color "#ffffff"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5
    outlines [ (1, "#00000099", 1, 1) ]

screen main_menu():
    tag menu
    default new_ui_main_hover = None

    add gui.main_menu_background
    add "gui/new_ui/menu/main_menu_ui.png"

    if new_ui_main_hover == "play":
        add Transform("gui/new_ui/menu/main_hover_raw.png", xysize=(497, 137)) xpos 0 ypos 343
        add "gui/new_ui/menu/main_menu_text_overlay.png"
    elif new_ui_main_hover == "continue":
        add Transform("gui/new_ui/menu/main_hover_raw.png", xysize=(497, 137)) xpos 0 ypos 536
        add "gui/new_ui/menu/main_menu_text_overlay.png"
    elif new_ui_main_hover == "settings":
        add Transform("gui/new_ui/menu/main_hover_raw.png", xysize=(497, 137)) xpos 0 ypos 727
        add "gui/new_ui/menu/main_menu_text_overlay.png"

    use new_ui_main_button("play", 0, 343, Start())
    use new_ui_main_button("continue", 0, 536, ShowMenu("load"))
    use new_ui_main_button("settings", 0, 727, ShowMenu("preferences"))

    button:
        xpos 1446
        ypos 864
        xysize (438, 216)
        background None
        hover_background None
        action Show("thank_you_screen")

screen new_ui_main_button(hover_name, x, y, action):
    button:
        xpos x
        ypos y
        xysize (497, 137)
        background None
        hover_background None
        hovered SetScreenVariable("new_ui_main_hover", hover_name)
        unhovered SetScreenVariable("new_ui_main_hover", None)
        action action

screen new_ui_menu_base(selected="load"):
    if main_menu:
        add "gui/new_ui/menu/main_menu_base.png"

    add "gui/new_ui/menu/menu_base.png"

    if main_menu:
        use new_ui_nav_button(_("Start"), 55, 150, Start(), selected == "start")
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

    add "gui/new_ui/textbox.png"

    if who is not None:
        text who id "who":
            style "new_ui_name_text"
            xpos 150
            ypos 741
            xsize 460

    text what id "what":
        style "new_ui_dialogue_text"
        xpos 135
        ypos 835
        xsize 1615

screen choice(items):
    zorder 20

    vbox:
        xalign 0.5
        ypos 785
        spacing 10

        for i in items:
            textbutton i.caption:
                style "new_ui_choice_button"
                text_style "new_ui_choice_button_text"
                action i.action

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    $ slot_section = "save" if str(title).lower().startswith("save") else "load"

    use new_ui_menu_base(slot_section)
    if slot_section == "save":
        text _("SAVE") xpos 1030 ypos 62 style "new_ui_title_text"
    else:
        add "gui/new_ui/menu/load_title.png" xpos 1023 ypos 70 zoom new_ui_scale

    fixed:
        xpos 0
        ypos 0

        for i, pos in enumerate([(640, 259), (1060, 259), (1482, 259), (640, 608), (1060, 608), (1482, 608)]):
            $ slot = i + 1
            $ slot_x, slot_y = pos
            $ has_save = FileLoadable(slot)

            button:
                xpos slot_x
                ypos slot_y
                xysize (361, 204)
                if has_save:
                    background None
                else:
                    background Transform("gui/new_ui/menu/slot_frame_empty.png", xysize=(361, 204))
                hover_background None
                hover_foreground Transform("gui/new_ui/menu/slot_hover_flourish.png", xysize=(449, 293), xpos=-38, ypos=-21)
                action FileAction(slot)
                key "save_delete" action FileDelete(slot)

                if has_save:
                    add AlphaMask(Transform(FileScreenshot(slot), xysize=(353, 196)), "gui/new_ui/menu/slot_screenshot_mask.png"):
                        xpos 4
                        ypos 4

                    add "gui/new_ui/menu/slot_frame_outline.png":
                        xpos 0
                        ypos 0

                text FileTime(slot, format=_("{#file_time}%a, %B %d %Y, %H:%M"), empty=_("Empty Slot")):
                    xalign 0.5
                    ypos 230
                    style "new_ui_small_text"

                text FileSaveName(slot):
                    xalign 0.5
                    ypos 83
                    style "new_ui_small_text"

    button:
        xpos 703
        ypos 949
        xysize (58, 65)
        background Transform("gui/new_ui/menu/page_prev.png", xysize=(58, 65))
        hover_background Transform("gui/new_ui/menu/page_prev.png", xysize=(58, 65), matrixcolor=BrightnessMatrix(0.18))
        action FilePagePrevious()

    hbox:
        xpos 795
        ypos 951
        spacing 34

        if config.has_autosave:
            textbutton _("A"):
                style "new_ui_transparent_button"
                text_style "new_ui_page_text"
                action FilePage("auto")

        if config.has_quicksave:
            textbutton _("Q"):
                style "new_ui_transparent_button"
                text_style "new_ui_page_text"
                action FilePage("quick")

        for page in range(1, 10):
            textbutton "[page]":
                style "new_ui_transparent_button"
                text_style "new_ui_page_text"
                action FilePage(page)

    button:
        xpos 1716
        ypos 949
        xysize (58, 65)
        background Transform("gui/new_ui/menu/page_next.png", xysize=(58, 65))
        hover_background Transform("gui/new_ui/menu/page_next.png", xysize=(58, 65), matrixcolor=BrightnessMatrix(0.18))
        action FilePageNext()

screen preferences():
    tag menu

    use new_ui_menu_base("preferences")
    add "gui/new_ui/menu/settings_title.png" xpos 826 ypos 71 zoom new_ui_scale

    text _("Display") xpos 635 ypos 205 style "new_ui_label_text"
    text _("Skip") xpos 1308 ypos 205 style "new_ui_label_text"
    text _("Text Speed") xpos 633 ypos 548 style "new_ui_label_text"
    text _("Auto-Forward Time") xpos 633 ypos 727 style "new_ui_label_text"
    text _("Volume") xpos 1308 ypos 548 style "new_ui_label_text"

    imagebutton:
        idle Transform("gui/new_ui/menu/radio_unselected_idle.png", xysize=(56, 51))
        hover Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        selected_idle Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        selected_hover Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        xpos 655
        ypos 289
        xysize (56, 51)
        action Preference("display", "window")
    text _("Window") xpos 730 ypos 299 style "new_ui_small_text"

    imagebutton:
        idle Transform("gui/new_ui/menu/radio_unselected_idle.png", xysize=(56, 51))
        hover Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        selected_idle Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        selected_hover Transform("gui/new_ui/menu/radio_selected_idle.png", xysize=(56, 51))
        xpos 655
        ypos 349
        xysize (56, 51)
        action Preference("display", "fullscreen")
    text _("Fullscreen") xpos 730 ypos 359 style "new_ui_small_text"

    imagebutton:
        idle Transform("gui/new_ui/menu/check_off_idle.png", xysize=(72, 49))
        hover Transform("gui/new_ui/menu/check_off_hover.png", xysize=(72, 49))
        selected_idle Transform("gui/new_ui/menu/check_on_idle.png", xysize=(72, 49))
        selected_hover Transform("gui/new_ui/menu/check_on_hover.png", xysize=(72, 49))
        xpos 1325
        ypos 289
        xysize (72, 49)
        action Preference("skip", "toggle")
    text _("Unseen Text") xpos 1425 ypos 299 style "new_ui_small_text"

    imagebutton:
        idle Transform("gui/new_ui/menu/check_off_idle.png", xysize=(72, 49))
        hover Transform("gui/new_ui/menu/check_off_hover.png", xysize=(72, 49))
        selected_idle Transform("gui/new_ui/menu/check_on_idle.png", xysize=(72, 49))
        selected_hover Transform("gui/new_ui/menu/check_on_hover.png", xysize=(72, 49))
        xpos 1325
        ypos 349
        xysize (72, 49)
        action Preference("after choices", "toggle")
    text _("After Choices") xpos 1425 ypos 359 style "new_ui_small_text"

    imagebutton:
        idle Transform("gui/new_ui/menu/check_off_idle.png", xysize=(72, 49))
        hover Transform("gui/new_ui/menu/check_off_hover.png", xysize=(72, 49))
        selected_idle Transform("gui/new_ui/menu/check_on_idle.png", xysize=(72, 49))
        selected_hover Transform("gui/new_ui/menu/check_on_hover.png", xysize=(72, 49))
        xpos 1325
        ypos 409
        xysize (72, 49)
        action InvertSelected(Preference("transitions", "toggle"))
    text _("Transitions") xpos 1425 ypos 419 style "new_ui_small_text"

    use new_ui_pref_slider("text speed", 665, 647, Preference("text speed"))
    use new_ui_pref_slider("auto-forward time", 665, 825, Preference("auto-forward time"))

    if config.has_music:
        text _("Music") xpos 1665 ypos 615 style "new_ui_small_text"
        use new_ui_pref_slider("music", 1310, 647, Preference("music volume"))

    if config.has_sound:
        text _("Sound") xpos 1665 ypos 710 style "new_ui_small_text"
        use new_ui_pref_slider("sound", 1310, 742, Preference("sound volume"))

    if config.has_voice:
        text _("Voice") xpos 1665 ypos 805 style "new_ui_small_text"
        use new_ui_pref_slider("voice", 1310, 837, Preference("voice volume"))

    imagebutton:
        idle Transform("gui/new_ui/menu/check_off_idle.png", xysize=(72, 49))
        hover Transform("gui/new_ui/menu/check_off_hover.png", xysize=(72, 49))
        selected_idle Transform("gui/new_ui/menu/check_on_idle.png", xysize=(72, 49))
        selected_hover Transform("gui/new_ui/menu/check_on_hover.png", xysize=(72, 49))
        xpos 1325
        ypos 943
        xysize (72, 49)
        action Preference("all mute", "toggle")
    text _("Mute all") xpos 1425 ypos 951 style "new_ui_small_text"

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

    add Solid("#00000066")

    frame:
        xpos 460
        ypos 370
        xysize (1000, 320)
        background Transform("gui/new_ui/menu/popup_frame.png", xysize=(1000, 320))

        text message:
            xpos 60
            ypos 90
            xsize 880
            text_align 0.5
            font new_ui_font_text
            size 32
            color "#f8d0ff"
            outlines [ (1, "#2d003a", 1, 1) ]

        if new_ui_confirm_hover == "yes":
            add Transform("gui/new_ui/menu/popup_heart_l.png", xysize=(30, 34)) xpos 215 ypos 227
            add Transform("gui/new_ui/menu/popup_heart_r.png", xysize=(30, 34)) xpos 375 ypos 227

        if new_ui_confirm_hover == "no":
            add Transform("gui/new_ui/menu/popup_heart_l.png", xysize=(30, 34)) xpos 595 ypos 227
            add Transform("gui/new_ui/menu/popup_heart_r.png", xysize=(30, 34)) xpos 755 ypos 227

        text _("Yes"):
            xpos 245
            ypos 213
            xsize 130
            text_align 0.5
            font new_ui_font_menu
            size 42
            color ("#f8d0ff" if new_ui_confirm_hover == "yes" else "#ffffff")
            outlines [ (1, "#2d003a", 1, 1) ]

        text _("No"):
            xpos 625
            ypos 213
            xsize 130
            text_align 0.5
            font new_ui_font_menu
            size 42
            color ("#f8d0ff" if new_ui_confirm_hover == "no" else "#ffffff")
            outlines [ (1, "#2d003a", 1, 1) ]

        button:
            xpos 200
            ypos 205
            xysize (220, 85)
            background None
            hover_background None
            hovered SetScreenVariable("new_ui_confirm_hover", "yes")
            unhovered SetScreenVariable("new_ui_confirm_hover", None)
            action yes_action

        button:
            xpos 580
            ypos 205
            xysize (220, 85)
            background None
            hover_background None
            hovered SetScreenVariable("new_ui_confirm_hover", "no")
            unhovered SetScreenVariable("new_ui_confirm_hover", None)
            action no_action

    key "game_menu" action no_action
