init python:
    define_images("LolaAndDorothyEventScene", "SchoolFirstPause/LolaAndDorothyEventScene", "LolaAndDorothyEventScene", 150)
    renpy.image("LolaAndDorothyEventVideo1", Movie(play="Images/SchoolFirstPause/LolaAndDorothyEventScene/LolaAndDorothyEventVideo1.webm", loop=True))

label LolaAndDorothyFirstPauseScene:
    scene LolaAndDorothyEventScene1 with Dissolve(0.5)
    MC "Hey girls, what are you doing?"
    scene LolaAndDorothyEventScene2 with Dissolve(0.5)
    Lola "Hey [MC]!"
    scene LolaAndDorothyEventScene3 with Dissolve(0.5)
    Lola "What's up?!"
    scene LolaAndDorothyEventScene4 with Dissolve(0.5)
    Leya "Hey [MC]!"
    scene LolaAndDorothyEventScene5 with Dissolve(0.5)
    Leya "Tsk!!"
    scene LolaAndDorothyEventScene6 with Dissolve(0.5)
    Leya "God damn it!!"
    scene LolaAndDorothyEventScene7 with Dissolve(0.5)
    Lola "What are you doing here? Did you get lost?"
    scene LolaAndDorothyEventScene8 with Dissolve(0.5)
    MC "No... not yet at least."
    MC "I'm just roaming around, trying to figure out where everything is at."
    MC "What are you doing?"
    scene LolaAndDorothyEventScene9 with Dissolve(0.5)
    Lola "Just passing the ball around, wasting a bit of time."
    Lola "And teaching Leya how to play."
    scene LolaAndDorothyEventScene10 with Dissolve(0.5)
    Lola "But she just started learning... and you can see."
    scene LolaAndDorothyEventScene11 with Dissolve(0.5)
    MC "That's nice! I didn't think she would was interested volleyball."
    scene LolaAndDorothyEventScene12 with Dissolve(0.5)
    Lola "Yeah, me neither."
    Lola "But she teaches me gymnastics, so I suggested that I would teach her a bit of volley."
    scene LolaAndDorothyEventScene13 with Dissolve(0.5)
    Lola "So it was more of a you help me, I help you situation"
    scene LolaAndDorothyEventScene14 with Dissolve(0.5)
    MC "And why would you want to learn gymnastics, just as a hobby?"
    scene LolaAndDorothyEventScene15 with Dissolve(0.5)
    Lola "Yeah... plus is nice to be flexible. And it helps me a lot with the stretching before training."
    scene LolaAndDorothyEventScene14 with Dissolve(0.5)
    MC "And are you learning faster then she's learning volley?"
    scene LolaAndDorothyEventScene16 with Dissolve(0.5)
    Leya "Not at all..."
    scene LolaAndDorothyEventScene17 with Dissolve(0.5)
    Lola "What do you mean not at all?!"
    scene LolaAndDorothyEventScene18 with Dissolve(0.5)
    Leya "You can't even do a handstand right. And we've been practicing it for weeks."
    scene LolaAndDorothyEventScene19 with Dissolve(0.5)
    Lola "But you've said that a handstand is a hard move. Even you struggle with it sometimes."
    scene LolaAndDorothyEventScene20 with Dissolve(0.5)
    Leya "I struggle?"
    scene LolaAndDorothyEventScene21 with Dissolve(1)
    Leya "Does it look like a struggle?!"
    scene LolaAndDorothyEventScene22 with Dissolve(0.5)
    Lola "Don't mind her, she's just showing off."
    scene LolaAndDorothyEventScene24 with Dissolve(0.5)
    MC "Wow! That's really cool! I would like to learn that..."
    MC "But Leya told me her classes only teach girls..."
    scene LolaAndDorothyEventScene23 with Dissolve(0.5)
    Leya "I mean... I could teach you when I teach Lola as well."
    scene LolaAndDorothyEventScene26 with Dissolve(0.5)
    Lola "So what do you say? Wanna play a pass or two, or do you want to try some gymnastics?"
    scene LolaAndDorothyEventScene25 with Dissolve(0.5)
    menu:
        "Play volley":
            $ Maria_Report_Lola = True
            MC "Let's play some volley! I haven't played in a while, but I used to be good at it."
            scene LolaAndDorothyEventScene26 with Dissolve(0.5)
            Lola "Okay then, let's see you!"
            scene LolaAndDorothyEventScene27 with Dissolve(1.5)
            Lola "Are you ready?!"
            MC "Yeap!"
            scene LolaAndDorothyEventScene28 with Dissolve(0.5)
            Lola "Okay, let's see if you catch this!"
            scene LolaAndDorothyEventScene29 with Dissolve(0.5)
            Lola "Good luck!"
            scene LolaAndDorothyEventScene30 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene LolaAndDorothyEventScene31 with Dissolve(0.5)
            Lola "Better not disappoint me!"
            scene LolaAndDorothyEventScene32 with Dissolve(0.5)
            MC "Okay, Leya, I will pass it to you next! Are you ready?!"
            Leya "Yeah! Shot it!"
            scene LolaAndDorothyEventScene33 with Dissolve(0.5)
            MC "Shoot it to Lola!"
            scene LolaAndDorothyEventScene34 with Dissolve(0.5)
            Lola "{color=#808080}*He actually got it... I was planning to mess with him a bit, but that was actually really good...*"
            scene LolaAndDorothyEventScene35 with Dissolve(0.5)
            Leya "Ughhhh!!!"
            scene LolaAndDorothyEventScene36 with Dissolve(0.5)
            Leya "Damn it! I messed up! Watch out [MC], it's coming to you!"
            scene LolaAndDorothyEventScene37 with Dissolve(0.5)
            MC "It's okay Leya, I'll pass it to Lola next!"
            scene LolaAndDorothyEventScene39 with Dissolve(0.5)
            Lola "Bring it on!"
            scene LolaAndDorothyEventScene38 with Dissolve(0.5)
            $ renpy.pause(0.1, hard=True)
            scene LolaAndDorothyEventScene40 with Dissolve(0.5)
            $ renpy.pause(0.1, hard=True)
            scene LolaAndDorothyEventScene41 with Dissolve(0.5)
            Lola "{color=#808080}*No way he shot it this hard!!*"
            Lola "{color=#808080}*It looked like he barely put any effort into it! How is he so strong?!*"
            scene LolaAndDorothyEventScene42 with Dissolve(0.5)
            Lola "{color=#808080}*Damn it! I fucked up!*"
            scene LolaAndDorothyEventScene43 with Dissolve(0.5)
            Leya "{color=#808080}*Now way... I've never seen Lola miss a ball..*"
            scene LolaAndDorothyEventScene44 with Dissolve(0.5)
            Leya "I'll get it!"
            scene LolaAndDorothyEventScene45 with Dissolve(0.5)
            Lola "Thank you Leya!"
            scene LolaAndDorothyEventScene46 with Dissolve(0.5)
            MC "Oh my God, Lola, I'm so sorry, are you fine?"
            scene LolaAndDorothyEventScene47 with Dissolve(0.5)
            Lola "Yeah, I'm okay, I just didn't expect the ball to come that fast."
            Lola "But how did you do it? It looked so effortlessly, and yet it was so strong."
            scene LolaAndDorothyEventScene48 with Dissolve(0.5)
            MC "Ummm... I don't think I did anything special... I just hit it..."
            MC "But I saw that you keep your arm pretty stiff, you should try letting it more loose."
            scene LolaAndDorothyEventScene49 with Dissolve(0.5)
            Lola "More loose? What do you mean?"
            scene LolaAndDorothyEventScene50 with Dissolve(0.5)
            MC "A bit more relaxed, and follow through a bit more after you hit it, put your whole body into it."
            MC "Do you want me to show you?"
            scene LolaAndDorothyEventScene49 with Dissolve(0.5)
            Lola "Uhhh... yeah, sure."
            scene LolaAndDorothyEventScene51 with Dissolve(0.5)
            Leya "{color=#808080}*What the.... I've never seen Lola let a man that close to her in my life.*"
            scene LolaAndDorothyEventScene52 with Dissolve(0.5)
            MC "Just keep your arm loose, let me guide it."
            scene LolaAndDorothyEventScene53 with Dissolve(0.5)
            Lola "Okay... what's next?"
            scene LolaAndDorothyEventScene54 with Dissolve(0.5)
            menu:
                "Grab her boob":
                    scene LolaAndDorothyEventScene55 with Dissolve(0.5)
                    MC "And then you just whip it, like you're throwing a rock."
                    scene LolaAndDorothyEventScene56 with Dissolve(0.5)
                    MC "Do you get it?"
                    scene LolaAndDorothyEventScene58 with Dissolve(0.5)
                    Leya "{color=#808080}*He just grabbed her boob!!!*"
                    Leya "{color=#808080}*She's going to flip out.*"
                    scene LolaAndDorothyEventScene57 with Dissolve(0.5)
                    Lola "Get. Your hands. Off of me. Right now!"
                    scene LolaAndDorothyEventScene59 with Dissolve(0.5)
                    MC "I'm sorry Lola, I was just trying to show the best way to spike the ball."
                    scene LolaAndDorothyEventScene60 with Dissolve(0.5)
                    Lola "I don't care what you tried to do!"
                    scene LolaAndDorothyEventScene61 with Dissolve(0.5)
                    Lola "Let's go Leya, we'll play in two, [MC] is leaving!"
                    $ Maria_Report_Lola_Grabbed_tit = True
                    call stat_reward({"Lola": {"love": -5, "corruption": 2}}, show_black=False, return_to=None)
                    $ advance_time_or_sleep()
                "Don't":
                    scene LolaAndDorothyEventScene62 with Dissolve(0.5)
                    MC "Just like that! Can you feel the difference?"
                    scene LolaAndDorothyEventScene63 with Dissolve(0.5)
                    Lola "Y-Yeah..."
                    scene LolaAndDorothyEventScene64 with Dissolve(0.5)
                    Leya "{color=#808080}*Why is Lola so shy... she's shuddering... to a man!*"
                    scene LolaAndDorothyEventScene65 with Dissolve(0.5)
                    MC "Okay then girls, I'll see you around, I have to go now."
                    scene LolaAndDorothyEventScene66 with Dissolve(0.5)
                    Leya "Okay, bye [MC]!"
                    scene LolaAndDorothyEventScene67 with Dissolve(0.5)
                    Lola "M-Maybe... you could show me a few more things next time...."
                    scene LolaAndDorothyEventScene68 with Dissolve(0.5)
                    MC "Of course I will."
                    scene LolaAndDorothyEventScene69 with Dissolve(0.5)
                    Lola "Okay then... bye, bye..."
                    $ Maria_Report_Lola_didnt_Grabbed_tit = True
                    call stat_reward({"Lola": {"love": 5, "corruption": 2, "obedience": 2}}, show_black=False, return_to=None)
                    $ advance_time_or_sleep()
        "Do gymnastic":
            $ Maria_Report_Leya = True
            scene LolaAndDorothyEventScene70 with Dissolve(0.5)
            Leya "Okay, then let's go inside the gym, it should be empty."
            scene LolaAndDorothyEventScene71 with Dissolve(1.5)
            Leya "Let us get changed first, we can't really move in this uniform."
            Leya "Wait for us in the gym."
            MC "Okay..."
            scene LolaAndDorothyEventScene72 with Dissolve(1.5)
            MC "{color=#808080}*Should I take a peak?*{color=#808080}"
            menu:
                "Take a peak":
                    $ Maria_Report_Leya_and_Lola_Naked = True
                    scene LolaAndDorothyEventScene73 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my God... They just started changing!!*{color=#808080}"
                    MC "{color=#808080}*And I can't hear them talking about something...*{color=#808080}"
                    scene LolaAndDorothyEventScene74 with Dissolve(0.5)
                    Leya "So what do you think about [MC]?"
                    Leya "Do you really think it was a good idea to invite him to our gymnastic lesson?"
                    scene LolaAndDorothyEventScene75 with Dissolve(0.5)
                    Lola "I mean... he looks so small and fragile, if he tries anything funny I can handle him."
                    Lola "And besides... he seems alright, maybe we can make a little fun of him."
                    scene LolaAndDorothyEventScene76 with Dissolve(0.5)
                    MC "{color=#808080}*Damn... Lola is so buffed, and Leya looks so skinny...*{color=#808080}"
                    MC "{color=#808080}*Almost unhealthy skinny, but I guess this is what you have to do to become a great gymnast.*{color=#808080}"
                    scene LolaAndDorothyEventScene77 with Dissolve(0.5)
                    MC "{color=#808080}*They both look like really great athletes.*{color=#808080}"
                    MC "{color=#808080}*In any case, I should leave now, if they catch me I'm fucked.*{color=#808080}"
                    menu:
                        "Stay":
                            MC "{color=#808080}*Fuck it, they are both way too hot for me to leave now.*{color=#808080}"
                            scene LolaAndDorothyEventScene78 with Dissolve(0.5)
                            Leya "I guess you're right... I just haven't been around boys all that much, I'm not sure how to always act..."
                            scene LolaAndDorothyEventScene79 with Dissolve(0.5)
                            Lola "I told you girl, he is chill, just talk to him like you would talk to me."
                            scene LolaAndDorothyEventScene80 with Dissolve(0.5)
                            MC "{color=#808080}*Oh my God, she's taking her bra off in front of Leya!*{color=#808080}"
                            MC "{color=#808080}*I guess they are both athletes, so seeing other girls naked is not that big of a deal...*{color=#808080}"
                            MC "{color=#808080}*Or girls just do that in regular...*{color=#808080}"
                            MC "{color=#808080}*But Lola's tits look amazing, I didn't think they would be that big due to how buff she is, but I was completely wrong!*{color=#808080}"
                            scene LolaAndDorothyEventScene81 with Dissolve(0.5)
                            Leya "You don't need to take change your bra Lola, we are just going to do a few stretches."
                            "{color=#808080}**Squeeeeeeak**"
                            scene LolaAndDorothyEventScene82 with Dissolve(0.5)
                            Leya "What was that?!"
                            scene LolaAndDorothyEventScene83 with Dissolve(0.5)
                            Lola "OH MY GOD, [MC_upper], GET THE FUCK OFF RIGHT NOW!!!!"
                            MC "{color=#808080}*Shit, I need to leave!*{color=#808080}"
                            scene BlackScreen with Dissolve(0.5)
                            call stat_reward({"Leya": {"love": -8, "corruption": 2}, "Lola": {"love": -8, "corruption": 2}}, show_black=False, return_to=None)
                            $ advance_time_or_sleep()
                        "leave":
                            MC "{color=#808080}*Let's not risk it...*{color=#808080}"
                            jump LolaAndDorothyGymnastic
                "Don't":
                    MC "{color=#808080}*Let's not risk it...*{color=#808080}"
                    jump LolaAndDorothyGymnastic

label LolaAndDorothyGymnastic:
    $ Maria_Report_Leya_Gymnastic = True
    scene LolaAndDorothyEventScene84 with Dissolve(1.5)
    MC "{color=#808080}*What is taking them so long...*"
    show LolaAndDorothyEventVideo1
    MC "{color=#808080}*God damn....*"
    scene LolaAndDorothyEventScene85 with Dissolve(0.5)
    Lola "What are you starring at?"
    scene LolaAndDorothyEventScene86 with Dissolve(0.5)
    Leya "Alright, let's get started!"
    Leya "Let's move a little bit."
    scene LolaAndDorothyEventScene87 with Dissolve(0.5)
    Leya "Okay, here should be fine."
    Leya "For starters, let's warm up. Just do as I do"
    scene LolaAndDorothyEventScene88 with Dissolve(0.5)
    Leya "Just like this."
    scene LolaAndDorothyEventScene89 with Dissolve(0.5)
    MC "Umm.... There is no way I'm gonna be able to do that..."
    scene LolaAndDorothyEventScene90 with Dissolve(0.5)
    Leya "Just go as far as you can, this is how you start."
    scene LolaAndDorothyEventScene91 with Dissolve(1)
    Leya "You are on the right track Lola!"
    scene LolaAndDorothyEventScene92 with Dissolve(0.5)
    Leya "But... uhhh... you're gonna have to work a bit more..."
    scene LolaAndDorothyEventScene93 with Dissolve(0.5)
    MC "Ughh.. I was never that flexible to be honest..."
    MC "I already feel like I'm dying! Can I take a breather?"
    scene LolaAndDorothyEventScene94 with Dissolve(0.5)
    Leya "It's alright, take a break, everyone has to start somewhere."
    scene LolaAndDorothyEventScene95 with Dissolve(0.5)
    Lola "Yeah, I will take a short pause as well, I'm beat."
    scene LolaAndDorothyEventScene96 with Dissolve(0.5)
    MC "But God damn, Leya, you are amazing, you didn't even break a sweat."
    MC "How long can you maintain that position for?"
    scene LolaAndDorothyEventScene97 with Dissolve(0.5)
    Leya "I can pretty much hold it for as long as I want, it's like sitting on a chair at this point."
    scene LolaAndDorothyEventScene98 with Dissolve(0.5)
    MC "That's so cool! I think you're the best gymnast I've ever seen!"
    scene LolaAndDorothyEventScene99 with Dissolve(0.5)
    Leya "Haha! You're damn right I am!"
    scene LolaAndDorothyEventScene100 with Dissolve(0.5)
    Lola "Well, she is actually top five in the country."
    Lola "So there are very slim chances you'll actually see someone better than her."
    scene LolaAndDorothyEventScene101 with Dissolve(0.5)
    MC "No way!! Really? Congrats!"
    scene LolaAndDorothyEventScene102 with Dissolve(0.5)
    Leya "Thanks..."
    scene LolaAndDorothyEventScene103 with Dissolve(0.5)
    MC "So if I show you a couple of poses, can you do them for me?"
    scene LolaAndDorothyEventScene104 with Dissolve(0.5)
    Leya "Uhhhh, I mean..... yeah.. I guess.."
    scene LolaAndDorothyEventScene105 with Dissolve(0.5)
    Leya "So which one do you want me to do?"
    scene LolaAndDorothyEventScene106 with Dissolve(0.5)
    MC "How about this one?"
    scene LolaAndDorothyEventScene107 with Dissolve(0.5)
    Leya "Oh, a standing split, of course, that's easy!"
    scene LolaAndDorothyEventScene108 with Dissolve(0.5)
    Leya "See? No problem at all!"
    scene LolaAndDorothyEventScene109 with Dissolve(0.5)
    Lola "Daaaaamn, that's so cool!"
    MC "That's really impressive Leya!"
    MC "{color=#808080}*She does it even better than Mhyrorin!*"
    scene LolaAndDorothyEventScene110 with Dissolve(0.5)
    Leya "Anything else?"
    scene LolaAndDorothyEventScene111 with Dissolve(0.5)
    MC "Hmmmm, let me think for a second..."
    jump LolaAndDorothyGymnastic_poseChoice

label LolaAndDorothyGymnastic_poseChoice:
    scene LolaAndDorothyEventScene111 with Dissolve(1.5)
    menu:
        "Wheel":
            scene LolaAndDorothyEventScene112 with Dissolve(0.5)
            MC "Can you do this one?"
            scene LolaAndDorothyEventScene113 with Dissolve(0.5)
            Leya "What is that? A wheel? Of course I can, I was doing that when I was five."
            scene LolaAndDorothyEventScene114 with Dissolve(1)
            Leya "So I could do this while standing up, but so you guys can learn, I will show you the easier way."
            Leya "You start from down here in this exact position, and then you simply push I guess... there's not much more to it..."
            scene LolaAndDorothyEventScene115 with Dissolve(0.5)
            Leya "And this is pretty much it, now you won't get this arch on your first try, and you won't be able to hold it for long, but you get there with time."
            scene LolaAndDorothyEventScene116 with Dissolve(0.5)
            MC "Wooow, you did it better than the girl in the image that I showed you."
            scene LolaAndDorothyEventScene117 with Dissolve(0.5)
            MC "Do you think you can do it Lola?"
            scene LolaAndDorothyEventScene118 with Dissolve(0.5)
            Lola "Who, me?? Hell no!"
            scene LolaAndDorothyEventScene119 with Dissolve(0.5)
            Leya "Come on Lola, at least try it!"
            scene LolaAndDorothyEventScene120 with Dissolve(0.5)
            Lola "Ughhhhh, okay..."
            scene LolaAndDorothyEventScene121 with Dissolve(1)
            Lola "Like this?"
            scene LolaAndDorothyEventScene122 with Dissolve(0.5)
            Leya "Yep, just like that!"
            Leya "Now push!!!"
            scene LolaAndDorothyEventScene123 with Dissolve(0.5)
            MC "That's perfect Lola! You got it!"
            Leya "Yeah, that's really good! The arch is still not perfect, but I told you, you get there with some time and practice!"
            scene LolaAndDorothyEventScene124 with Dissolve(1)
            Lola "God damn... That's really hard, I thought my head was gonna explode."
            scene LolaAndDorothyEventScene125 with Dissolve(0.5)
            Lola "And why aren't you doing it as well?!"
            scene LolaAndDorothyEventScene126 with Dissolve(0.5)
            MC "Cause I would break my neck and die?"
            scene LolaAndDorothyEventScene127 with Dissolve(0.5)
            Lola "I guess that's a good point..."
            scene LolaAndDorothyEventScene128 with Dissolve(0.5)
            Leya "Anything else you want me to try?"
            scene LolaAndDorothyEventScene129 with Dissolve(0.5)
            Lola "Wait a second, I wanna chose too!"
            jump LolaAndDorothyGymnastic_poseChoice
        "Oversplit Handstand":
            scene LolaAndDorothyEventScene112 with Dissolve(0.5)
            MC "What about this one?"
            scene LolaAndDorothyEventScene113 with Dissolve(0.5)
            Leya "Uhhhh, I don't think I have done this one before, but I can try..."
            scene LolaAndDorothyEventScene130 with Dissolve(1.5)
            Leya "Ughhh.. this one is a bit difficult... Am I doing it right? Is like in the photo?"
            scene LolaAndDorothyEventScene131 with Dissolve(0.5)
            MC "......."
            Lola "........."
            MC "Y..."
            Lola "Yeah..."
            MC "Maybe raise your head up a little bit..."
            scene LolaAndDorothyEventScene132 with Dissolve(0.5)
            Leya "Like this?"
            scene LolaAndDorothyEventScene133 with Dissolve(0.5)
            MC "Y-yeah... that's perfect... it even looks a bit uncanny..."
            MC "I didn't even know the human body can do that... I showed you a drawing...."
            scene LolaAndDorothyEventScene134 with Dissolve(0.5)
            Lola "That does look a bit uncanny... I'm not even going to attempt that..."
            scene LolaAndDorothyEventScene135 with Dissolve(0.5)
            Leya "So I got it right? Can I stand normally now?"
            scene LolaAndDorothyEventScene133 with Dissolve(0.5)
            MC "Yeah you got it perfect"
            scene LolaAndDorothyEventScene135 with Dissolve(0.5)
            Leya "Okay, nice! Anything else?"
            jump LolaAndDorothyGymnastic_poseChoice
        "Head to feet retroflexion":
            scene LolaAndDorothyEventScene112 with Dissolve(0.5)
            MC "This one looks good!"
            scene LolaAndDorothyEventScene113 with Dissolve(0.5)
            Leya "Oh, I did this one at a competition once!"
            Leya "Is not that complicated, you just need to be really, really flexible"
            scene LolaAndDorothyEventScene136 with Dissolve(0.5)
            Lola "Uhhh... Leya... are you okay?"
            MC "Do you want me to call an ambulance?"
            scene LolaAndDorothyEventScene137 with Dissolve(0.5)
            Leya "What do you mean?! You were the ones telling me to do this pose! You saw how it looked, why are you acting scared now?!"
            scene LolaAndDorothyEventScene138 with Dissolve(0.5)
            Lola "To be honest, we were just messing around, I didn't think it was possible to do it..."
            scene LolaAndDorothyEventScene139 with Dissolve(0.5)
            Leya "You really think that little of me? I thought you knew I was one of the best!"
            scene LolaAndDorothyEventScene138 with Dissolve(0.5)
            Lola "That's.... really creppy..."
            scene LolaAndDorothyEventScene140 with Dissolve(0.5)
            MC "Yeah... and hot..."
            scene LolaAndDorothyEventScene141 with Dissolve(0.5)
            Lola "And what?!"
            scene LolaAndDorothyEventScene142 with Dissolve(0.5)
            Leya "And what?!"
            scene LolaAndDorothyEventScene143 with Dissolve(0.5)
            MC "And hard, in like, hard to do!"
            scene LolaAndDorothyEventScene144 with Dissolve(0.5)
            Leya "Ohhh, harder, I though I misunderstood you."
            Leya "Yeah, even for me is a bit difficult to hold, it hurts my back a little."
            Leya "Is there anything else?"
            jump LolaAndDorothyGymnastic_poseChoice
        "Nothing":
            scene LolaAndDorothyEventScene145 with Dissolve(0.5)
            MC "Nope, that was all!"
            MC "And it's a little late anyway, we have to go to class soon, and I have a bit more left to do before the class starts."
            MC "So I'll go now!"
            scene LolaAndDorothyEventScene146 with Dissolve(0.5)
            Lola "Okay, [MC], see you later!"
            scene LolaAndDorothyEventScene147 with Dissolve(0.5)
            Leya "Bye, bye!!"
            call stat_reward({"Leya": {"love": 5, "corruption": 2}, "Lola": {"love": 2}}, return_to=None)
            $ advance_time_or_sleep()

