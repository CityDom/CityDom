default talked_to_mom = False
default complimented_mom = False
default flirted_with_mom = False

default talked_to_Isabella = False
default complimented_Isabella = False
default flirted_with_Isabella = False

default talked_to_Clair = False
default complimented_Clair = False
default flirted_with_Clair = False

default dropped_fork = False
default checked_mom = False
default checked_Isabella = False
default checked_Clair = False
init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("DinnerScene", "DinnerGroupScenes", "DinnerScene", 100)

label DinnerEventLVL1:
    scene DinnerScene25 with Dissolve(0.5)
    McMom "Come on already, breakfast is getting cold!"
    MC "I know, sorry for being late."
    McMom "Come sit down, kiddo."
    scene DinnerScene25 with Dissolve(0.5)
    menu:
        "eat":
            label DinnerMenuLVL1:
                scene DinnerScene24 with Dissolve(0.5)
                McMom "Did it get cold?"
                MC "No mom, it's still hot."
                McMom "I'm glad to hear that, is it good?"
                MC "It's really good mom."
                McMom "Thank you kiddo, I really spent a lot of time on it."
                label talk_menu:
                    scene DinnerScene24 with Dissolve(0.5)
                    menu:
                        "Talk to mom":
                            menu:
                                "talk":
                                    if talked_to_mom:
                                        MC "{color=#808080}**I already talked to her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "Hey mom, how is work lately?"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "Oh wow, since when do you care so much about my work?"
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "I always cared mom!"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "It's been okay kiddo, a lot of ups and downs as always, but right now things are pretty bad..."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "I'm sorry to hear that, mom, is there anything I can do to help?"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "You can eat up and tell me how good it is."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "I'll take that as a no..."
                                        scene DinnerScene24 with Dissolve(0.5)
                                        $ talked_to_mom = True
                                        jump talk_menu
                                "compliment":
                                    if complimented_mom:
                                        MC "{color=#808080}**I already complimented her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "Hey mom, did you eat already?"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "No, I just decided to not eat in the morning and late at night anymore, I'll just grab something at work."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "There is still some time until lunch, you will starve until then."
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "That's the point kiddo, I'm trying to lose weight."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "What!?!"
                                        MC "Why would you want to lose weight?"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "I'm getting old, [MC], I put weight a lot faster now."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "That's not true, mom!!"
                                        MC "You look like a model, you are the best looking mom I've ever seen!"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "Awwwww, thank you kiddo, that's sweet, but I don't know if that's really the case."
                                        McMom "I have to lose some more weight."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "That weight is distributed in all the nice places mom, I don't think you should lose any!"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "Okay, kiddo, that's sweet, but that's no way to talk to your mom."
                                        McMom "You are stretching your luck here."
                                        McMom "Now finish your food, it's getting cold."
                                        $ Mom_love = Mom_love + 2
                                        $ check_and_update_character_stats("Mom")
                                        $ complimented_mom = True
                                        scene DinnerScene24 with Dissolve(0.5)
                                        jump talk_menu
                                "flirt":
                                    if flirted_with_mom:
                                        MC "{color=#808080}**I already flirted with her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "Hey mom, the food is looking really good!"
                                        scene DinnerScene23 with Dissolve(0.5)
                                        McMom "Aww, thank you kiddo, I really put a lot of effort into it."
                                        scene DinnerScene22 with Dissolve(0.5)
                                        MC "No need to thank me mom, it's delicious!"
                                        scene DinnerScene26 with Dissolve(0.5)
                                        MC "And you are looking really good as well today!"
                                        scene DinnerScene21 with Dissolve(0.5)
                                        McMom "You shouldn't stare at your mom like that kiddo!"
                                        MC "I'm sorry mom I just..."
                                        McMom "Just shut up and eat your food already!"
                                        $ Mom_love = Mom_love - 5
                                        $ Mom_Corruption = Mom_Corruption + 2
                                        $ check_and_update_character_stats("Mom")
                                        $ flirted_with_mom = True
                                        scene DinnerScene24 with Dissolve(0.5)
                                        jump talk_menu
                        "Talk to Isabella":
                            menu:
                                "talk":
                                    if talked_to_Isabella:
                                        MC "{color=#808080}**I already talked to her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene19 with Dissolve(0.5)
                                        MC "Hey sis, how is school lately?"
                                        scene DinnerScene13 with Dissolve(0.5)
                                        Isabella "Since when do you care about what I'm doing in school?"
                                        scene DinnerScene19 with Dissolve(0.5)
                                        MC "Sheesh, Isa, you don't need to be so harsh, I always cared."
                                        scene DinnerScene13 with Dissolve(0.5)
                                        Isabella "Yeah, sure, I've been doing okay, nothing special."
                                        $ talked_to_Isabella = True
                                        scene DinnerScene24 with Dissolve(0.5)
                                        jump talk_menu
                                "compliment":
                                    if complimented_Isabella:
                                        MC "{color=#808080}**I already complimented her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene14 with Dissolve(0.5)
                                        MC "Hey sis, how's the food?"
                                        scene DinnerScene27 with Dissolve(0.5)
                                        Isabella "It's really good, mom outdid herself again!"
                                        scene DinnerScene28 with Dissolve(0.5)
                                        MC "Are you really eating all of that? Didn't you say that you were going to eat less?"
                                        scene DinnerScene29 with Dissolve(0.5)
                                        Isabella "Obviously I'm not eating all this, mom just put all of this on my plate."
                                        Isabella "But yea, I'm trying to eat a bit less."
                                        scene DinnerScene30 with Dissolve(0.5)
                                        MC "Why would you do that? You already look amazing!"
                                        scene DinnerScene31 with Dissolve(0.5)
                                        Isabella "Thank you bro, but I could look better."
                                        scene DinnerScene32 with Dissolve(0.5)
                                        McMom "Enough with the weird talk, kids!"
                                        McMom "The food is getting cold!!"
                                        scene DinnerScene29 with Dissolve(0.5)
                                        Isabella "Okay, mom..."
                                        $ LilSis_love = LilSis_love + 2
                                        $ check_and_update_character_stats("LilSis")
                                        $ complimented_Isabella = True
                                        scene DinnerScene24 with Dissolve(0.5)
                                        jump talk_menu
                                "flirt":
                                    if flirted_with_Isabella:
                                        MC "{color=#808080}**I already flirted with her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene19 with Dissolve(0.5)
                                        MC "Hey sis, looking good this morning."
                                        scene DinnerScene27 with Dissolve(0.5)
                                        Isabella "Thanks bro, I've been trying to lose some weight lately."
                                        scene DinnerScene28 with Dissolve(0.5)
                                        MC "It shows, Isa, you are looking amazing!"
                                        scene DinnerScene33 with Dissolve(0.5)
                                        MC "You look reaaaly good!"
                                        scene DinnerScene34 with Dissolve(0.5)
                                        Isabella "Stop staring at me like that, [MC], it's disgusting."
                                        $ LilSis_love = LilSis_love - 5
                                        $ check_and_update_character_stats("LilSis")
                                        $ flirted_with_Isabella = True
                                        scene DinnerScene24 with Dissolve(0.5)
                                        jump talk_menu
                        "Talk to Claire":
                            menu:
                                "talk":
                                    if talked_to_Clair:
                                        MC "{color=#808080}**I already talked to her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene12 with Dissolve(0.5)
                                        MC "Hey Claire, how's the food?"
                                        Clair "Just let me eat in peace loser..."
                                        MC "Geez...."
                                        $ talked_to_Clair = True
                                        jump talk_menu
                                "compliment":
                                    if complimented_Clair:
                                        MC "{color=#808080}**I already complimented her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene12 with Dissolve(0.5)
                                        MC "Hey, Claire, I see you are starting to eat less and less, is everything ok?"
                                        Clair "Nothing that concerns you."
                                        MC "Come on, Claire, why do you have to be so cold?"
                                        MC "I'm saying that because it shows, you are looking better and better!"
                                        scene DinnerScene11 with Dissolve(0.5)
                                        Clair "...."
                                        Clair "Don't try to compliment me, it's disgusting."
                                        MC "{color=#808080}*So there is some humanity in her after all*{/color}"
                                        $ complimented_Clair = True
                                        jump talk_menu
                                "flirt":
                                    if flirted_with_Clair:
                                        MC "{color=#808080}**I already complimented her.**"
                                        jump talk_menu
                                    else:
                                        scene DinnerScene12 with Dissolve(0.5)
                                        MC "Hey Clair, you're looking really hot this morning!"
                                        Clair "Don't say disgusting stuff like that to me, loser!"
                                        $ flirted_with_Clair = True
                                        jump talk_menu
                        "Drop the fork":
                            if dropped_fork:
                                MC "{color=#808080}*It would be weird if I dropped it twice*{/color}"
                                jump talk_menu
                            else:
                                scene DinnerScene1 with Dissolve(0.5)
                                MC "Damn, I dropped my fork!"
                                Clair "You are such a dumbass."
                                McMom "Claire!!! Watch your mouth!"
                                MC "I don't really see where it landed..."
                                MC "{color=#808080}*Okay, now who should I check out?*{/color}"
                                menu:
                                    "check out mom":
                                        if checked_mom or checked_Isabella or checked_Clair:
                                            MC "{color=#808080}*They will start to suspect me, I should just get up*{/color}"
                                            jump talk_menu
                                        else: 
                                            scene DinnerScene7 with Dissolve(0.5)
                                            MC "{color=#808080}*Damn... I hope she's not looking under the table as well...*{/color}"
                                            McMom "Have you found it yet?!"
                                            MC "Just a second mom, I can't manage to grab it!"
                                            scene DinnerScene6 with Dissolve(0.5)
                                            MC "{color=#808080}*Damn, always sitting like a lady, huh? Not my lucky day I guess...*{/color}"
                                            McMom "What it's taking so long? Just get up already!"
                                            MC "Just a second, I almost got it..."
                                            MC "{color=#808080}*I can't even get a little peak*{/color}"
                                            MC "I've got it!!"
                                            $ checked_mom = True
                                            $ checked_Isabella = True
                                            $ checked_Clair = True
                                            $ dropped_fork = True
                                            jump talk_menu
                                    "check out Isabella":
                                        if checked_mom or checked_Isabella or checked_Clair:
                                            MC "{color=#808080}*They will start to suspect me, I should just get up*{/color}"
                                            jump talk_menu
                                        else: 
                                            scene DinnerScene5 with Dissolve(0.5)
                                            MC "{color=#808080}*I hope Isa won't see me...*{/color}"
                                            Isabella "What are you doing down there? Just get the fork already!"
                                            MC "I'm trying sis, I don't see where it landed!"
                                            scene DinnerScene4 with Dissolve(0.5)
                                            Isabella "Do you want me to help you look for it?"
                                            MC "{color=#808080}*fuck, fuck, fuck!*{/color}"
                                            MC "It's okay, I think I see it, no need to look for it!"
                                            Isabella "..."
                                            Isabella "Did you get it? I hope you are not doing something stupid."
                                            MC "Yep, got it!"
                                            $ checked_mom = True
                                            $ checked_Isabella = True
                                            $ checked_Clair = True
                                            $ dropped_fork = True
                                            jump talk_menu
                                    "check out Claire":
                                        if checked_mom or checked_Isabella or checked_Clair:
                                            MC "{color=#808080}*They will start to suspect me, I should just get up*{/color}"
                                            jump talk_menu
                                        else:
                                            scene DinnerScene3 with Dissolve(0.5)
                                            MC "{color=#808080}*I hope she just minds her business as always...*{/color}"
                                            MC "{color=#808080}*I really cant risk it with her...*{/color}"
                                            scene DinnerScene2 with Dissolve(0.5)
                                            MC "{color=#808080}*I can't see anything from this angle anyway*{/color}"
                                            Clair "What the fuck are you doing loser? The fork is right there, where are you looking?"
                                            McMom "CLAIRE!!!!"
                                            Clair "Alright, I'm sorry..."
                                            MC "{color=#808080}*Thanks god for mom..*{/color}"
                                            $ checked_mom = True
                                            $ checked_Isabella = True
                                            $ checked_Clair = True
                                            $ dropped_fork = True
                                            jump talk_menu
                        "Leave":
                            scene DinnerScene23 with Dissolve(0.5)
                            McMom "Wait, what are you doing? You didn't finish your food!"
                            MC "I'm so sorry mom, I really have to go."
                            McMom "Okay.... I'll leave it in the fridge."
                            $ talked_to_mom = False
                            $ complimented_mom = False
                            $ flirted_with_mom = False
                            $ talked_to_Isabella = False
                            $ complimented_Isabella = False
                            $ flirted_with_Isabella = False
                            $ talked_to_Clair = False
                            $ complimented_Clair = False
                            $ flirted_with_Clair = False
                            $ dropped_fork = False
                            $ checked_mom = False
                            $ checked_Isabella = False
                            $ checked_Clair = False
                            $ Location = "Entrance"
                            $ advance_time_or_sleep()
        "leave":
            MC "Sorry mom, I really don't have time now."
            $ Location = "Entrance"
            $ renpy.call("GameLoop")