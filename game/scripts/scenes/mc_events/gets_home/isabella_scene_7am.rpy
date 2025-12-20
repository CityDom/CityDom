init python:
    define_images("Isabella_Scene_7AM_", "MCEvents/MC_GetsHome/Isabella/7AM", "Isabella_Scene_7AM_", 100)

label MC_GetsHome_Isabella_7AM:
    scene Jennifer_Scene_6AM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_6AM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_4 with Dissolve(0.5)
            Isabella "Mom!! Someone is knocking at the door!!"
            "....."
            Jennifer "I AM IN THE SHOWER, ISABELLA! GO ANSWER THE DOOR!"
            Isabella "Ughhh, why do I gotta do everything in this house!"
            scene Isabella_Scene_7AM_1 with Dissolve(0.5)
            Isabella "Yeah, we don't buy anything, sorry."
            scene Isabella_Scene_7AM_2 with Dissolve(0.5)
            Isabella "Oh, sorry, I thought you were the sales man."
            scene Isabella_Scene_7AM_3 with Dissolve(0.5)
            MC "You open the door to the sales man dressed like that?"
            scene Isabella_Scene_7AM_4 with Dissolve(0.5)
            Isabella "Huh? Of course not, yuck!"
            scene Isabella_Scene_7AM_5 with Dissolve(0.5)
            Isabella "That's why I hid behind the door."
            scene Isabella_Scene_7AM_6 with Dissolve(0.5)
            Isabella "But why do you ask? You think this outfit is too revealing?"
            scene Isabella_Scene_7AM_7 with Dissolve(0.5)
            MC "Ummm, not really..."
            MC "I just don't want any weirdo to be staring at my little sister."
            scene Isabella_Scene_7AM_8 with Dissolve(0.5)
            Isabella "Like you're doing right now?"
            scene Isabella_Scene_7AM_9 with Dissolve(0.5)
            MC "Yeah, but I'm not \"any weirdo\"!"
            scene Isabella_Scene_7AM_10 with Dissolve(0.5)
            Isabella "Right, you are my brother, that's why it's even weirder..."
            Isabella "You almost made a cute comment, but you had to ruin it, like always..."
            Isabella "Just get in the house already..."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")