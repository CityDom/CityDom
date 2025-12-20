init python:
    def get_upper_name(character):
        # Handle both string names and Character objects safely.
        if isinstance(character, str):
            return character.upper()
        name = getattr(character, "name", None) or getattr(character, "who", None)
        if name is None:
            name = str(character)
        return name.upper()

label GameIntro:
    scene WarningScreen
    menu:
        "I Agree":
            hide WarningScreen
        "Exit":
            $ renpy.quit()
    scene BlackScreen
    $ mc_name = renpy.input("What is your name?", default="").strip()
    if mc_name == "":
        $ mc_name = "John"

    # Dynamically set the MC character object with the chosen name.
    $ MC = Character(mc_name)
    $ MC_upper = get_upper_name(MC)
    scene IntroScene1 with Dissolve(0.5)
    McDad "I'm sorry things went this way, [MC]..."
    McDad "But at least you will get to spend some time with your mom and sisters."
    McDad "You haven't seen them in a few years now."
    McDad "Maybe catch up on things."
    scene IntroScene2 with Dissolve(0.5)
    MC "It's okay, dad!"
    MC "I understand it wasn't your fault."
    MC "But I'm excited to see the girls again."
    MC "I think it's actually been around six or seven years since I left to live with you."
    MC "So... some catching up would be nice!"
    scene IntroScene3 with Dissolve(0.5)
    McDad "Okay, [MC]."
    McDad "I'll go now. Your mom will get out of the house to greet you."
    McDad "And I don't want her to see me."
    McDad "Take your luggage from the back already."
    scene IntroScene4 with Dissolve(0.5)
    MC "There was only my backpack..."
    MC "What did you do with the rest of the luggage?"
    MC "You said you put them in the trunk."
    scene IntroScene5 with Dissolve(0.5)
    McDad "Uhhh... I might've forgotten them..."
    McDad "I'll drop by in a couple of days to bring them to you."
    McDad "'Till then you'll work something out."
    McDad "Your mom is coming!"
    scene IntroScene6 with Dissolve(0.5)
    McDad "Gotta go! Bye!"
    MC "{color=#808080}*Asshole...*{/color}"
    Jennifer "[MC_upper]!!!"
    MC "Oh, hey mom! Long time no s-"
    show IntroVideo1
    Jennifer "[MC_upper], IS THAT YOU?!"
    scene IntroScene12 with Dissolve(0.5)
    MC "{color=#808080}*Oh my god...*{/color}"
    MC "{color=#808080}*No way this is mom!!!*{/color}"
    MC "{color=#808080}*Thinking about it... She didn't change that much since I was a kid.*{/color}"
    MC "{color=#808080}*But now she looks so hot.*{/color}"
    scene introscene10 with Dissolve(0.5)
    Jennifer "Ummmm... [MC]?"
    scene introscene11 with Dissolve(0.5)
    Jennifer "{color=#808080}*Uhhh... please don't tell me that's not [MC]...*{/color}"
    scene IntroScene9 with Dissolve(0.5)
    MC "Yeah mom, it's me!"
    MC "I got lost in thought a little bit, I haven't seen you in so long!"
    scene introscene13 with Dissolve(0.5)
    Jennifer "Come to mommy kiddo, I missed you so much!!"
    scene introscene14 with Dissolve(1)
    Jennifer "Come here! You've grown so much!"
    Jennifer "You are almost as tall as me now!"
    scene introscene15 with Dissolve(0.5)
    MC "{color=#808080}*I think I might be in heaven right now!*{/color}"
    scene introscene16 with Dissolve(0.5)
    MC "{color=#808080}*Even though I can't breathe.*{/color}"
    scene introscene15 with Dissolve(0.5)
    MC "{color=#808080}*They are like two massive pillows!*{/color}"
    MC "{color=#808080}*But way, way softer!*{/color}"
    scene introscene16 with Dissolve(0.5)
    MC "Mmmmm mmmmmmf mmmmhh..."
    MC "{color=#808080}*I might actually die if I stay like this any longer!!*{/color}"
    scene introscene15 with Dissolve(0.5)
    MC "Mom, I can-"
    scene introscene16 with Dissolve(0.5)
    MC "Mmmmm mmmmmmffff mmmmhhhhh..."
    Jennifer "You've grown into such a handsome young man!"
    scene introscene15 with Dissolve(0.5)
    MC "I can't breathe!!!"
    scene introscene17 with Dissolve(0.5)
    Jennifer "Oh yeah, sorry, I'm just so happy to see you!"
    scene introscene18 with Dissolve(0.5)
    Jennifer "How long has it been?"
    Jennifer "I think at least a couple of years!"
    scene IntroScene19 with Dissolve(0.5)
    MC "I think way more than that mom..."
    MC "At least six or seven..."
    scene introscene18 with Dissolve(0.5)
    Jennifer "Haha! I might've lost track of time then."
    Jennifer "With the two little devils on my head all the time."
    show IntroVideo2
    Jennifer "Speaking of the devil..."
    scene introscene24 with Dissolve(0.5)
    Jennifer "I was wondering when she was going to show up."
    scene introscene20 with Dissolve(0.5)
    Isabella "What's with all this commotion mom?"
    Isabella "I told you, I can't be late for school today!"
    Isabella "And I don't wanna go without eating anything before leaving."
    scene introscene21 with Dissolve(0.5)
    Isabella "And who is this guy?"
    scene introscene22 with Dissolve(0.5)
    Isabella "Hmmmm...."
    Isabella "{color=#808080}*Wait a second...*{/color}"
    scene introscene23 with Dissolve(0.5)
    Isabella "Oh my god, there's no way..."
    Isabella "[MC], is that you?"
    scene introscene25 with Dissolve(0.5)
    MC "Hey, Isa! Long time no see!"
    scene introscene26 with Dissolve(0.5)
    MC "Uhhh... what are you doing?"
    scene introscene27 with Dissolve(0.5)
    MC "Ummm.. wait a second, Isa!"
    scene introscene28 with Dissolve(0.5)
    Jennifer "Isabella, wait! You don't have any shoes on!"
    scene introscene29 with Dissolve(0.5)
    MC "ISA WAIT!!!"
    scene introscene30 with Dissolve(0.5)
    Isabella "I missed you so much, [MC]!!!"
    scene introscene31 with Dissolve(0.5)
    Jennifer "[MC], be careful!!"
    scene introscene32 with Dissolve(0.5)
    Jennifer "[MC], are you alright?!"
    Isabella "Oh my god. [MC], are you ok?"
    MC "Uhhhh... yeah... I'm fine..."
    MC "{color=#808080}*Her fat ass is sitting right on my dick, if she doesn't get off soon I might explode!*{/color}"
    MC "{color=#808080}*She is a bit heavier than the last time I saw her.*{/color}"
    MC "{color=#808080}*Also, her tits got so huge.*{/color}"
    scene introscene33 with Dissolve(0.5)
    MC "I just lost my balance."
    MC "And hurt my butt a little."
    scene introscene34 with Dissolve(0.5)
    Isabella "Hehe, you're still the same weak kid I knew!"
    scene introscene35 with Dissolve(0.5)
    MC "You just caught me off guard!"
    MC "I didn't expect you to be so happy to see me again!"
    scene introscene34 with Dissolve(0.5)
    Isabella "What can I say, I'm still the adorable little sister you know and love."
    scene introscene36 with Dissolve(0.5)
    MC "Yeah, more like the same ol' brat that bugs me all the time!"
    Isabella "Oh wow, what a nice memory you have of me."
    MC "Who could forget what an annoying little kid you were."
    MC "And apparently you didn't change one bit, you're still the same kid."
    scene introscene37 with Dissolve(0.5)
    Isabella "You seem to live in the past, big bro!"
    Isabella "I'm no longer a little kid!"
    Isabella "And where do you think you are putting your hands?"
    scene introscene39 with Dissolve(0.5)
    Isabella "It seems that you didn't change at all."
    Isabella "The same ol' dirty little pervert."
    scene introscene38 with Dissolve(0.5)
    MC "Look who's talking!"
    MC "On what do you think you're sitting?"
    MC "Making yourself all comfortable like that, huh?"
    MC "Pervert!"
    scene introscene41 with Dissolve(0.5)
    Isabella "I ended up in this position because of your weak legs!"
    Isabella "And I wouldn't want to get into a pervert competition with you."
    Isabella "I'd lose drastically!"
    scene introscene42 with Dissolve(0.5)
    MC "And what makes you say that?"
    scene introscene43 with Dissolve(0.5)
    Isabella "Maybe the fact that you can barely look me in my eyes?"
    scene introscene44 with Dissolve(0.5)
    MC "I was just admiring how much you've grown, lil' sis!"
    scene introscene43 with Dissolve(0.5)
    Isabella "Yeah, right!"
    Isabella "And what do you think? Have I grown?"
    scene introscene45 with Dissolve(0.5)
    Jennifer "I don't know what you kids are talking about there, but stop fighting!"
    scene introscene40 with Dissolve(0.5)
    Jennifer "Isa, get off your brother, he's hurt!"
    Jennifer "And you shouldn't sit on him like that anyways!"
    scene introscene46 with Dissolve(0.5)
    Isabella "We are not fighting, mom!"
    Isabella "We are just teasing each other."
    scene introscene48 with Dissolve(0.5)
    Jennifer "Just get off of him already and let's go inside!"
    Jennifer "[MC] must be tired from the road."
    scene introscene47 with Dissolve(0.5)
    Claire "What's with all the fuss?"
    Claire "Mom, is breakfast ready yet? What are y'all doing?"
    scene introscene49 with Dissolve(0.5)
    Claire "And who is that guy?"
    Claire "Don't tell me Isabella finally got a boyfriend."
    show IntroVideo3
    MC "{color=#808080}*Ughhh.... that must be Claire...*{/color}"
    MC "{color=#808080}*And she seems to be the same ol' bitch that I know.*{/color}"
    MC "{color=#808080}*She's super annoying and seems to hate everyone.*{/color}"
    MC "{color=#808080}*It got even worse ever since dad left.*{/color}"
    MC "{color=#808080}*But after I went to live with dad, she started hating me even more because I was the one going with him and not her.*{/color}"
    MC "{color=#808080}*I don't know what she liked so much about that asshole.*{/color}"
    scene IntroScene50 with Dissolve(0.5)
    Isabella "Very funny, Claire."
    Isabella "But I don't remember ever seeing you with a man either."
    Isabella "And you are already a bitter old hag!"
    Isabella "I still got time!"
    scene IntroScene51 with Dissolve(0.5)
    Claire "You got some nerve in you, Isabella!"
    Claire "How about you shut up before I come over there and shut you up myself in front of your boyfriend?"
    scene IntroScene52 with Dissolve(0.5)
    Jennifer "CLAIRE! ISABELLA!"
    Jennifer "Stop fighting now!"
    Jennifer "And that's not her boyfriend!"
    Jennifer "It's your brother!"
    Jennifer "[MC] arrived."
    scene IntroScene53 with Dissolve(0.5)
    MC "Hey, Claire! Long time no see, right?"
    scene IntroScene54 with Dissolve(0.5)
    Claire "Oh great... The loser is back."
    Claire "Is that all the fuss?"
    Claire "And why is Isa on top of him? That's disgusting!"
    scene IntroScene55 with Dissolve(0.5)
    Claire "Wait... does that mean..."
    scene IntroScene56 with Dissolve(0.5)
    Claire "That dad is here as well?"
    MC "{color=#808080}*This is one of the few times you could see her with a slight smile on her face.*{/color}"
    scene IntroScene57 with Dissolve(0.5)
    MC "I'm sorry, Claire, he left as soon as he dropped me."
    MC "You know he's scared of mom, he never wants to meet eyes with her."
    scene IntroScene58 with Dissolve(0.5)
    Claire "Ughhh..."
    Claire "Thanks a lot, mom! You managed to ruin everything again!!"
    Claire "Now, are you making breakfast or not? I have to leave for school!"
    scene IntroScene59 with Dissolve(0.5)
    Jennifer "I'm sorry, Claire, I didn't mean to do that."
    Jennifer "I didn't even see him."
    Jennifer "I'll help [MC] with his luggage and make breakfast."
    scene IntroScene60 with Dissolve(0.5)
    Claire "UGHHHH!! Just do it already!"
    MC "{color=#808080}*Mom is always going easy on her...*{/color}"
    MC "{color=#808080}*Since she feels that it's her fault for dad leaving.*{/color}"
    MC "{color=#808080}*And for Claire's resentment.*{/color}"
    scene IntroScene61 with Dissolve(0.5)
    Jennifer "I'm sorry for that, [MC]... It's my fault."
    Jennifer "So don't think bad of her."
    Jennifer "She's not always like that!"
    scene IntroScene63 with Dissolve(0.5)
    Isabella "{color=#808080}*She ABSOLUTELY is always like that.*{/color}"
    MC "{color=#808080}*From what I remember she's like that all the time...*{/color}" 
    scene IntroScene61 with Dissolve(0.5)
    Jennifer "Anyway, let's go inside."
    Jennifer "I guess you are hungry, [MC]."
    Jennifer "I'll make breakfast."
    scene IntroScene99 with Dissolve(0.5)
    Jennifer "Isa, help [MC] with his luggage."
    scene IntroScene67 with Dissolve(0.5)
    Jennifer "Speaking of that... Where is your stuff?"
    Jennifer "I only saw you with a backpack and that's gone as well now."
    scene IntroScene64 with Dissolve(0.5)
    MC "Uhhh... yeah... about that..."
    MC "Dad forgot to put my luggage in the trunk..."
    MC "He said he'll drop by in a few days to give me the rest of my stuff."
    MC "I only have my backpack with a few clothes."
    scene IntroScene65 with Dissolve(0.5)
    Jennifer "Ughhh... I knew that asshole was good for nothing."
    Jennifer "And where is your backpack?"
    scene IntroScene64 with Dissolve(0.5)
    MC "Uhhh..."
    MC "It must've fallen when Isa jumped on me."
    scene IntroScene66 with Dissolve(0.5)
    MC "I'll look for it, I don't know where it went."
    scene IntroScene67 with Dissolve(0.5)
    Jennifer "Okay, [MC], I'll go prepare the breakfast."
    scene IntroScene68 with Dissolve(0.5)
    Jennifer "Isa, help [MC] find his backpack and get him to his room."
    scene IntroScene69 with Dissolve(0.5)
    Isabella "Okay, mom!"
    scene IntroScene68 with Dissolve(0.5)
    Jennifer "Come in like 30 minutes to eat."
    scene IntroScene70 with Dissolve(0.5)
    Isabella "Sooo... where did you throw it?"
    Isabella "Or when did you throw it?"
    scene IntroScene71 with Dissolve(0.5)
    MC "I threw it when you were about to jump on me."
    MC "But I don't really remember where..."
    MC "I haven't had a lot of time to think about it."
    MC "You just threw yourself at me."
    scene IntroScene72 with Dissolve(0.5)
    Isabella "My bad for being such a loving and adorable sister..."
    scene IntroScene73 with Dissolve(0.5)
    MC "You can go inside if you want."
    MC "I forgot you don't have any shoes on."
    MC "I'll get the backpack and come as well."
    scene IntroScene74 with Dissolve(0.5)
    Isabella "It's okay, I don't like these leggings anyway."
    scene IntroScene75 with Dissolve(0.5)
    Isabella "Plus..."
    scene IntroScene76 with Dissolve(0.5)
    Isabella "I think it's right there."
    scene IntroScene77 with Dissolve(0.5)
    Isabella "On that rock."
    scene IntroScene78 with Dissolve(0.5)
    MC "Yep, there it is."
    scene IntroScene79 with Dissolve(0.5)
    Isabella "And... how was it?"
    scene IntroScene80 with Dissolve(0.5)
    MC "How was what?"
    scene IntroScene81 with Dissolve(0.5)
    Isabella "You know... living with dad."
    scene IntroScene82 with Dissolve(0.5)
    MC "Ehh... you know... not the best.."
    MC "He's got a new girlfriend."
    MC "And she has a kid with her. So we were all living together."
    MC "But over all it was okay, a bit annoying though."
    scene IntroScene84 with Dissolve(0.5)
    Isabella "Really? Well... I guess it's normal..."
    scene IntroScene85 with Dissolve(0.5)
    Isabella "And... how are the girls?"
    Isabella "Did you get along with them?"
    scene IntroScene86 with Dissolve(0.5)
    MC "Pretty good, the daughter was pissing me off a little."
    MC "But all in all, it was alright..."
    scene IntroScene87 with Dissolve(0.5)
    Isabella "So... you've had it pretty good, huh?"
    Isabella "I bet you are sad about coming here."
    scene IntroScene88 with Dissolve(0.5)
    MC "Haha, what are you crying about, sis?"
    MC "Are you worried that you've been replaced?"
    scene IntroScene89 with Dissolve(0.5)
    Isabella "Why are you laughing, you asshole!"
    scene IntroScene88 with Dissolve(0.5)
    Isabella "......"
    scene IntroScene89 with Dissolve(0.5)
    Isabella "Maybe a little bit...."
    scene IntroScene88 with Dissolve(0.5)
    MC "You have nothing to worry about, Isa."
    MC "I'm happy that I'm here now."
    MC "And I don't know about that asshole, but you know I always called in and thought about you."
    MC "Nobody can replace how annoying you are."
    scene IntroScene90 with Dissolve(0.5)
    Isabella "You really are an asshole, you know that, right?"
    scene IntroScene92 with Dissolve(0.5)
    MC "Just as I was before I left."
    MC "Haven't changed one bit."
    scene IntroScene91 with Dissolve(0.5)
    Isabella "Hmmm.. maybe a little bit."
    Isabella "I don't remember you being this nice."
    scene IntroScene92 with Dissolve(0.5)
    MC "What can I say, sis, people grow."
    MC "Now come here already."
    scene IntroScene93 with Dissolve(0.5)
    MC "I really missed you, sis. I'm glad I came back."
    MC "And don't worry, nobody can replace you guys."
    scene IntroScene94 with Dissolve(0.5)
    Isabella "I'm glad you're here as well, big bro."
    Isabella "And I'm really happy you feel that way."
    Isabella "It's just... I..."
    scene IntroScene95 with Dissolve(0.5)
    Isabella "I don't know why he replaced us.."
    scene IntroScene96 with Dissolve(0.5)
    MC "You really haven't spend that much time with him, huh?"
    MC "He's still the same asshole that you remember, nothing changed."
    MC "I don't know what he thinks, or why he did what he did, but I'm here now."
    MC "And I won't ever leave you."
    scene IntroScene95 with Dissolve(0.5)
    Isabella "Thank you, [MC]..."
    scene IntroScene97 with Dissolve(0.5)
    Isabella "I feel a lot better now."
    scene IntroScene98 with Dissolve(0.5)
    Isabella "Now let's go show you the rooms."
    Isabella "Mom prepared yours already."
    scene BlackScreen with Dissolve(3)
    MC "A month went by..."
    MC "Time flies pretty quick, huh?"
    MC "All the lovey-dovey attitude from mom and Isa went by fast."
    MC "Mom went back to the nice yet stern mother."
    MC "Isa went back to being an annoying little brat."
    MC "And Claire... well... she's the same."
    MC "A bitch who hates the hell out of me and everything else."
    scene IntroScene100 with Dissolve(0.5)
    MC "So all in all things are better than before."
    MC "The biggest problem is that I'm sitting here, blue balled, every single day, 24/7."
    MC "Even Isa grew up hot as fuck..."
    MC "Not even mentioning Claire, looking like a complete bimbo."
    MC "I can't live like this... beating my dick five times a day thinking about my family..."
    MC "I have to do something... take my mind from it..."
    MC "............"
    Unknown "You really love bitching about everything, don't you, kid?"
    Unknown "You'll never fuck anyone acting like that...."
    scene IntroScene101 with Dissolve(0.5)
    MC "{color=#808080}*What the fuck was that?!?!?*{/color}"
    MC "{color=#808080}*Who the fuck said that....*{/color}"
    scene IntroScene102 with Dissolve(0.5)
    MC "{color=#808080}*Uhhh right... I must be dreaming...*{/color}"
    MC "{color=#808080}*Being blue balled all this time finally caught up to me.*{/color}"
    scene IntroScene101 with Dissolve(0.5)
    MC "{color=#808080}*I'm starting to hallucinate.*{/color}"
    scene IntroScene104 with Dissolve(0.5)
    Unknown "I'm as real as it gets, kid."
    Unknown "You really are a loser, huh?"
    Unknown "Having me next to you and the first thing you do is having a panic attack..."
    scene IntroScene105 with Dissolve(0.5)
    MC "Wait!! Don't come any closer!!"
    MC "MOM!! SOMEBODY!!! HELP!!!"
    scene IntroScene106 with Dissolve(0.5)
    Unknown "Ughhh... why did I think he was a good idea...."
    Unknown "I always get this reaction..."
    scene IntroScene107 with Dissolve(0.5)
    Unknown "Maybe I'm approaching this whole situation incorrectly I guess..."
    Unknown "I guess I could try a different approach..."
    scene IntroScene108 with Dissolve(0.5)
    MC "GET AWAY FROM ME!!!"
    MC "I'LL CALL THE POLICE!!"
    scene IntroScene109 with Dissolve(0.5)
    MC "WHAT DO YOU WANT FROM ME? MONEY? I DON'T HAVE ANY!!"
    MC "{color=#808080}*Wait what...*{/color}"
    MC "{color=#808080}*She disappeared...*{/color}"
    scene IntroScene110 with Dissolve(0.5)
    MC "{color=#808080}*I really was just imagining things...*{/color}"
    MC "{color=#808080}*Thank god... it scared the shit out of me!*{/color}"
    MC "{color=#808080}*....*{/color}"
    MC "{color=#808080}*She was so fucking hot though..*{/color}"
    MC "{color=#808080}*If I would've realized it was just a hallucination...*{/color}"
    MC "{color=#808080}*Maybe I could've done something with her...*{/color}"
    show IntroVideo4
    Unknown "Awwwww, you think I'm hot? How nice!"
    Unknown "And what exactly do you think you were going to do with me, huh?"
    show IntroVideo5
    MC "AAAAAAAAA MOM, COME HERE, SOMEBODY IS IN MY ROOM!!!"
    MC "HELP!!!!"
    scene IntroScene111 with Dissolve(0.5)
    Unknown "UGHHHHHH!!!!!!"
    Unknown "STOP YELLING LIKE A LITTLE BITCH!!!"
    scene IntroScene112 with Dissolve(0.5)
    Unknown "Every single FUCKING time!!"
    scene IntroScene113 with Dissolve(0.5)
    Unknown "You want me to scream with you?"
    Unknown "Maybe that would calm you down!"
    scene IntroScene114 with Dissolve(0.5)
    Unknown "AAAAAAAAAAA!!! HELP!!!!!"
    Unknown "SOMEBODY PLEASE HELP!!!!!"
    Unknown "I'M A VIRGIN LOSER!!!!!!!"
    scene IntroScene115 with Dissolve(0.5)
    Unknown "Feeling better now?"
    Unknown "Don't you get it?"
    Unknown "Nobody can hear us, you dumbass!"
    scene IntroScene116 with Dissolve(0.5)
    MC "{color=#808080}*She's right!*{/color}"
    MC "{color=#808080}*Mom hasn't gone to sleep yet...*{/color}"
    MC "{color=#808080}*And she usually barges in my room at every little sound.*{/color}"
    scene IntroScene117 with Dissolve(0.5)
    Unknown "Of course I'm fucking right!"
    Unknown "Do you think I'd come in here not expecting you to cry like a bitch?"
    Unknown "Even though... you are one of the few..."
    Unknown "Most people usually pass out."
    scene IntroScene118 with Dissolve(0.5)
    MC "{color=#808080}*Wait, can she read my thoughts?*{/color}"
    MC "{color=#808080}*This happened multiple times already!*{/color}"
    scene IntroScene119 with Dissolve(0.5)
    Unknown "UGHHHHH!!!!!"
    scene IntroScene120 with Dissolve(0.5)
    Unknown "Yes, I can read them, finally catching up to the situation, aren't we?"
    scene IntroScene121 with Dissolve(0.5)
    MC "Ughhh... okay... I give up..."
    MC "Just let me know... are you here to kill me or hurt me?"
    scene IntroScene122 with Dissolve(0.5)
    Unknown "Hmmmm...."
    scene IntroScene123 with Dissolve(0.5)
    Unknown "This is rather a big change of mood."
    Unknown "What happened?"
    Unknown "Did you go psycho all of the sudden?"
    scene IntroScene121 with Dissolve(0.5)
    MC "Just tell me if you're going to kill or hurt me please..."
    scene IntroScene124 with Dissolve(0.5)
    Unknown "Ughhh.... Noooo.. I won't fucking kill you..."
    Unknown "Neither will I hurt you."
    Unknown "If I wanted to I would've done it already!"
    Unknown "Yada yada yada..."
    scene IntroScene123 with Dissolve(0.5)
    Unknown "Are you really going to make me say every cliché thing in existence?"
    scene IntroScene125 with Dissolve(0.5)
    MC "Phew! Thank goodness!!"
    MC "I really thought I was gonna die!"
    scene IntroScene126 with Dissolve(0.5)
    MC "Why the fuck didn't you start with that then?"
    MC "You scared the shit out of me!"
    scene IntroScene127 with Dissolve(0.5)
    Unknown "Hmmm..."
    scene IntroScene128 with Dissolve(0.5)
    Unknown "Yeah.. I never really thought about it.."
    Unknown "But what could a cute little girl like me ever do to you?"
    scene IntroScene129 with Dissolve(0.5)
    Unknown "See? Totally innocent!"
    Unknown "Couldn't even harm a flower!"
    scene IntroScene130 with Dissolve(0.5)
    MC "Maybe the big ass horns on your head destroy the innocent girl appearance a little bit..."
    scene IntroScene131 with Dissolve(0.5)
    Unknown "Whaaaaaat..."
    Unknown "Don't you like them?"
    Unknown "I'm pretty insecure about them, so please don't be mean!"
    Unknown "I know they are usually more bent... but it's not like I can do anything about it!"
    scene IntroScene132 with Dissolve(0.5)
    MC "Can you please stop mocking me?"
    MC "Okay... let's start over..."
    MC "What's your name?"
    scene IntroScene127 with Dissolve(0.5)
    Unknown "Hmmm..."
    scene IntroScene128 with Dissolve(0.5)
    Unknown "You put your big boy pants on."
    scene IntroScene133 with Dissolve(0.5)
    Mhyrorin "My name is Mhyrorin, nice to meet you, kiddo!"
    scene IntroScene132 with Dissolve(0.5)
    MC "Yeah, because that's a totally innocent name a little girl like you would have!"
    scene IntroScene134 with Dissolve(0.5)
    Mhyrorin "It's not like I named myself, you asshole!"
    Mhyrorin "Don't be so mean!"
    scene IntroScene135 with Dissolve(0.5)
    MC "Yeah.. I get it.."
    MC "I don't have the coolest name either..."
    MC "My name is [MC], nice to meet you!"
    scene IntroScene136 with Dissolve(0.5)
    Mhyrorin "Hmmm..."
    scene IntroScene137 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*I thought this kid would be like the others..*{/color}"
    Mhyrorin "{color=#808080}*But I guess I was wrong..*{/color}"
    Mhyrorin "{color=#808080}*I never made it past the screaming part before...*{/color}"
    Mhyrorin "{color=#808080}*This kid really is different.*{/color}"
    scene IntroScene138 with Dissolve(0.5)
    Mhyrorin "Nice to meet you too, [MC]!"
    scene IntroScene139 with Dissolve(0.5)
    MC "~Sigh~..."
    scene IntroScene140 with Dissolve(0.5)
    MC "You are actually pretty chill, huh?"
    MC "But no wonder people get scared when you barge in like that."
    MC "Being all creepy right next to me without making a sound.."
    MC "Actually... how the fuck did you get in here?"
    MC "And why are you butt ass naked?"
    scene IntroScene141 with Dissolve(0.5)
    Mhyrorin "I know I'm not the best at it!"
    Mhyrorin "I'm still practicing my entrances, okay?!"
    scene IntroScene142 with Dissolve(0.5)
    Mhyrorin "........"
    scene IntroScene141 with Dissolve(0.5)
    Mhyrorin "And I got in on the window..."
    Mhyrorin "It's not my fault you are deaf as shit!"
    scene IntroScene142 with Dissolve(0.5)
    Mhyrorin "........"
    scene IntroScene143 with Dissolve(0.5)
    Mhyrorin "And I'm totally not butt ass naked!!!"
    Mhyrorin "I got a really cute pair of panties!!"
    scene IntroScene144 with Dissolve(0.5)
    MC "Yeah... whatever you say... just don't get mad at me that I'm hard as shit."
    MC "You look so hot I could cum just looking at you."
    scene IntroScene145 with Dissolve(0.5)
    Mhyrorin "Awwwwwwww!!!!!"
    Mhyrorin "That's the cutest thing someone ever said to me!"
    Mhyrorin "It means a lot! Thank you!"
    scene IntroScene146 with Dissolve(0.5)
    Mhyrorin "But do you really say these kind of things to girls you just met a minute ago?"
    Mhyrorin "No wonder you are a virgin..."
    Mhyrorin "Actually, it's amazing you are not in prison by now."
    scene IntroScene147 with Dissolve(0.5)
    MC "Of course I don't say this kind of shit to other girls!"
    MC "But since you can read my thoughts, what's the point?!"
    scene IntroScene148 with Dissolve(0.5)
    Mhyrorin "Ohhh... yeah..."
    Mhyrorin "Forgot about that, haha!"
    Mhyrorin "My bad!"
    scene IntroScene149 with Dissolve(0.5)
    MC "Sooooo... Why are you here?"
    MC "What do you want from me?"
    scene IntroScene150 with Dissolve(0.5)
    Mhyrorin "Finally getting to the good part, aren't we?"
    scene IntroScene151 with Dissolve(0.5)
    Mhyrorin "I was wondering when you will ask that!"
    scene IntroScene152 with Dissolve(0.5)
    Mhyrorin "You really exceeded my expectations, you know?"
    scene IntroScene153 with Dissolve(0.5)
    Mhyrorin "So you better not disappoint me on this one!"
    Mhyrorin "It would make me really sad!"
    scene IntroScene154 with Dissolve(0.5)
    Mhyrorin "So just be nice and quiet for me, alright?!"
    scene IntroScene155 with Dissolve(0.5)
    Mhyrorin "I bet it won't take long!"
    scene IntroScene156 with Dissolve(0.5)
    Mhyrorin "........"
    Mhyrorin "{color=#808080}*Did he just....*{/color}"
    Mhyrorin "{color=#808080}*No way he put his foot on my face.*{/color}"
    scene IntroScene157 with Dissolve(0.5)
    Mhyrorin "What the fuck are you doing?!"
    Mhyrorin "Didn't I tell you to just sit still and let me do my thing?!"
    scene IntroScene159 with Dissolve(0.5)
    MC "What the fuck are YOU doing?"
    MC "Crawling up on me like that?"
    MC "It's hot as fuck but also reaaaaaaally creepy, you know?!"
    MC "What do you want?!"
    scene IntroScene158 with Dissolve(0.5)
    Mhyrorin "Ohhhhhh, I get it!"
    Mhyrorin "You are that kind of guy!"
    Mhyrorin "It's okay, I won't judge you..."
    Mhyrorin "I like this kind of stuff too!"
    scene IntroScene160 with Dissolve(0.5)
    Mhyrorin "Mmmmmm..."
    Mhyrorin "You are not bad at all, [MC]."
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo6", "IntroVideo7", "IntroVideo8", "IntroVideo9"])
    Mhyrorin "~Slurp~ You taste quite good!"
    MC "{color=#808080}*What the fuck is she doing?!*{/color}"
    MC "{color=#808080}*I can't move my leg at all!*{/color}"
    MC "{color=#808080}*How is she so fucking strong?!*{/color}"
    MC "{color=#808080}*She's just moving my leg around like I'm a doll.*{/color}"
    MC "{color=#808080}*UGHHHH....*{/color}"
    MC "{color=#808080}*I can't move at all...*{/color}"
    MC "{color=#808080}*Why am I even trying.... also...*{/color}"
    MC "{color=#808080}*Why am I thinking all this, she can hear my thoughts anyway?!*{/color}"
    MC "Just -GHHHHHH- let go of me already!!"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene161 with Dissolve(0.5)
    Mhyrorin "Geez, why so snappy?"
    Mhyrorin "Don't tell me you didn't like it!"
    Mhyrorin "You can't hide any feelings from me!"
    scene IntroScene162 with Dissolve(0.5)
    Mhyrorin "Now that I'm done with the appetizer."
    Mhyrorin "Let me enjoy my entrée!"
    MC "Wait, are you going to suck my dick?!"
    scene IntroScene163 with Dissolve(0.5)
    Mhyrorin "Of course I'm going to suck your dick, you dumbass."
    scene IntroScene164 with Dissolve(0.5)
    MC "Wait!!! Can I... uhhhh... go take a shower first?"
    MC "I didn't shower like all day!"
    scene IntroScene163 with Dissolve(0.5)
    Mhyrorin "Like I'd give a fuck about that."
    Mhyrorin "You better not disappoint me, [MC]."
    Mhyrorin "It would really be a shame!"
    scene IntroScene165 with Dissolve(0.5)
    Mhyrorin "........."
    Mhyrorin "Huh......??"
    scene IntroScene166 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Wait a fucking second....*{/color}"
    Mhyrorin "{color=#808080}*What the fuck is this?!*{/color}"
    Mhyrorin "{color=#808080}*I didn't expect this!*{/color}"
    Mhyrorin "{color=#808080}*What is with this horse cock next to my face?!*{/color}"
    Mhyrorin "{color=#808080}*I set my expectations pretty low but this goes beyond my wildest hopes!!*{/color}"
    Mhyrorin "{color=#808080}*I can't touch this!! It will break me!*{/color}"
    Mhyrorin "{color=#808080}*Fuck, fuck, fuck, what do I do?!*{/color}"
    scene IntroScene168 with Dissolve(0.5)
    Mhyrorin "Uhhhh, you know what? Maybe you were right."
    Mhyrorin "You should go take a shower!"
    Mhyrorin "Better yet, I think it's better if I come some other day, don't you think so?"
    Mhyrorin "It was all just a big misunderstanding, haha!"
    Mhyrorin "I'm gonna leave now, bye, bye!"
    scene IntroScene169 with Dissolve(0.5)
    Mhyrorin "Wait, wait, wait! Not by the horns! They are really sensitive!!"
    Mhyrorin "Okay, okay, I won't leave, just let go of them!"
    scene IntroScene170 with Dissolve(0.5)
    MC "Stop acting like you are the victim here."
    MC "You can break my wrist whenever you want with your strength and speed."
    MC "But you just want it, don't you?!"
    Mhyrorin "{color=#808080}*Fuck, fuck, fuck, I'm in big trouble.*{/color}"
    Mhyrorin "{color=#808080}*From the moment he pulled out that thing my body won't listen to me!*{/color}"
    Mhyrorin "{color=#808080}*It just moves according to what he wants!*{/color}"
    scene IntroScene171 with Dissolve(0.5)
    Mhyrorin "Wait! Let's talk things over!"
    Mhyrorin "That thing couldn't fit in my mouth anyway!"
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo10", "IntroVideo11", "IntroVideo12", "IntroVideo13"])
    Mhyrorin "{color=#808080}*Uhhhh... It's touching my face...*{/color}"
    Mhyrorin "{color=#808080}*What is this feeling??*{/color}"
    Mhyrorin "{color=#808080}*I feel like I might faint just from that!*{/color}"
    MC "What happened to all the big talk, huh?!"
    MC "I'm sure we can make it fit."
    Mhyrorin "{color=#808080}*No way I'm going to get my mouth raped by this kid!*{/color}"
    Mhyrorin "{color=#808080}*What have I done?!*{/color}"
    MC "You got yourself into this, [Mhyrorin]!"
    MC "Now don't be so picky!"
    MC "Open wide!"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene172 with Dissolve(0.5)
    Mhyrorin "Please wait, you are going to break my jaw!"
    Mhyrorin "Let me go, please!"
    scene IntroScene173 with Dissolve(0.5)
    MC "You are free to go whenever you want, [Mhyrorin]!"
    MC "And you know that! I'm just guiding you!"
    MC "But you want it too, don't you?"
    scene IntroScene174 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*I'm pretty sure I don't want him to break my fucking jaw!*{/color}"
    Mhyrorin "{color=#808080}*But for some reason I can't oppose him.*{/color}"
    Mhyrorin "{color=#808080}*My whole body does whatever he wants!*{/color}"
    MC "Now don't make me repeat myself, [Mhyrorin]!"
    MC "Open wide!"
    Mhyrorin "{color=#808080}*Fuck!!!! I have no control over myself!*{/color}"
    Mhyrorin "{color=#808080}*I'm just obeying his orders against my will!!*{/color}"
    Mhyrorin "{color=#808080}*At this point I'll just become his mindless slut!*{/color}"
    scene IntroScene175 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Ughhhh!!!! Just do it already!*{/color}"
    Mhyrorin "{color=#808080}*I can't wait to taste it!!!*{/color}"
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo14", "IntroVideo15", "IntroVideo16", "IntroVideo17"])
    MC "Good job, slut!"
    MC "Do you mind if I call you slut? I feel like it fits you more now!"
    Mhyrorin "Aaaaaaaaaaaaaaa!" 
    MC "I'll take that as a no, slut!"
    MC "Now don't let me do all the work!"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene176 with Dissolve(0.5)
    MC "If you want it so much, do it yourself."
    Mhyrorin "........."
    MC "Come on now, are you going to stay like that all night?"
    Mhyrorin "{color=#808080}*No way I'm going to do this myself!!!*{/color}"
    Mhyrorin "........."
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo18", "IntroVideo19", "IntroVideo20", "IntroVideo21"])
    Mhyrorin "{color=#808080}*IT COULDN'T HAVE GONE ANY WORSE THAN THIS...*{/color}"
    Mhyrorin "{color=#808080}*But it tastes so good.....*{/color}"
    Mhyrorin "{color=#808080}*And his cock is so hard!*{/color}"
    Mhyrorin "{color=#808080}*I feel like it could break my teeth with every slap!*{/color}"
    Mhyrorin "{color=#808080}*I can't stop myself!!*{/color}"
    Mhyrorin "{color=#808080}*I have to snap myself out of it!*{/color}"
    Mhyrorin "{color=#808080}*........*{/color}"
    Mhyrorin "{color=#808080}*But at the same time... I don't want to!*{/color}"
    $ ShouldSeeSwitchSceneButton = False
    show IntroVideo22
    MC "We are done with the foreplay, slut!"
    MC "Weren't you so impatient to get your entrée?"
    MC "What are you waiting for?"
    MC "Sit up nice!"
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo23", "IntroVideo24", "IntroVideo25", "IntroVideo26"])
    MC "Juuuust like that!"
    MC "Good girl!"
    MC "I see that you kept your slutty face."
    MC "It suits you well, you look beautiful!"
    Mhyrorin "Fangk yuuu!"
    MC "And who gave you permission to stroke my dick like that?"
    MC "Aren't you getting a little cocky?!"
    MC "Or did you already become addicted?!"
    Mhyrorin "Ah'm thowwee, Ah cahnt thtop!"
    Mhyrorin "Pweathe, fowgive me!"
    MC "Now suck it, slut!"
    Mhyrorin "Pweathe, wet me goh!"
    MC "I don't understand what you're blabbering there."
    MC "Are you saying you can't wait anymore?"
    MC "Fine then!"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene177 with Dissolve(0.5)
    "{size=+30}{color=#FF0000}~CRACK~{/color}{/size}"
    MC "Ha, ha, you were right!"
    MC "Your jaw did break!"
    MC "But I bet it's fine, your super human speed and strength have to come with healing as well!"
    scene IntroScene179 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Fuck, he's right!*{/color}"
    Mhyrorin "{color=#808080}*It still fucking hurts though, but that's not my problem now...*{/color}"
    Mhyrorin "{color=#808080}*My problem at the moment is this monster!*{/color}"
    scene IntroScene178 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*I at least managed to fit the head!*{/color}"
    Mhyrorin "{color=#808080}*But it already filled my entire mouth!*{/color}"
    Mhyrorin "{color=#808080}*I'm so scared right now!*{/color}"
    Mhyrorin "{color=#808080}*But the taste!*{/color}"
    show IntroVideo27
    Mhyrorin "{color=#808080}*THE TASTE IS SO FUCKING GOOD!*{/color}"
    Mhyrorin "{color=#808080}*WHAT IS THIS?!?!?! THERE IS NO WAY IT'S THIS DELICIOUS!!*{/color}"
    Mhyrorin "{color=#808080}*THIS IS THE BEST THING I'VE EVER PUT IN MY MOUTH!!!*{/color}"
    MC "What are you doing, slut? It's time to move your head, not your hands!"
    scene IntroScene180 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Fuck, fuck, fuck, this is not good at all!!!*{/color}"
    Mhyrorin "{color=#808080}*If this bastard shoves it in I'm done!*{/color}"
    Mhyrorin "{color=#808080}*Just cum already!!!!*{/color}"
    scene IntroScene181 with Dissolve(0.5)
    MC "Enjoy your meal!!!"
    Mhyrorin "MMmmMMMmmmmmmM!!"
    MC "What's the problem, slut?"
    MC "Are you trying to tell me something?"
    show IntroVideo32
    Mhyrorin "MmmMMmmmMMMhHH MMMmmMmMMHHhhhh!!!!!"
    MC "Is your long awaited entrée that good? Enjoy it at it's fullness then!"
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo28", "IntroVideo31", "IntroVideo29", "IntroVideo30"])
    Mhyrorin "{color=#808080}*FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK, FUCK*{/color}"
    Mhyrorin "{color=#808080}*I CAN'T BELIEVE MY THROAT IS GETTING RAPED BY THIS BOY!!!*{/color}"
    Mhyrorin "{color=#808080}*I'M CUMMING JUST FROM SUCKING THIS DICK, THIS SHOULDN'T BE POSSIBLE!*{/color}"
    Mhyrorin "{color=#808080}*I FEEL HIM GOING DOWN MY THROAT!!!*{/color}"
    Mhyrorin "{color=#808080}*HE REACHES MY STOMACH!!!*{/color}"
    MC "How is it, [Mhyrorin], did I disappoint you?"
    MC "Was this what you were looking for?!"
    Mhyrorin "{color=#808080}*He's doing what he wants with me!*{/color}"
    Mhyrorin "{color=#808080}*And I feel my consciousness slowly fading away.*{/color}"
    Mhyrorin "{color=#808080}*If this keeps up any longer there will be no turning back!*{/color}"
    MC "Fuck... I'm getting close!"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene183 with Dissolve(0.5)
    Mhyrorin "Here it comes!!!"
    scene IntroScene182 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    scene IntroScene184 with Dissolve(0.5)
    MC "Drink it all, slut!"
    Mhyrorin "{color=#808080}*It's finally over, he filled my mouth and my stomach immediately.*{/color}"
    Mhyrorin "{color=#808080}*And on top of it all....*{/color}"
    scene IntroScene187 with Dissolve(0.5)
    Mhyrorin "Ith's delithiuth!!!!"
    scene IntroScene185 with Dissolve(0.5)
    MC "Ughhh, fuck!"
    scene IntroScene186 with Dissolve(0.5)
    MC "{color=#808080}*I feel like I'm getting a little dizzy...*{/color}"
    MC "{color=#808080}*Something is off...*{/color}"
    scene IntroScene189 with Dissolve(0.5)
    MC "{color=#808080}*It looks like she already passed out...*{/color}"
    MC "{color=#808080}*She is completely unconscious.*{/color}"
    scene IntroScene190 with Dissolve(0.5)
    MC "{color=#808080}*Her throat was amazing!*{/color}"
    MC "{color=#808080}*I can't believe my first ever blowjob was with her!*{/color}"
    scene IntroScene191 with Dissolve(0.5)
    MC "{color=#808080}*Maybe I can fuck her now that she's out!*{/color}"
    scene IntroScene188 with Dissolve(0.5)
    MC "{color=#808080}*I just gotta...*{/color}"
    scene IntroScene192 with Dissolve(0.5)
    MC "{color=#808080}*I just gotta- I gotta get up....*{/color}"
    scene IntroScene188 with Dissolve(0.5)
    MC "{color=#808080}*My body doesn't want to move...*{/color}"
    MC "{color=#808080}*Did she do something to me?*{/color}"
    scene IntroScene193 with Dissolve(0.5)
    MC "{color=#808080}*I'm feeling so tired...*{/color}"
    MC "Fuck...."
    scene BlackScreen with Dissolve(3)
    "{color=#808080}**The morning next day.**{/color}"
    scene IntroScene194 with Dissolve(3)
    $ renpy.pause(0.5, hard=True)
    scene IntroScene195 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    scene IntroScene196 with Dissolve(0.5)
    MC "...."
    MC "{color=#808080}*My head hurts like hell...*{/color}"
    scene IntroScene197 with Dissolve(0.5)
    MC "{color=#808080}*So in the end it was just a dream...*{/color}"
    scene IntroScene198 with Dissolve(0.5)
    MC "{color=#808080}*I gotta stop eating right before I go to sleep...*{/color}"
    MC "{color=#808080}*That dream was really something else...*{/color}"
    Mhyrorin "Good morning, sunshine!"
    show IntroVideo33
    Mhyrorin "By the way, it wasn't a dream!"
    MC "Ughhh.... great..."
    MC "Now I'm for sure dead..."
    scene IntroScene200 with Dissolve(0.5)
    Mhyrorin "Yeah, you better wish you were dead!"
    Mhyrorin "What the fuck was that last night?!"
    Mhyrorin "Are you completely insane?"
    scene IntroScene201 with Dissolve(0.5)
    MC "I'm sorry, okay?"
    MC "I'm usually not this bold!"
    MC "And it was also my first time, so don't be mad at me...."
    MC "I only know what to do from porn!"
    scene IntroScene202 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Ughhhh...*{/color}"
    Mhyrorin "{color=#808080}*Of course this virgin learned it from porn...*{/color}"
    Mhyrorin "{color=#808080}*I can't believe I let this loser fuck the shit out of my mouth*{/color}"
    scene IntroScene203 with Dissolve(0.5)
    Mhyrorin "You managed to fuck it all up!"
    Mhyrorin "I hope you're glad!"
    scene IntroScene204 with Dissolve(0.5)
    MC "Wait, what do you mean? What did I do?!"
    scene IntroScene203 with Dissolve(0.5)
    Mhyrorin "There is a ritual, a whole process, and you fucked it up!"
    scene IntroScene204 with Dissolve(0.5)
    MC "Wait a second, go easy on me."
    MC "First of all... what the hell are you?"
    scene IntroScene205 with Dissolve(0.5)
    Mhyrorin "What do you mean, what am I?"
    Mhyrorin "I'm a cute, innocent girl that you raped last night."
    Mhyrorin "So be ready for the cops to show up at your front door soon!"
    scene IntroScene206 with Dissolve(0.5)
    MC "Cut the bullshit, [Mhyrorin]..."
    MC "No cute, innocent girl has that monstrous power and speed that you have..."
    MC "And should I even mention the two big ass horns on your head?"
    MC "So what are you? A vampire of some kind?"
    scene IntroScene207 with Dissolve(0.5)
    Mhyrorin "Hey, don't compare me to those lowly creatures!"
    Mhyrorin "We are nothing like those disgusting worms."
    Mhyrorin "As a succubus, I am a creature woven from the threads of shadow and desire, a being that dances on the edge of dreams and reality."
    Mhyrorin "My essence is one of seduction, not merely of the flesh, but of the soul."
    Mhyrorin "Drawing forth the hidden yearnings that lie buried within the hearts of mortals."
    Mhyrorin "We are masters of manipulation, weaving illusions as easily as one breathes, to ensnare the senses and captivate the mind."
    Mhyrorin "A succubus, an embodiment of desires unfettered, a creature of both darkness and light."
    scene IntroScene208 with Dissolve(0.5)
    MC "So.... uhhhhhh...."
    MC "Kinda like a vampire..."
    scene IntroScene209 with Dissolve(0.5)
    Mhyrorin "Ughhhh...."
    Mhyrorin "Vampires bite your neck and drink your blood!"
    Mhyrorin "We suck your dick and drink your cum!"
    Mhyrorin "Do you understand if I put it like that?"
    scene IntroScene210 with Dissolve(0.5)
    MC "Uhhh... yeah, it's a lot clearer like that!"
    scene IntroScene211 with Dissolve(0.5)
    Mhyrorin "We also might suck your life essence and your soul..."
    Mhyrorin "But that's beside the point!"
    Mhyrorin "Let's not get lost in small details."
    scene IntroScene212 with Dissolve(0.5)
    MC "Ummmmm, excuse me?"
    MC "What do you mean by sucking my soul?"
    scene IntroScene213 with Dissolve(0.5)
    Mhyrorin "We suck a little bit of your soul, okay?"
    Mhyrorin "It's not that big of a deal!"
    scene IntroScene214 with Dissolve(0.5)
    Mhyrorin "Okay, maybe not a little..."
    scene IntroScene215 with Dissolve(0.5)
    Mhyrorin "But who cares about that, right?"
    scene IntroScene216 with Dissolve(0.5)
    Mhyrorin "And you managed to fuck it all up!"
    Mhyrorin "Hope you are fucking happy!"
    scene IntroScene217 with Dissolve(0.5)
    MC "Wait, what did I do?!"
    MC "I didn't know there even was something to fuck up."
    scene IntroScene218 with Dissolve(0.5)
    Mhyrorin "There is, dumbass..."
    Mhyrorin "There always is..."
    Mhyrorin "But this time it was only one thing!"
    scene IntroScene219 with Dissolve(0.5)
    Mhyrorin "And you managed to fuck it up!"
    Mhyrorin "Now I'm so screwed, I can't even show my face back home!"
    scene IntroScene220 with Dissolve(0.5)
    Mhyrorin "Can you please calm down a minute and tell me what's wrong?"
    Mhyrorin "Maybe we can fix it."
    scene IntroScene223 with Dissolve(0.5)
    Mhyrorin "There is nothing to fix now."
    Mhyrorin "It's a whole process that needs to be followed, once that's broken there is nothing you can do."
    scene IntroScene222 with Dissolve(0.5)
    MC "What process, can you just explain it to me from start to finish already?"
    MC "I don't understand what you're trying to say."
    scene IntroScene223 with Dissolve(0.5)
    Mhyrorin "Okay, so I told you what a succubus is, right?"
    Mhyrorin "What we do is find victims like you, lonely, horny, pathetic, depressing losers."
    scene IntroScene224 with Dissolve(0.5)
    MC "Okay, geez, you don't gotta say it like that..."
    scene IntroScene225 with Dissolve(0.5)
    Mhyrorin "First, we have to seduce them."
    Mhyrorin "We can't just rape them, you have to make them desire and lust for you."
    Mhyrorin "That part was pretty easy."
    scene IntroScene224 with Dissolve(0.5)
    MC "You don't have to be so mean, you know? I had some pent up horniness."
    scene IntroScene226 with Dissolve(0.5)
    Mhyrorin "Then, you have to make them cum for you."
    Mhyrorin "You can suck them, fuck them, jerk them off, hands, feet, tits, some people prefer armpits, anything works."
    scene IntroScene227 with Dissolve(0.5)
    Mhyrorin "And then you consume their cum, and a part of their life essence, their soul."
    Mhyrorin "With that, your powers as a succubus grow and your hunger calms down."
    Mhyrorin "If the human manages to survive it, they become our slaves and live stock until we squeeze every last bit of soul within them."
    Mhyrorin "Tree easy steps, and you managed to fuck it up!"
    scene IntroScene228 with Dissolve(0.5)
    MC "Wait... but that sounds like part of the course..."
    MC "It pretty much happened just like that."
    MC "So what's the problem?"
    scene IntroScene229 with Dissolve(0.5)
    Mhyrorin "UGHHHHHHH!!!"
    Mhyrorin "THE PROBLEM IS THAT I CAME FIRST, OKAY?"
    Mhyrorin "THAT'S THE FUCKING PROBLEM!"
    scene IntroScene228 with Dissolve(0.5)
    MC "And how does that change things?"
    MC "Are you not allowed to do so?"
    scene IntroScene229 with Dissolve(0.5)
    Mhyrorin "I am!"
    Mhyrorin "But not before you do!"
    scene IntroScene228 with Dissolve(0.5)
    MC "Is that so bad? You seem pretty fine to me..."
    scene IntroScene230 with Dissolve(0.5)
    Mhyrorin "Yeah, it's extremely fucking bad!"
    Mhyrorin "By doing that, the roles are reversed!"
    Mhyrorin "I become...."
    Mhyrorin "Your slave...."
    scene IntroScene231 with Dissolve(0.5)
    MC "Wait, what?!"
    MC "So, you are my slave now?!"
    scene IntroScene232 with Dissolve(0.5)
    Mhyrorin "Yeah.... I'm your slave now...."
    scene IntroScene233 with Dissolve(0.5)
    MC "So now you will call me master?"
    scene IntroScene236 with Dissolve(0.5)
    Mhyrorin "Fuck no!"
    scene IntroScene237 with Dissolve(0.5)
    MC "Ehh..."
    MC "I mean... even with that, what's the problem?"
    MC "It's not like I can force you to do anything."
    MC "You are way stronger than me, you could kill me any time you want..."
    MC "Wait...."
    scene IntroScene238 with Dissolve(0.5)
    MC "That's not why you're here, right?"
    MC "Uhhhh, please don't kill me."
    MC "I won't make you do anything, you can live freely as you want."
    scene IntroScene239 with Dissolve(0.5)
    Mhyrorin "Ughhh, stop crying kid, I'm not going to kill you."
    Mhyrorin "To be more exact, I CAN'T kill you, I'm not allowed."
    scene IntroScene236 with Dissolve(0.5)
    Mhyrorin "Once you shoved your cock into my mouth and I came, we made a pact."
    Mhyrorin "And as your slave I'm not allowed to harm you in any way."
    Mhyrorin "Even worse... I have to protect you."
    Mhyrorin "We are linked now, you die, I die..."
    scene IntroScene237 with Dissolve(0.5)
    MC "So you really are my slave..."
    scene IntroScene240 with Dissolve(0.5)
    MC "That's awesome!!"
    MC "That means I can do whatever I want with you?"
    scene IntroScene239 with Dissolve(0.5)
    Mhyrorin "Kinda... yeah..."
    scene IntroScene240 with Dissolve(0.5)
    MC "Then suck my dick again!"
    scene IntroScene241 with Dissolve(0.5)
    Mhyrorin "Don't try your luck with me, kiddo!"
    Mhyrorin "I have ways to fuck you up without hurting you."
    scene IntroScene242 with Dissolve(0.5)
    MC "Ehhh.... it was worth a try..."
    MC "But you said I can make you do anything I want."
    scene IntroScene241 with Dissolve(0.5)
    Mhyrorin "I said kinda."
    Mhyrorin "If the roles were reversed, I could've told you to jump off of a bridge and die and you would do it."
    Mhyrorin "But as we are now, you can't make me do everything."
    Mhyrorin "Only small things that I wouldn't care about anyway."
    Mhyrorin "That's if things stay as they are now..."
    scene IntroScene242 with Dissolve(0.5)
    MC "Wait, so there are ways to make you completely submit to me?"
    MC "What are they?"
    scene IntroScene241 with Dissolve(0.5)
    Mhyrorin "I'm not gonna tell you? The fuck!?"
    Mhyrorin "I'm not interested in becoming your submissive slave!"
    scene IntroScene242 with Dissolve(0.5)
    MC "But you can do some small things, can't you?"
    MC "Hmmm... shake your tits for me."
    scene IntroScene243 with Dissolve(0.5)
    Mhyrorin "What the fuck kind of request is that?"
    Mhyrorin "I'm not going to do something that degrading."
    scene IntroScene245 with Dissolve(0.5)
    Mhyrorin "UGHHHHHHH!!!"
    Mhyrorin "{color=#808080}*My head feels like it's going to burst open!*{/color}"
    Mhyrorin "{color=#808080}*I can't believe he is powerful enough to make me do this shit!*{/color}"
    scene IntroScene244 with Dissolve(0.5)
    Mhyrorin "Fine, I'll do it!!"
    Mhyrorin "But just so you know, I'm not your sex toy, okay?!"
    scene IntroScene246 with Dissolve(0.5)
    MC "{color=#808080}*We'll see about that...*{/color}"
    scene IntroScene244 with Dissolve(0.5)
    Mhyrorin "I can read your thoughts, dumbass!!"
    scene IntroScene246 with Dissolve(0.5)
    MC "{color=#808080}*Shit, I forgot she can do that!*{/color}"
    scene IntroScene244 with Dissolve(0.5)
    Mhyrorin "Well, don't forget again!"
    scene IntroScene246 with Dissolve(0.5)
    MC "Okay, geez, you were the one trying to make me a slave in the first place!"
    MC "So don't get angry at me now that the roles are reversed!"
    MC "Either way, I'm going to have lots of fun with you!"
    scene IntroScene236 with Dissolve(0.5)
    Mhyrorin "Okay, so what did you say you want?"
    scene IntroScene237 with Dissolve(0.5)
    MC "Come closer, hands behind your head and shake your tits for me."
    scene IntroScene236 with Dissolve(0.5)
    Mhyrorin "Oh, yeah, that stupid shit..."
    Mhyrorin "I think I'll just let my head explode.."
    scene IntroScene237 with Dissolve(0.5)
    MC "Suit yourself."
    Mhyrorin ".........."
    scene IntroScene239 with Dissolve(0.5)
    Mhyrorin "Ughhhhh!!"
    Mhyrorin "Fine!"
    scene IntroScene248 with Dissolve(0.5)
    Mhyrorin "Like this?!"
    scene IntroScene249 with Dissolve(0.5)
    MC "Yeah, now shake 'em!"
    scene IntroScene250 with Dissolve(0.5)
    Mhyrorin "God, I feel so stupid..."
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["IntroVideo34", "IntroVideo35", "IntroVideo36", "IntroVideo37"])
    Mhyrorin "Jesus Christ, kid, you don't gotta stare at them like that."
    Mhyrorin "Have you never seen a pair of tits in your life?"
    MC "No... but either way, they are amazing!"
    MC "They are way better than all I've seen in any porn."
    Mhyrorin "Th.. thanks..."
    MC "No need to thank me! I could watch them all day, every day."
    MC "So get used to doing that more often!"
    Mhyrorin "....ughhh...."
    Mhyrorin "Okay, but don't forget I do this because I have no choice!"
    MC "Hmmm, you become pretty submissive if handled well."
    Mhyrorin "Fuck you..."
    MC "Sooo, can I touch them?"
    $ ShouldSeeSwitchSceneButton = False
    scene IntroScene252 with Dissolve(0.5)
    Mhyrorin "No, you can't!"
    scene IntroScene253 with Dissolve(0.5)
    Mhyrorin "........"
    scene IntroScene254 with Dissolve(0.5)
    Mhyrorin "Haha, you are not powerful enough to make me do it!"
    Mhyrorin "Fuck you!"
    scene IntroScene255 with Dissolve(0.5)
    MC "Fuck you!"
    MC "You don't seem to be in any position to make fun of me."
    MC "Look at you, already all sweaty!"
    scene IntroScene256 with Dissolve(0.5)
    Mhyrorin "Don't laugh at me about that, ok? I got made fun of because of it."
    Mhyrorin "I try to excise a lot to get rid of it, but it's just how I am."
    scene IntroScene257 with Dissolve(0.5)
    MC "It's okay, you look really hot all sweaty and wet."
    MC "You don't gotta be ashamed of it."
    scene IntroScene258 with Dissolve(0.5)
    Mhyrorin "...."
    scene IntroScene259 with Dissolve(0.5)
    Mhyrorin "T-Thank you..."
    scene IntroScene258 with Dissolve(0.5)
    MC "See, I told you, you get submissive really quick!"
    scene IntroScene259 with Dissolve(0.5)
    Mhyrorin "Fuck off..."
    scene IntroScene258 with Dissolve(0.5)
    MC "Sooo... are you going to stay here all day?"
    scene IntroScene262 with Dissolve(0.5)
    MC "I hope you can turn yourself invisible or something like that 'cause my family doesn't give a fuck about knocking when it comes to my room."
    MC "I need to go have breakfast soon, my mom might come in at any moment to call me."
    scene IntroScene261 with Dissolve(0.5)
    Mhyrorin "No, I also, have to go, I have to make a stupid report of this whole situation..."
    Mhyrorin "I just got a few more things to tell you. Actually, this is the reason why I came here."
    Mhyrorin "You want to fuck your family, don't you?"
    scene IntroScene263 with Dissolve(0.5)
    MC "..................................................................."
    scene IntroScene264 with Dissolve(0.5)
    MC "Haha, what is this sick joke?"
    MC "Of course I don't!"
    MC "That's disgusting!"
    MC "They all look great and all, but I only see them as my loving mother and sisters!"
    MC "I could never look at them in a sexual way... or uhhhmm.. uhmmm.. anything like that!"
    scene IntroScene265 with Dissolve(0.5)
    Mhyrorin "Yaaapa, yaaapa, shuuuut the fuck up, kid."
    Mhyrorin "They are all really hot."
    Mhyrorin "If I were you, I'd want to fuck the shit out of all of them!"
    scene IntroScene261 with Dissolve(0.5)
    Mhyrorin "To be honest, I'd fuck the shit out of them either way!"
    Mhyrorin "Why do you think I came to you in the first place?"
    Mhyrorin "I told you, you can't hide any feelings from me, it's part of the succubus powers or however you want to call them."
    Mhyrorin "So, don't lie to me about it."
    scene IntroScene266 with Dissolve(0.5)
    Mhyrorin "And to be honest, I think that it's pretty hot!"
    Mhyrorin "So I'd like to help you with that."
    scene IntroScene267 with Dissolve(0.5)
    MC "Ughhh, you're right, they are hot as fuck..."
    MC "Sooo... what's in for you? You don't seem like the type of person... type of succubus to do charity."
    scene IntroScene268 with Dissolve(0.5)
    Mhyrorin "Whaaaaaaaat? What do you mean by that?"
    Mhyrorin "That doesn't sound like me at all."
    Mhyrorin "Can't I just do something nice for my-"
    scene IntroScene269 with Dissolve(0.5)
    Mhyrorin "Master..."
    scene IntroScene270 with Dissolve(0.5)
    MC "Haha, you are sooo funny!"
    MC "But I do like the sound of that."
    scene IntroScene269 with Dissolve(0.5)
    Mhyrorin "Yeah, don't get used to it!"
    scene IntroScene271 with Dissolve(0.5)
    Mhyrorin "Okay, so I'll keep it short and clear, so shut the fuck up and listen!"
    Mhyrorin "First, I don't need you to fuck your family in particular, I only said that because I find it really hot."
    Mhyrorin "I want to help you fuck as many women as possible!"
    scene IntroScene272 with Dissolve(0.5)
    Mhyrorin "Second, the way we'll make that happen is-"
    scene IntroScene273 with Dissolve(0.5)
    Mhyrorin "........."
    scene IntroScene274 with Dissolve(0.5)
    Mhyrorin "Could you stop staring at my tits for a single fucking second and listen to me?!"
    Mhyrorin "If you're not paying attention, I'll just leave!"
    scene IntroScene276 with Dissolve(0.5)
    MC "I'm sorry, it's just that... they are so... beautiful and big..."
    MC "It's really hard to take my eyes off of them!"
    scene IntroScene277 with Dissolve(0.5)
    Mhyrorin "......."
    Mhyrorin "{color=#808080}*God, I hate him so much!*{/color}"
    scene IntroScene278 with Dissolve(0.5)
    Mhyrorin "Thank you, it's okay, but now listen to me, alright?!"
    scene IntroScene279 with Dissolve(0.5)
    Mhyrorin "Okay, so second."
    Mhyrorin "Now that we forged a pact when you made me cum and then filled up my stomach."
    Mhyrorin "You gained certain powers."
    Mhyrorin "Powers that will help you seduce, corrupt and enslave whatever girl you want!"
    Mhyrorin "But It's not like you can just pull your cock out and fuck them."
    scene IntroScene280 with Dissolve(0.5)
    Mhyrorin "So then to my third point."
    Mhyrorin "You have to act as your usual self."
    Mhyrorin "Little acts of affection coupled with little acts of perversion."
    Mhyrorin "Little by little, nothing to harsh or they'll start resenting or even hating you!"
    Mhyrorin "But that only gets you so far."
    scene IntroScene281 with Dissolve(0.5)
    Mhyrorin "So, fourth!"
    Mhyrorin "Ughh... how should I put it so you could understand..."
    Mhyrorin "You can view it as a game, you stack up points on the love meter, corruption meter, submission meter and exhibitionism meter."
    Mhyrorin "Once you stack up enough points, you have to trigger them with your cum."
    Mhyrorin "Because now that we are linked, your cum has certain effects on women."
    Mhyrorin "For now, let's just say it pushes their true self out. It's not mind control or anything like that, it's just revealing their true desire."
    Mhyrorin "So putting it in their drinks or food should be good enough for starters."
    Mhyrorin "And that's how that works!"
    scene IntroScene282 with Dissolve(0.5)
    Mhyrorin "And now to my fifth and final point."
    Mhyrorin "What do I get from all of this."
    Mhyrorin "From now on, every time a woman grows attracted to you my powers grow..."
    Mhyrorin "Every \"love meter\" and so on that you fill up empowers me."
    Mhyrorin "And what will truly spike my growth even faster will be that every time you cum in a woman I will ta- "
    scene IntroScene283 with Dissolve(0.5)
    MC "Including you?"
    Mhyrorin "...."
    scene IntroScene284 with Dissolve(0.5)
    Mhyrorin "Ughhhhh...."
    Mhyrorin "Yeah.... including me...."
    Mhyrorin "Actually... especially me...."
    scene IntroScene285 with Dissolve(0.5)
    Mhyrorin "But that's not going to happen, so forget about it!"
    scene IntroScene267 with Dissolve(0.5)
    MC "Yeah... whatever you say."
    scene IntroScene285 with Dissolve(0.5)
    Mhyrorin "I'm serious!!!"
    scene IntroScene282 with Dissolve(0.5)
    Mhyrorin "Anyway! Every time you will cum in or on a woman, I will take a bit of your soul or life energy or whatever you wanna call it."
    Mhyrorin "So don't cum too ofter because you're going to end up dead."
    Mhyrorin "But don't worry too much, as you get more powerful you'll be able to do it more often."
    Mhyrorin "Plus, now that I'm your slave, if you die, I die, and I'm not really a fan of dying!"
    Mhyrorin "So be very careful!"
    scene IntroScene286 with Dissolve(0.5)
    Mhyrorin "So that's all for now."
    Mhyrorin "Any questions?"
    scene IntroScene270 with Dissolve(0.5)
    MC "Uhhhh... yeah... I have a few..."
    MC "First of-"
    scene IntroScene288 with Dissolve(0.5)
    Mhyrorin "Uhhh... about that..."
    Mhyrorin "I don't actually have time for any questions right now."
    Mhyrorin "Yeah... sorry about that..."
    scene IntroScene289 with Dissolve(0.5)
    Mhyrorin "But you can call me any time you want as long as you are in this room and I'll be here in an instant."
    Mhyrorin "Because that's how much I love and care about you and not because I ended up as your fucking slave and my head would explode if I wouldn't."
    scene IntroScene290 with Dissolve(0.5)
    Mhyrorin "Soo... don't forget what I told you and get to work!"
    Mhyrorin "Aaaand yeah... see you later, byeeee!"
    MC "Bye b-"
    scene BlackScreen with Dissolve(0.1)
    $ renpy.pause(0.1, hard=True)
    scene IntroScene291 with Dissolve(0.5)
    MC "Jesus Christ, she's so fast, I always forget..."
    scene IntroScene292 with Dissolve(0.5)
    MC "So...."
    MC "Last night I got my dick sucked for the first time by a succubus..."
    MC "She became my slave..."
    MC "And now she will help me fuck my mom and my sisters and pretty much every girl I want..."
    MC "Like that will ever happen..."
    MC "In any case, I will try I guess... It's not like that's not what I was doing until now..."
    MC "Plus, she doesn't seem like the type to lie.. or maybe it's because she's my slave and can't lie to me..."
    MC "Either way, I will do as she says for now, it's not like I got anything to lose..."
    Jennifer "[MC_upper]!!!!!"
    Jennifer "DON'T TELL ME YOU ARE STILL SLEEPING!!"
    Jennifer "COME DOWN TO EAT ALREADY!!!"
    MC "Well... there's my signal... I should go eat now..."
    scene IntroScene293 with Dissolve(0.5)
    MC "I should get dressed first."
    scene IntroScene294 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*Thank god.. it seems like he's going to play along...*{/color}"
    Mhyrorin "{color=#808080}*I'm in so much fucking trouble... I fucked up big time!*{/color}"
    scene IntroScene295 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*I hope they at least won't kill me...*{/color}"
    scene IntroScene296 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*At least I got him, and he seems really promising.*{/color}"
    scene IntroScene297 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*If there is anyone that could eventually get me out of all of this it's him.*{/color}"
    scene IntroScene298 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*For now, I got to be careful and keep him hidden at any cost.*{/color}"
    scene IntroScene299 with Dissolve(0.5)
    Mhyrorin "{color=#808080}*The rest is in his hands.*{/color}"
    scene BlackScreen with Dissolve(0.1)
    $ renpy.pause(0.1, hard=True)
    scene IntroScene300 with Dissolve(0.5)
    Jennifer "ARE YOU COMING ALREADY?!?!!?!"
    MC "I WAS GETTING DRESSED, I'LL BE THERE IN LIKE 10 SECONDS!!!"
    $ calendar.Day = 1
    $ calendar.Hours = 3
    $ Location = "Hallway"
    jump GameLoop

label skipintro:
    $ calendar.Hours = 3
    $ Location = "Hallway"
    jump GameLoop
