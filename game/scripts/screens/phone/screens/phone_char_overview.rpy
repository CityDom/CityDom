screen CharOverviewScreen():
    add "CharStats/" + selected_character + "Body.png" xalign 0.5 yalign 0.5

    imagebutton:
        xpos 1780
        ypos 1003
        auto "Exit_%s.png"
        action [Hide("CharOverviewScreen"),
                SetVariable("StatsButtonsAreActive", True),
                SetVariable("CharacterSelectionIsShowing", True)]
