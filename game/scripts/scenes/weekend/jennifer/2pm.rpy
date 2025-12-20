init python:
    define_images("Jennifer_weekend_2PM_", "WeekendScenes/JenniferScenes/2PM", "Jennifer_weekend_2PM_", 100)

init python:
    # Quick fade to black and back, like a camera shutter closing/opening.
    shutter = Fade(0.08, 0.04, 0.08, color="#000")

label Jennifer_weekend_2PM:
    scene Jennifer_morning44_0
    menu:
        "Knock":
            Jennifer "What?!"            
            MC "Can I come in?"
            Jennifer "Why? What now?"
            MC "Just wanted to talk, that's all."
            Jennifer "I don't know what's up with your timing. You always wanna talk when I get dressed."
            Jennifer "Wait a few minutes, I'll be out in a moment!"
            menu:
                "Wait":
                    MC "Oke..."
                    scene blackscreen with Dissolve(0.5)
                    "{color=#808080}**Fifteen minutes later...**{color=#808080}"
                    scene Jennifer_weekend_2PM_1 with Dissolve(0.5)
                    Mhyrorin "[MC]... I don't think this is a good idea..."
                    Mhyrorin "Are you suuuuuure you wanna do this?"
                    scene Jennifer_weekend_2PM_2 with Dissolve(0.5)
                    MC "Hah, don't tell me you're backing down now."
                    MC "I didn't take you for such a scaredy cat."
                    scene Jennifer_weekend_2PM_3 with Dissolve(0.5)
                    Mhyrorin "You do realize I'm scared for you, not of you, right?"
                    scene Jennifer_weekend_2PM_4 with Dissolve(0.5)
                    MC "I'm pretty strong you know? I might surprise you."
                    scene Jennifer_weekend_2PM_5 with Dissolve(0.5)
                    Mhyrorin "Aham, right..."
                    scene Jennifer_weekend_2PM_6
                    with shutter
                    pause 0.5
                    scene Jennifer_weekend_2PM_7
                    with shutter
                    pause 0.5
                    scene Jennifer_weekend_2PM_8
                    with shutter
                    pause 0.5
                    scene Jennifer_weekend_2PM_9
                    with shutter
                    pause 0.5
                    scene Jennifer_weekend_2PM_10
                    with shutter
                    pause 0.5
                    ".........."
                    scene Jennifer_weekend_2PM_11 with Dissolve(0.5)
                    Mhyrorin "Uhhh... are you good?"
                    scene Jennifer_weekend_2PM_12 with Dissolve(0.5)
                    MC "Oh, yeah, I'm peachy."
                    scene Jennifer_weekend_2PM_13 with Dissolve(0.5)
                    Mhyrorin "Are you suuuuuure?"
                    scene Jennifer_weekend_2PM_14 with Dissolve(0.5)
                    MC "Yeah... I've been thrown harder. I'm used to it at this point..."
                    scene Jennifer_weekend_2PM_15 with Dissolve(0.5)
                    Mhyrorin "Thrown harder?! Who the fuck can throw you har-"
                    scene Jennifer_weekend_2PM_16 with Dissolve(0.5)
                    Jennifer "I'm done changing honey, where are you?"
                    scene Jennifer_weekend_2PM_17 with Dissolve(0.5)
                    MC "Hey mom, I'm down here..."
                    scene Jennifer_weekend_2PM_18 with Dissolve(0.5)
                    Jennifer "OH MY GOD, [MC_upper], ARE YOU OKAY?"
                    scene Jennifer_weekend_2PM_19 with Dissolve(0.5)
                    MC "Yep, I'm peachy. I just... uhhh... tripped and fell..."
                    scene Jennifer_weekend_2PM_20 with Dissolve(0.5)
                    Jennifer "Come on [MC], you have to be more careful. You scared the crap out of me. Are you sure you are alright?"
                    scene Jennifer_weekend_2PM_21 with Dissolve(0.5)
                    MC "Yeah, yeah, I'm good. I'll be more careful."
                    scene Jennifer_weekend_2PM_22 with Dissolve(0.5)
                    Jennifer "Okay, now tell me what you wanted to talk about."
                    scene Jennifer_weekend_2PM_23 with Dissolve(0.5)
                    MC "Uhhhh, I wanted to ask If I could help you with the cleaning, but right now I think I'd rather lay down for a bit, sorry."
                    scene Jennifer_weekend_2PM_22 with Dissolve(0.5)
                    Jennifer "Haha, it's okay. Let me know if you need anything"
                    scene BlackScreen with Dissolve(0.5)
                    "{color=#808080}**Mom love + 2**{color=#808080}"
                    $ Jennifer_love = Jennifer_love + 2
                    $ check_and_update_character_stats("Jennifer")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "Ah, but I'm in a hurry..."
                    MC "I'll tell you some other time!"
                    $ Location = "Hallway"
                    $ renpy.call("GameLoop")
        "Peek":
            scene Jennifer_weekend_2PM_25 with Dissolve(0.5)
            MC "{color=#808080}*Jackpot!*{/color}"
            scene Jennifer_weekend_2PM_26 with Dissolve(0.5)
            MC "{color=#808080}*I'm BiSsing out of my fucking mind.*{/color}"
            scene Jennifer_weekend_2PM_27 with Dissolve(0.5)
            Isabella "You are fucking disgusting, you know that right?"
            scene Jennifer_weekend_2PM_28 with Dissolve(0.5)
            MC "Uhhh... fuck..."
            scene Jennifer_weekend_2PM_29 with Dissolve(0.5)
            MC "What a surprise seeing you, beautiful. Do you come here often?"
            scene Jennifer_weekend_2PM_30 with Dissolve(0.5)
            Isabella "Move over creep, I'm telling mom!"
            scene Jennifer_weekend_2PM_31 with Dissolve(0.5)
            MC "No, no, no, Isa, you can't! I will die. I'm your brother, don't you care if I die?!"
            scene Jennifer_weekend_2PM_32 with Dissolve(0.5)
            pause
            scene Jennifer_weekend_2PM_33 with Dissolve(0.5)
            MC "Okay, okay, something else... Ummmm... Uhhhhh..."
            scene Jennifer_weekend_2PM_34 with Dissolve(0.5)
            MC "A favor!"
            scene Jennifer_weekend_2PM_35 with Dissolve(0.5)
            Isabella "Move over or I'm screaming."
            scene Jennifer_weekend_2PM_36 with Dissolve(0.5)
            pause
            scene Jennifer_weekend_2PM_37 with Dissolve(0.5)
            Jennifer "Huh?"
            scene Jennifer_weekend_2PM_38 with Dissolve(0.5)
            Jennifer "KIDS!! ARE YOU THERE? WHAT ARE YOU DOING? I HOPE YOU'RE NOT FIGHTING!"
            scene Jennifer_weekend_2PM_39 with Dissolve(0.5)
            Isabella "HE IS SP-"
            scene Jennifer_weekend_2PM_40 with Dissolve(0.5)
            Isabella "MMMMMMMMMMMMMM!!!!"
            scene Jennifer_weekend_2PM_41 with Dissolve(0.5)
            MC "YEAH MOM, WE'RE NOT FIGHTING, IT'S FINE!"
            scene Jennifer_weekend_2PM_42 with Dissolve(0.5)
            Isabella "Ughhhhhh..."
            scene Jennifer_weekend_2PM_43 with Dissolve(0.5)
            MC "Okay, okay, three favors! Anything you want, any time you want, just please don't tell mom!"
            scene Jennifer_weekend_2PM_44 with Dissolve(0.5)
            Isabella "Five! And you help me with my homework without bitching!"
            scene Jennifer_weekend_2PM_45 with Dissolve(0.5)
            MC "Done, five it is plus homework, it's a deal!"
            scene Jennifer_weekend_2PM_46 with Dissolve(0.5)
            MC "Uhhhh... Thank God!"
            scene Jennifer_weekend_2PM_47 with Dissolve(0.5)
            MC "Honestly, I thought I was a goner for a second there. You didn't get this mad at me even when you caught me spying on you."
            scene Jennifer_weekend_2PM_48 with Dissolve(0.5)
            Isabella "You are such a fucking dumbass, stop talking!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You get out of the room**{/color}"
            "{color=#808080}**Jennifer love + 2**{/color}"
            "{color=#808080}**Isabella love - 2**{/color}"
            "{color=#808080}**Isabella corruption + 2**{/color}"
            $ Jennifer_love = Jennifer_love + 2
            $ Isabella_love = Isabella_love - 2
            $ Isabella_Corruption = Isabella_Corruption + 2
            $ check_and_update_character_stats("Jennifer")
            $ check_and_update_character_stats("Isabella")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Open":
            scene Jennifer_weekend_2PM_24 with Dissolve(0.5)
            Jennifer "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Mom love - 5**{color=#808080}"
            $ Jennifer_love = Jennifer_love - 5
            $ check_and_update_character_stats("Jennifer")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
