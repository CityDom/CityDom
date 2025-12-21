init python:
    def hideMainHud():
        renpy.hide_screen("MainHud")

    def synchronize_school_clock():
        calendar.align_school_period_to_class()

screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "HomeSubplace/map.png"
        imagebutton:
            auto "MapIcons/entrance_icon_%s.png"
            xpos 1000 ypos 700
            action [
                Function(set_typing_state, False),
                Function(clear_typing_state),
                SetVariable("MapScreenShown", False),
                Return("Housefront"),
                Show("MainHud"),
                Hide("MapScreen")
            ]
            hovered renpy.log(f"[DEBUG] Entrance Button Clicked. Returning Location: Housefront")
            at buttonScale
        if beenToSchoolOnce:
            if is_in_school_hours():
                imagebutton:
                    auto "MapIcons/school_icon_%s.png"
                    xpos 200
                    ypos 700
                    action [
                            Function(set_typing_state, False),
                            Function(clear_typing_state),
                            SetVariable("MapScreenShown", False),
                            Function(synchronize_school_clock),
                            Return("School"),
                            Show("MainHud"),
                            Hide("MapScreen")]
                    at buttonScale
            
            if not is_in_school_hours():
                add "MapIcons/school_icon_closed.png" xpos 200 ypos 700
                imagebutton:
                    auto "MapIcons/closed_%s.png" xpos 200 ypos 750
                    action NullAction()
                    hovered Show("tooltip", image_path="MapIcons/SchoolProgram.png", xpos=120, ypos=810)
                    unhovered Hide("tooltip")
        else:
            add "MapIcons/school_icon_closed.png" xpos 200 ypos 700
            imagebutton:
                auto "MapIcons/closed_%s.png" xpos 200 ypos 750
                action NullAction()
                hovered Show("tooltip", image_path="MapIcons/FirstTimeWithFamilyWarning.png", xpos=30, ypos=810)
                unhovered Hide("tooltip")

label GetOutOfSchoolItsLate:
    MC "The school is closing soon, I should go home."
    # $ advance_time_or_sleep()
    $ Location = "School"
    jump GameLoop

screen tooltip(image_path, xpos, ypos):
    frame:
        background None
        at tooltip_pos(xpos, ypos)
        add image_path
    zorder 200

transform tooltip_pos(xpos, ypos):
    xoffset xpos
    yoffset ypos
