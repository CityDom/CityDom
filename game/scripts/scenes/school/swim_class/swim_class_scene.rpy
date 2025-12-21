init python:
    define_images("SwimClass_Scene", "SwimClass/SwimClass", "SwimClass_Scene", 200)

label SwimClass_Scene:
    scene SwimClass_Scene1 with Dissolve(0.5)
    Tanya "BREAK IS OVER, GET YOUR ASSES OVER HERE AND FORM A LINE!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**2 minutes later, everyone gathers.**{/color}"
    scene SwimClass_Scene2 with Dissolve(0.5)
    Tanya "ALRIGHT GIRLS! LISTEN UP! I'M NOT GOING TO REPEAT MYSELF!"
    scene SwimClass_Scene3 with Dissolve(0.5)
    Tanya "FROM NOW ON, YOU'LL BE LEARNING HOW TO JUMP IN THE WATER!!"
    Tanya "IF YOU PAID ATTENTION IN MY CLASS, YOU SHOULD ALREADY KNOW HOW TO SWIM!"
    scene SwimClass_Scene4 with Dissolve(0.5)
    Tanya "AND YES, I'M TALKING TO YOU, LEYA!"
    scene SwimClass_Scene5 with Dissolve(0.5)
    Leya "Tsk..."
    scene SwimClass_Scene6 with Dissolve(0.5)
    Tanya "AND THAT'S ALL! SHORT AND SIMPLE! ANY QUESTIONS?"
    scene SwimClass_Scene7 with Dissolve(0.5)
    Isabella "ME, ME, ME!!"
    scene SwimClass_Scene8 with Dissolve(0.5)
    Isabella "ME, ME, ME, ME, ME!!!"
    scene SwimClass_Scene9 with Dissolve(0.5)
    Tanya "......"
    scene SwimClass_Scene10 with Dissolve(0.5)
    Tanya "Anyone else?"
    scene SwimClass_Scene11 with Dissolve(0.5)
    Isabella "ME, ME, MEEEEEEEEEEE!!!!!"
    scene SwimClass_Scene12 with Dissolve(0.5)
    Tanya "Ughhh... yes, Isabella, what's your question?"
    scene SwimClass_Scene13 with Dissolve(0.5)
    Isabella "Why are you always yelling? We can all hear you, we are standing TWO meters from you."
    scene SwimClass_Scene14 with Dissolve(0.5)
    Tanya "ALRIGHT CLASS, ISABELLA IS DONE WITH HER STAND UP NUMBER AND WE ALL LAUGHED SUPER HARD, WE CAN START THE CLASS!"
    Tanya "ISABELLA WILL BE FIRST!"
    scene SwimClass_Scene15 with Dissolve(0.5)
    Isabella "Damn, she's so mean! Can't she take a joke?"
    scene SwimClass_Scene16 with Dissolve(0.5)
    MC "Don't act like you didn't ask for it."
    scene SwimClass_Scene17 with Dissolve(0.5)
    Isabella "Ugh, whatever, you people hate fun!"
    scene SwimClass_Scene18 with Dissolve(0.5)
    Tanya "ISA, MOVE YOUR ASS!"
    scene SwimClass_Scene19 with Dissolve(1.5)
    Tanya "I HOPE YOU'RE NOT GETTING SCARED NOW, ISA!"
    scene SwimClass_Scene20 with Dissolve(0.5)
    Isabella "Are you kidding me?! I've trained my whole life for this! I'm an expert!"
    scene SwimClass_Scene21 with Dissolve(0.5)
    Tanya "Wait a minute there, you brat!"
    Tanya "You are not just jumping on your ass, making some lame cannonball!"
    Tanya "We are making head first dives here!"
    scene SwimClass_Scene22 with Dissolve(0.5)
    Isabella "Ummm... excuse me, what?"
    scene SwimClass_Scene23 with Dissolve(0.5)
    Tanya "ARE YOU NOT HEARING ME ISA? WE'RE STANDING TWO METERS FROM EACH OTHER. IT SEEMS THAT I STILL NEED TO YELL!"
    Tanya "WE ARE LEARNING TO JUMP HEAD FIRST!!"
    scene SwimClass_Scene24 with Dissolve(0.5)
    Tanya "I WILL SHOW YOU STEP BY STEP AFTER WHICH YOU ARE NEXT, SO PAY ATTENTION!"
    scene SwimClass_Scene25 with Dissolve(0.5)
    Tanya "FIRST OF ALL, YOU POSITION YOURSELF! THE LEGS CLOSE TO THE EDGE, BUT NOT OVERHANGING!"
    scene SwimClass_Scene26 with Dissolve(0.5)
    Tanya "SECOND, RAISE YOUR ARMS, BICEPS TO THE EARS, AND HANDS LOCKED."
    scene SwimClass_Scene27 with Dissolve(0.5)
    Tanya "THIRD, BEND YOUR KNEES, TIGHTEN YOUR CORE, AND LEAN FORWARD!"
    Tanya "AND LASTLY, WHEN YOU JUMP, TUCK YOUR CHIN, AND LET THE GRAVITY DO THE REST!"
    scene SwimClass_Scene28 with Dissolve(0.5)
    Dorothy "Ummmm, how are we supposed to do that?"
    Sophie "I don't know, girl, she's crazy!"
    scene SwimClass_Scene29 with Dissolve(0.5)
    Tanya "OKAY ISA, YOU'RE UP!"
    scene SwimClass_Scene30 with Dissolve(0.5)
    MC "So, what do you think? Can you make that dive?"
    scene SwimClass_Scene31 with Dissolve(0.5)
    Maria "Hell nah, I can barely swim. How about you, can you pull it off?"
    if Maria_Report_AnnaAndEmma_ass == True:
        scene SwimClass_Scene32 with Dissolve(0.5)
        MC "Uhhh... I think I can make it, I don't know..."
        scene SwimClass_Scene33 with Dissolve(0.5)
        MC "But I'm sure you can pull it off as well!"
        scene SwimClass_Scene34 with Dissolve(0.5)
        MC "Like you usually do!"
        scene SwimClass_Scene35 with Dissolve(0.5)
        Maria "What the fuck are you doing, idiot?!"
        scene SwimClass_Scene36 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene37 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene36 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene37 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene36 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene37 with Dissolve(0.3)
        $ renpy.pause(0.3, hard=True)
        scene SwimClass_Scene36 with Dissolve(0.3)
        MC "I'm doing my best to respect our deal, have you forgotten the twins?"
        scene SwimClass_Scene38 with Dissolve(0.5)
        Maria "Ugh, right, I forgot about that..."
        scene SwimClass_Scene39 with Dissolve(0.5)
        Maria "But if someone sees us, I'll say you forced me."
        scene SwimClass_Scene40 with Dissolve(0.5)
        MC "Yeah, whatever you say. But you better get used to it."
        scene SwimClass_Scene41 with Dissolve(0.5)
        MC "Anyway, I should be next, better for Tanya to not see me."
        jump McDivesInTheWater
    else:
        scene SwimClass_Scene41 with Dissolve(0.5)
        MC "I think... I don't know for sure."
        jump McDivesInTheWater

label McDivesInTheWater:
    scene SwimClass_Scene42 with Dissolve(0.5)
    Tanya "ALRIGHT, [MC_upper], GET YOUR ASS UP AND COME HERE!"
    scene SwimClass_Scene44 with Dissolve(0.5)
    MC "Alright, alright..."
    scene SwimClass_Scene43 with Dissolve(0.5)
    MC "Okay, and now, what do I do?"
    scene SwimClass_Scene45 with Dissolve(0.5)
    Tanya "I TOLD YOU THAT I WON'T REPEAT MYSELF, SHRIMP!"
    Tanya "SO GO AHEAD AND JUMP!"
    scene SwimClass_Scene46 with Dissolve(0.5)
    Tanya "IT SEEMS THAT YOU LISTENED A LITTLE!"
    MC "Yeah, I wish I didn't, my ears will start bleeding!"
    scene SwimClass_Scene47 with Dissolve(0.5)
    Tanya "Uhhh... ALRIGHT! YOU KINDA GOT THE GIST OF IT! NOW JUMP!"
    scene SwimClass_Scene48 with Dissolve(0.5)
    MC "{color=#808080}*Ughh.. I feel so stupid...*{/color}"
    MC "{color=#808080}*It's now or never I guess...*{/color}"
    scene SwimClass_Scene49 with Dissolve(0.5)
    Tanya "GOOD JOB, SHRIMP! THAT WAS PRETTY GOOD!!"
    Tanya "MARIA, YOU'RE UP!"
    scene SwimClass_Scene50 with Dissolve(0.5)
    MC "{color=#808080}*Agh, I think I caught too much speed and I'm not sure how deep the pool is right now.*{/color}"
    scene SwimClass_Scene51 with Dissolve(0.5)
    MC "{color=#808080}*I shouldn't have retracted my hands, I have to feel the bottom of the pool...*{/color}"
    scene SwimClass_Scene52 with Dissolve(0.5)
    MC "{color=#808080}*OUCH, FUCK!*{/color}"
    MC "{color=#808080}*I knew it, I'm so stupid! But maybe I can play it off!*{/color}"
    scene SwimClass_Scene53 with Dissolve(0.5)
    Tanya "Okay, wait a second to make sure [MC] is out of the way."
    scene SwimClass_Scene54 with Dissolve(0.5)
    Tanya "He should be out any second now..."
    scene SwimClass_Scene55 with Dissolve(0.5)
    "........."    
    scene SwimClass_Scene56 with Dissolve(0.5)
    "......................"    
    scene SwimClass_Scene57 with Dissolve(0.5)
    Maria "Ummm... I'm not an expert in body language, but he looks passed out."
    Tanya "Hmmm... He does look a bit dizzy..."
    Maria "Ummm... Teach? I don't wanna be the kind of girl to tell you how to do your job, but shouldn't you get him out?"
    Tanya "Hmmm... I guess you're right."
    scene SwimClass_Scene58 with Dissolve(0.5)
    Tanya "{color=#808080}*God damn it [MC], you better be alright, Jennifer is going to kill me!*{/color}"
    scene SwimClass_Scene59 with Dissolve(2)
    Isabella "[MC_upper], [MC_upper]!!!!"
    scene SwimClass_Scene60 with Dissolve(0.5)
    Isabella "[MC], please! Wake up!"
    scene SwimClass_Scene61 with Dissolve(0.5)
    Isabella "Don't do this to me please!"
    scene SwimClass_Scene62 with Dissolve(0.5)
    Maria "God damn it, [MC], this is not a joke! Wake up!"
    scene SwimClass_Scene63 with Dissolve(0.5)
    Maria "C'moooonnnn, [MC], don't leave me!"
    scene SwimClass_Scene64 with Dissolve(0.5)
    Maria "{color=#808080}*Not you too...*{/color}"
    scene SwimClass_Scene65 with Dissolve(0.5)
    MC "{color=#808080}*HAH! I knew she cared a little about me!*{/color}"
    MC "{color=#808080}*She's even holding my hand tight!*{/color}"
    scene SwimClass_Scene66 with Dissolve(0.5)
    MC "{color=#808080}*And Isa is getting kinda close to my private parts...*{/color}"
    MC "{color=#808080}*Now I only have to prevent my dick from going hard and everything is going perfect!*{/color}"
    scene SwimClass_Scene67 with Dissolve(0.5)
    MC "{color=#808080}*The main event is yet to come.*{/color}"
    MC "{color=#808080}*She's probably thinking about it.*{/color}"
    scene SwimClass_Scene68 with Dissolve(0.5)
    Tanya "God damn it, I have to do it!"
    scene SwimClass_Scene69 with Dissolve(0.5)
    Tanya "Okay, [MC], I never paid attention in class to this, but how hard can it be?"
    scene SwimClass_Scene70 with Dissolve(0.5)
    MC "{color=#808080}*Umm... Excuse me, WHAT?!*{/color}"
    scene SwimClass_Scene71 with Dissolve(0.5)
    Tanya "Don't blame me for what happens next."
    scene SwimClass_Scene72 with Dissolve(0.5)
    Tanya "Here we go!"
    scene SwimClass_Scene73 with Dissolve(0.5)
    MC "{color=#808080}*HUMPFFF!!!*{/color}"
    MC "{color=#808080}*IS THIS BITCH CRAZY!? SHE'S GOING TO BREAK MY STERNUM!*{/color}"
    MC "{color=#808080}*I FORGOT HOW STRONG SHE WAS!*{/color}"
    scene SwimClass_Scene71 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene72 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene71 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene72 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene71 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene72 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene71 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene SwimClass_Scene72 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    Tanya "C'mon, C'mon, C'mon, [MC], please!"
    scene SwimClass_Scene73 with Dissolve(0.2)
    Isabella "God damn it, Tanya, he is still out, do something already!"
    scene SwimClass_Scene75 with Dissolve(0.2)
    Tanya "UGH! FINE!"
    scene SwimClass_Scene76 with Dissolve(0.2)
    MC "{color=#808080}*Finally...*{/color}"
    scene SwimClass_Scene77 with Dissolve(0.2)
    MC "{color=#808080}*The main event!*{/color}"
    scene SwimClass_Scene78 with Dissolve(0.2)
    Isabella "{color=#808080}*Oh my God, she's actually doing it!*{/color}"
    scene SwimClass_Scene79 with Dissolve(0.2)
    Tanya "GHAAAAAAH!!"
    scene SwimClass_Scene80 with Dissolve(0.2)
    Tanya "phooo"
    scene SwimClass_Scene81 with Dissolve(0.2)
    Tanya "GHAAAAAAH!!"
    scene SwimClass_Scene80 with Dissolve(0.2)
    Tanya "{color=#808080}*Ughhhh, I forgot how many times I have to do this!*{/color}"
    scene SwimClass_Scene81 with Dissolve(0.2)
    Tanya "GHAAAAAAH!!"
    scene SwimClass_Scene80 with Dissolve(0.2)
    Tanya "phooo"
    scene SwimClass_Scene82 with Dissolve(0.2)
    MC "{color=#808080}*I could actually die right now and I wouldn't even be mad about it.*{/color}"
    MC "{color=#808080}*For how hard she looks.*{/color}"
    scene SwimClass_Scene83 with Dissolve(0.5)
    MC "{color=#808080}*Her lips sure are soft..*{/color}"
    scene SwimClass_Scene82 with Dissolve(0.5)
    MC "{color=#808080}*But sadly I don't think I can withstand this any longer.*{/color}"
    MC "{color=#808080}*She's exhaling like a leaf blower, my lungs are going to pop.*{/color}"
    scene SwimClass_Scene84 with Dissolve(0.5)
    MC "{color=#808080}*But before I stop this... maybe...*{/color}"
    menu:
        "Stick your tongue out":
            scene SwimClass_Scene85 with Dissolve(0.5)
            Tanya "Huh?!"
            MC "{color=#808080}*What?! Oh my god, she stuck her tongue out as well out of reflex!*{/color}"
            scene SwimClass_Scene86 with Dissolve(0.5)
            Tanya "{color=#808080}*Did he...? No, he couldn't...*{/color}"
            scene SwimClass_Scene87 with Dissolve(0.5)
            MC "GHAAAAAAHHHHH!!"
            scene SwimClass_Scene88 with Dissolve(0.5)
            Isabella "OH MY GOD, [MC_upper]!!!"
            scene SwimClass_Scene89 with Dissolve(0.5)
            Maria "{color=#808080}*Thank god... he's back...*{/color}"
            Maria "{color=#808080}*But wait... is the teacher... or did he...*{/color}"
            scene SwimClass_Scene90 with Dissolve(0.5)
            IsabellaCry "[MC], are you alright?"
            scene SwimClass_Scene91 with Dissolve(0.5)
            Tanya "{color=#808080}*Oh my god, what did I do?!*{/color}"
            Tanya "{color=#808080}*But I couldn't possibly... And I think he did it first...*{/color}"
            Tanya "{color=#808080}*But even so... I did it as well... to my own little cousin!*{/color}"
            Tanya "{color=#808080}*That was my first kiss...*{/color}"
            scene SwimClass_Scene92 with Dissolve(0.5)
            Tanya "{color=#808080}*Ughh... what am I thinking, I am the teacher here, I can't show myself to the girls like that.*{/color}"
            Tanya "{color=#808080}*I should be happy [MC] is alright right now.*{/color}"
            scene SwimClass_Scene93 with Dissolve(0.5)
            IsabellaCry "I'm so glad you are alright!"
            IsabellaCry "Don't you ever scare me like that!"
            IsabellaCry "I almost fainted!"
            scene SwimClass_Scene94 with Dissolve(0.5)
            IsabellaCry "I was so, so scared!"
            scene SwimClass_Scene95 with Dissolve(0.5)
            Tanya "Alright girls, nothing to see here!"
            Tanya "You are free early today! Not a word to the other teachers!"
            scene SwimClass_Scene96 with Dissolve(0.5)
            Selina "UGH, finally, I was about to throw up!"
            scene SwimClass_Scene97 with Dissolve(0.5)
            Tanya "I will go check on the girls, I'll leave these two to you, Maria."
            scene SwimClass_Scene98 with Dissolve(0.5)
            Tanya "I have to make sure none of them got traumatized or something like that."
            Tanya "If what happened here gets out, I'm in deep trouble."
            Tanya "So please keep what happened here between us as well."
            scene SwimClass_Scene99 with Dissolve(0.5)
            Tanya "And get Isa and lead [MC] to the infirmary."
            scene SwimClass_Scene100 with Dissolve(0.5)
            Maria "Okay teach, leave 'em to me, you have nothing to worry about here."
            scene SwimClass_Scene101 with Dissolve(0.5)
            Tanya "Thank you, Maria, I'm counting on you."
            scene SwimClass_Scene102 with Dissolve(0.5)
            MC "Uhh... Isa? Not to ruin the moment..."
            MC "But your tits are crushing my lungs more than Tanya did with all her force."
            scene SwimClass_Scene103 with Dissolve(0.5)
            Isabella "That's disgusting."
            Isabella "Plus, you did ruin the moment."
            Isabella "PLUS, don't say that with Maria here. Actually, don't say stuff like that to your little sister at all!"
            scene SwimClass_Scene104 with Dissolve(0.5)
            MC "Isa. I'm dying. Get your fat ass off of me!"
            scene SwimClass_Scene105 with Dissolve(0.5)
            Isabella "Okay, okay, geez..."
            scene SwimClass_Scene106 with Dissolve(0.5)
            Isabella "You don't have to be so mean about it!"
            MC "Sorry, but you were actually killing me."
            scene SwimClass_Scene107 with Dissolve(0.5)
            MC "Could you please check in at the infirmary to see if the nurse is there?"
            MC "I wouldn't wanna go all the way there for nothing."
            scene SwimClass_Scene108 with Dissolve(0.5)
            Isabella "No! I wanna stay with you! Maria should go!"
            scene SwimClass_Scene109 with Dissolve(0.5)
            MC "Tanya told Maria to take care of me here, so stop being such a brat and go!"
            scene SwimClass_Scene110 with Dissolve(0.5)
            Isabella "Humph! Alright, I'll go. Maria this, Maria that, have it your way then!"
            scene SwimClass_Scene111 with Dissolve(0.5)
            MC "I sure do hate to see her leave."
            scene SwimClass_Scene112 with Dissolve(0.5)
            Maria "But I love to see her go..."
            scene SwimClass_Scene113 with Dissolve(0.5)
            MC "Ummm, excuse me? That's my sister you freak! Don't talk like that about her."
            scene SwimClass_Scene114 with Dissolve(0.5)
            Maria "You are the freak that shouldn't talk like that about his sister, but here we are, freak!"
            scene SwimClass_Scene115 with Dissolve(0.5)
            MC "Ughhh, whatever, we should probably get going as well."
            scene SwimClass_Scene116 with Dissolve(0.5)
            Maria "Huh?! Already? Are you sure you are fine?"
            Maria "What happened there anyway? How did you pass out?"
            scene SwimClass_Scene117 with Dissolve(0.5)
            MC "Huh? Pass out? I didn't pass out, I just hurt my head a little."
            scene SwimClass_Scene118 with Dissolve(0.5)
            Maria "You. Did. What?!"
            Maria "Then all of that was..."
            scene SwimClass_Scene119 with Dissolve(0.5)
            MC "Yep. I made it the fuck up."
            MC "World-class act, right?"
            scene SwimClass_Scene120 with Dissolve(0.5)
            Maria "UGHHHH, you asshole! You really had me worried for a second there!"
            scene SwimClass_Scene121 with Dissolve(0.5)
            MC "Yeah, I thought you would realize I was bullshittin'."
            MC "And I didn't expect you to worry so much, that was really nice of you."
            MC "I knew you secretly loved me."
            scene SwimClass_Scene122 with Dissolve(0.5)
            Maria "Hah, in your dreams, new guy!"
            scene SwimClass_Scene123 with Dissolve(0.5)
            MC "Are you sure? How come you are still holding my hand?"
            scene SwimClass_Scene124 with Dissolve(0.5)
            MC "Not that I can complain, your hands are softer than I imagined."
            scene SwimClass_Scene125 with Dissolve(0.5)
            Maria "......."
            scene SwimClass_Scene126 with Dissolve(0.5)
            Maria "I just forgot I was holding it, okay? Now stop being annoying."
            scene SwimClass_Scene127 with Dissolve(0.5)
            Maria "If you're alright, let's get going. It would be weird if people saw us still being here."
            scene SwimClass_Scene128 with Dissolve(0.5)
            Maria "And stop fondling my thighs, geez, you really can't hold it in, can you?!"
            scene SwimClass_Scene129 with Dissolve(0.5)
            MC "Oh c'mon, can you even blame me for that? Just take a look at yourself."
            scene SwimClass_Scene130 with Dissolve(0.5)
            Maria "Ugh, let's just go already!"
            call stat_reward({"Maria": {"love": 2}, "Tanya": {"love": -5, "corruption": 2}}, return_to=None)
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")
        "Don't":
            MC "{color=#808080}*Nah, if I'm caught, I'm not only expelled, but my whole family will hear about it.*{/color}"
            MC "{color=#808080}*I'll just resist some more; her normal kisses are perfect anyway.*{/color}"
            scene SwimClass_Scene69 with Dissolve(0.5)
            Tanya "Alright, let's go again, I will go harder this time!"
            scene SwimClass_Scene131 with Dissolve(0.5)
            MC "{color=#808080}*Nope, no you don't. I'm not dying today, fuck this.*{/color}"
            scene SwimClass_Scene132 with Dissolve(0.5)
            MC "GHAAAAAH!!"
            scene SwimClass_Scene88 with Dissolve(0.5)
            Isabella "OH MY GOD, [MC_upper]!!!"
            scene SwimClass_Scene90 with Dissolve(0.5)
            IsabellaCry "Are you alright?"
            scene SwimClass_Scene91 with Dissolve(0.5)
            Tanya "{color=#808080}*Oh my god, I did it...*{/color}"
            Tanya "{color=#808080}*That was my first kiss... and it was with my little cousin...*{/color}"
            scene SwimClass_Scene92 with Dissolve(0.5)
            Tanya "{color=#808080}*Ughh... I shouldn't think about it like that, I did it to save him, it wasn't a kiss!*{/color}"
            Tanya "{color=#808080}*I should be happy [MC] is alright right now.*{/color}"
            scene SwimClass_Scene93 with Dissolve(0.5)
            IsabellaCry "I'm so glad you are alright!"
            IsabellaCry "Don't you ever scare me like that!"
            IsabellaCry "I almost fainted!"
            scene SwimClass_Scene94 with Dissolve(0.5)
            IsabellaCry "I was so, so scared!"
            scene SwimClass_Scene95 with Dissolve(0.5)
            Tanya "Alright girls, nothing to see here!"
            Tanya "You are free early today! Not a word to the other teachers!"
            scene SwimClass_Scene96 with Dissolve(0.5)
            Selina "UGH, finally, I was about to throw up!"
            scene SwimClass_Scene97 with Dissolve(0.5)
            Tanya "I will go check on the girls, I'll leave these two to you, Maria."
            scene SwimClass_Scene98 with Dissolve(0.5)
            Tanya "I have to make sure none of them got traumatized or something like that."
            Tanya "If what happened here gets out, I'm in deep trouble."
            Tanya "So please keep what happened here between us as well."
            scene SwimClass_Scene99 with Dissolve(0.5)
            Tanya "And get Isa and lead [MC] to the infirmary."
            scene SwimClass_Scene100 with Dissolve(0.5)
            Maria "Okay teach, leave 'em to me, you have nothing to worry about here."
            scene SwimClass_Scene101 with Dissolve(0.5)
            Tanya "Thank you, Maria, I'm counting on you."
            scene SwimClass_Scene102 with Dissolve(0.5)
            MC "Uhh... Isa? Not to ruin the moment..."
            MC "But your tits are crushing my lungs more than Tanya did with all her force."
            scene SwimClass_Scene103 with Dissolve(0.5)
            Isabella "That's disgusting."
            Isabella "Plus, you did ruin the moment."
            Isabella "PLUS, don't say that with Maria here. Actually, don't say stuff like that to your little sister at all!"
            scene SwimClass_Scene104 with Dissolve(0.5)
            MC "Isa. I'm dying. Get your fat ass off of me!"
            scene SwimClass_Scene105 with Dissolve(0.5)
            Isabella "Okay, okay, geez..."
            scene SwimClass_Scene106 with Dissolve(0.5)
            Isabella "You don't have to be so mean about it!"
            MC "Sorry, but you were actually killing me."
            scene SwimClass_Scene107 with Dissolve(0.5)
            MC "Could you please check in at the infirmary to see if the nurse is there?"
            MC "I wouldn't wanna go all the way there for nothing."
            scene SwimClass_Scene108 with Dissolve(0.5)
            Isabella "No! I wanna stay with you! Maria should go!"
            scene SwimClass_Scene109 with Dissolve(0.5)
            MC "Tanya told Maria to take care of me here, so stop being such a brat and go!"
            scene SwimClass_Scene110 with Dissolve(0.5)
            Isabella "Humph! Alright, I'll go. Maria this, Maria that, have it your way then!"
            scene SwimClass_Scene111 with Dissolve(0.5)
            MC "I sure do hate to see her leave."
            scene SwimClass_Scene112 with Dissolve(0.5)
            Maria "But I love to see her go..."
            scene SwimClass_Scene113 with Dissolve(0.5)
            MC "Ummm, excuse me? That's my sister, you freak! Don't talk like that about her."
            scene SwimClass_Scene114 with Dissolve(0.5)
            Maria "You are the freak that shouldn't talk like that about his sister, but here we are, freak!"
            scene SwimClass_Scene115 with Dissolve(0.5)
            MC "Ughhh, whatever, we should probably get going as well."
            scene SwimClass_Scene116 with Dissolve(0.5)
            Maria "Huh?! Already? Are you sure you are fine?"
            Maria "What happened there anyway? How did you pass out?"
            scene SwimClass_Scene117 with Dissolve(0.5)
            MC "Huh? Pass out? I didn't pass out, I just hurt my head a little."
            scene SwimClass_Scene118 with Dissolve(0.5)
            Maria "You. Did. What!?"
            Maria "Then all of that was..."
            scene SwimClass_Scene119 with Dissolve(0.5)
            MC "Yep. I made it the fuck up."
            MC "World-class act, right?"
            scene SwimClass_Scene120 with Dissolve(0.5)
            Maria "UGHHHH, you asshole! You really had me worried for a second there!"
            scene SwimClass_Scene121 with Dissolve(0.5)
            MC "Yeah, I thought you would realize I was bullshittin'."
            MC "And I didn't expect you to worry so much; that was really nice of you."
            MC "I knew you secretly loved me."
            scene SwimClass_Scene122 with Dissolve(0.5)
            Maria "Hah, in your dreams, new guy!"
            scene SwimClass_Scene123 with Dissolve(0.5)
            MC "Are you sure? How come you are still holding my hand?"
            scene SwimClass_Scene124 with Dissolve(0.5)
            MC "Not that I can complain; your hands are softer than I imagined."
            scene SwimClass_Scene125 with Dissolve(0.5)
            Maria "......."
            scene SwimClass_Scene126 with Dissolve(0.5)
            Maria "I just forgot I was holding it, okay? Now stop being annoying."
            scene SwimClass_Scene127 with Dissolve(0.5)
            Maria "If you're alright, let's get going. It would be weird if people saw us still being here."
            scene SwimClass_Scene128 with Dissolve(0.5)
            Maria "And stop fondling my thighs, geez, you really can't hold it in, can you?!"
            scene SwimClass_Scene129 with Dissolve(0.5)
            MC "Oh c'mon, can you even blame me for that? Just take a look at yourself."
            scene SwimClass_Scene130 with Dissolve(0.5)
            Maria "Ugh, let's just go already!"
            call stat_reward({"Maria": {"love": 2}, "Tanya": {"corruption": 2}}, return_to=None)
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")


