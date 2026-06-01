init offset = 20

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