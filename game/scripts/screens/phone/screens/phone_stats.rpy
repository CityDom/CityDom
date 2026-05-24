default citydom_details_closing = False
default citydom_details_tab = "info"
default citydom_details_body_view = "front"
default citydom_details_outfit = 1

init python:
    CITYDOM_DETAILS_CHARACTERS = (
        "Jennifer", "Isabella", "Claire", "Maria", "Alis", "Sophie", "Lola",
        "Selina", "Helena", "Dorothy", "Leya", "Greta", "Jannice", "Criss",
        "Luna", "Asako", "Angeline", "Scarlet", "Tanya", "Anna", "Emma",
        "Sandra",
    )

    CITYDOM_DETAILS_ACCENTS = {
        "Jennifer": "#e8648c",
        "Isabella": "#7896ff",
        "Claire": "#50d28c",
        "Maria": "#e879dc",
        "Scarlet": "#d45b70",
        "Tanya": "#f0aa5a",
    }

    CITYDOM_DETAILS_META = {
        "Jennifer": {"relation": "Mother", "age": "38", "occupation": "Business Executive", "status": "Divorced", "temperament": "Calm", "style": "Elegant"},
        "Isabella": {"relation": "Sister", "age": "20", "occupation": "Fashion Student", "status": "Single", "temperament": "Playful", "style": "Kawaii"},
        "Claire": {"relation": "Friend", "age": "22", "occupation": "Bartender / Student", "status": "Complicated", "temperament": "Fiery", "style": "Bold"},
        "Maria": {"relation": "Friend", "age": "???", "occupation": "Student", "status": "Unknown", "temperament": "Dry", "style": "Alt"},
    }

    CITYDOM_DETAILS_PROFILES = {
        "Jennifer": {
            "nickname": "Mom", "birth": "14.03.1986", "gender": "Female", "orientation": "Heterosexual", "species": "Human",
            "bio": "She is my mom - calm, composed, and exacting. Strict in every way a parent can be, yet surprisingly understanding when it matters. She had my sister young and has spent every year since proving herself to a world that underestimated her. She rarely lets her guard down.",
            "love": -2, "corruption": 2, "obedience": 2, "level": 1,
            "height": "168cm", "weight": "58kg", "bodyType": "Hourglass", "hairColor": "Jet Black", "hairStyle": "Sleek updo", "eyes": "Dark Brown",
            "bust": "36in", "waist": "24in", "hips": "35in", "braSize": "36C", "cupSize": "C", "thigh": "22in",
            "fitnessLevel": "Moderate", "flexibility": 42, "stamina": 55, "scars": "Small scar, left knee",
            "tattoos": (), "piercings": ("Earrings",), "nipplePierced": False, "genitalPierced": False,
            "favoriteOutfit": "Tailored business suit", "underwearStyle": "Classic / Elegant", "preferredShoes": "Black heels",
            "accessories": ("Pearl necklace", "Slim watch"), "makeupPreference": "Professional",
            "confidenceLevel": 84, "intelligenceType": "Book Smart", "temperament": "Calm",
            "dominantRatio": 78, "flirtStyle": "Reserved", "humorType": "Deadpan", "phobias": ("Failure", "Vulnerability"),
            "favoritePosition": "???", "orgasmSensitivity": 45, "kinks": (), "experienceLevel": "Experienced",
            "toyPreference": (), "safeWord": "???", "relationshipStatus": "Divorced", "currentPartners": (), "crushTargets": (),
            "firstTime": "16", "experienceRating": "Expert",
        },
        "Isabella": {
            "nickname": "Bella", "birth": "22.07.2004", "gender": "Female", "orientation": "Bisexual", "species": "Human",
            "bio": "My little sister - always cheerful, clingy at the worst moments, and somehow loveable anyway. She studies fashion design and treats every day like a mood board. Beneath the bubbly surface she's more sensitive than she lets on.",
            "love": 12, "corruption": 5, "obedience": 8, "level": 2,
            "height": "162cm", "weight": "52kg", "bodyType": "Petite", "hairColor": "Dark Indigo", "hairStyle": "Twin tails", "eyes": "Light Blue",
            "bust": "34in", "waist": "22in", "hips": "33in", "braSize": "34B", "cupSize": "B", "thigh": "19in",
            "fitnessLevel": "Light", "flexibility": 78, "stamina": 38, "scars": "None",
            "tattoos": ("Small star - ankle",), "piercings": ("Earrings", "Belly button"), "nipplePierced": False, "genitalPierced": False,
            "favoriteOutfit": "Pastel crop top + mini skirt", "underwearStyle": "Cute / Kawaii", "preferredShoes": "Platform sneakers",
            "accessories": ("Hair ribbons", "Charm bracelets", "Layered rings"), "makeupPreference": "Soft glam",
            "confidenceLevel": 62, "intelligenceType": "Emotional", "temperament": "Playful",
            "dominantRatio": 18, "flirtStyle": "Shy", "humorType": "Silly", "phobias": ("Being alone", "Loud arguments"),
            "favoritePosition": "Missionary", "orgasmSensitivity": 76, "kinks": ("Teasing", "Cuddling", "Light bondage", "Praise"),
            "experienceLevel": "Novice", "toyPreference": ("Vibrator",), "safeWord": "Starlight",
            "relationshipStatus": "Single", "currentPartners": (), "crushTargets": ("Unknown",), "firstTime": "19", "experienceRating": "Novice",
        },
        "Claire": {
            "nickname": "Cee", "birth": "05.11.2002", "gender": "Female", "orientation": "Heterosexual", "species": "Human",
            "bio": "My childhood best friend. She's the life of every party and always knows how to have a good time. Behind the bright smile she carries more than she lets on - and on quiet nights she's a completely different person.",
            "love": 8, "corruption": 14, "obedience": 4, "level": 2,
            "height": "165cm", "weight": "55kg", "bodyType": "Athletic", "hairColor": "Auburn", "hairStyle": "Messy waves", "eyes": "Hazel Green",
            "bust": "35in", "waist": "23in", "hips": "36in", "braSize": "36B", "cupSize": "B", "thigh": "21in",
            "fitnessLevel": "High", "flexibility": 68, "stamina": 72, "scars": "None",
            "tattoos": ("Rose - right ribs", "Quote - inner wrist"), "piercings": ("Earrings", "Nose stud", "Nipple (R)"), "nipplePierced": True, "genitalPierced": False,
            "favoriteOutfit": "Crop top + ripped jeans", "underwearStyle": "Sporty / Minimal", "preferredShoes": "Ankle boots",
            "accessories": ("Sunglasses", "Layered necklaces", "Rings"), "makeupPreference": "Bold / Dramatic",
            "confidenceLevel": 91, "intelligenceType": "Street Smart", "temperament": "Fiery",
            "dominantRatio": 62, "flirtStyle": "Bold", "humorType": "Dirty", "phobias": ("Commitment", "Boredom"),
            "favoritePosition": "Doggy style", "orgasmSensitivity": 63, "kinks": ("Voyeurism", "Spanking", "Role-play", "Public teasing", "Rough"),
            "experienceLevel": "Experienced", "toyPreference": ("Handcuffs", "Blindfold"), "safeWord": "Crimson",
            "relationshipStatus": "It's complicated", "currentPartners": ("Unknown",), "crushTargets": (), "firstTime": "17", "experienceRating": "Expert",
        },
    }

    CITYDOM_DETAILS_SCHEDULES = {
        "Jennifer": (
            ("6:00 AM", "Morning routine", "Bathroom / Kitchen"),
            ("8:30 AM", "Leaves for work", "Office"),
            ("6:00 PM", "Returns home", "Hallway"),
            ("9:00 PM", "Reading or TV", "Lounge"),
        ),
        "Isabella": (
            ("8:00 AM", "Checks phone", "Bedroom"),
            ("10:00 AM", "Classes", "University"),
            ("6:30 PM", "Design work", "Study"),
            ("9:00 PM", "Gaming or shows", "Bedroom"),
        ),
        "Claire": (
            ("9:30 AM", "Wakes up", "Bedroom"),
            ("1:00 PM", "Part-time shift", "Bar"),
            ("5:00 PM", "Gym", "Gym"),
            ("10:00 PM", "Socials", "City"),
        ),
    }

    def citydom_details_accent(name=None):
        return CITYDOM_DETAILS_ACCENTS.get(name or store.selected_character, "#c084d4")

    def citydom_details_hex_rgba(hex_color, alpha):
        hex_color = hex_color.strip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return "#%02x%02x%02x%02x" % (r, g, b, int(max(0, min(1, alpha)) * 255))

    def citydom_details_profile(name, field, default="???"):
        profile = CITYDOM_DETAILS_PROFILES.get(name, {})
        if field in profile:
            return profile[field]
        return default

    def citydom_details_value(name, suffix, default=0):
        profile_key = {"love": "love", "Love": "love", "Corruption": "corruption", "corruption": "corruption", "Obedience": "obedience", "obedience": "obedience", "level": "level"}.get(suffix)
        store_names = (suffix, suffix.capitalize(), suffix.lower())
        for candidate in store_names:
            attr = "%s_%s" % (name, candidate)
            if hasattr(store, attr):
                return getattr(store, attr)
        if profile_key:
            return citydom_details_profile(name, profile_key, default)
        return default

    def citydom_details_info(name):
        return citydom_details_profile(name, "bio", getattr(store, "%s_Info1" % name, "Details are not available yet."))

    def citydom_details_meta(name, field, default="???"):
        if field in ("nickname", "birth", "gender", "orientation", "species", "relationshipStatus", "experienceRating", "firstTime", "experienceLevel"):
            return citydom_details_profile(name, field, default)
        if field in CITYDOM_DETAILS_PROFILES.get(name, {}):
            return CITYDOM_DETAILS_PROFILES[name][field]
        return CITYDOM_DETAILS_META.get(name, {}).get(field, default)

    def citydom_details_list(name, field):
        items = citydom_details_profile(name, field, ())
        if not items:
            return "-"
        return ", ".join([str(i) for i in items])

    def citydom_details_bool(name, field):
        return "Yes" if citydom_details_profile(name, field, False) else "No"

    def citydom_details_percent(name, field, default=0):
        value = citydom_details_profile(name, field, default)
        try:
            return int(max(0, min(100, value)))
        except Exception:
            return 0

    def citydom_details_character_image(name, view):
        ending = "Back" if view == "back" else "Front"
        candidates = (
            "CharStats/%s%s.png" % (name, ending),
            "CharStats/%s%s.png" % (name.lower(), ending),
            "CharStats/%s%s.png" % (name.capitalize(), ending),
        )
        for candidate in candidates:
            if renpy.loadable(candidate):
                return candidate
        return None

    def citydom_details_rail_portrait(name):
        path = "gui/citydom_ui_v2/details_rail_portrait_%s.png" % name
        if renpy.loadable(path):
            return path
        return "gui/citydom_ui_v2/details_rail_idle.png"

    def citydom_details_close():
        store.citydom_details_closing = True
        renpy.restart_interaction()

    def citydom_details_finish_close():
        store.citydom_details_closing = False
        store.citydom_details_tab = "info"
        store.citydom_details_body_view = "front"
        store.citydom_details_outfit = 1
        store.selected_character = "Jennifer"
        store.CharacterSelectionIsShowing = False
        store.StatsScreenShown = False
        store.ShowPhone = True
        renpy.hide_screen("StatsScreen")
        renpy.hide_screen("character_select_screen")
        renpy.show_screen("MainHud")
        renpy.restart_interaction()

transform citydom_details_show:
    subpixel True
    alpha 0.0
    zoom 0.96
    yoffset 26
    warp citydom_hud_curve 0.38 alpha 1.0 zoom 1.0 yoffset 0

transform citydom_details_hide:
    subpixel True
    alpha 1.0
    zoom 1.0
    yoffset 0
    warp citydom_hud_curve 0.28 alpha 0.0 zoom 0.97 yoffset 18

transform citydom_details_rail_motion:
    subpixel True
    on hover:
        warp citydom_hud_curve 0.14 zoom 1.10
    on idle:
        warp citydom_hud_curve 0.14 zoom 1.0

transform citydom_details_content_in:
    subpixel True
    alpha 0.0
    yoffset 12
    warp citydom_hud_curve 0.26 alpha 1.0 yoffset 0

style citydom_details_title is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 38
    color "#ffe6fb"
    outlines [ (1, "#ff5bd680", 0, 0) ]
    kerning 4

style citydom_details_label is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 11
    bold True
    color "#c69beaab"
    outlines [ (1, "#06001080", 0, 0) ]
    kerning 2

style citydom_details_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 18
    color "#efe0fff2"
    outlines [ (1, "#06001090", 0, 0) ]
    line_spacing 5

style citydom_details_small is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 13
    color "#dbc2f2e6"
    outlines [ (1, "#06001085", 0, 0) ]

style citydom_details_number is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 32
    color "#ffe6fb"
    outlines [ (1, "#ff5bd660", 0, 0) ]

screen citydom_details_stat_card(label, value, color, icon):
    $ _pct = int(130 * max(0, min(100, ((value + 20) / 40.0) * 100)) / 100.0)
    fixed:
        xysize (174, 126)
        add "gui/citydom_ui_v2/details_stat_card_bg.png"
        text icon:
            xalign 0.5
            ypos 15
            size 18
            color color
        text ("%+d" % value):
            xalign 0.5
            ypos 38
            style "citydom_details_number"
            color color
        text label.upper():
            xalign 0.5
            ypos 80
            style "citydom_details_label"
            color "#d8b2f0d8"
        add Solid("#ffffff18", xysize=(130, 4)):
            xpos 22
            ypos 106
        add Solid(color, xysize=(_pct, 4)):
            xpos 22
            ypos 106

screen citydom_details_field(label, value, x, y, w=250):
    fixed:
        xpos x
        ypos y
        xysize (w, 48)
        text label.upper():
            ypos 0
            style "citydom_details_label"
        text value:
            ypos 18
            xsize w
            style "citydom_details_small"
            color "#f1e4fff2"

screen citydom_details_bar_field(label, value, x, y, color, w=540):
    $ _value = int(max(0, min(100, value)))
    fixed:
        xpos x
        ypos y
        xysize (w, 32)
        text label.upper():
            ypos 0
            style "citydom_details_label"
        text "%d%%" % _value:
            xpos w - 38
            ypos 0
            style "citydom_details_small"
            size 9
            color color
        add Solid("#ffffff12", xysize=(w, 4)):
            ypos 22
        add Solid(color, xysize=(int(w * _value / 100.0), 4)):
            ypos 22

screen citydom_details_measure_tile(label, value, x, y, color):
    fixed:
        xpos x
        ypos y
        xysize (176, 74)
        add Transform("gui/citydom_ui_v2/details_stat_card_bg.png", xysize=(176, 74))
        text value:
            xalign 0.5
            ypos 14
            style "citydom_details_number"
            size 20
            color color
        text label.upper():
            xalign 0.5
            ypos 48
            style "citydom_details_label"
            color citydom_details_hex_rgba(color, 0.88)

screen citydom_details_section_header(title, x, y, color):
    text title.upper():
        xpos x
        ypos y
        style "citydom_details_label"
        color citydom_details_hex_rgba(color, 0.72)

screen citydom_details_tab_button(tab_id, label, x):
    $ _active = citydom_details_tab == tab_id
    $ _tab_bg = "gui/citydom_ui_v2/details_tab_active.png" if _active else None
    $ _tab_color = citydom_details_hex_rgba(citydom_details_accent(), 0.95) if _active else "#c69bea91"
    button:
        xpos x
        ypos 28
        xysize (92, 34)
        background _tab_bg
        hover_background "gui/citydom_ui_v2/details_tab_active.png"
        action SetVariable("citydom_details_tab", tab_id)
        text label.upper():
            xalign 0.5
            yalign 0.5
            style "citydom_details_label"
            color _tab_color

screen citydom_details_info_panel(name):
    $ _accent = citydom_details_accent(name)
    fixed:
        at citydom_details_content_in
        xysize (650, 1265)

        fixed:
            xpos 24
            ypos 20
            xysize (600, 150)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 150))
            text "ABOUT":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            text citydom_details_info(name):
                xpos 22
                ypos 48
                xsize 548
                ysize 84
                style "citydom_details_text"
                size 14

        fixed:
            xpos 24
            ypos 190
            xysize (600, 232)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 232))
            text "RELATIONSHIP STATS":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            fixed:
                xpos 22
                ypos 44
                xysize (90, 26)
                add Transform("gui/citydom_ui_v2/details_toggle_bg.png", xysize=(90, 26))
                text "LEVEL %d" % citydom_details_value(name, "level", 1):
                    xalign 0.5
                    ypos 6
                    style "citydom_details_label"
                    size 8
                    color _accent
            hbox:
                xpos 22
                ypos 84
                spacing 18
                use citydom_details_stat_card("Love", citydom_details_value(name, "love"), "#e864a0", "♥")
                use citydom_details_stat_card("Corruption", citydom_details_value(name, "Corruption"), "#a03cdc", "◇")
                use citydom_details_stat_card("Obedience", citydom_details_value(name, "Obedience"), "#64a0ff", "◆")

        fixed:
            xpos 24
            ypos 442
            xysize (600, 274)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 274))
            text "BASIC INFO":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Name", name, 22, 50)
            use citydom_details_field("Nickname", citydom_details_meta(name, "nickname"), 300, 50)
            use citydom_details_field("Age", citydom_details_meta(name, "age"), 22, 104)
            use citydom_details_field("Date of Birth", citydom_details_meta(name, "birth"), 300, 104)
            use citydom_details_field("Gender", citydom_details_meta(name, "gender"), 22, 158)
            use citydom_details_field("Sexual Orientation", citydom_details_meta(name, "orientation"), 300, 158)
            use citydom_details_field("Species", citydom_details_meta(name, "species"), 22, 212)
            use citydom_details_field("Occupation", citydom_details_meta(name, "occupation"), 300, 212)

        fixed:
            xpos 24
            ypos 736
            xysize (600, 294)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 294))
            text "PSYCH PROFILE":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_bar_field("Confidence", citydom_details_percent(name, "confidenceLevel"), 22, 50, _accent)
            use citydom_details_bar_field("Dominant / Submissive", citydom_details_percent(name, "dominantRatio", 50), 22, 92, "#e864a0")
            use citydom_details_field("Intelligence Type", citydom_details_profile(name, "intelligenceType"), 22, 132)
            use citydom_details_field("Temperament", citydom_details_profile(name, "temperament", citydom_details_meta(name, "temperament")), 300, 132)
            use citydom_details_field("Flirt Style", citydom_details_profile(name, "flirtStyle"), 22, 184)
            use citydom_details_field("Humor Type", citydom_details_profile(name, "humorType"), 300, 184)
            use citydom_details_field("Phobias / Turn-Offs", citydom_details_list(name, "phobias"), 22, 236, 540)

        fixed:
            xpos 24
            ypos 1050
            xysize (600, 190)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 190))
            text "RELATIONSHIP INFO":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Status", citydom_details_meta(name, "relationshipStatus", citydom_details_meta(name, "status")), 22, 50)
            use citydom_details_field("Experience Rating", citydom_details_meta(name, "experienceRating"), 300, 50)
            use citydom_details_field("First Time", citydom_details_meta(name, "firstTime"), 22, 104)
            use citydom_details_field("Current Partners", citydom_details_list(name, "currentPartners"), 300, 104)
            use citydom_details_field("Crush Targets", citydom_details_list(name, "crushTargets"), 22, 150, 520)

screen citydom_details_body_panel(name):
    $ _accent = citydom_details_accent(name)
    fixed:
        at citydom_details_content_in
        xysize (650, 1060)
        fixed:
            xpos 24
            ypos 20
            xysize (600, 222)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 222))
            text "PHYSICAL CHARACTERISTICS":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Body Type", citydom_details_profile(name, "bodyType"), 22, 54)
            use citydom_details_field("Height", citydom_details_profile(name, "height"), 300, 54)
            use citydom_details_field("Weight", citydom_details_profile(name, "weight"), 22, 112)
            use citydom_details_field("Eyes", citydom_details_profile(name, "eyes"), 300, 112)
            use citydom_details_field("Hair Color", citydom_details_profile(name, "hairColor"), 22, 162)
            use citydom_details_field("Hair Style", citydom_details_profile(name, "hairStyle"), 300, 162)

        fixed:
            xpos 24
            ypos 262
            xysize (600, 218)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 218))
            text "MEASUREMENTS":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_measure_tile("Bust", citydom_details_profile(name, "bust"), 22, 50, _accent)
            use citydom_details_measure_tile("Waist", citydom_details_profile(name, "waist"), 212, 50, _accent)
            use citydom_details_measure_tile("Hips", citydom_details_profile(name, "hips"), 402, 50, _accent)
            use citydom_details_measure_tile("Bra", citydom_details_profile(name, "braSize"), 22, 128, _accent)
            use citydom_details_measure_tile("Cup", citydom_details_profile(name, "cupSize"), 212, 128, _accent)
            use citydom_details_measure_tile("Thigh", citydom_details_profile(name, "thigh"), 402, 128, _accent)

        fixed:
            xpos 24
            ypos 504
            xysize (600, 300)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 300))
            text "HEALTH & FITNESS":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Fitness Level", citydom_details_profile(name, "fitnessLevel"), 22, 50)
            use citydom_details_field("Scars / Marks", citydom_details_profile(name, "scars"), 300, 50)
            use citydom_details_bar_field("Flexibility", citydom_details_percent(name, "flexibility"), 22, 106, "#64c8ff")
            use citydom_details_bar_field("Stamina / Endurance", citydom_details_percent(name, "stamina"), 22, 148, "#ffa050")
            use citydom_details_field("Nipple Pierced", citydom_details_bool(name, "nipplePierced"), 22, 190)
            use citydom_details_field("Genital Piercing", citydom_details_bool(name, "genitalPierced"), 300, 190)
            use citydom_details_field("Tattoos", citydom_details_list(name, "tattoos"), 22, 242)
            use citydom_details_field("Piercings", citydom_details_list(name, "piercings"), 300, 242)

        fixed:
            xpos 24
            ypos 828
            xysize (600, 202)
            add Transform("gui/citydom_ui_v2/details_card_tall_bg.png", xysize=(600, 202))
            text "STYLE & APPEARANCE":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Favorite Outfit", citydom_details_profile(name, "favoriteOutfit", citydom_details_meta(name, "style")), 22, 50)
            use citydom_details_field("Underwear Style", citydom_details_profile(name, "underwearStyle"), 300, 50)
            use citydom_details_field("Preferred Shoes", citydom_details_profile(name, "preferredShoes"), 22, 104)
            use citydom_details_field("Makeup", citydom_details_profile(name, "makeupPreference"), 300, 104)
            use citydom_details_field("Accessories", citydom_details_list(name, "accessories"), 22, 156, 540)

screen citydom_details_kinks_panel(name):
    $ _accent = citydom_details_accent(name)
    fixed:
        at citydom_details_content_in
        xysize (650, 520)
        fixed:
            xpos 24
            ypos 20
            xysize (600, 190)
            add "gui/citydom_ui_v2/details_card_tall_bg.png"
            text "EXPERIENCE & SENSITIVITY":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            use citydom_details_field("Experience Level", citydom_details_profile(name, "experienceLevel"), 22, 54)
            use citydom_details_field("Experience Rating", citydom_details_profile(name, "experienceRating"), 300, 54)
            use citydom_details_field("Favorite Position", citydom_details_profile(name, "favoritePosition"), 22, 112)
            use citydom_details_field("Safe Word", citydom_details_profile(name, "safeWord"), 300, 112)
            use citydom_details_bar_field("Sensitivity", citydom_details_percent(name, "orgasmSensitivity"), 22, 154, "#e864a0")

        fixed:
            xpos 24
            ypos 232
            xysize (600, 118)
            add "gui/citydom_ui_v2/details_card_bg.png"
            text "KINKS":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            text citydom_details_list(name, "kinks"):
                xpos 22
                ypos 54
                xsize 540
                style "citydom_details_text"
                size 15

        fixed:
            xpos 24
            ypos 370
            xysize (600, 118)
            add "gui/citydom_ui_v2/details_card_bg.png"
            text "TOY PREFERENCES":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)
            text citydom_details_list(name, "toyPreference"):
                xpos 22
                ypos 54
                xsize 540
                style "citydom_details_text"
                size 15

screen citydom_details_schedule_panel(name):
    $ _accent = citydom_details_accent(name)
    $ _schedule = CITYDOM_DETAILS_SCHEDULES.get(name, ())
    fixed:
        at citydom_details_content_in
        xysize (650, 620)
        fixed:
            xpos 24
            ypos 20
            xysize (600, 520)
            add "gui/citydom_ui_v2/details_card_tall_bg.png":
                xysize (600, 520)
            text "SCHEDULE":
                xpos 22
                ypos 18
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.72)

            if _schedule:
                vbox:
                    xpos 22
                    ypos 54
                    spacing 16
                    for time, activity, loc in _schedule:
                        hbox:
                            spacing 16
                            text time:
                                xsize 92
                                style "citydom_details_small"
                                color citydom_details_hex_rgba(_accent, 0.85)
                            vbox:
                                spacing 2
                                text activity:
                                    xsize 380
                                    style "citydom_details_text"
                                    size 15
                                text loc:
                                    xsize 380
                                    style "citydom_details_label"
                                    color "#a678c870"
            else:
                text "No schedule data available yet.":
                    xpos 22
                    ypos 58
                    style "citydom_details_text"
                    size 15

screen StatsScreen():
    modal True
    zorder 300

    if citydom_details_closing:
        timer 0.30 action Function(citydom_details_finish_close)

    key "K_ESCAPE" action Function(citydom_details_close)

    add "gui/citydom_ui_v2/details_overlay_dim.png"

    fixed:
        xpos 340
        ypos 160
        xysize (1240, 760)
        if citydom_details_closing:
            at citydom_details_hide
        else:
            at citydom_details_show

        add "gui/citydom_ui_v2/details_panel_bg.png"

        fixed:
            xpos 0
            ypos 0
            xysize (68, 760)
            add Solid("#00000855", xysize=(68, 760))
            viewport:
                xpos 0
                ypos 20
                xysize (68, 720)
                draggable True
                mousewheel True
                scrollbars None
                vbox:
                    xsize 68
                    spacing 8
                    for char_name in CITYDOM_DETAILS_CHARACTERS:
                        $ _active = selected_character == char_name
                        $ _rail_bg = "gui/citydom_ui_v2/details_rail_active.png" if _active else "gui/citydom_ui_v2/details_rail_idle.png"
                        button:
                            xalign 0.5
                            xysize (48, 48)
                            background _rail_bg
                            hover_background "gui/citydom_ui_v2/details_rail_active.png"
                            at citydom_details_rail_motion
                            action [SetVariable("selected_character", char_name), SetVariable("citydom_details_tab", "info"), SetVariable("citydom_details_body_view", "front"), SetVariable("citydom_details_outfit", 1)]
                            add citydom_details_rail_portrait(char_name):
                                xalign 0.5
                                yalign 0.5
                            if _active:
                                add Solid(citydom_details_hex_rgba(citydom_details_accent(char_name), 0.95), xysize=(2, 20)):
                                    xpos 47
                                    ypos 10

        fixed:
            xpos 68
            ypos 0
            xysize (430, 760)
            add "gui/citydom_ui_v2/details_showcase_bg.png"
            $ _accent = citydom_details_accent(selected_character)
            $ _image = citydom_details_character_image(selected_character, citydom_details_body_view)

            text citydom_details_meta(selected_character, "relation").upper():
                xpos 42
                ypos 46
                style "citydom_details_label"
                color citydom_details_hex_rgba(_accent, 0.65)

            text selected_character:
                xpos 42
                ypos 72
                xsize 340
                style "citydom_details_title"
                color "#ffe6fb"

            add Solid(citydom_details_hex_rgba(_accent, 0.30), xysize=(2, 570)):
                xpos 0
                ypos 100

            if _image:
                add Transform(_image, zoom=0.58):
                    xalign 0.5
                    ypos 158
            else:
                text "?":
                    xalign 0.5
                    ypos 260
                    size 120
                    color citydom_details_hex_rgba(_accent, 0.35)

            fixed:
                xpos 0
                ypos 660
                xysize (430, 100)
                add Solid("#0000084d", xysize=(430, 100))
                hbox:
                    xpos 50
                    ypos 40
                    spacing 10
                    text "<":
                        style "citydom_details_label"
                        color citydom_details_hex_rgba(_accent, 0.72)
                    text "OUTFIT %d" % citydom_details_outfit:
                        style "citydom_details_label"
                        color citydom_details_hex_rgba(_accent, 0.72)
                    text ">":
                        style "citydom_details_label"
                        color citydom_details_hex_rgba(_accent, 0.72)
                button:
                    xpos 300
                    ypos 32
                    xysize (94, 34)
                    background "gui/citydom_ui_v2/details_body_toggle_bg.png"
                    hover_background "gui/citydom_ui_v2/details_body_toggle_bg.png"
                    action ToggleVariable("citydom_details_body_view", true_value="back", false_value="front")
                    fixed:
                        xysize (94, 34)
                        text ("> BACK" if citydom_details_body_view == "front" else "< FRONT"):
                            xalign 0.5
                            ypos 10
                            style "citydom_details_label"
                            size 8
                            color citydom_details_hex_rgba(_accent, 0.9)

        fixed:
            xpos 498
            ypos 0
            xysize (742, 760)

            use citydom_details_tab_button("info", "Info", 42)
            use citydom_details_tab_button("body", "Body", 144)
            use citydom_details_tab_button("kinks", "Kinks", 246)
            use citydom_details_tab_button("schedule", "Schedule", 348)

            imagebutton:
                idle "gui/citydom_ui_v2/details_close_idle.png"
                hover "gui/citydom_ui_v2/details_close_hover.png"
                xpos 684
                ypos 28
                action Function(citydom_details_close)

            add "gui/citydom_ui_v2/chain_divider_details.png":
                xcenter 371
                ypos 82

            viewport:
                xpos 28
                ypos 106
                xysize (680, 620)
                draggable True
                mousewheel True
                scrollbars None

                if citydom_details_tab == "info":
                    use citydom_details_info_panel(selected_character)
                elif citydom_details_tab == "body":
                    use citydom_details_body_panel(selected_character)
                elif citydom_details_tab == "kinks":
                    use citydom_details_kinks_panel(selected_character)
                else:
                    use citydom_details_schedule_panel(selected_character)

screen character_progress_bar(character):
    null
