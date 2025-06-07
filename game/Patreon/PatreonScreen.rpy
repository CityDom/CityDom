screen thank_you_screen():
    add "gui/ThankYouList.png"  # Background image
    imagebutton:
        auto "Exit_%s.png" 
        action [Hide("thank_you_screen"), Return()]
        xpos 10
        ypos 1000
        at buttonScale
        focus_mask True