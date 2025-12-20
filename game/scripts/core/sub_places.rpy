init python:
    # How much to compress spacing between sublocation icons (1.0 = original).
    SUBLOC_POS_SCALE_X = 0.75
    SUBLOC_POS_SCALE_Y = 0.85

    # Push whole row closer to the bottom (positive values move DOWN).
    SUBLOC_BOTTOM_SHIFT = 50
    SUBLOC_RIGHT_SHIFT = 40   # pixels; + moves RIGHT, - moves LEFT

    # Fine-tune offsets (icon vs. shadow)
    SUBLOC_ICON_Y_OFFSET = 8
    SUBLOC_SHADOW_OFFSET = 3

    HOVER_ZOOM = 1.10      # how much to zoom on hover
    HOVER_DUR  = 0.08      # animation time

transform subloc_hover_zoom:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        linear HOVER_DUR zoom 1.0
    on hover:
        linear HOVER_DUR zoom HOVER_ZOOM
