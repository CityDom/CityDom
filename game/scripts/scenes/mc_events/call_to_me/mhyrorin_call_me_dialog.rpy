label MhyrorinCallToMeDialog:

    MC "[Mhyrorin], are you here?"
    if str(Location).lower() == "my room":
        if 0 <= calendar.Hours < 12:
            MC "[Mhyrorin], are you here?"
            MC "She should be coming from the window."
            MC "......"
            MC "I never know if I should be yelling or she hears me anyway..."
            scene MhyrorinScene1 with Dissolve(0.5)
            MC "Ummmm, [Mhyrorin]?"
            scene MhyrorinScene2 with Dissolve(0.5)
            MC "......"
            MC "Doesn't seem like she's here..."
            scene MhyrorinScene3 with Dissolve(0.5)
            Mhyrorin "Have you called me, loser?"
            scene MhyrorinScene4 with Dissolve(0.5)
            Mhyrorin "What are we looking at?"
            Mhyrorin "Something at the window?"
            scene MhyrorinScene5 with Dissolve(0.5)
            MC "Jesus Christ, [Mhyrorin], you sca-"
            scene BlackScreen with Dissolve(0.05)
            $ renpy.pause(0.01, hard=True)
            scene MhyrorinScene6 with Dissolve(0.5)
            MC "What the..."
            Mhyrorin "You look like you've seen a ghost kid, are you ok?"
            scene MhyrorinScene7 with Dissolve(0.5)
            MC "Can you stop scaring me like that? For fuck's sake, I'm gonna have a heart attack one of these days."
            scene MhyrorinScene8 with Dissolve(0.5)
            Mhyrorin "Stop being a bitch already."
            Mhyrorin "You've put me through a shit ton of problems so I don't have a lot of time."
            Mhyrorin "So do you want to ask me something or are you going to make me do some degrading shit again?"
            scene MhyrorinScene9 with Dissolve(0.5)
            label AskOrShakeMhyrorin:
                menu:
                    "Ask her something":
                        MC "I wanted to ask you something."
                        scene MhyrorinScene10 with Dissolve(0.5)
                        Mhyrorin "Really?"
                        Mhyrorin "Okay, but make it short... at least I don't have to shake my tits again."
                        label MhyrorinQuestions:
                            scene MhyrorinScene11 with Dissolve(0.5)
                            menu:
                                "Are there more of you?":
                                    MC "Are there more succubuses?"
                                    scene MhyrorinScene12 with Dissolve(0.5)
                                    Mhyrorin "Yeah, quite a few, even though our numbers have been thinning nowadays."
                                    Mhyrorin "But our city is not really in this realm..."
                                    Mhyrorin "Ughh.. it's hard to explain... but yeah, there are quite a lot of us."
                                    Mhyrorin "Anything else?"
                                    jump MhyrorinQuestions
                                "In what trouble did I put you?":
                                    MC "Why are you always saying that I caused you a lot of trouble?"
                                    MC "Is something bad about to happen?"
                                    scene MhyrorinScene12 with Dissolve(0.5)
                                    Mhyrorin "Something bad already happened."
                                    Mhyrorin "Me becoming your slave is not really in the agenda of a succubus."
                                    Mhyrorin "Especially not one of my ranking."
                                    Mhyrorin "And even though my ranking is not really high, I still have some bosses and people to answer to."
                                    Mhyrorin "And if they catch on to what really happened here, I'll be in big trouble, but you should be safe, so don't worry about it."
                                    Mhyrorin "Any other question?"
                                    jump MhyrorinQuestions
                                "Girls progress":
                                    MC "You said that I should think of it as a game with love meters and so on..."
                                    MC "But how should I know when a counter is filled?"
                                    scene MhyrorinScene12 with Dissolve(0.5)
                                    Mhyrorin "I messed around with your phone a little bit when you were sleeping..."
                                    scene MhyrorinScene13 with Dissolve(0.5)
                                    MC "Wait, you did what?"
                                    scene MhyrorinScene10 with Dissolve(0.5)
                                    Mhyrorin "Hehe, you think I don't know my way around phones? I'm not that old!"
                                    Mhyrorin "And I'm quite a programmer myself, yeah, I know, I don't look like the nerdy programmer type."
                                    Mhyrorin "So yeah, you should see an app in your phone that keeps track of all that stuff, so you shouldn't worry about that."
                                    Mhyrorin "Any other questions?"
                                    jump MhyrorinQuestions
                                "Girls breakthrough":
                                    MC "You said something about filling the counters will only get me so far, what should I do when that happens?"
                                    scene MhyrorinScene12 with Dissolve(0.5)
                                    Mhyrorin "You have a short memory, don't you?"
                                    Mhyrorin "When you get the chance, you have to feed them your cum, but don't risk it."
                                    Mhyrorin "If you stick it in their mouth when they sleep and catch you, you are fucked."
                                    Mhyrorin "Try to put it in their drinks or food when you get the chance."
                                    Mhyrorin "Anything else you forgot about?"
                                    jump MhyrorinQuestions
                                "Anything else I should know?":
                                    MC "Are there any more things that I should know and that you didn't have the time to tell me yet?"
                                    scene MhyrorinScene14 with Dissolve(0.5)
                                    Mhyrorin "Well... there is one thing..."
                                    Mhyrorin "And it's actually really bad..."
                                    scene MhyrorinScene15 with Dissolve(0.5)
                                    MC "Wait what?!"
                                    MC "What is it? Tell me!"
                                    scene MhyrorinScene14 with Dissolve(0.5)
                                    Mhyrorin "Well, you see..."
                                    Mhyrorin "I have an incurrable succubus illness..."
                                    Mhyrorin "And when you fucked my throat you caught it..."
                                    scene MhyrorinScene15 with Dissolve(0.5)
                                    MC "WHAT?!"
                                    MC "Why didn't you tell me till now?!?!?"
                                    MC "What will happen to me?!"
                                    scene MhyrorinScene14 with Dissolve(0.5)
                                    Mhyrorin "Well... no human caught it until now so I don't know for sure, but from what I've read, your dick is going to fall off."
                                    scene MhyrorinScene15 with Dissolve(0.5)
                                    MC "Haha, funny joke, [Mhyrorin], but ever since you became my slave, I can sense when you are lying to me."
                                    scene MhyrorinScene16 with Dissolve(0.5)
                                    Mhyrorin "Ughhhhh... for fuck's sake, I even put up with the headache just to make this joke."
                                    Mhyrorin "It's so not fun being a fucking slave."
                                    scene MhyrorinScene17 with Dissolve(0.5)
                                    Mhyrorin "If there is something worth telling you and that you should know about, I'll tell you without you asking."
                                    Mhyrorin "So don't worry about that."
                                    Mhyrorin "Are we done?"
                                    jump MhyrorinQuestions
                                "What do you think about me?":
                                    MC "Well... uhhh.. I wanted to ask you..."
                                    MC "What do you think about me?"
                                    scene MhyrorinScene18 with Dissolve(0.5)
                                    Mhyrorin "What do you mean? You are my beloved master!"
                                    Mhyrorin "And I am you lowly, good for nothing slave."
                                    scene MhyrorinScene19 with Dissolve(0.5)
                                    Mhyrorin "I would do anything for you!"
                                    Mhyrorin "I'm getting so hot just sitting next to you!"
                                    scene MhyrorinScene20 with Dissolve(0.5)
                                    Mhyrorin "Please, let this horny slut suck your cock, please master!!"
                                    Mhyrorin "I might die if I don't!!"
                                    scene MhyrorinScene22 with Dissolve(0.5)
                                    Mhyrorin "Is that what you want to hear? You virgin?"
                                    scene MhyrorinScene23 with Dissolve(0.5)
                                    MC "Fuck you!"
                                    scene MhyrorinScene22 with Dissolve(0.5)
                                    Mhyrorin "What? Did I get your hopes up?"
                                    scene MhyrorinScene24 with Dissolve(0.5)
                                    Mhyrorin "Oh, I see that I got your dick up..."
                                    Mhyrorin "Jesus Christ, your cock is huge, kid, that's beyond big."
                                    Mhyrorin "You should get that checked out."
                                    scene MhyrorinScene25 with Dissolve(0.5)
                                    MC "Ughhh, thank you, but I don't think it's any illness..."
                                    scene MhyrorinScene22 with Dissolve(0.5)
                                    Mhyrorin "Anyway..."
                                    scene MhyrorinScene12 with Dissolve(0.5)
                                    Mhyrorin "Anything else you want to ask me?"
                                    jump MhyrorinQuestions
                                "That's all":
                                    MC "That's all..."
                                    scene MhyrorinScene17 with Dissolve(0.5)
                                    Mhyrorin "Really? You made me come all the way here just for that?"
                                    Mhyrorin "Are you sure there isn't anything else? I don't want to come here again when your ass starts remembering stuff."
                                    jump AskOrShakeMhyrorin
                    "Make her degrade herself":
                        MC "The latter."
                        scene MhyrorinScene16 with Dissolve(0.5)
                        Mhyrorin "Ughhhh, of course... why did I expect anything else from you."
                        Mhyrorin "Come on now, tell me, I don't have all day."
                        scene MhyrorinScene13 with Dissolve(0.5)
                        label chooseDegradingOption:
                            menu:
                                "Shake your tits":
                                    MC "I want you to shake your tits for me."
                                    scene MhyrorinScene17 with Dissolve(0.5)
                                    Mhyrorin "For real? Again?"
                                    Mhyrorin "You will never get enough of them, won't you?"
                                    Mhyrorin "Okay, I guess..."
                                    $ ShouldSeeSwitchSceneButton = True
                                    $ play_video_sequence(["MhyrorinVideo1", "MhyrorinVideo2", "MhyrorinVideo3", "MhyrorinVideo4"])
                                    Mhyrorin "Is this okay?"
                                    MC "Are you trying to do a good job? How nice of you."
                                    MC "I'm glad you are this dedicated."
                                    Mhyrorin "I just don't want my head exploding if I somehow don't do what you want."
                                    Mhyrorin "God... how the fuck have I reached so low..."
                                    Mhyrorin "Have you jizzed your pants yet? I don't have all day!"
                                    MC "Yeah, that's enough, good girl!"
                                    $ ShouldSeeSwitchSceneButton = False
                                    scene MhyrorinScene28 with Dissolve(0.5)
                                    Mhyrorin "Fuck you! You're lucky I'm the slave here!"
                                    Mhyrorin "I would've made your life hell if it was the other way around."
                                    scene MhyrorinScene29 with Dissolve(0.5)
                                    MC "Then how do you expect me to treat you nicely?"
                                    scene MhyrorinScene30 with Dissolve(0.5)
                                    Mhyrorin "...."
                                    scene MhyrorinScene31 with Dissolve(0.5)
                                    Mhyrorin "Well... I guess you got a point..."
                                    scene MhyrorinScene32 with Dissolve(0.5)
                                    Mhyrorin "Anyway, I don't have time for chitchat, I have to go."
                                    Mhyrorin "Let me know if there is something important that I need to know."
                                    Mhyrorin "Not this stupid shit again!"
                                    Mhyrorin "So... see ya!"
                                    scene BlackScreen with Dissolve(0.05)
                                    $ renpy.pause(0.01, hard=True)
                                    scene MhyrorinScene33 with Dissolve(0.5)
                                    MC "Ughhh, I hate it so much when she does this shit."
                                    MC "It startles me every time."
                                    $ current_location = str(Location).lower()
                                    $ advance_time_or_sleep()
                                "Shake your ass":
                                    MC "I want you to twerk for me."
                                    scene MhyrorinScene34 with Dissolve(0.5)
                                    Mhyrorin "What?"
                                    Mhyrorin "What the fuck is twerk?"
                                    scene MhyrorinScene35 with Dissolve(0.5)
                                    Mhyrorin "OOHHHHHH!!"
                                    Mhyrorin "Wait, is that when you shake your ass?"
                                    Mhyrorin "....."
                                    scene MhyrorinScene36 with Dissolve(0.5)
                                    Mhyrorin "Ughhh, and I bet you can force me to do it..."
                                    Mhyrorin "I can't be fucked to even try to resist it, since you can make me shake my tits you can make me shake my ass as well..."
                                    scene MhyrorinScene68 with Dissolve(0.5)
                                    Mhyrorin "Like this?"
                                    scene MhyrorinScene69 with Dissolve(0.5)
                                    MC "Uhhh... yeah, yeah..."
                                    scene MhyrorinScene70 with Dissolve(0.5)
                                    MC "Or.... Can you do it with your hands behind your head?"
                                    scene MhyrorinScene71 with Dissolve(0.5)
                                    Mhyrorin "Tsk..."
                                    scene MhyrorinScene72 with Dissolve(0.5)
                                    Mhyrorin "Happy, now, asshole?"
                                    scene MhyrorinScene73 with Dissolve(0.5)
                                    MC "Yep, yep, super happy, you can go ahead!"
                                    scene MhyrorinScene74 with Dissolve(0.5)
                                    Mhyrorin "Ughhh..."
                                    window hide
                                    $ ShouldSeeSwitchSceneButton = True
                                    $ play_video_sequence(["MhyrorinVideo17", "MhyrorinVideo18", "MhyrorinVideo19", "MhyrorinVideo20"])
                                    pause
                                    $ ShouldSeeSwitchSceneButton = False
                                    show MhyrorinVideo21 with Dissolve(0.5)
                                    Mhyrorin "How long am I supposed to do this?"
                                    show MhyrorinVideo22 with Dissolve(0.5)
                                    MC "......"
                                    scene MhyrorinScene75 with Dissolve(0.5)
                                    Mhyrorin "Helloooooo!!"
                                    scene MhyrorinScene76 with Dissolve(0.5)
                                    Mhyrorin "What the fuck are you doing? I hope you're not beating your meat back there!"
                                    scene MhyrorinScene77 with Dissolve(0.5)
                                    Mhyrorin "Huh?"
                                    scene MhyrorinScene78 with Dissolve(0.5)
                                    Mhyrorin "Hallooo!! Are you there?"
                                    window hide
                                    scene MhyrorinScene79 with Dissolve(0.2)
                                    $ renpy.pause(0.2, hard=True)
                                    scene MhyrorinScene80 with Dissolve(0.2)
                                    $ renpy.pause(0.2, hard=True)
                                    scene MhyrorinScene79 with Dissolve(0.2)
                                    $ renpy.pause(0.2, hard=True)
                                    scene MhyrorinScene80 with Dissolve(0.2)
                                    $ renpy.pause(0.5, hard=True)
                                    scene MhyrorinScene81 with Dissolve(0.2)
                                    Mhyrorin "{color=#808080}*Ah, shit, I think I short circuit him.*"
                                    scene MhyrorinScene82 with Dissolve(0.2)
                                    Mhyrorin "Uhhhh... okay, if you don't need anything else, I will see my way out!"
                                    Mhyrorin "Bye byee!"
                                    window hide
                                    $ current_location = str(Location).lower()
                                    $ advance_time_or_sleep()
                                "Show me your mouth":
                                    MC "I want you to get on your knees and open your mouth."
                                    scene MhyrorinScene37 with Dissolve(0.5)
                                    Mhyrorin "You must be delusional, kid!"
                                    Mhyrorin "Uhhhh, I won't suck you off."
                                    Mhyrorin "And you are not strong enough to make me do it, so forget about it."
                                    scene MhyrorinScene38 with Dissolve(0.5)
                                    MC "I don't want you to suck me off, [Mhyrorin]."
                                    MC "I mean... of course I want to, but I know I can't make you do that."
                                    MC "But I'm not even going to touch you."
                                    MC "So I believe I'm strong enough to make you sit on your knees and open your mouth."
                                    MC "Do you want to test it to see if you can resist?"
                                    scene MhyrorinScene36 with Dissolve(0.5)
                                    Mhyrorin "UGHHHHH!!"
                                    Mhyrorin "Fuck my life, you are most likely right..."
                                    Mhyrorin "I can't be fucked to endure a headache right now."
                                    scene MhyrorinScene40 with Dissolve(0.5)
                                    MC "Yeah, I thought so."
                                    scene MhyrorinScene41 with Dissolve(0.5)
                                    Mhyrorin "Fuck you, you don't gotta be so mean about it"
                                    scene MhyrorinScene42 with Dissolve(0.5)
                                    MC "If the roles were reversed you would've been way worse than me."
                                    scene MhyrorinScene39 with Dissolve(0.5)
                                    Mhyrorin "You don't know that!!"
                                    Mhyrorin "Ehhh.. I guess you're right..."
                                    Mhyrorin "Soo... is this position okay?"
                                    scene MhyrorinScene42 with Dissolve(0.5)
                                    MC "Yeah, that's perfect, now open your mouth and stick your tongue out."
                                    scene MhyrorinScene44 with Dissolve(0.5)
                                    Mhyrorin "Are you really going to make me do that?"
                                    Mhyrorin "Don't you have any mercy for my dignity?"
                                    scene MhyrorinScene45 with Dissolve(0.5)
                                    MC "You didn't seem to have any for mine the night we met."
                                    MC "Also, there is no dignity hurt here, you look really good like that."
                                    MC "And do the thing with your eyes that you did when you sucked me off..."
                                    scene MhyrorinScene46 with Dissolve(0.5)
                                    Mhyrorin "There is no thing with the eyes!"
                                    Mhyrorin "I didn't do that intentionally!"
                                    Mhyrorin "It's not my fault you shoved that monster down my throat."
                                    scene MhyrorinScene47 with Dissolve(0.5)
                                    MC "Ohh, c'mon, you look really beautiful when you do that, I really like it."
                                    scene MhyrorinScene48 with Dissolve(0.5)
                                    Mhyrorin "..... Okay, but just so you know, I'm only doing it because of the slave contract. Are we clear?"
                                    scene MhyrorinScene48 with Dissolve(0.5)
                                    MC "Yeah, yeah, you really have a soft spot, don't you?"
                                    scene MhyrorinScene48 with Dissolve(0.5)
                                    Mhyrorin "Fuck you... maybe..."
                                    scene MhyrorinScene50 with Dissolve(0.5)
                                    Mhyrorin "Ith thith good?"
                                    MC "Yeah, you look really good, now shove your fingers down your throat."
                                    MC "And you better not complain, I'm not touching you."
                                    Mhyrorin "Yoo cahnt make me touch mythelf, dumbath, yoo are not powerful enowf!"
                                    MC "Fuck..."
                                    Mhyrorin "Awe we done he-uh?"
                                    MC "....."
                                    MC "Yeah, you are done."
                                    Mhyrorin "Fank ooo!"
                                    scene MhyrorinScene51 with Dissolve(0.5)
                                    Mhyrorin "Though it's fun to see you keep trying in vain, you virgin."
                                    Mhyrorin "You are too weak and you will remain like that."
                                    scene MhyrorinScene40 with Dissolve(0.5)
                                    MC "We'll see about that."
                                    scene MhyrorinScene37 with Dissolve(0.5)
                                    Mhyrorin "Anyway, have you had your fun with me?"
                                    Mhyrorin "I have things to do, important things, so if you don't mind, I'll go now, see ya!"
                                    scene BlackScreen with Dissolve(0.05)
                                    $ renpy.pause(0.01, hard=True)
                                    scene MhyrorinScene52 with Dissolve(0.5)
                                    MC "Fuck, I have to get stronger in order to make her do more things."
                                    $ current_location = str(Location).lower()
                                    $ advance_time_or_sleep()
                                "Pose for me":
                                    MC "I just want you to do a few poses for me."
                                    scene MhyrorinScene53 with Dissolve(0.5)
                                    Mhyrorin "Whaaat?"
                                    Mhyrorin "Why would you want me to do that?"
                                    scene MhyrorinScene54 with Dissolve(0.5)
                                    MC "Because you are hot as fuck and I want to see you in different poses?"
                                    MC "It's not really rocket science."
                                    scene MhyrorinScene55 with Dissolve(0.5)
                                    Mhyrorin "Ohhhh.... well, if you put it like that..."
                                    scene MhyrorinScene56 with Dissolve(0.5)
                                    Mhyrorin "What do you want?"
                                    scene MhyrorinScene57 with Dissolve(0.5)
                                    menu:
                                        "Do the Jack-o pose":
                                            MC "I want you to do the jack-o pose."
                                            scene MhyrorinScene58 with Dissolve(0.5)
                                            Mhyrorin "Jack-o pose?"
                                            Mhyrorin "Well, that's one thing I've never heard before. What is that?"
                                            scene MhyrorinScene59 with Dissolve(0.5)
                                            MC "Well... I'm not really sure how to explain it.."
                                            MC "First, do a squat, begin by standing with your feet shoulder-width apart. Then, slowly lower yourself into a squat position."
                                            MC "Second, lean your torso forward slightly."
                                            MC "Then, your head should be resting on your hands."
                                            MC "And finally arch your back as much as you can."
                                            Mhyrorin "........."
                                            scene MhyrorinScene58 with Dissolve(0.5)
                                            Mhyrorin "Well, that's an awfully detailed explanation for somebody who said he doesn't know how to explain it..."
                                            MC "What can I say, I watched a lot of girls do it."
                                            scene MhyrorinScene60 with Dissolve(0.5)
                                            Mhyrorin "Ehhh, of course your incel ass knows it from porn, what did I expect..."
                                            scene MhyrorinScene61 with Dissolve(0.5)
                                            MC "AcTuAlLy, it's from a super famous game called gui-"
                                            scene MhyrorinScene60 with Dissolve(0.5)
                                            Mhyrorin "Jesus Christ, kid, I don't care!"
                                            Mhyrorin "I'll just do it, so you could let me go already."
                                            scene MhyrorinScene42 with Dissolve(0.5)
                                            MC "Yep, that's almost perfect, bend your back a bit more."
                                            $ ShouldSeeSwitchSceneButton = True
                                            $ play_video_sequence(["MhyrorinVideo5", "MhyrorinVideo6", "MhyrorinVideo7", "MhyrorinVideo8"])
                                            Mhyrorin "Is- is this okay?"
                                            MC "Yeah, that's actually perfect!"
                                            MC "I mean, there are multiple variations of it, but you nailed it!"
                                            MC "You look really hot!"
                                            Mhyrorin "...."
                                            Mhyrorin "Thank you..."
                                            MC "There it goes, your weak spot, you like to be spoiled, don't you?"
                                            Mhyrorin "....."
                                            Mhyrorin "Maybe..."
                                            Mhyrorin "Am I done here? Did you jizz your pants already?"
                                            Mhyrorin "I have things to do, you know?"
                                            MC "Yeah, you're done, good girl."
                                            Mhyrorin "Fuck you!"
                                            $ ShouldSeeSwitchSceneButton = False
                                            scene MhyrorinScene58 with Dissolve(0.5)
                                            Mhyrorin "Okay, kiddo, glad you had your fun, but I have to go now."
                                            Mhyrorin "See ya!"
                                            scene BlackScreen with Dissolve(0.05)
                                            $ renpy.pause(0.01, hard=True)
                                            scene MhyrorinScene52 with Dissolve(0.5)
                                            $ current_location = str(Location).lower()
                                            $ advance_time_or_sleep()
                                        "Do the splits":
                                            MC "Can you do the splits?"
                                            scene MhyrorinScene60 with Dissolve(0.5)
                                            Mhyrorin "Ughhh, that's what you want?"
                                            Mhyrorin "Of course I can, but let me see, I haven't done it in a while."
                                            scene MhyrorinScene42 with Dissolve(0.5)
                                            MC "Damn, you are really flexible!"
                                            MC "I didn't expect you to pull this off so flawlessly!"
                                            MC "You look really good in this position!"
                                            $ ShouldSeeSwitchSceneButton = True
                                            $ play_video_sequence(["MhyrorinVideo9", "MhyrorinVideo10", "MhyrorinVideo11", "MhyrorinVideo12"])
                                            Mhyrorin "Th-thank you..."
                                            Mhyrorin "So... is this position good?"
                                            MC "It's perfect, you are perfect at this, don't be surprised if I have you do this more!"
                                            Mhyrorin "It's okay... I wouldn't mind..."
                                            MC "Hehe, you are so docile when you are getting complimented."
                                            Mhyrorin "I know, okay?"
                                            Mhyrorin "But you don't have to abuse it, fuck you!"
                                            Mhyrorin "Are we done here? I have some serious meetings I have to attend to."
                                            MC "Yeah, we are done, you can go."
                                            Mhyrorin "Finally..."
                                            $ ShouldSeeSwitchSceneButton = False
                                            scene MhyrorinScene58 with Dissolve(0.5)
                                            Mhyrorin "Okay, kiddo, glad you had your fun, but I have to go now."
                                            Mhyrorin "See ya!"
                                            scene BlackScreen with Dissolve(0.05)
                                            $ renpy.pause(0.01, hard=True)
                                            scene MhyrorinScene52 with Dissolve(0.5)
                                            $ current_location = str(Location).lower()
                                            $ advance_time_or_sleep()
                                        "Do the standing split":
                                            MC "Can you do a standing split?"
                                            scene MhyrorinScene60 with Dissolve(0.5)
                                            Mhyrorin "Ughhh, that's what you want?"
                                            Mhyrorin "Let me see, I don't think I've ever tried it before, so don't blow my head if I don't manage to do it."
                                            scene MhyrorinScene62 with Dissolve(0.5)
                                            MC "Damn, what the fuck, were you always this flexible?"
                                            $ ShouldSeeSwitchSceneButton = True
                                            $ play_video_sequence(["MhyrorinVideo13", "MhyrorinVideo14", "MhyrorinVideo15", "MhyrorinVideo16"])
                                            Mhyrorin "Not at all, I worked for it."
                                            Mhyrorin "So? How is it? Is this what you wanted?"
                                            MC "It's what I wanted and more!"
                                            MC "It really shows the work that you put in, you look amazing!!"
                                            Mhyrorin "..."
                                            Mhyrorin "Thanks..."
                                            Mhyrorin "But can I go now? I don't really have time to pose for you all day."
                                            MC "Almost, just one more thing..."
                                            $ ShouldSeeSwitchSceneButton = False
                                            scene MhyrorinScene65 with Dissolve(0.5)
                                            Mhyrorin "I hope you're not taking a photo right now!"
                                            MC "Come on, you look so good, it's a waste not to capture this moment."
                                            MC "Plus, since I can't even touch you, I need some jerk off material for later, also a new phone background."
                                            scene MhyrorinScene66 with Dissolve(0.5)
                                            Mhyrorin "Are you going to put me as a your background?"
                                            scene MhyrorinScene67 with Dissolve(0.5)
                                            MC "Of course I will, you have no idea how good you look right now!"
                                            Mhyrorin "...."
                                            scene MhyrorinScene66 with Dissolve(0.5)
                                            Mhyrorin "Fine then..."
                                            scene MhyrorinScene63 with Dissolve(0.5)
                                            $ renpy.pause(0.05, hard=True)
                                            scene MhyrorinScene64 with Dissolve(0.5)
                                            $ renpy.pause(0.05, hard=True)
                                            scene MhyrorinScene63 with Dissolve(0.5)
                                            $ background_buttons["MhyrorinBackground"] = True
                                            MC "That's perfect!"
                                            MC "Okay, we are done now."
                                            scene MhyrorinScene58 with Dissolve(0.5)
                                            Mhyrorin "Finally..."
                                            Mhyrorin "See ya!"
                                            scene BlackScreen with Dissolve(0.05)
                                            $ renpy.pause(0.01, hard=True)
                                            scene MhyrorinScene52 with Dissolve(0.5)
                                            $ advance_time_or_sleep()
                                            $ current_location = str(Location).lower()
                                            jump GameLoop
                                        # ! TODO I'm still thinking about what to do with these scenes, at this moment it seems they don't fit in this section
                                        # "Spread your ass":
                                        #     MC "Turn around and spread your ass for me"
                                        #     scene MhyrorinScene58 with Dissolve(0.5)
                                        #     Mhyrorin "Have you hit your head?"
                                        #     Mhyrorin "Or did you become mentally challenged all of the sudden?"
                                        #     Mhyrorin "I already told you, you are not touching me, let alone fucking my ass."
                                        #     scene MhyrorinScene59 with Dissolve(0.5)
                                        #     MC "Did I say anything about touching or fucking your ass?"
                                        #     MC "I only said to turn around and spread that ass for me."
                                        #     MC "If you wanna appose it, fine."
                                        #     MC "But I doubt I'm not powerful enough to make you do that while not laying a finger on you."
                                        #     scene MhyrorinScene60 with Dissolve(0.5)
                                        #     Mhyrorin "UGHHHH"
                                        #     Mhyrorin "Fuck you!"
                                        #     scene MhyrorinScene42 with Dissolve(0.5)
                                        #     MC "God damn, you actually look really good."

                                        # "Put your legs behind your head":
                                        #     MC "Lay on your back and put your legs behind your head?"
                                        #     scene MhyrorinScene58 with Dissolve(0.5)
                                        #     Mhyrorin "Are you dumb? Why the fuck would I do that?"
                                        #     scene MhyrorinScene59 with Dissolve(0.5)
                                        #     MC "Ummmm... the whole thing with you being my slave and doing what I want?"
                                        #     MC "Have you forgotten?"
                                        #     scene MhyrorinScene58 with Dissolve(0.5)
                                        #     Mhyrorin "I didn't forget, you dumbass."
                                        #     Mhyrorin "But you can't make me lay on my back, legs spread, and you rearranging my guts."
                                        #     scene MhyrorinScene59 with Dissolve(0.5)
                                        #     MC "Why do you always think I'm going to do something like that?"
                                        #     MC "I won't be laying a single hand on you, I just want to see you do that pose."
                                        #     scene MhyrorinScene58 with Dissolve(0.5)
                                        #     Mhyrorin "Seriously?"
                                        #     Mhyrorin "You are sick."
                                        #     scene MhyrorinScene60 with Dissolve(0.5)
                                        #     Mhyrorin "Ughhh, fine then, I'll do it"
                    "That's all":
                        MC "That's all I wanted, you can go now."
                        scene MhyrorinScene17 with Dissolve(0.5)
                        Mhyrorin "Ughhhh, I came all the way just for this?"
                        Mhyrorin "Okay, call me if you need anything else!"
                        Mhyrorin "But not some stupid shit!!"
                        scene BlackScreen with Dissolve(0.05)
                        $ renpy.pause(0.01, hard=True)
                        scene MhyrorinScene26 with Dissolve(0.5)
                        MC "Jesus Christ, she always scares me when she does that..."
                        $ current_location = str(Location).lower()
                        $ advance_time_or_sleep()
        else:
            "......."
            MC "{color=#808080}*She doesn't seem to be answering...*{/color}"
            MC "{color=#808080}*Oh, yeah, she said that she is available only before evening.*{/color}"
            $ current_location = str(Location).lower()
            jump GameLoop
    else:
        MC "......"
        MC "{color=#808080}She doesn't seem to answer...*{/color}"
        MC "{color=#808080}Oh wait, that's right, she said I have to be in my room.*{/color}"
        $ current_location = str(Location).lower()
        jump GameLoop