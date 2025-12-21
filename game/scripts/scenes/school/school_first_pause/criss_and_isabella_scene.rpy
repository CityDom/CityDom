init python:
    define_images("CrissAndIsabellaScene", "SchoolFirstPause/CrissAndIsabellaEventScene", "CrissAndIsabellaScene", 100)

label CrissAndIsabellaFirstPauseScene:
    $ Maria_Report_Criss = True
    scene CrissAndIsabellaScene1 with Dissolve(0.5)
    MC "Hey girls, what's up?"
    scene CrissAndIsabellaScene2 with Dissolve(0.5)
    Isabella "Hey, bro!"
    Criss "Hey, [MC]!"
    scene CrissAndIsabellaScene3 with Dissolve(0.5)
    Isabella "We're just gossiping, making time pass faster, it's pretty boring in here..."
    Isabella "How about you? Did you make any friends?"
    scene CrissAndIsabellaScene4 with Dissolve(0.5)
    MC "I mean... I didn't got the chance yet, but most of them seem alright... I think..."
    scene CrissAndIsabellaScene5 with Dissolve(0.5)
    Isabella "And how about your desk mate? Did you two get along?"
    scene CrissAndIsabellaScene6 with Dissolve(0.5)
    MC "Oh, Maria? She's actually really cool, we get along pretty well."
    MC "And she's my type, but don't tell her."
    scene CrissAndIsabellaScene7 with Dissolve(0.5)
    Isabella "Is she huh?! Well, since you don't have that many friends, why not spend some time with us, huh?"
    scene CrissAndIsabellaScene8 with Dissolve(0.5)
    MC "Uhhh... okay..."
    scene CrissAndIsabellaScene9 with Dissolve(0.5)
    Isabella "Let's play truth or dare!"
    scene CrissAndIsabellaScene10 with Dissolve(0.5)
    Criss "Right here? On the staircase? Are you sure?"
    scene CrissAndIsabellaScene11 with Dissolve(0.5)
    Isabella "You worry about it too much, it's okay, who cares."
    scene CrissAndIsabellaScene12 with Dissolve(0.5)
    MC "Okay then, who's first?"
    scene CrissAndIsabellaScene13 with Dissolve(0.5)
    Isabella "You are, now chose, truth or dare?"
    scene CrissAndIsabellaScene14 with Dissolve(0.5)
    MC "Hmmm... truth.."
    scene CrissAndIsabellaScene13 with Dissolve(0.5)
    Isabella "Is it true that you already like a girl from this school?"
    scene CrissAndIsabellaScene15 with Dissolve(0.5)
    MC "Yeah, that's true."
    scene CrissAndIsabellaScene13 with Dissolve(0.5)
    Isabella "Really...? And who is that?"
    scene CrissAndIsabellaScene15 with Dissolve(0.5)
    MC "I already answered if It's true that I liked someone, I don't have to answer that as well."
    scene CrissAndIsabellaScene16 with Dissolve(0.5)
    Isabella "Ughhh!!"
    scene CrissAndIsabellaScene17 with Dissolve(0.5)
    Isabella "Okay!"
    scene CrissAndIsabellaScene18 with Dissolve(0.5)
    Isabella "You're next Criss, truth or date?!"
    scene CrissAndIsabellaScene19 with Dissolve(0.5)
    Criss "Me?! Uhhh... ummm..."
    Criss "Dare..."
    scene CrissAndIsabellaScene20 with Dissolve(0.5)
    Isabella "Hehe, I dare you to go in the hallway and scream as loud as you can!"
    scene CrissAndIsabellaScene21 with Dissolve(0.5)
    Criss "Wait, wait, wait, anything but that please, I don't want to draw attention or cause any problems!"
    scene CrissAndIsabellaScene22 with Dissolve(0.5)
    Isabella "A dare is a dare, Criss, you gotta do it!"
    scene CrissAndIsabellaScene23 with Dissolve(0.5)
    MC "Don't be mean, Isa, if she's not comfortable with it, let her be."
    scene CrissAndIsabellaScene24 with Dissolve(0.5)
    Isabella "Okay, smart ass, then dare her to do something."
    scene CrissAndIsabellaScene25 with Dissolve(0.5)
    MC "Hmmmm..."
    scene CrissAndIsabellaScene26 with Dissolve(0.5)
    MC "Give me a kiss on the chick!"
    scene CrissAndIsabellaScene27 with Dissolve(0.5)
    Criss "Uhhh..."
    scene CrissAndIsabellaScene28 with Dissolve(0.5)
    Isabella "What the fuck kind of dare is that, [MC]?!!?"
    scene CrissAndIsabellaScene29 with Dissolve(0.5)
    MC "What do you mean!?!? Nobody is here, so she won't draw any attention, and she won't cause any problems, exactly what she wanted!"
    scene CrissAndIsabellaScene30 with Dissolve(0.5)
    Criss "Sorry, [MC], I don't think I can-"
    scene CrissAndIsabellaScene31 with Dissolve(0.5)
    MC "Sorry, Criss, but you already declined Isa's dare, if you decline my as well you're out of the game."
    scene CrissAndIsabellaScene32 with Dissolve(0.5)
    Isabella "Tsk.. Just refuse him Criss, you can't even play a single game with this pervert!"
    scene CrissAndIsabellaScene33 with Dissolve(0.5)
    Criss "Okay... I'll do it..."
    scene CrissAndIsabellaScene34 with Dissolve(0.5)
    Isabella "YOU'LL WHAT?!?!"
    scene CrissAndIsabellaScene35 with Dissolve(0.5)
    Criss "I don't want to get out of the game... Plus, it's just on the chick, right?"
    scene CrissAndIsabellaScene36 with Dissolve(0.5)
    MC "Yeah, nothing more."
    scene CrissAndIsabellaScene37 with Dissolve(0.5)
    Criss "Okay...."
    scene CrissAndIsabellaScene38 with Dissolve(0.5)
    Isabella "Tsk!!"
    scene CrissAndIsabellaScene39 with Dissolve(0.5)
    Criss "Can you bend down a little? You are too tall..."
    scene CrissAndIsabellaScene40 with Dissolve(0.5)
    MC "Whatever makes you feel more comfortable, Criss."
    scene CrissAndIsabellaScene41 with Dissolve(0.5)
    Criss "T-t-t-t turn your head please..."
    MC "Of course!"
    scene CrissAndIsabellaScene42 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    scene CrissAndIsabellaScene43 with Dissolve(0.5)
    Isabella "{color=#808080}*You better not try any dumb shit, [MC]!*"
    scene CrissAndIsabellaScene44 with Dissolve(0.5)
    menu:
        "Turn":
            scene CrissAndIsabellaScene45 with Dissolve(0.5)
            Criss "{color=#808080}*Hmmm?!"
            Criss "{color=#808080}*Did he...?!"
            scene CrissAndIsabellaScene46 with Dissolve(0.5)
            Isabella "{color=#808080}*Of course he does it... what was I thinking...*"
            Isabella "{color=#808080}*What a dumbass...*"
            scene CrissAndIsabellaScene47 with Dissolve(0.5)
            Criss "Huh?!"
            scene CrissAndIsabellaScene48 with Dissolve(0.5)
            Criss "Get away! Why would you do that?!"
            scene CrissAndIsabellaScene49 with Dissolve(0.5)
            MC "Criss! Wait, I'm sorry, it was just a joke!"
            Criss "I'm sorry, I have to go!"
            scene CrissAndIsabellaScene50 with Dissolve(0.5)
            MC "I don't get it, it was just a kiss, why is she so mad?"
            scene CrissAndIsabellaScene51 with Dissolve(0.5)
            Isabella "Ughhhh!!! You're such a dumbass!!"
            scene CrissAndIsabellaScene52 with Dissolve(0.5)
            Isabella "It was her first kiss!! That's why!!"
            Isabella "And you've taken it, and made her cry."
            Isabella "Now I gotta go after her."
            scene CrissAndIsabellaScene53 with Dissolve(0.5)
            Isabella "You just can't stop yourself from being a pervert!"
            scene BlackScreen with Dissolve(0.5)
            $ Maria_Report_Criss_Kissed = True
            call stat_reward({"Criss": {"love": -5, "corruption": 2}, "Isabella": {"love": -5}}, show_black=False, return_to=None)
            $ advance_time_or_sleep()
        "Don't":
            $ Maria_Report_Criss_didnt_Kissed = True
            $ Maria_Report_Isabella = True
            scene CrissAndIsabellaScene54 with Dissolve(0.5)
            $ renpy.pause(1, hard=True)
            scene CrissAndIsabellaScene55 with Dissolve(0.5)
            MC "See? It wasn't that hard, was it?"
            scene CrissAndIsabellaScene56 with Dissolve(0.5)
            Criss "Y-yes...."
            scene CrissAndIsabellaScene57 with Dissolve(0.5)
            Isabella "Tsk..."
            scene CrissAndIsabellaScene58 with Dissolve(0.5)
            Isabella "Okay love birds, the dare is over, I'm next."
            scene CrissAndIsabellaScene59 with Dissolve(0.5)
            MC "Okay then, what do you chose? Truth or dare?"
            scene CrissAndIsabellaScene60 with Dissolve(0.5)
            Isabella "Dare."
            scene CrissAndIsabellaScene61 with Dissolve(0.5)
            MC "I dare you to go in the hallway and scream as loud as you can! Let's see if you can do it."
            scene CrissAndIsabellaScene62 with Dissolve(0.5)
            Isabella "I do that twice a day dumbass, try something harder."
            scene CrissAndIsabellaScene61 with Dissolve(0.5)
            MC "Then kiss me as well, maybe that would be a bit harder for you."
            scene CrissAndIsabellaScene63 with Dissolve(0.5)
            Isabella "Go fuck yourself!"
            scene CrissAndIsabellaScene64 with Dissolve(0.5)
            MC "Then kiss Criss."
            scene CrissAndIsabellaScene65 with Dissolve(0.5)
            Criss "Huh?!"
            scene CrissAndIsabellaScene66 with Dissolve(0.5)
            Criss "Wha-what do you mean?!"
            scene CrissAndIsabellaScene67 with Dissolve(0.5)
            Isabella "Ughhhh..."
            Isabella "Of course the pervert choses that."
            scene CrissAndIsabellaScene68 with Dissolve(0.5)
            Isabella "Alright... let's get this over with."
            scene CrissAndIsabellaScene69 with Dissolve(0.5)
            Criss "Wait, wait, wait!"
            Criss "Don't I get a saying in this?!"
            scene CrissAndIsabellaScene70 with Dissolve(0.5)
            Isabella "Stop complaining Criss, we've known each other for sixteen years"
            scene CrissAndIsabellaScene71 with Dissolve(0.5)
            Criss "I-I know, but I'm really not into kissing girls, you know?"
            Criss "I don't really swing that way..."
            scene CrissAndIsabellaScene72 with Dissolve(0.5)
            Isabella "Huh? What are you talking about? I'm not kissing you on the mouth, that's disgusting!"
            scene CrissAndIsabellaScene73 with Dissolve(0.5)
            Isabella "Now stop being such a scaredy-cat and turn your head, you can close your eyes if you want."
            scene CrissAndIsabellaScene74 with Dissolve(0.5)
            Criss "Okay..."
            scene CrissAndIsabellaScene75 with Dissolve(0.5)
            Isabella "Okay, here I go, are you ready?"
            scene CrissAndIsabellaScene76 with Dissolve(0.5)
            Criss "Yeah..."
            scene CrissAndIsabellaScene77 with Dissolve(0.5)
            menu:
                "Call Criss":
                    $ Maria_Report_Isabella_Kissed_Criss = True
                    MC "Criss, watch out!!"
                    scene CrissAndIsabellaScene78 with Dissolve(0.5)
                    Criss "Huh?! Why?!"
                    scene CrissAndIsabellaScene79 with Dissolve(0.5)
                    Criss "MMmmmM Ummmfff"
                    scene CrissAndIsabellaScene80 with Dissolve(0.5)
                    Isabella "{color=#808080}*Hmmm... her cheek is really soft, I have to ask her what creme she uses.*"
                    scene CrissAndIsabellaScene81 with Dissolve(0.5)
                    Isabella "Huh?!"
                    scene CrissAndIsabellaScene82 with Dissolve(0.5)
                    Isabella "{color=#808080}*Wait what?!!?*"
                    scene CrissAndIsabellaScene83 with Dissolve(0.5)
                    Isabella "Damn it, Criss, why would you do that?!"
                    scene CrissAndIsabellaScene84 with Dissolve(0.5)
                    Criss "I'm so sorry Isa, [MC] told me to watch out and I turned around to see what happen, I didn't mean to do that, I promise!"
                    scene CrissAndIsabellaScene85 with Dissolve(0.5)
                    Isabella "Of-fucking-course he did!"
                    scene CrissAndIsabellaScene86 with Dissolve(0.5)
                    Isabella "You really can't refrain yourself, can't you?!"
                    scene CrissAndIsabellaScene87 with Dissolve(0.5)
                    MC "Ohhh, c'mon Isa, it was just a joke."
                    MC "Plus, you said it yourself, you know each other for sixteen, is not that big of a deal."
                    scene CrissAndIsabellaScene86 with Dissolve(0.5)
                    Isabella "Yeah, right!"
                    scene CrissAndIsabellaScene88 with Dissolve(0.5)
                    Isabella "Come on, Criss."
                    Isabella "It was pointless to try to do something with him."
                    call stat_reward({"Criss": {"love": -5, "corruption": 2}, "Isabella": {"love": -5, "corruption": 2}}, return_to=None)
                    $ advance_time_or_sleep()
                "Don't":
                    $ Maria_Report_Isabella_didnt_Kiss_Criss = True
                    scene CrissAndIsabellaScene89 with Dissolve(0.5)
                    Isabella "Smooch!"
                    scene CrissAndIsabellaScene90 with Dissolve(0.5)
                    Isabella "See? No big deal at all!"
                    scene CrissAndIsabellaScene91 with Dissolve(0.5)
                    Isabella "Now it's your turn again, let's see how you like these fun dares!"
                    scene CrissAndIsabellaScene92 with Dissolve(0.5)
                    MC "Well... you see..."
                    scene CrissAndIsabellaScene93 with Dissolve(0.5)
                    MC "I kinda have to go, I was just passing by to the library, but I forgot."
                    MC "So.... byee."
                    scene CrissAndIsabellaScene94 with Dissolve(0.5)
                    Isabella "Don't you dare!"
                    scene CrissAndIsabellaScene95 with Dissolve(0.5)
                    Isabella "Just so you know, you lost!"
                    Isabella "And you're a pussy!"
                    call stat_reward({"Criss": {"love": 2}, "Isabella": {"love": 2}}, dissolve_time=1, return_to=None)
                    $ Location = "ArtClassFront"
                    $ advance_time_or_sleep()
