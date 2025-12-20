init python:
    define_images("Isabella_Scene_8PM_", "MCEvents/MC_GetsHome/Isabella/8PM", "Isabella_Scene_8PM_", 100)

label MC_GetsHome_Isabella_8PM:
    scene Claire_Scene_6PM_4 with Dissolve(0.5)
    menu:
        "Knock":
            scene Claire_Scene_6PM_1 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_5 with Dissolve(1)
            MC "{color=#808080}*C'mooon....*"
            MC "{color=#808080}*I think they are all upstairs...*"
            scene Claire_Scene_8PM_1 with Dissolve(1)
            Jennifer "KIDS!! CAN ONE OF YOU ANSWER THE DOOR? I'M CHANGING!"
            scene Claire_Scene_8PM_2 with Dissolve(1)
            MC "{color=#808080}*Huh? Someone opened it...*"
            scene Isabella_Scene_8PM_1 with Dissolve(0.5)
            MC "Oh, Isa, what's up?"
            scene Isabella_Scene_8PM_2 with Dissolve(0.5)
            MC "Ummm.. Isa?"
            scene Isabella_Scene_8PM_3 with Dissolve(0.5)
            MC "Isaaaaaa!!"
            scene Isabella_Scene_8PM_4 with Dissolve(0.5)
            Isabella "Yeah, wait a second, I'm trying to decide on something"
            scene Isabella_Scene_8PM_5 with Dissolve(0.5)
            Isabella "I want to post a photo, but I can't chose which one."
            Isabella "What do you think?"
            scene Isabella_Scene_8PM_6 with Dissolve(0.5)
            MC "Uhhh, sure, show me..."
            scene Isabella_Scene_8PM_7 with Dissolve(0.5)
            Isabella "Okay, so between this one..."
            scene Isabella_Scene_8PM_8 with Dissolve(0.5)
            Isabella "Aaand..."
            scene Isabella_Scene_8PM_9 with Dissolve(0.5)
            Isabella "This one."
            scene Isabella_Scene_8PM_10 with Dissolve(0.5)
            Isabella "What do you think?"
            scene Isabella_Scene_8PM_11 with Dissolve(0.5)
            MC "Uhh... can you show me the first one again?"
            scene Isabella_Scene_8PM_9 with Dissolve(0.5)
            Isabella "This one?"
            scene Isabella_Scene_8PM_12 with Dissolve(0.5)
            MC "Aren't they the exact same picture?"
            scene Isabella_Scene_8PM_13 with Dissolve(0.5)
            Isabella "Ughh... why did I even think of asking you?"
            Isabella "They are clearly different..."
            scene Isabella_Scene_8PM_14 with Dissolve(0.5)
            MC "Well, if you really want me to be honest..."
            MC "I think both of them are not good"
            scene Isabella_Scene_8PM_15 with Dissolve(0.5)
            Isabella "GAAAAHHH!!!"
            scene Isabella_Scene_8PM_16 with Dissolve(0.5)
            Isabella "How could you say that?!"
            scene Isabella_Scene_8PM_17 with Dissolve(0.5)
            MC "What? You wanted my opinion."
            MC "I mean..."
            scene Isabella_Scene_8PM_18 with Dissolve(0.5)
            MC "Look at this!"
            MC "What are these clothes?"
            scene Isabella_Scene_8PM_19 with Dissolve(0.5)
            MC "You dress like you're 35."
            MC "Are these mom's clothes? I've never seen you in them."
            scene Isabella_Scene_8PM_20 with Dissolve(0.5)
            Isabella "It's hers alright?"
            Isabella "I don't have that many nice clothes..." 
            scene Isabella_Scene_8PM_21 with Dissolve(0.5)
            Isabella "But I like them. What's the problem?"
            scene Isabella_Scene_8PM_22 with Dissolve(0.5)
            MC "Isa... you look waaay too good to be wearing clothes like that..."
            scene Isabella_Scene_8PM_23 with Dissolve(0.5)
            Isabella "...."
            scene Isabella_Scene_8PM_24 with Dissolve(0.5)
            Isabella "So what are you saying? That I should dress more revealingly?"
            Isabella "I don't have clothes like that, and mom would never buy them for me..."
            Isabella "And I don't have money for that..."
            scene Isabella_Scene_8PM_25 with Dissolve(0.5)
            MC "So if I were to buy them for you, would you wear them?"
            scene Isabella_Scene_8PM_26 with Dissolve(0.5)
            Isabella "Huh? You'd actually do that?"
            scene Isabella_Scene_8PM_27 with Dissolve(0.5)
            MC "Of course I would, but only if you'd wear them"
            scene Isabella_Scene_8PM_28 with Dissolve(0.5)
            Isabella "Wait! You're actually serious!"
            Isabella "Okay then! I'll do it!"
            scene Isabella_Scene_8PM_29 with Dissolve(0.5)
            Isabella "Actually, I'll have to see them first of course..."
            Isabella "But I'll go with you to buy them, so that shouldn't be a problem..."
            scene Isabella_Scene_8PM_30 with Dissolve(0.5)
            MC "Uhhh... no you don't."
            MC "I pay for them, I chose them."
            scene Isabella_Scene_8PM_31 with Dissolve(0.5)
            Isabella "Huh?! No the hell you don't!"
            Isabella "Like I'd let you chose the clothes I'll be wearing."
            scene Isabella_Scene_8PM_32 with Dissolve(0.5)
            MC "Well... it's not like I'm making you do it."
            MC "So we either do it or we don't."
            scene Isabella_Scene_8PM_33 with Dissolve(0.5)
            Isabella "....."
            scene Isabella_Scene_8PM_34 with Dissolve(0.5)
            Isabella "Oke, but if you buy something stupid or I don't like it, don't put it on me."
            scene Isabella_Scene_8PM_35 with Dissolve(0.5)
            MC "Deal."
            scene Isabella_Scene_8PM_36 with Dissolve(0.5)
            Isabella "Deal."
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")
            $ Location = "entrance"
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")