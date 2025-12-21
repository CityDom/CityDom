label JenniferNight34:

    scene Jennifer_night34_1 with Dissolve(0.5)
    MC "Hey mom!"
    Jennifer "....."
    scene Jennifer_night34_2 with Dissolve(0.5)
    MC "Umm.. mom?"
    Jennifer "........"
    MC "{color=#808080}*Hmmm.... what is she doing?*{/color}"
    scene Jennifer_night34_3 with Dissolve(0.5)
    MC "{color=#808080}*Oh.. she s doing her daily late night prayer....*{/color}"
    scene Jennifer_night34_4 with Dissolve(0.5)
    MC "Hey mom, I wanted to ask you.."
    Jennifer "............"
    scene Jennifer_night34_5 with Dissolve(0.5)
    MC "{color=#808080}*Ummm..... I guess if I keep disturbing her she'll be mad at me...*{/color}"
    scene Jennifer_night34_6 with Dissolve(0.5)
    MC "{color=#808080}*But I guess I could spend some more time here!*{/color}"
    scene Jennifer_night34_7 with Dissolve(0.5)
    MC "{color=#808080}*I'm shocked every time I see them...*{/color}"
    MC "{color=#808080}*Some day I'll be able to touch them too!*{/color}"
    MC "{color=#808080}*Anyway I should leave... she won't be finishing this prayer any time soon.*{/color}"
    menu:
        "Pray with her":
            MC "{color=#808080}*On second thought...*{/color}"
            scene Jennifer_night34_9 with Dissolve(0.5)
            MC "{color=#808080}*I guess I'll sit with her for a bit..*{/color}"
            scene Jennifer_night34_10 with Dissolve(0.5)
            MC "{color=#808080}*This is getting boring...*{/color}"
            scene Jennifer_night34_11 with Dissolve(0.5)
            MC "{color=#808080}*Well... Since she's not paying attention to me...*{/color}"
            scene Jennifer_night34_12 with Dissolve(0.5)
            MC "{color=#808080}*I might as well..*{/color}"
            scene Jennifer_night34_13 with Dissolve(0.5)
            MC "{color=#808080}*Enjoy the view!*{/color}"
            MC "{color=#808080}*.....*{/color}"
            MC "{color=#808080}*.............*{/color}"
            MC "{color=#808080}*With a view like that I could sit here all night!*{/color}"
            scene Jennifer_night34_14 with Dissolve(0.5)
            MC "{color=#808080}*...*{/color}"
            MC "{color=#808080}*.......*{/color}"
            MC "{color=#808080}*..................*{/color}"
            MC "Gah!"
            MC "{color=#808080}*Oh my god I gasped out loudly..*"
            MC "{color=#808080}*... No fucking way*{/color}"
            scene Jennifer_night34_15 with Dissolve(0.5)
            MC "{color=#808080}*Her robe opened..*{/color}"
            MC "{color=#808080}*They are...*{/color}"
            MC "{color=#808080}*So beautiful...*{/color}"
            scene Jennifer_night34_16 with Dissolve(0.5)
            MC "{color=#808080}*I'm in shock..*{/color}"
            MC "{color=#808080}*I can't take my eyes out of them.*{/color}"
            scene Jennifer_night34_17 with Dissolve(0.5)
            Jennifer "Amen!"
            MC "...."
            Jennifer "Ahhh, I'm exhausted."
            MC ".........."
            scene Jennifer_night34_18 with Dissolve(0.5)
            Jennifer "Hey kiddo, I'm surprised you joined me tonight."
            MC "......................."
            scene Jennifer_night34_19 with Dissolve(0.5)
            Jennifer "Ummmm kiddo?"
            Jennifer "{color=#808080}*Is he staring at my cleavage?*{/color}"
            scene Jennifer_night34_20 with Dissolve(0.5)
            MC "..........."
            Jennifer "{color=#808080}*And why do I feel a breeze on my boobs?*{/color}"
            scene Jennifer_night34_21 with Dissolve(0.5)
            Jennifer "{color=#808080}*Please don't tell me...*{/color}"
            scene Jennifer_night34_22 with Dissolve(0.5)
            Jennifer "{color=#808080}*My robe opened!!!*{/color}"
            scene Jennifer_night34_23 with Dissolve(0.5)
            Jennifer "KYAAAAAAAAA!!!"
            MC "{color=#808080}*She finally noticed... It's okay, whatever happens I'm fine with it.*{/color}"
            MC "{color=#808080}*I'm at peace.*{/color}"
            scene Jennifer_night34_25 with Dissolve(0.5)
            Jennifer "[MC], why didn't you tell me my robe opened?"
            MC "I tried to mom, but you didn't seem to pay any attention to me."
            MC "{color=#808080}*Hmmm.. That's weird.. she's not as mad as I expected her to be.*{/color}"
            scene Jennifer_night34_26 with Dissolve(0.5)
            MC "It's okay, mom, I used to see them a lot when I was little."
            MC "And besides, your robe opened up for just a second."
            MC "{color=#808080}*I think I was in trance for like 15 minutes*{/color}"
            scene Jennifer_night34_25 with Dissolve(0.5)
            Jennifer "But you are not a kid anymore [MC]..."
            Jennifer "I'm sorry, I should be more careful."
            scene Jennifer_night34_26 with Dissolve(0.5)
            MC "It doesn't matter mom.. I'm still the same kid!"
            scene Jennifer_night34_25 with Dissolve(0.5)
            Jennifer "It does matter, kiddo... You are not a kid anymore and you shouldn't see me like this!"
            Jennifer "Now please leave..."
            scene Jennifer_night34_26 with Dissolve(0.5)
            MC "Oke mom, bye!"
            call stat_reward({"Jennifer": {"love": 2, "corruption": 2, "obedience": 2}}, show_black=False, return_to=None)
            $ Location = "hallway"
            $ advance_time_or_sleep()
        "Leave":
            scene Jennifer_night34_8 with Dissolve(0.5)
            "{color=#808080}**You leave the room.**"
            $ Location = "hallway"
            $ renpy.call("GameLoop")

