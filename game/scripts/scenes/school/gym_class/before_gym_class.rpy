init python:
    define_images("BeforeGymClass_Scene", "GymClass/BeforeGymClass", "BeforeGymClass_Scene", 60)
    renpy.image("BeforeGymClass_Movie1", Movie(channel="movie", play="Images/GymClass/BeforeGymClass/BeforeGymClass_Movie1.webm", loop=True, group="pov_group"))

label BeforeGymClass_FromInside_Scene:
    MC "{color=#808080}*I should get out of here, the girls should be coming in any second...*"
    $ Location = "GymLockerRoomFront"
    $ renpy.call("GameLoop")

label BeforeGymClass_Scene:
    scene BeforeGymClass_Scene1 with Dissolve(0.5)
    MC "{color=#808080}*Huh? The girls seem to be changing...*"
    MC "{color=#808080}*Do I take a peek?*"
    menu:
        "Take a peek":
            MC "{color=#808080}*Why am I even asking myself that? Of course I am.*"
            scene BeforeGymClass_Scene2 with Dissolve(0.5)
            MC "{color=#808080}*Fuck, this door squeaks so loudly.*"
            MC "{color=#808080}*But they are all chatting; they shouldn't hear it.*"
            scene BeforeGymClass_Scene3 with Dissolve(0.5)
            MC "{color=#808080}*Wait, is that Maria?*"
            MC "{color=#808080}*What the fuck, she's so hot, I sometimes forget about that.*"
            scene BeforeGymClass_Scene4 with Dissolve(0.5)
            Maria "{color=#808080}*Huh...*"
            scene BeforeGymClass_Scene5 with Dissolve(0.5)
            Maria "{color=#808080}*What the...*"
            scene BeforeGymClass_Scene6 with Dissolve(0.5)
            MC "{color=#808080}*Ughhh, of course god damn Dumbo hears me!*"
            $ MC_LS = mc_name + " lip syncing"
            scene BeforeGymClass_Scene7 with Dissolve(0.5)
            MC_LS "You better shut up!"
            scene BeforeGymClass_Scene8 with Dissolve(0.5)
            MariaLS "Get out now!"
            scene BeforeGymClass_Scene9 with Dissolve(0.5)
            Maria "{color=#808080}*Tsk, he's not even listening to me. What the fuck is he doing?!*"
            scene BeforeGymClass_Scene10 with Dissolve(0.5)
            Maria "{color=#808080}*Oh, of course...*"
            scene BeforeGymClass_Scene11 with Dissolve(0.5)
            Isabella "Oh, c'mon Maria, what are you doing?"
            scene BeforeGymClass_Scene12 with Dissolve(0.5)
            Isabella "You don't have to be ashamed of them!"            
            scene BeforeGymClass_Scene13 with Dissolve(0.5)
            Isabella "Plus, we're all girls here, so there's nothing to hide!"
            scene BeforeGymClass_Scene14 with Dissolve(0.5)
            Maria "Uhhh, wait, no, Isa, this is not what it's abou-"
            scene BeforeGymClass_Scene15 with Dissolve(0.5)
            Isabella "See? They are beautiful! They are as big as mine!"
            scene BeforeGymClass_Scene16 with Dissolve(0.5)
            Isabella "And trust me, I've got some really good genetics!"
            scene BeforeGymClass_Scene17 with Dissolve(0.5)
            Isabella "Of course, not everyone can have milk jugs like Sophie."
            scene BeforeGymClass_Scene18 with Dissolve(0.5)
            Isabella "But between you and me, that's all plastic!"
            scene BeforeGymClass_Scene19 with Dissolve(0.5)
            Sophie "Huh?! What do you mean by that?"
            scene BeforeGymClass_Scene20 with Dissolve(0.5)
            Sophie "Alis, what does she mean by that?!"
            scene BeforeGymClass_Scene21 with Dissolve(0.5)
            Alis "She's saying you had a boob job."
            scene BeforeGymClass_Scene22 with Dissolve(0.5)
            Sophie "GAAAHHHH!!!"
            scene BeforeGymClass_Scene23 with Dissolve(0.5)
            Sophie "How could you say that?!?!"
            scene BeforeGymClass_Scene24 with Dissolve(0.5)
            Sophie "I'll have you know, this is all real!"
            scene BeforeGymClass_Scene25 with Dissolve(0.5)
            Isabella "Hmmmm... Reaaaaaally?"
            Isabella "I don't know, Sophie, they look pretty stiff to me..."
            scene BeforeGymClass_Scene26 with Dissolve(0.5)
            Sophie "HUH?! Stiff?!"
            show BeforeGymClass_Movie1
            Sophie "Does this look stiff to you?!"
            scene BeforeGymClass_Scene27 with Dissolve(0.5)
            Isabella "You can jiggle them all you want, Sophie, I'm still not convinced."
            scene BeforeGymClass_Scene28 with Dissolve(0.5)
            Isabella "This is how you test it!"
            Isabella "See? This is how soft natural boobs feel!"
            scene BeforeGymClass_Scene29 with Dissolve(0.5)
            Maria "{color=#808080}*Wait... is she trying to...*"
            scene BeforeGymClass_Scene30 with Dissolve(0.5)
            Maria "{color=#808080}*No way, she actually is!*"
            Maria "{color=#808080}*I guess she really is his sister.*"
            scene BeforeGymClass_Scene31 with Dissolve(0.5)
            MC "{color=#808080}*I'm so proud of you, Isa!*"
            MC "{color=#808080}*You really are my sister!!*"
            scene BeforeGymClass_Scene32 with Dissolve(0.5)
            Sophie "But this is exactly how mine are!"
            Sophie "Actually, mine are even softer!!"
            Sophie "Here! Check for yourself!"
            scene BeforeGymClass_Scene33 with Dissolve(0.5)
            Maria "{color=#808080}*And it actually worked, oh my god!*"
            scene BeforeGymClass_Scene34 with Dissolve(0.5)
            Isabella "Hehe, don't mind if I do!"
            scene BeforeGymClass_Scene35 with Dissolve(0.5)
            Sophie "So?! Say something!"
            scene BeforeGymClass_Scene36 with Dissolve(0.5)
            Isabella "Hmmmm...."
            scene BeforeGymClass_Scene37 with Dissolve(0.5)
            Isabella "I'm not so sure..."
            scene BeforeGymClass_Scene38 with Dissolve(0.5)
            Sophie "What do you mean you're not sure?!"
            Sophie "Maybe you're testing it wrong!"
            scene BeforeGymClass_Scene39 with Dissolve(0.5)
            Isabella "Hey, don't question my testing!"
            Isabella "It's hard to say because they are bigger than my head!"
            scene BeforeGymClass_Scene40 with Dissolve(0.5)
            Isabella "What do you think, Maria? Try them!"
            scene BeforeGymClass_Scene41 with Dissolve(0.5)
            Maria "Huh, wait, what?! Me?"
            scene BeforeGymClass_Scene42 with Dissolve(0.5)
            Sophie "Come on, already! You'll see that they are real!"
            scene BeforeGymClass_Scene43 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god, Maria, you antisocial bitch, stop acting like a shy little girl and do it!*"
            MC "{color=#808080}*I know you always wanted to!*"
            scene BeforeGymClass_Scene44 with Dissolve(0.5)
            Maria "Okay, okay, geez..."
            scene BeforeGymClass_Scene45 with Dissolve(0.5)
            Sophie "Ouch, your nails hurt."
            scene BeforeGymClass_Scene46 with Dissolve(0.5)
            Maria "Oh, sorry, I forgot about that, I'll stop."
            scene BeforeGymClass_Scene47 with Dissolve(0.5)
            Sophie "No, it's okay, just tell me, what do you think?!"
            scene BeforeGymClass_Scene48 with Dissolve(0.5)
            Maria "Uhhh... I mean... They seem pretty real to me..."
            scene BeforeGymClass_Scene49 with Dissolve(0.5)
            Isabella "Hmmm, well, I think you're right, they seem real!"
            Isabella "I guess you're just that gifted, Sophie, I'm jealous!"
            scene BeforeGymClass_Scene50 with Dissolve(0.5)
            Sophie "Haha, I told you they were real!"
            Sophie "You are free to envy me!"
            scene BeforeGymClass_Scene51 with Dissolve(0.5)
            Selina "{color=#808080}*Tsk, damn cow...*"
            scene BeforeGymClass_Scene52 with Dissolve(0.5)
            Isabella "Well... that's a bummer, I'm usually right about these..."
            scene BeforeGymClass_Scene53 with Dissolve(0.5)
            Isabella "I wonder if [MC] would've guessed it right."
            scene BeforeGymClass_Scene54 with Dissolve(0.5)
            Maria "Hah, I bet he would've!"
            scene BeforeGymClass_Scene55 with Dissolve(0.5)
            Isabella "Hah, I know, right? It's because that's all he thinks about!"
            scene BeforeGymClass_Scene56 with Dissolve(0.5)
            Isabella "Thank God that window is so high up."
            Isabella "I bet he would've gotten the idea to peep on us!"
            scene BeforeGymClass_Scene57 with Dissolve(0.5)
            Isabella "I would die of shame if he did that!"
            Maria "{color=#808080}*Ah, shit, I forgot he was peeking on us!*"
            scene BeforeGymClass_Scene58 with Dissolve(0.5)
            Maria "{color=#808080}*The twins are leaving... And I bet he's still there!*"
            Maria "{color=#808080}*He won't see them until it's too late if they come from that way.*"
            scene BeforeGymClass_Scene59 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene BeforeGymClass_Scene60 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene BeforeGymClass_Scene59 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene BeforeGymClass_Scene60 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene BeforeGymClass_Scene59 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene BeforeGymClass_Scene60 with Dissolve(0.2)
            MC "{color=#808080}*Ah, shit, I think that's my cue.*"
            MC "{color=#808080}*Someone must be getting out, thanks Maria!*"
            call stat_reward({"Alis": {"corruption": 2}, "Anna": {"corruption": 2}, "Criss": {"corruption": 2}, "Dorothy": {"corruption": 2}, "Emma": {"corruption": 2}, "Greta": {"corruption": 2}, "Helena": {"corruption": 2}, "Isabella": {"corruption": 2}, "Leya": {"corruption": 2}, "Lola": {"corruption": 2}, "Maria": {"love": 2, "corruption": 2, "obedience": 2}, "Selina": {"corruption": 2}, "Sophie": {"corruption": 2}}, return_to=None)
            $ Location = "GymLockerRoomFront"
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")
        "Don't":
            MC "{color=#808080}*Nah, it's too risky, this door is squeaky as hell, they might hear me.*"
            $ renpy.call("GameLoop")
