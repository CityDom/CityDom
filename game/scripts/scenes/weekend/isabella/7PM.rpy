init python:
    define_images("Isabella_weekend_7PM_", "WeekendScenes/IsabellaScenes/7PM", "Isabella_weekend_7PM_", 100)


default rant_cps = 45
default rant_scroll_duration = 16.0
default rant_scroll_start_delay = 1
default rant_visible_height = 110
default rant_auto_advance_time = 10.0


init python:
    def scroll_rant_adjustment(adj, duration=14.0):
        if adj.range <= 0:
            return

        step = adj.range / (duration * 20.0)
        new_value = min(adj.value + step, adj.range)

        try:
            adj.change(new_value)
        except Exception:
            adj.value = new_value

        renpy.restart_interaction()

style rant_dialogue is new_ui_dialogue_text:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0


screen scrolling_rant(who, what):
    modal True
    zorder 100

    default rant_adjustment = ui.adjustment()
    default rant_scroll_active = False

    fixed:
        id "window"
        xalign 0.5
        ypos 1023
        xysize (900, 250)
        at citydom_dialogue_panel_show
        add Frame(citydom_ui_asset("dialogue_glass_panel"), 6, 6, 6, 6)

        if who is not None:
            text who:
                id "who"
                xpos -2000
                ypos -2000
                xsize 1
                at citydom_dialogue_engine_text_hidden

            $ _rant_who = renpy.filter_text_tags(str(who).upper(), allow=[])

            text _rant_who:
                style "new_ui_name_text"
                xpos 36
                ypos 28
                xsize 430

            add citydom_dialogue_gradient_name(_rant_who):
                xpos 36
                ypos 28

            add citydom_ui_asset("dialogue_header_rule"):
                xpos 36
                ypos 55

        viewport:
            xpos 36
            ypos (75 if who is not None else 36)
            xsize 828
            ysize (167 if who is not None else 78)

            draggable False
            mousewheel False
            yadjustment rant_adjustment

            text what:
                id "what"
                style "rant_dialogue"
                xsize gui.dialogue_width
                slow_cps rant_cps

    timer rant_scroll_start_delay action SetScreenVariable("rant_scroll_active", True)
    timer 0.05 repeat True action If(rant_scroll_active, Function(scroll_rant_adjustment, rant_adjustment, rant_scroll_duration), NullAction())

    # Auto-continue after this many seconds.
    timer rant_auto_advance_time action Return()

    key "dismiss" action Return()


define MC_rant = Character("[mc_name]", kind=MC, screen="scrolling_rant")


label Isabella_weekend_7PM:
    scene Isabella_weekend_7PM_1 with Dissolve(0.5)
    Isabella "See? I told you it wouldn't be that bad!"

    scene Isabella_weekend_7PM_2 with Dissolve(0.5)
    Criss "Yeah... I guess you were right..."

    scene Isabella_weekend_7PM_3 with Dissolve(0.5)
    Criss "And [MC] wasn't as bad as I thought he would be. You blew it way out of proportion."

    scene Isabella_weekend_7PM_4 with Dissolve(0.5)
    Isabella "Trust me, don't let your guard down. He's behaving because you two barely know each other."

    scene Isabella_weekend_7PM_5 with Dissolve(0.5)
    MC "What the fuck does she mean I'm \"behaving only because I barely know her\"?"
    MC "I'm always on my best behavior!"

    scene Isabella_weekend_7PM_6 with Dissolve(0.5)
    Mhyrorin "To be honest..."
    extend " from the bottom of my heart... "
    extend " I couldn't give less of a fuck..."

    scene Isabella_weekend_7PM_7 with Dissolve(0.5)
    Mhyrorin "Can you remind me why I'm holding you like a damn boom pole?"

    scene Isabella_weekend_7PM_8 with Dissolve(0.5)

    $ rant_cps = 70
    $ rant_scroll_duration = 10.0
    $ rant_scroll_start_delay = 1
    $ rant_visible_height = 110
    $ rant_auto_advance_time = 10.0

    $ mc_rant = "Because it was time you'd do something to help me and also because you love me so very much and we are besties and I always play with you when you are bored and you threw me across the room that one time and you always make fun of me so it was time for some payback and it helps both of us if I could actually finally maybe get some pussy wouldn't you think so, so maybe instead of complaining so God damn much all the time you could just quit yapping and bitching and help me without making a big fuss about it!"

    $ renpy.say(MC_rant, mc_rant)
    scene Isabella_weekend_7PM_9 with Dissolve(0.5)
    Mhyrorin "Okay, okay, geez... my bad... you were letting that pile for a while huh?"
    scene Isabella_weekend_7PM_8 with Dissolve(0.5)
    MC "Thank you for understanding!"
    scene Isabella_weekend_7PM_10 with Dissolve(0.5)
    if calendar.Day == 6:
        Isabella "Okaaay, tomorrow at the same time then?"
    elif calendar.Day == 0:
        Isabella "Okaaay, see you at school!"
    scene Isabella_weekend_7PM_11 with Dissolve(0.5)
    Criss "yep, see you then!"
    scene Isabella_weekend_7PM_12 with Dissolve(0.5)
    MC "Ah, great, I missed everything, thanks a lot!"
    scene Isabella_weekend_7PM_13 with Dissolve(0.5)
    Mhyrorin "Sowwwyyy...."
    scene Isabella_weekend_7PM_14 with Dissolve(0.5)
    MC "It's okay. Let's return to headquarters. Also, only pick mes say \"sowwy\", although it was cute."
    scene BlackScreen with Dissolve(0.5)
    "...."
    scene Isabella_weekend_7PM_15 with Dissolve(0.5)
    Mhyrorin "What is a pick me?"
    scene Isabella_weekend_7PM_16 with Dissolve(0.5)
    MC "That's a conversation for another time. But in short, a bit of you with a bit of Isa with a lot of Criss."
    scene Isabella_weekend_7PM_17 with Dissolve(0.5)
    Mhyrorin "Uhhh... yeah... I'll take it as a compliment, I guess..."
    call stat_reward({"Criss": {"love": 2}, "Isabella": {"love": 2}}, return_to=None)
    $ Location = "My room"
    $ advance_time_or_sleep()
