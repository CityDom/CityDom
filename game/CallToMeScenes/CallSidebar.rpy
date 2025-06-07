screen sidebar_screen():
    add "CallToMeSidebar.png" xpos 1700 ypos 140
    imagebutton:
        idle "CallToMeImages/Mhyrorin_CallToMeIcon_idle.png"
        xpos 1735
        ypos 180
        action Jump("MhyrorinCallToMeDialog")

    imagebutton:
        idle "CallToMeImages/Isabella_CallToMeIcon_idle.png"
        xpos 1735
        ypos 340
        action Jump("IsabellaCallToMeDialog")

    imagebutton:
        idle "CallToMeImages/Jennifer_CallToMeIcon_idle.png"
        xpos 1735
        ypos 500
        action Jump("JenniferCallToMeDialog")

    imagebutton:
        idle "CallToMeImages/Claire_CallToMeIcon_idle.png"
        xpos 1735
        ypos 660
        action Jump("ClaireCallToMeDialog")