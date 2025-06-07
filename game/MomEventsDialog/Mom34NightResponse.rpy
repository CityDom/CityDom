label MomNight34:

    scene NIGHT34MOM1 with Dissolve(0.5)
    MC "Hey mom!"
    McMom "....."
    scene NIGHT34MOM2 with Dissolve(0.5)
    MC "Umm.. mom?"
    McMom "........"
    MC "{color=#808080}*Hmmm.... what is she doing?*{/color}"
    scene NIGHT34MOM3 with Dissolve(0.5)
    MC "{color=#808080}*Oh.. she s doing her daily late night prayer....*{/color}"
    scene NIGHT34MOM4 with Dissolve(0.5)
    MC "Hey mom, I wanted to ask you.."
    McMom "............"
    scene NIGHT34MOM5 with Dissolve(0.5)
    MC "{color=#808080}*Ummm..... I guess if I keep disturbing her she'll be mad at me...*{/color}"
    scene NIGHT34MOM6 with Dissolve(0.5)
    MC "{color=#808080}*But I guess I could spend some more time here!*{/color}"
    scene NIGHT34MOM7 with Dissolve(0.5)
    MC "{color=#808080}*I'm shocked every time I see them...*{/color}"
    MC "{color=#808080}*Some day I'll be able to touch them too!*{/color}"
    MC "{color=#808080}*Anyway I should leave... she won't be finishing this prayer any time soon.*{/color}"
    menu:
        "Pray with her":
            MC "{color=#808080}*On second thought...*{/color}"
            scene NIGHT34MOM9 with Dissolve(0.5)
            MC "{color=#808080}*I guess I'll sit with her for a bit..*{/color}"
            scene NIGHT34MOM10 with Dissolve(0.5)
            MC "{color=#808080}*This is getting boring...*{/color}"
            scene NIGHT34MOM11 with Dissolve(0.5)
            MC "{color=#808080}*Well... Since she's not paying attention to me...*{/color}"
            scene NIGHT34MOM12 with Dissolve(0.5)
            MC "{color=#808080}*I might as well..*{/color}"
            scene NIGHT34MOM13 with Dissolve(0.5)
            MC "{color=#808080}*Enjoy the view!*{/color}"
            MC "{color=#808080}*.....*{/color}"
            MC "{color=#808080}*.............*{/color}"
            MC "{color=#808080}*With a view like that I could sit here all night!*{/color}"
            scene NIGHT34MOM14 with Dissolve(0.5)
            MC "{color=#808080}*...*{/color}"
            MC "{color=#808080}*.......*{/color}"
            MC "{color=#808080}*..................*{/color}"
            MC "Gah!"
            MC "{color=#808080}*Oh my god I gasped out loudly..*"
            MC "{color=#808080}*... No fucking way*{/color}"
            scene NIGHT34MOM15 with Dissolve(0.5)
            MC "{color=#808080}*Her robe opened..*{/color}"
            MC "{color=#808080}*They are...*{/color}"
            MC "{color=#808080}*So beautiful...*{/color}"
            scene NIGHT34MOM16 with Dissolve(0.5)
            MC "{color=#808080}*I'm in shock..*{/color}"
            MC "{color=#808080}*I can't take my eyes out of them.*{/color}"
            scene NIGHT34MOM17 with Dissolve(0.5)
            McMom "Amen!"
            MC "...."
            McMom "Ahhh, I'm exhausted."
            MC ".........."
            scene NIGHT34MOM18 with Dissolve(0.5)
            McMom "Hey kiddo, I'm surprised you joined me tonight."
            MC "......................."
            scene NIGHT34MOM19 with Dissolve(0.5)
            McMom "Ummmm kiddo?"
            McMom "{color=#808080}*Is he staring at my cleavage?*{/color}"
            scene NIGHT34MOM20 with Dissolve(0.5)
            MC "..........."
            McMom "{color=#808080}*And why do I feel a breeze on my boobs?*{/color}"
            scene NIGHT34MOM21 with Dissolve(0.5)
            McMom "{color=#808080}*Please don't tell me...*{/color}"
            scene NIGHT34MOM22 with Dissolve(0.5)
            McMom "{color=#808080}*My robe opened!!!*{/color}"
            scene NIGHT34MOM23 with Dissolve(0.5)
            McMom "KYAAAAAAAAA!!!"
            MC "{color=#808080}*She finally noticed... It's okay, whatever happens I'm fine with it.*{/color}"
            MC "{color=#808080}*I'm at peace.*{/color}"
            scene NIGHT34MOM25 with Dissolve(0.5)
            McMom "[MC], why didn't you tell me my robe opened?"
            MC "I tried to mom, but you didn't seem to pay any attention to me."
            MC "{color=#808080}*Hmmm.. That's weird.. she's not as mad as I expected her to be.*{/color}"
            scene NIGHT34MOM26 with Dissolve(0.5)
            MC "It's okay, mom, I used to see them a lot when I was little."
            MC "And besides, your robe opened up for just a second."
            MC "{color=#808080}*I think I was in trance for like 15 minutes*{/color}"
            scene NIGHT34MOM25 with Dissolve(0.5)
            McMom "But you are not a kid anymore [MC]..."
            McMom "I'm sorry, I should be more careful."
            scene NIGHT34MOM26 with Dissolve(0.5)
            MC "It doesn't matter mom.. I'm still the same kid!"
            scene NIGHT34MOM25 with Dissolve(0.5)
            McMom "It does matter, kiddo... You are not a kid anymore and you shouldn't see me like this!"
            McMom "Now please leave..."
            scene NIGHT34MOM26 with Dissolve(0.5)
            MC "Oke mom, bye!"
            "{color=#808080}**Mom love + 2**{color=#808080}"
            "{color=#808080}**Mom corruption + 2**{color=#808080}"
            "{color=#808080}**Mom obedience + 2**{color=#808080}"
            $ Mom_Corruption = Mom_Corruption + 2
            $ Mom_love = Mom_love + 2
            $ Mom_Obedience = Mom_Obedience + 2
            $ check_and_update_character_stats("Mom")
            $ Location = "hallway"
            $ advance_time_or_sleep()
        "Leave":
            scene NIGHT34MOM8 with Dissolve(0.5)
            "{color=#808080}**You leave the room.**"
            $ Location = "hallway"
            $ renpy.call("GameLoop")

