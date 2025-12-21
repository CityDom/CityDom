init python:
    define_images("Jennifer_weekend_8AM_", "WeekendScenes/JenniferScenes/8AM", "Jennifer_weekend_8AM_", 100)

label Jennifer_weekend_8AM:
    scene Jennifer_weekend_8AM_1 with Dissolve(0.5)
    Jennifer "You have to know how to do at least some basic cooking, sweetie."
    Jennifer "You can't go through life just eating fast food."
    scene Jennifer_weekend_8AM_2 with Dissolve(0.5)
    Isabella "Mom, this is just a smoothie and some toast..."
    Isabella "Are you sure you're not just trying to slack off?"
    scene Jennifer_weekend_8AM_3 with Dissolve(0.5)
    Jennifer "Oh, you are so right, sweetie."
    Jennifer "If you want we can swap. I cook and you clean the whole house after, deal?"
    scene Jennifer_weekend_8AM_4 with Dissolve(0.5)
    Isabella "Tsk...."
    scene Jennifer_weekend_8AM_5 with Dissolve(0.5)
    MC "Haha, wait, is Isa cooking? Let me pull up a chair, I gotta watch this."
    scene Jennifer_weekend_8AM_6 with Dissolve(0.5)
    Isabella "I'm not doing this if he's just going to sit there and laugh at me."
    scene Jennifer_weekend_8AM_7 with Dissolve(0.5)
    Jennifer "C'mon Isa, he won't laugh at you."
    scene Jennifer_weekend_8AM_8 with Dissolve(0.5)
    MC "Haha, we'll see about that."
    scene Jennifer_weekend_8AM_9 with Dissolve(0.5)
    Isabella "Ughhhh, you're so annoying!"
    scene Jennifer_weekend_8AM_10 with Dissolve(0.5)
    MC "Hah! Let's see how you like it! You do this to me all the time!"
    Jennifer "You won't laugh at her, right [MC]?"
    scene Jennifer_weekend_8AM_11 with Dissolve(0.5)
    MC "Huh?"
    scene Jennifer_weekend_8AM_12 with Dissolve(0.5)
    Jennifer "You won't laugh at her, right [MC]?"
    scene Jennifer_weekend_8AM_13 with Dissolve(0.5)
    MC "Oh, no, of course not mom."
    scene Jennifer_weekend_8AM_14 with Dissolve(0.5)
    Isabella "Huh?"
    scene Jennifer_weekend_8AM_15 with Dissolve(0.5)
    Jennifer "Yes, sweetie?"
    scene Jennifer_weekend_8AM_16 with Dissolve(0.5)
    Isabella "Huh?"
    scene Jennifer_weekend_8AM_17 with Dissolve(0.5)
    Isabella "Ok then... I guess..."
    scene Jennifer_weekend_8AM_18 with Dissolve(0.5)
    Isabella "So, what am I supposed to do again?"
    scene Jennifer_weekend_8AM_19 with Dissolve(0.5)
    Jennifer "Just finish cutting the rest of the fruit for me and toss it in the blender."
    Jennifer "I've already done most of it, so just add some milk after and blend it all up, okay?"
    scene Jennifer_weekend_8AM_18 with Dissolve(0.5)
    Isabella "Okay, I can do that..."
    scene Jennifer_weekend_8AM_20 with Dissolve(0.5)
    Isabella "Like this?"
    scene Jennifer_weekend_8AM_21 with Dissolve(0.5)
    Jennifer "Yep, just like that."
    scene Jennifer_weekend_8AM_22 with Dissolve(0.5)
    MC "{color=#808080}God, this is so fucking boring...{/color}"
    scene Jennifer_weekend_8AM_23 with Dissolve(0.5)
    MC "{color=#808080}I need to find a way to make things more interesting without pocking the bear.{/color}"
    scene Jennifer_weekend_8AM_24 with Dissolve(0.5)
    menu:
        "ask mom to help":
            scene Jennifer_weekend_8AM_25 with Dissolve(0.5)
            MC "Oke, I'm down to bet my whole allowance that she's dropping that bottle."
            scene Jennifer_weekend_8AM_26 with Dissolve(0.5)
            MC "Do you want me to help her, or..."
            scene Jennifer_weekend_8AM_27 with Dissolve(0.5)
            Jennifer "She's a grown woman [MC], she can do it herself, don't underestimate her."
            scene Jennifer_weekend_8AM_28 with Dissolve(0.5)
            Isabella "I am so going to drop this bottle, help... please..."
            scene Jennifer_weekend_8AM_29 with Dissolve(0.5)
            Jennifer "Oh, right away."
            scene Jennifer_weekend_8AM_30 with Dissolve(0.5)
            Jennifer "Don't worry sweetie, mommy is here to help you."
            scene Jennifer_weekend_8AM_31 with Dissolve(0.5)
            MC "{color=#808080}*Hah, I guess even for Isa, with those pair of jugs on the back of the neck...*"
            scene Jennifer_weekend_8AM_32 with Dissolve(0.5)
            MC "{color=#808080}*You got to feel a bit excited.*{/color}"
            scene Jennifer_weekend_8AM_33 with Dissolve(0.5)
            Isabella "Thanks mom, I really needed that."
            scene Jennifer_weekend_8AM_34 with Dissolve(0.5)
            Jennifer "No problem sweetie, you know I'm always here to help you."
            scene Jennifer_weekend_8AM_35 with Dissolve(0.5)
            MC "{color=#808080}*Well, this is quite wholesome. It would've been even more so if I wasn't so hard right now...*"
            scene Jennifer_weekend_8AM_36 with Dissolve(0.5)
            MC "{color=#808080}*Sometimes I forget how nice Jennifer is.*{/color}"
            MC "{color=#808080}I wonder how I would've ended up if she was the one raising me.{/color}"
            scene Jennifer_weekend_8AM_37 with Dissolve(0.5)
            MC "{color=#808080}*Well... I guess that's as much action as I'm going to see right now.*"
            MC "{color=#808080}*At this point I'm just sitting in the cuck chair and I'm not really a fan of it.*"
            scene Jennifer_weekend_8AM_38 with Dissolve(0.5)
            MC "Well... fun is over, Isa didn't break anything."
            MC "And I guess this is the mom and daughter bonding session, so I'll take my leave."
            scene Jennifer_weekend_8AM_39 with Dissolve(0.5)
            Isabella "Bye bye!!!"
            Jennifer "Be careful honey!"
            scene Jennifer_weekend_8AM_40 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god I was actually sitting in the cuck chair. They don't even acknowledge me being here.*"
            scene Jennifer_weekend_8AM_41 with Dissolve(0.5)
            MC "{color=#808080}*Although, mom and Isa getting closer to each other doesn't sound bad at all, it might make things easier actually.*"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You get out of the room**{/color}"
            call stat_reward({"Isabella": {"obedience": 2}, "Jennifer": {"obedience": 2}}, show_black=False, return_to=None)
            $ Location = "Livingroom"
            $ advance_time_or_sleep()
        "scare Isabella":
            scene Jennifer_weekend_8AM_42 with Dissolve(0.5)
            Jennifer "You are doing really well honey, keep it up!"
            scene Jennifer_weekend_8AM_43 with Dissolve(0.5)
            MC "{color=#808080}*She's just pouring milk into a blender, what is there to praise so much about?*{/color}"
            MC "{color=#808080}*Anyway, I'm reaching my limit here, let's try something.*{/color}"
            scene Jennifer_weekend_8AM_44 with Dissolve(0.5)
            MC "I gotta admit, you are doing better than I thought you would."
            scene Jennifer_weekend_8AM_77 with Dissolve(0.5)
            MC "But are you planning to put the spider that's on your hand in the blender as well?"
            scene Jennifer_weekend_8AM_45 with Dissolve(0.5)
            Isabella "The whAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA?!!!"
            scene Jennifer_weekend_8AM_46 with Dissolve(0.5)
            Jennifer "This boy will be the death of me..."
            scene Jennifer_weekend_8AM_47 with Dissolve(0.5)
            ".............."
            scene Jennifer_weekend_8AM_48 with Dissolve(0.5)
            Jennifer "Are you okay sweetie?"
            scene Jennifer_weekend_8AM_49 with Dissolve(0.5)
            Isabella "Y-yeah... I'm sorry..."
            scene Jennifer_weekend_8AM_50 with Dissolve(0.5)
            Jennifer "It's okay honey, mommy will help you clean up."
            scene Jennifer_weekend_8AM_51 with Dissolve(0.5)
            Jennifer "And you!"
            scene Jennifer_weekend_8AM_52 with Dissolve(0.5)
            Jennifer "Tissues, now!"
            scene Jennifer_weekend_8AM_53 with Dissolve(0.5)
            MC "Y-yes ma'am! Right away!"
            scene Jennifer_weekend_8AM_54 with Dissolve(0.5)
            Jennifer "No need to be sad."
            scene Jennifer_weekend_8AM_55 with Dissolve(0.5)
            Jennifer "Hey, look at me."
            Jennifer "Accidents like this happen all the time in the kitchen."
            scene Jennifer_weekend_8AM_56 with Dissolve(0.5)
            MC "{color=#808080}*God damn, mom, you don't have to get her even wetter.*"
            scene Jennifer_weekend_8AM_57 with Dissolve(0.5)
            Jennifer "Can you hurry up with those tissues already?!"
            scene Jennifer_weekend_8AM_58 with Dissolve(0.5)
            MC "Right here, ma'am!"
            scene Jennifer_weekend_8AM_59 with Dissolve(0.5)
            Jennifer "Mhm."
            scene Jennifer_weekend_8AM_60 with Dissolve(0.5)
            Jennifer "Don't let it happen again!"
            scene Jennifer_weekend_8AM_61 with Dissolve(0.5)
            MC "Of course not, ma'am."
            scene Jennifer_weekend_8AM_62 with Dissolve(0.5)
            Jennifer "It's just a little bit of milk, nothing to worry about."
            scene Jennifer_weekend_8AM_63 with Dissolve(0.5)
            Isabella "Thanks mom..."
            scene Jennifer_weekend_8AM_64 with Dissolve(0.5)
            Jennifer "The face is done."
            scene Jennifer_weekend_8AM_65 with Dissolve(0.5)
            Jennifer "Another napkin!"
            scene Jennifer_weekend_8AM_66 with Dissolve(0.5)
            Jennifer "Let mommy take care of this real quick as well."
            scene Jennifer_weekend_8AM_67 with Dissolve(0.5)
            Isabella "Oh, okay..."
            scene Jennifer_weekend_8AM_68 with Dissolve(0.5)
            MC "{color=#808080}*Hah, I didn't expect Isa to be so flustered by this.*"
            MC "{color=#808080}*This is finally getting interesting.*"
            scene Jennifer_weekend_8AM_69 with Dissolve(0.5)
            Isabella "Huh?"
            scene Jennifer_weekend_8AM_70 with Dissolve(0.5)
            Isabella "Hmph..."
            scene Jennifer_weekend_8AM_71 with Dissolve(0.5)
            Jennifer "Huh? What's wrong sweetie?"
            scene Jennifer_weekend_8AM_72 with Dissolve(0.5)
            Jennifer "Hmm?"
            scene Jennifer_weekend_8AM_73 with Dissolve(0.5)
            Jennifer "Get out!"
            scene Jennifer_weekend_8AM_74 with Dissolve(0.5)
            MC "Huh?! But I didn't do anything now!"
            scene Jennifer_weekend_8AM_75 with Dissolve(0.5)
            Jennifer "Get out!"
            scene Jennifer_weekend_8AM_76 with Dissolve(0.5)
            MC "UGHHHH..."
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You get out of the room**{/color}"
            call stat_reward({"Isabella": {"love": -2, "corruption": 2}, "Jennifer": {"love": -2, "corruption": 2}}, show_black=False, return_to=None)
            $ Location = "Livingroom"
            $ advance_time_or_sleep()
        "leave":
            scene Jennifer_weekend_8AM_78 with Dissolve(0.5)
            MC "{color=#808080}*I can't even be bothered actually...*"
            MC "{color=#808080}*Something will spill and somehow it will be my fault.*"
            scene Jennifer_weekend_8AM_79 with Dissolve(0.5)
            MC "Any idea when it will be done?"
            scene Jennifer_weekend_8AM_80 with Dissolve(0.5)
            Jennifer "In about 20 minutes or so."
            Jennifer "And don't forget we eat in the garden on weekends, you can wait out there if you want."
            scene Jennifer_weekend_8AM_81 with Dissolve(0.5)
            MC "Yeah, yeah, you tell me every time."
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You get out of the room**{/color}"
            call stat_reward({"Isabella": {"love": 2}, "Jennifer": {"love": 2}}, show_black=False, return_to=None)
            $ Location = "Livingroom"
            $ advance_time_or_sleep()