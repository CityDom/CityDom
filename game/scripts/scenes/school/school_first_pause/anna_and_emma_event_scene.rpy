init python:
    define_images("AnnaAndEmmaScene", "SchoolFirstPause/AnnaAndEmmaEventScene", "AnnaAndEmmaScene", 100)

label AnnaAndEmmaFirstPauseScene:
    $ Maria_Report_AnnaAndEmma = True
    scene AnnaAndEmmaScene1 with Dissolve(0.5)
    MC "Hey Anna, hey Emma, what's up!"
    scene AnnaAndEmmaScene2 with Dissolve(0.5)
    Anna "You again? What do you want?"
    scene AnnaAndEmmaScene3 with Dissolve(0.5)
    Emma "Why are you even here? Just to watch us in swim suits?"
    scene AnnaAndEmmaScene4 with Dissolve(0.5)
    Anna "That's really creepy, we should let the teacher know."
    scene AnnaAndEmmaScene3 with Dissolve(0.5)
    Emma "You're right Anna, maybe he'll get expelled."
    scene AnnaAndEmmaScene5 with Dissolve(0.5)
    MC "I'm just walking around the school, trying to get a feeling of the place."
    MC "Why do you have to be so rude."
    MC "And it's break, we don't even have physical education next, you have no reason to be here either."
    MC "I didn't expect you two to be half naked in the pool when the class starts in a few minutes."
    scene AnnaAndEmmaScene6 with Dissolve(0.5)
    Anna "Hey, Emma, this guy has some attitude in him."
    scene AnnaAndEmmaScene7 with Dissolve(0.5)
    Emma "It does seem like he doesn't really know his place."
    scene AnnaAndEmmaScene8 with Dissolve(0.5)
    Emma "What do you want to do with, Anna?"
    Anna "Just have a little bit of fun with him, Emma."
    scene AnnaAndEmmaScene9 with Dissolve(0.5)
    Anna "So what's the big idea? You think you can come in this school and do whatever you want!?"
    scene AnnaAndEmmaScene10 with Dissolve(0.5)
    MC "I think I'm free to roam around the school, is not like it's yours."
    MC "And who are you to tell me where I can or can't go?"
    scene AnnaAndEmmaScene11 with Dissolve(0.5)
    Anna "Wow there, new guy, don't get so riled up, it's slippery around here."
    Anna "You might slip and fall into the pool."
    scene AnnaAndEmmaScene12 with Dissolve(0.5)
    MC "Aww, so sweet of you to warn me about that."
    MC "See, it's not that hard to be nice."
    MC "But it's ok, I know how to swim."
    scene AnnaAndEmmaScene13 with Dissolve(0.5)
    Emma "So you know how to swim, huh? That's perfect, let's see you in action!"
    scene AnnaAndEmmaScene14 with Dissolve(0.5)
    MC "Huh?"
    scene AnnaAndEmmaScene15 with Dissolve(0.5)
    MC "Hold up, wait a second!"
    scene AnnaAndEmmaScene16 with Dissolve(0.5)
    Emma "Have a nice swim!"
    scene AnnaAndEmmaScene17 with Dissolve(0.5)
    MC "Wait, wait, wait!!!"
    menu:
        "Grab them":
            scene AnnaAndEmmaScene18 with Dissolve(0.5)
            MC "Tsk..."
            scene AnnaAndEmmaScene19 with Dissolve(0.5)
            MC "You girls are coming with me then!"
            scene AnnaAndEmmaScene20 with Dissolve(0.5)
            EmmaAndAnna "WAIT, DON'T!!"
            scene AnnaAndEmmaScene21 with Dissolve(0.5)
            EmmaAndAnna "KYAAAAAAAAA!!!!!"
            scene AnnaAndEmmaScene22 with Dissolve(0.5)
            "{color=#808080}**!!SPLASH!!**"
            scene AnnaAndEmmaScene23 with Dissolve(0.5)
            MC "{color=#808080}*Ha, I managed to get them as well.*"
            scene AnnaAndEmmaScene24 with Dissolve(1.5)
            Anna "WHAT WAS THAT!?!?!"
            Anna "WHY DID YOU DO THAT?!"
            scene AnnaAndEmmaScene25 with Dissolve(0.5)
            Emma "WHO DO YOU THINK YOU ARE TO DRAG US IN THE POOL LIKE THAT?!"
            scene AnnaAndEmmaScene26 with Dissolve(0.5)
            MC "ARE YOU TWO STUPID? YOU PUSHED ME IN THE WATER, AND I'M FULLY CLOTHED!"
            MC "YOU SHOULD BE APOLOGIZING!!!"
            scene AnnaAndEmmaScene27 with Dissolve(0.5)
            MC "HOW AM I SUPPOSED TO GET DRY BEFORE CLASS STARTS?!!?"
            scene AnnaAndEmmaScene28 with Dissolve(0.5)
            MC "NOT TO MENTION THAT-"
            scene AnnaAndEmmaScene29 with Dissolve(0.5)
            MC "{color=#808080}*Wait what... oh my God... their tits are out.*"
            MC "{color=#808080}*And they didn't even realize it...*"
            MC "{color=#808080}*Let me shut the fuck up before they do.*"
            scene AnnaAndEmmaScene30 with Dissolve(0.5)
            Emma "What happened asshole?! Out of words already?!!?"
            scene AnnaAndEmmaScene31 with Dissolve(0.5)
            Anna "Don't stop now, say what's on your mind!!"
            scene AnnaAndEmmaScene32 with Dissolve(0.5)
            MC "I was thinking that... you two are perfect twins..."
            MC "But I wasn't expecting your tits to be exactly the same as well..."
            scene AnnaAndEmmaScene33 with Dissolve(0.5)
            Anna "HUH?!?!"
            Anna "I know for a fact you are not talking about our breast right now!!"
            scene AnnaAndEmmaScene34 with Dissolve(0.5)
            Anna "{color=#808080}*What the....*"
            Anna "{color=#808080}*OH MY GOD MY BOOBS ARE OUT!!*"
            scene AnnaAndEmmaScene35 with Dissolve(0.5)
            Emma "Oh my God, Anna, your boobs are out!!!!"
            scene AnnaAndEmmaScene36 with Dissolve(0.5)
            Anna "Yours are as well, Emma!!"
            scene AnnaAndEmmaScene37 with Dissolve(0.5)
            EmmaAndAnna "KYAAAAAAAAAAAAA!!!!!"
            MC "{color=#808080}*Maybe I shouldn't have said that...*"
            MC "{color=#808080}*But they pissed me off...*"
            scene AnnaAndEmmaScene38 with Dissolve(0.5)
            MC "Okay girls... I will let you get dressed I guess..."
            MC "I have to get changed as well..."
            scene AnnaAndEmmaScene39 with Dissolve(0.5)
            Emma "Fuck you!!!"
            Emma "Just leave already!!"
            scene AnnaAndEmmaScene40 with Dissolve(0.5)
            Anna "Yeah, you leave already you asshole!!"
            scene AnnaAndEmmaScene41 with Dissolve(0.5)
            call stat_reward({"Anna": {"love": -5, "corruption": 2}, "Emma": {"love": -5, "corruption": 2}}, return_to=None)
            $ Maria_Report_AnnaAndEmma_tits = True
            $ advance_time_or_sleep()
        "Don't":
            scene AnnaAndEmmaScene42 with Dissolve(0.5)
            MC "You assholes!!!!"
            scene AnnaAndEmmaScene43 with Dissolve(0.5)
            EmmaAndAnna "Haha, got your ass!!"
            scene AnnaAndEmmaScene44 with Dissolve(0.5)
            EmmaAndAnna "Don't mess with uss, asshole!!"
            scene AnnaAndEmmaScene45 with Dissolve(0.5)
            "........."
            scene AnnaAndEmmaScene46 with Dissolve(0.5)
            Anna "Ummm... Do you think he was telling the truth when he said he knows how to swim?"
            scene AnnaAndEmmaScene47 with Dissolve(0.5)
            Emma "I hope so... why would he lie..."
            scene BlackScreen with Dissolve(1)
            "{color=#808080}*Two minutes later*"
            scene AnnaAndEmmaScene46 with Dissolve(1)
            Anna "He... he's still not coming up..."
            scene AnnaAndEmmaScene47 with Dissolve(0.5)
            Emma "I'm sure he's fine..."
            scene AnnaAndEmmaScene49 with Dissolve(0.5)
            MC "Were you two really not going to jump in for me?!"
            scene AnnaAndEmmaScene50 with Dissolve(0.5)
            Anna "We still deciding on it... but we were going to!"
            scene AnnaAndEmmaScene51 with Dissolve(0.5)
            MC "What the fuck do you mean still deciding on it?! I was in there for like 2 minutes!!"
            scene AnnaAndEmmaScene52 with Dissolve(0.5)
            Emma "But you said you knew how to swim..."
            scene AnnaAndEmmaScene53 with Dissolve(0.5)
            MC "What if I was lying just to impress you?!!? Or I had a cramp or something!"
            scene AnnaAndEmmaScene54 with Dissolve(0.5)
            "............"
            scene AnnaAndEmmaScene55 with Dissolve(0.5)
            MC "Are you not even going to at least apologize?!!? Were you raised by wolves?!"
            scene AnnaAndEmmaScene56 with Dissolve(0.5)
            EmmaAndAnna "We're sorry...."
            scene AnnaAndEmmaScene77 with Dissolve(0.5)
            MC "Even my shoes are full of water now..."
            scene AnnaAndEmmaScene78 with Dissolve(0.5)
            MC "Do you know how it feels to have wet socks and on top of that wet shoes?!"
            scene AnnaAndEmmaScene57 with Dissolve(0.5)
            MC "I know it's funny to make fun of the new guy, but I could've drown, are you crazy?!"
            "............."
            MC "{color=#808080}*I think I actually scared them a little... they really got worried...*"
            MC "{color=#808080}*I thought they were like Selina... but they are just brats...*"
            MC "{color=#808080}*I should try to lighten the mood a little...*"
            scene AnnaAndEmmaScene58 with Dissolve(0.5)
            MC "But your coordination was actually impressive there."
            MC "You two went for pushing me without saying a thing or even glancing at each other."
            scene AnnaAndEmmaScene59 with Dissolve(0.5)
            Anna "Of course it was, we always think the same."
            scene AnnaAndEmmaScene60 with Dissolve(0.5)
            MC "{color=#808080}*Aaaand they are back to normal...*"
            MC "It was actually a good prank, I can't deny it"
            scene AnnaAndEmmaScene61 with Dissolve(0.5)
            Emma "Of course it was! We are the best at it!"
            scene AnnaAndEmmaScene60 with Dissolve(0.5)
            MC "Yeah, it would've been funnier if I wasn't in the regular uniform, couldn't you wait until physical education, when I was in swimming shorts."
            scene AnnaAndEmmaScene62 with Dissolve(0.5)
            Anna "Stop crying so much, there are a lot of uniforms laying around, you can get changed."
            scene AnnaAndEmmaScene63 with Dissolve(0.5)
            MC "I'll go then, you are lucky I didn't have my phone with me."
            scene AnnaAndEmmaScene64 with Dissolve(0.5)
            EmmaAndAnna "Uhhhh..."
            Anna "We knew that already!"
            Emma "Yeah, of course we knew that, we wouldn't push you in the pool if you had it."
            Anna "Yeah, that's right, we're not stupid!"
            scene AnnaAndEmmaScene65 with Dissolve(0.5)
            MC "Of course, you are not stupid at all..."
            MC "Can you direct me to the changing room? I'm not sure where it is."
            scene AnnaAndEmmaScene66 with Dissolve(0.5)
            Anna "Of course we can, we're always nice to new colleagues."
            scene AnnaAndEmmaScene67 with Dissolve(0.5)
            menu:
                "Grab their ass":
                    scene AnnaAndEmmaScene68 with Dissolve(0.5)
                    MC "What can I say..."
                    scene AnnaAndEmmaScene69 with Dissolve(0.5)
                    MC "I'm so lucky to have such nice colleagues!"
                    scene AnnaAndEmmaScene70 with Dissolve(0.5)
                    EmmaAndAnna "{color=#808080}*Is he....*"
                    EmmaAndAnna "{color=#808080}*Touching my ass?!?!*"
                    scene AnnaAndEmmaScene71 with Dissolve(0.5)
                    EmmaAndAnna "GET YOUR HAND OFF MY ASS RIGHT NO-"
                    scene AnnaAndEmmaScene73 with Dissolve(0.5)
                    MC "Atatata, I don't wanna hear it."
                    MC "And I'm pretty sure you don't want the teacher to hear why I was all wet!"
                    scene AnnaAndEmmaScene72 with Dissolve(0.5)
                    MC "Yeah, that's what I thought!"
                    scene AnnaAndEmmaScene74 with Dissolve(0.5)
                    MC "Now, shall we go?"
                    scene AnnaAndEmmaScene75 with Dissolve(0.5)
                    EmmaAndAnna "Fuck you!"
                    scene BlackScreen with Dissolve(0.5)
                    $ Maria_Report_AnnaAndEmma_ass = True
                    call stat_reward({"Anna": {"love": -5, "corruption": 2, "obedience": 2}, "Emma": {"love": -5, "corruption": 2, "obedience": 2}}, return_to=None)
                    $ advance_time_or_sleep()
                "Don't":
                    scene AnnaAndEmmaScene75 with Dissolve(0.5)
                    MC "Yeah, whatever you say, let's just go, I still have water in my shoes."
                    call stat_reward({"Anna": {"love": 2}, "Emma": {"love": 2}}, return_to=None)
                    $ advance_time_or_sleep()