init python:
    define_images("Isa_Team_Scene", "GymClass/Isa_Team_Scene", "Isa_Team_Scene", 74)

label Isa_Team_Scene:
    if not Watched_GymClass_Isa_Team_Scene:
        $ Watched_GymClass_Isa_Team_Scene = True
        scene Isa_Team_Scene1 with Dissolve(0.5)
        Isabella "Oh my god, finally! You're here; sit down already!"
        scene Isa_Team_Scene2 with Dissolve(0.5)
        MC "Alright, alright. What's the hurry?"
        scene Isa_Team_Scene3 with Dissolve(0.5)
        Isabella "Okay, girls, we can't let Lola's team beat us again!"
        Isabella "Now we have [MC] as well! We can win!"
        scene Isa_Team_Scene4 with Dissolve(0.5)
        Sophie "Until now, we had the teacher on our team!"
        Sophie "No way [MC] is better than her!"
        scene Isa_Team_Scene5 with Dissolve(0.5)
        Helena "Yeah, but she never really tried her best. She usually just wants to balance the teams..."
        scene Isa_Team_Scene6 with Dissolve(0.5)
        Criss "Does [MC] even know how to play?"
        scene Isa_Team_Scene7 with Dissolve(0.5)
        Isabella "Uhhh... I don't know..."
        Isabella "Have you ever played before, [MC]?"
        scene Isa_Team_Scene8 with Dissolve(0.5)
        MC "Uhhh, I played a few times, yeah..."
        scene Isa_Team_Scene9 with Dissolve(0.5)
        Maria "By the sound of that, it's over..."
        scene Isa_Team_Scene10 with Dissolve(0.5)
        MC "Does it even matter that much? I don't think it even counts toward our final grade..."
        scene Isa_Team_Scene11 with Dissolve(0.5)
        "{color=#808080}**Stare....**{/color}"
        scene Isa_Team_Scene12 with Dissolve(0.5)
        Isabella "Of course it matters, [MC]!"
        Isabella "Do you really want Selina to win?"
        scene Isa_Team_Scene13 with Dissolve(0.5)
        Sophie "She won't shut up about it for a week!"
        Sophie "Don't get me started about those twins!"
        scene Isa_Team_Scene14 with Dissolve(0.5)
        Maria "Do you want to hear them on repeat in class about how they won?"
        Maria "Just wait until Dorothy gives a speech about how her team's discipline won the game!"
        scene Isa_Team_Scene15 with Dissolve(0.5)
        MC "Oh, so you all just hate each other."
        scene Isa_Team_Scene16 with Dissolve(0.5)
        pause
        scene Isa_Team_Scene17 with Dissolve(0.5)
        Tanya "{color=#808080}*It seems like the shrimp got the girls fired up for this one...*{/color}"
        scene Isa_Team_Scene18 with Dissolve(0.5)
        MC "Alright, damn. Let's do it then. Are they really that good?"
        scene Isa_Team_Scene19 with Dissolve(0.5)
        Isabella "No, that's the worst part—they're trash!"
        Isabella "But Lola hard carries them!"
        scene Isa_Team_Scene20 with Dissolve(0.5)
        MC "So if I match Lola, can you girls handle the rest?"
        scene Isa_Team_Scene13 with Dissolve(0.5)
        Sophie "You can't match her! She's too good!"
        scene Isa_Team_Scene14 with Dissolve(0.5)
        Maria "I don't think you've ever seen her play—she's crazy."
        scene Isa_Team_Scene12 with Dissolve(0.5)
        Isabella "Yeah, only Tanya was able to match her."
        scene Isa_Team_Scene21 with Dissolve(0.5)
        MC "And you, Alis, what do you think? You haven't said a word."
        MC "You're pretty tall and seem more athletic than Sophie."
        scene Isa_Team_Scene22 with Dissolve(0.5)
        Alis "Huh, me? No, I'm pretty average..."
        scene Isa_Team_Scene23 with Dissolve(0.5)
        Isabella "That's because you never try your best!"
        scene Isa_Team_Scene24 with Dissolve(0.5)
        Alis "Maybe I just need a little bit of motivation!"
        scene Isa_Team_Scene25 with Dissolve(0.5)
        Helena "{color=#808080}*Ah shit...*{/color}"
        scene Isa_Team_Scene26 with Dissolve(0.5)
        Alis "Think you can motivate me?"
        scene Isa_Team_Scene27 with Dissolve(0.5)
        Isabella "It's okay, Alis, no need to be this motivated!"
        scene Isa_Team_Scene28 with Dissolve(0.5)
        Alis "Ahhh, how unlucky..."
        scene Isa_Team_Scene29 with Dissolve(0.5)
        Tanya "Alright girls, party's over, break it off!"
        Tanya "No reason to fight—you have to be a team!"
        scene Isa_Team_Scene30 with Dissolve(0.5)
        Isabella "Yeah, you heard her. Let's discuss how we play!"
        call stat_reward({"Alis": {"love": 2}, "Criss": {"love": 2}, "Helena": {"love": 2}, "Isabella": {"love": 2}, "Maria": {"love": 2}, "Sophie": {"love": 2}}, return_to=None)
    else:
        MC "{color=#808080}*I already talked to them about this.*{/color}"
    $ renpy.call("GameLoop")