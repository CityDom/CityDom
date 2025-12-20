init python:
    define_images("Mhyrorin_Scene_2AM_", "MCEvents/MC_GetsHome/Mhyrorin/2AM", "Mhyrorin_Scene_2AM_", 100)

label MC_GetsHome_Mhyrorin_2AM:
    scene Jennifer_Scene_10PM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Mhyrorin_Scene_2AM_1 with Dissolve(0.5)
            MC "{color=#808080}*God damn it... I think they all fell asleep...*"
            scene Mhyrorin_Scene_2AM_2 with Dissolve(0.5)
            Mhyrorin "Damn... what are we going to do now?"
            scene Mhyrorin_Scene_2AM_3 with Dissolve(0.5)
            MC "HUH?"
            scene Mhyrorin_Scene_2AM_4 with Dissolve(0.5)
            MC "You really have to stop doing this shit."
            MC "I'm not even jumping anymore, my heart just stops for 3 seconds."
            MC "I'll just drop flat one day, and you're going right after me..."
            scene Mhyrorin_Scene_2AM_5 with Dissolve(0.5)
            Mhyrorin "Maybe stop being such a bitch."
            scene Mhyrorin_Scene_2AM_6 with Dissolve(0.5)
            Mhyrorin "Ever tought about it?"
            scene Mhyrorin_Scene_2AM_7 with Dissolve(0.5)
            MC "So did you came here just to make fun of me? Or to what do I owe the pleasure?"
            scene Mhyrorin_Scene_2AM_8 with Dissolve(0.5)
            Mhyrorin "Got a bit of free time, can't I just spend it with you?"
            scene Mhyrorin_Scene_2AM_9 with Dissolve(0.5)
            Mhyrorin "Stop looking at my tits god damn it!" 
            scene Mhyrorin_Scene_2AM_10 with Dissolve(0.5)
            MC "Ma'am, I don't want to sound objectifying..."
            MC "But half of you is tits!"
            scene Mhyrorin_Scene_2AM_11 with Dissolve(0.5)
            Mhyrorin "You're lucky I'm taking that as a compliment..."
            scene Mhyrorin_Scene_2AM_12 with Dissolve(0.5)
            Mhyrorin "So do you plan to stay out here all night?"
            MC "Do I have an option?"
            Mhyrorin "Is your window open?"
            MC "Uhh... yes? Can you get in and open the door from the other side?"
            scene Mhyrorin_Scene_2AM_13 with Dissolve(0.5)
            Mhyrorin "That just sounds like extra steps..."
            scene Mhyrorin_Scene_2AM_14 with Dissolve(0.5)
            Mhyrorin "You're coming with me!"
            scene Mhyrorin_Scene_2AM_15 with Dissolve(0.5)
            MC "UHHHH.... I can wait for you to open the door, you know?"
            MC "Or I can sleep outside, there's no problem, it wouldn't be the first time, haha!"
            scene Mhyrorin_Scene_2AM_16 with Dissolve(0.5)
            Mhyrorin "Stop being such a bitch!"
            scene Mhyrorin_Scene_2AM_17 with Dissolve(0.5)
            Mhyrorin "It's gonna be fun!"
            scene BlackScreen with Dissolve(0.5)
            MC "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            scene Mhyrorin_Scene_2AM_18 with Dissolve(0.5)
            MC "Just... uhhh... Please don't drop me, okay?"
            scene Mhyrorin_Scene_2AM_19 with Dissolve(0.5)
            Mhyrorin "Yeah, yeah, I'm not dropping you... stop crying..."
            scene Mhyrorin_Scene_2AM_20 with Dissolve(0.5)
            Mhyrorin "Even if I were to drop you, I can catch you like 10 times over!"
            scene Mhyrorin_Scene_2AM_21 with Dissolve(0.5)
            Mhyrorin "Wanna see?"
            scene Mhyrorin_Scene_2AM_22 with Dissolve(0.5)
            MC "I'd have a heart attack and die before you'd catch me the first time."
            MC "Just get me in my room please..."
            scene Mhyrorin_Scene_2AM_23 with Dissolve(0.5)
            MC "Oh my god, I love you floor, I'll never disrespect you again!"
            scene Mhyrorin_Scene_2AM_24 with Dissolve(0.5)
            Mhyrorin "Stop bitching, we barely flew five meters..."
            scene Mhyrorin_Scene_2AM_25 with Dissolve(0.5)
            MC "That's five meters more than what I'd like to be, alright?"
            scene Mhyrorin_Scene_2AM_26 with Dissolve(0.5)
            Mhyrorin "Yeah, yeah, whatever, you'll get used to it."
            scene Mhyrorin_Scene_2AM_27 with Dissolve(0.5)
            Mhyrorin "Anyway, I gotta go now, be safe alright?"
            scene Mhyrorin_Scene_2AM_28 with Dissolve(0.5)
            MC "Alright mom, I'll be safe, it's not like you tell me this twelve times a day..."
            scene Mhyrorin_Scene_2AM_29 with Dissolve(0.5)
            Mhyrorin "Okay then, cya!"
            scene BlackScreen with Dissolve(0.1)
            $ renpy.pause(0.1, hard=True)
            scene Mhyrorin_Scene_2AM_30 with Dissolve(0.1)
            MC "...."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "my room"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
