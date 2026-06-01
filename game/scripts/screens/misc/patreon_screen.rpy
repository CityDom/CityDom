init offset = 20

define citydom_patreon_font_title = "fonts/citydom_patreon/RussoOne-Regular.ttf"
define citydom_patreon_font_body = "fonts/citydom_patreon/Nunito-wght.ttf"

init python:
    CITYDOM_PATREON_TIERS = (
        {
            "id": 3,
            "name": "Legend",
            "label": "Tier 3",
            "icon": "♕",
            "color": "#fbbf24",
            "text_color": "#fde68a",
            "count": "10 patrons",
            "supporters": ("Dovacak008", "NightOwlXX", "BlazeSerpent", "QuantumKira", "VoidWalker99", "ArcaneRiku", "NeonSamurai", "GhostPulse", "StarForged", "LunaVex"),
            "y": 380,
            "h": 254,
        },
        {
            "id": 2,
            "name": "Champion",
            "label": "Tier 2",
            "icon": "☆",
            "color": "#a78bfa",
            "text_color": "#ddd6fe",
            "count": "20 patrons",
            "supporters": ("stefan schmölzl", "DxDestarossa", "2 Stacked VCRs", "CrimsonEdge", "ZephyrMoth", "IronCeleste", "OmegaDrift", "SilverFang7", "PixelWraith", "TwilightRen", "CosmicJade", "HexRunner", "NullProtocol", "DarkPetal", "SkyBreach", "RubyPhantom", "CipherRogue", "EchoStrike", "FrostLynx", "NebulaCrow"),
            "y": 680,
            "h": 330,
        },
        {
            "id": 1,
            "name": "Supporter",
            "label": "Tier 1",
            "icon": "♡",
            "color": "#34d399",
            "text_color": "#a7f3d0",
            "count": "30 patrons",
            "supporters": ("Saus", "wosh50", "김성호", "MirageKei", "TurboNova", "GlitchDawn", "SolarMimic", "PrismByte", "VoltReign", "ChaosLark", "RuneBreaker", "StormCipher", "EmberSky", "PatchworkZen", "AquaForge", "NanoDrift", "BinaryWolf", "CrystalMaw", "FluxRaven", "OraclePin", "TerraBlaze", "WarpGlyph", "ShadowMint", "ZeroKnot", "PulseArc", "RiftSeeker", "GlowSpectre", "IronDelta", "CometShard", "VexelRoot"),
            "y": 1056,
            "h": 456,
        },
    )

    CITYDOM_PATREON_STARS = (
        (58, 64, 1, 0.30, 0.1, 2.6), (154, 196, 2, 0.42, 0.8, 3.4), (318, 640, 2, 0.35, 1.5, 2.8),
        (510, 414, 1, 0.45, 0.3, 4.1), (728, 526, 2, 0.30, 2.1, 3.0), (904, 132, 1, 0.38, 1.2, 2.5),
        (1118, 308, 2, 0.40, 0.6, 3.8), (1374, 82, 1, 0.34, 1.8, 2.6), (1626, 508, 3, 0.42, 0.2, 3.2),
        (1818, 282, 2, 0.36, 2.4, 2.9), (244, 908, 1, 0.30, 1.1, 3.5), (658, 1038, 2, 0.40, 2.0, 3.1),
        (1214, 972, 1, 0.34, 0.4, 4.0), (1742, 936, 2, 0.38, 1.7, 2.7), (1518, 720, 1, 0.36, 1.0, 3.6),
        (140, 1014, 1, 0.26, 2.2, 3.7), (392, 86, 1, 0.32, 0.6, 2.8), (582, 188, 2, 0.34, 1.4, 3.2),
        (774, 830, 1, 0.30, 0.9, 2.9), (1018, 642, 2, 0.38, 2.6, 3.5), (1282, 1112, 1, 0.28, 1.7, 4.2),
        (1456, 386, 2, 0.36, 0.4, 3.1), (1698, 104, 1, 0.31, 2.8, 3.9), (1872, 724, 2, 0.34, 1.2, 2.6),
        (84, 430, 2, 0.28, 1.9, 3.4), (286, 1198, 1, 0.33, 0.2, 3.0), (448, 742, 1, 0.30, 2.0, 4.1),
        (612, 1260, 2, 0.37, 0.7, 2.8), (826, 1002, 1, 0.29, 1.5, 3.6), (986, 472, 1, 0.41, 0.1, 2.7),
        (1168, 176, 2, 0.33, 2.4, 3.8), (1328, 816, 1, 0.27, 0.8, 4.0), (1588, 1240, 2, 0.35, 1.3, 3.2),
        (1776, 1468, 1, 0.28, 2.6, 2.9), (1846, 1118, 1, 0.40, 0.5, 3.7), (118, 1508, 2, 0.36, 1.1, 3.3),
        (336, 1462, 1, 0.30, 2.2, 2.8), (542, 1588, 2, 0.34, 0.9, 3.6), (760, 1408, 1, 0.31, 1.8, 3.0),
        (1054, 1516, 2, 0.38, 0.3, 3.5), (1258, 1360, 1, 0.29, 2.1, 4.0), (1492, 1548, 1, 0.33, 1.0, 2.7),
        (1660, 1368, 2, 0.37, 1.7, 3.9), (1900, 1526, 1, 0.32, 0.6, 3.1), (226, 310, 1, 0.35, 2.5, 2.6),
        (686, 278, 2, 0.28, 1.2, 3.4), (1198, 566, 1, 0.31, 0.4, 2.9), (1558, 178, 2, 0.34, 1.6, 4.1),
        (1728, 602, 1, 0.30, 2.3, 3.3), (930, 1162, 2, 0.36, 0.9, 3.8), (1430, 708, 1, 0.32, 1.5, 2.8),
        (90, 806, 1, 0.28, 0.7, 3.4), (514, 1062, 2, 0.35, 1.9, 3.0), (1106, 1244, 1, 0.31, 2.7, 3.6),
    )

    def citydom_patreon_chip_width(name):
        extra = 12 if any(ord(ch) > 127 for ch in name) else 0
        return max(86, min(196, int(46 + (len(name) * 9.2) + extra)))

    def citydom_patreon_chip_rows(names, max_width=1018, gap=12):
        rows = []
        row = []
        used = 0
        for name in names:
            width = citydom_patreon_chip_width(name)
            next_used = used + width + (gap if row else 0)
            if row and next_used > max_width:
                rows.append(row)
                row = []
                used = 0
            row.append((name, width))
            used += width + (gap if len(row) > 1 else 0)
        if row:
            rows.append(row)
        return rows

transform citydom_patreon_screen_show:
    subpixel True
    alpha 0.0
    warp citydom_hud_curve 0.40 alpha 1.0

transform citydom_patreon_hero_show:
    subpixel True
    alpha 0.0
    yoffset 18
    warp citydom_hud_curve 0.46 alpha 1.0 yoffset 0

transform citydom_patreon_sparkle_float:
    subpixel True
    alpha 0.0
    yoffset 10
    warp citydom_hud_curve 0.42 alpha 1.0 yoffset 0
    block:
        linear 1.5 yoffset -12
        linear 1.5 yoffset 0
        repeat

transform citydom_patreon_card_show(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset 22
    pause delay
    warp citydom_hud_curve 0.45 alpha 1.0 yoffset 0

transform citydom_patreon_chip_motion:
    subpixel True
    on hover:
        warp citydom_hud_curve 0.16 yoffset -1 zoom 1.02
    on idle:
        warp citydom_hud_curve 0.16 yoffset 0 zoom 1.0

transform citydom_patreon_footer_motion:
    subpixel True
    on hover:
        warp citydom_hud_curve 0.18 yoffset -2 zoom 1.015
    on idle:
        warp citydom_hud_curve 0.18 yoffset 0 zoom 1.0

transform citydom_patreon_star_twinkle(delay=0.0, duration=3.0, max_alpha=0.45):
    subpixel True
    alpha 0.10
    zoom 1.0
    pause delay
    block:
        linear duration alpha max_alpha zoom 1.35
        linear duration alpha 0.10 zoom 1.0
        repeat

style citydom_patreon_tier_label is default:
    font citydom_patreon_font_title
    size 18
    color "#ffffff99"
    outlines [ (1, "#00000080", 0, 1) ]
    kerning 2

style citydom_patreon_tier_name is default:
    font citydom_patreon_font_title
    size 28
    color "#ffffff"
    outlines [ (2, "#00000099", 0, 2) ]

style citydom_patreon_body is default:
    font citydom_patreon_font_body
    size 18
    color "#9d7fc4"
    outlines [ ]

style citydom_patreon_chip_text is default:
    font citydom_patreon_font_body
    size 17
    bold True
    color "#ffffff"
    outlines [ (1, "#00000080", 0, 1) ]

style citydom_patreon_count_text is default:
    font citydom_patreon_font_body
    size 16
    bold True
    color "#ffffff"
    outlines [ ]

style citydom_patreon_footer_text is default:
    font citydom_patreon_font_body
    size 13
    bold True
    color "#9d7fc4"
    outlines [ ]
    kerning 3

screen citydom_patreon_chip(name, tier):
    $ _w = citydom_patreon_chip_width(name)
    button:
        style "citydom_ui_card_button"
        xysize (_w, 38)
        idle_background Frame(citydom_ui_asset("patreon_chip_tier_%d_idle" % tier["id"]), 20, 20, 20, 20)
        hover_background Frame(citydom_ui_asset("patreon_chip_tier_%d_hover" % tier["id"]), 20, 20, 20, 20)
        action NullAction()
        at citydom_patreon_chip_motion

        text name:
            xalign 0.5
            yalign 0.5
            style "citydom_patreon_chip_text"
            color tier["text_color"]
            hover_color tier["color"]

screen citydom_patreon_tier_card(tier, index):
    fixed:
        xpos 400
        ypos tier["y"]
        xysize (1120, tier["h"])
        at citydom_patreon_card_show(index * 0.15)

        add citydom_ui_asset("patreon_card_tier_%d" % tier["id"])

        fixed:
            xpos 38
            ypos 38
            xysize (58, 58)
            add citydom_ui_asset("patreon_icon_tier_%d" % tier["id"])

        text tier["label"].upper():
            xpos 112
            ypos 40
            style "citydom_patreon_tier_label"
            color tier["color"]

        text tier["name"]:
            xpos 112
            ypos 66
            style "citydom_patreon_tier_name"
            color tier["text_color"]

        fixed:
            xpos 916
            ypos 40
            xysize (150, 42)
            add citydom_ui_asset("patreon_count_tier_%d" % tier["id"])
            text tier["count"]:
                xalign 0.5
                yalign 0.5
                style "citydom_patreon_count_text"
                color tier["color"]

        add Solid(tier["color"] + "4d", xysize=(1000, 1)):
            xpos 38
            ypos 110

        vbox:
            xpos 38
            ypos 130
            spacing 8
            for row in citydom_patreon_chip_rows(tier["supporters"]):
                hbox:
                    spacing 12
                    for name, _w in row:
                        use citydom_patreon_chip(name, tier)

screen thank_you_screen():
    modal True
    zorder 500

    key "game_menu" action Hide("thank_you_screen", transition=Dissolve(0.35))
    key "K_ESCAPE" action Hide("thank_you_screen", transition=Dissolve(0.35))

    fixed:
        at citydom_patreon_screen_show
        add citydom_ui_asset("patreon_bg")

        for _x, _y, _size, _alpha, _delay, _duration in CITYDOM_PATREON_STARS:
            add citydom_ui_asset("patreon_star_%d" % _size):
                xpos _x
                ypos _y
                at citydom_patreon_star_twinkle(_delay, _duration, _alpha)

        viewport:
            xpos 0
            ypos 0
            xysize (1920, 1080)
            child_size (1920, 1600)
            draggable True
            mousewheel True
            scrollbars None

            fixed:
                xysize (1920, 1600)

                fixed:
                    xalign 0.5
                    ypos 62
                    xysize (900, 260)
                    at citydom_patreon_hero_show

                    fixed:
                        xalign 0.5
                        ypos 0
                        xysize (64, 64)
                        at citydom_patreon_sparkle_float
                        add citydom_ui_asset("patreon_sparkle_badge")

                    add citydom_ui_asset("patreon_title_thank_you"):
                        xalign 0.5
                        ypos 66

                    text "— FOR YOUR SUPPORT —":
                        xalign 0.5
                        ypos 205
                        font citydom_patreon_font_title
                        size 24
                        color "#9d7fc4"
                        kerning 8

                    text "Every contribution makes a difference. Thank you to all the incredible patrons who make this possible.":
                        xalign 0.5
                        ypos 250
                        xsize 460
                        style "citydom_patreon_body"
                        text_align 0.5
                        color "#6b4f8a"
                        line_spacing 5

                for _index, _tier in enumerate(CITYDOM_PATREON_TIERS):
                    use citydom_patreon_tier_card(_tier, _index)

                fixed:
                    xpos 780
                    ypos 1538
                    xysize (360, 44)
                    at citydom_patreon_card_show(0.45)

                    button:
                        style "citydom_ui_card_button"
                        xysize (360, 44)
                        idle_background citydom_ui_asset("patreon_footer_pill")
                        hover_background citydom_ui_asset("patreon_footer_pill_hover")
                        action OpenURL("https://www.patreon.com/CityDom")
                        at citydom_patreon_footer_motion

                        add citydom_ui_asset("patreon_footer_heart"):
                            xpos 34
                            ypos 16
                        text "SUPPORT ME ON PATREON":
                            xalign 0.5
                            yalign 0.5
                            style "citydom_patreon_footer_text"
                        add citydom_ui_asset("patreon_footer_heart"):
                            xpos 312
                            ypos 16

        imagebutton:
            idle citydom_ui_asset("patreon_close_idle")
            hover citydom_ui_asset("patreon_close_hover")
            xpos 1818
            ypos 34
            action Hide("thank_you_screen", transition=Dissolve(0.35))
            at citydom_patreon_chip_motion
        text "×":
            xpos 1832
            ypos 33
            size 32
            color "#c084fccc"
            outlines [ (1, "#00000099", 0, 1) ]
