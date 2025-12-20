init python:
    define_images("Isabella_Scene_11PM_", "MCEvents/MC_GetsHome/Isabella/11PM", "Isabella_Scene_11PM_", 100)

label MC_GetsHome_Isabella_11PM:
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
            scene Isabella_Scene_11PM_1 with Dissolve(0.5)
            "{color=#808080}*KNOCK KNOCK KNOCK!!!*"
            "...................."
            "{color=#808080}*KNOCK KNOCK KNOCK!!!*"
            scene Isabella_Scene_11PM_2 with Dissolve(0.5)
            Isabella "......"
            scene Isabella_Scene_11PM_3 with Dissolve(0.5)
            Isabella "Huh?"
            scene Isabella_Scene_11PM_4 with Dissolve(0.5)
            Isabella "Eh?"
            scene Isabella_Scene_11PM_5 with Dissolve(0.5)
            Isabella "Ehhh??!"
            scene Isabella_Scene_11PM_6 with Dissolve(0.5)
            Isabella "I'm not going! I don't care!"
            Isabella "Just because I'm the youngest that doesn't mean I have to do all the biddings around the house!"
            Isabella "Y'all always make me do this, and I'm sick of it."
            Isabella "How about one of you closes or opens the door. How about one of you gets a bottle of water. How about one of you turns off the light."
            Isabella "So I don't care!"
            scene BlackScreen with Dissolve(0.5)
            pause
            scene Isabella_Scene_11PM_7 with Dissolve(0.5)
            MC "......"
            MC "Sometimes I actually feel bad for you..."
            MC "You should seriously think about calling child protection..."
            Isabella "Are you coming in or not?"
            MC "Yeah, yeah..."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
