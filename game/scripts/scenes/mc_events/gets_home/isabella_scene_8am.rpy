init python:
    define_images("Isabella_Scene_8AM_", "MCEvents/MC_GetsHome/Isabella/8AM", "Isabella_Scene_8AM_", 100)

label MC_GetsHome_Isabella_8AM:
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
            Jennifer "Isabella, go see who is at the door!"
            Isabella "I'm in the shower! Why don't you go?!"
            Jennifer "I HAVE TO STIR THE FOOD, ISABELLA!"
            scene Isabella_Scene_8AM_1 with Dissolve(0.5)
            MC "{color=#808080}*Uhhhh, this is gonna take a while...*{color=#808080}"
            scene Isabella_Scene_8AM_2 with Dissolve(0.5)
            Isabella "I SAID I'M IN THE SHOWER! I CAN'T RIGHT NOW! TELL CLAIRE OR [MC_upper]!"
            scene Isabella_Scene_8AM_3 with Dissolve(0.5)
            Jennifer "CLAIRE IS AT THE TOILET UPSTAIRS, AND [MC_upper] IS NOT HOME."
            Jennifer "I'M NOT ARGUING WITH YOU ANYMORE, ISABELLA, GO RIGHT NOW!"
            scene Isabella_Scene_8AM_4 with Dissolve(0.5)
            Isabella "OH, BUT WHEN YOU ARE IN THE SHOWER, IT'S STILL ME WHO HAS TO GO?!?!"
            Jennifer "....."
            scene Isabella_Scene_8AM_5 with Dissolve(0.5)
            Isabella "UGHHHH!!!"
            scene Isabella_Scene_8AM_6 with Dissolve(0.5)
            MC "{color=#808080}*I better set out a tent, who knows how long I'll be here...*{color=#808080}"
            scene Isabella_Scene_8AM_7 with Dissolve(0.5)
            Isabella "YEAH, WHO THE FU... WHO IS IT?!?!"
            scene Isabella_Scene_8AM_8 with Dissolve(0.5)
            MC "Just open the door already..."
            scene Isabella_Scene_8AM_9 with Dissolve(0.5)
            Isabella "Have you grown so senile you can't remember to get your damn keys?!"
            scene Isabella_Scene_8AM_10 with Dissolve(0.5)
            MC "Ihh, someone is a bit mad today..."
            scene Isabella_Scene_8AM_11 with Dissolve(0.5)
            MC "And why are you wet?"
            scene Isabella_Scene_8AM_12 with Dissolve(0.5)
            Isabella "It's a crazy new trend where people pour water on themselves and then use a thing called soap."
            Isabella "Have you ever thought of trying it?"
            scene Isabella_Scene_8AM_13 with Dissolve(0.5)
            Isabella "Igh{w=0.2}{nw}"
            scene Isabella_Scene_8AM_14 with Dissolve(0.2)
            MC "Since when did you get so sarcastic?"
            scene Isabella_Scene_8AM_15 with Dissolve(0.2)
            Isabella "Close the door, [MC], what the hell, what if someone sees me?!"
            scene Isabella_Scene_8AM_16 with Dissolve(0.2)
            MC "I'm standing in front of the door for a reason."
            MC "Do you think I'd let anyone see you like this?"
            scene Isabella_Scene_8AM_17  with Dissolve(0.2)
            Isabella "Just get in already..."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")