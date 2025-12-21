init python:
    define_images("Jennifer_weekend_1PM_", "WeekendScenes/JenniferScenes/1PM", "Jennifer_weekend_1PM_", 100)

label Jennifer_weekend_1PM:
    scene Jennifer_weekend_1PM_1 with Dissolve(0.5)
    MC "Oh, hey mom. Welcome home."
    scene Jennifer_weekend_1PM_2 with Dissolve(0.5)
    Jennifer "Hey sweetie."
    scene Jennifer_weekend_1PM_3 with Dissolve(0.5)
    Jennifer "Can you help mommy with these bags? I'm so tiered."
    scene Jennifer_weekend_1PM_4 with Dissolve(0.5)
    MC "Of course, give'em here."
    scene Jennifer_weekend_1PM_5 with Dissolve(0.5)
    Jennifer "Here you go, thank you honey."
    scene Jennifer_weekend_1PM_6 with Dissolve(0.5)
    Jennifer "Just a second so I can take these off, then we'll get these in the kitchen."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**A few moments later...**"
    scene Jennifer_weekend_1PM_7 with Dissolve(0.5)
    MC "If you're so tiered, why don't you let me put the food in the fridge?"
    scene Jennifer_weekend_1PM_8 with Dissolve(0.5)
    Jennifer "Because you don't organize things the way I like them."
    scene Jennifer_weekend_1PM_9 with Dissolve(0.5)
    Jennifer "First organize your room, and then we can talk about helping me in the kitchen."
    scene Jennifer_weekend_1PM_10 with Dissolve(0.5)
    Isabella "Hey mom, will I also talk to myself when I get to be your age?"
    scene Jennifer_weekend_1PM_11 with Dissolve(0.5)
    MC "And you call me mean."
    scene Jennifer_weekend_1PM_12 with Dissolve(0.5)
    Jennifer "Hey Isa, are you wearing my glasses again?"
    scene Jennifer_weekend_1PM_13 with Dissolve(0.5)
    Isabella "No way, I actually am. How did you know?" 
    scene Jennifer_weekend_1PM_14 with Dissolve(0.5)
    Jennifer "Just a wild guess..."
    scene Jennifer_weekend_1PM_15 with Dissolve(0.5)
    MC "What do you want Isa? Can't you see we are busy keeping this house in order?"
    MC "While you have fun all day long, we work our asses off."
    scene Jennifer_weekend_1PM_16 with Dissolve(0.5)
    Isabella "Aham, yeah, yeah, two venti iced, half-caf, oat milk caramel macchiato please."
    scene Jennifer_weekend_1PM_17 with Dissolve(0.5)
    MC "Mom, wanna go back to only raising two kids?"
    scene Jennifer_weekend_1PM_18 with Dissolve(0.5)
    Jennifer "That was a bad joke [MC]. Don't say that again."
    scene Jennifer_weekend_1PM_19 with Dissolve(0.5)
    Jennifer "Now give these to Isa and let me finish here."
    scene Jennifer_weekend_1PM_20 with Dissolve(0.5)
    Jennifer "And you lady-"
    scene Jennifer_weekend_1PM_21 with Dissolve(0.5)
    Jennifer "GHAAAAH!!!"
    scene Jennifer_weekend_1PM_22 with Dissolve(0.5)
    Isabella "What? Geez... I didn't leave wet spots on the floor or anything..."
    scene Jennifer_weekend_1PM_23 with Dissolve(0.5)
    Jennifer "Isabella! What are you doing dressed like that with you brother around?!"
    scene Jennifer_weekend_1PM_24 with Dissolve(0.5)
    Isabella "Ughhh... Geez... relax, I wear this at the beach all the time..."
    scene Jennifer_weekend_1PM_25 with Dissolve(0.5)
    Jennifer "..."
    scene Jennifer_weekend_1PM_26 with Dissolve(0.5)
    Jennifer "Wrap a towel around you next time."
    scene Jennifer_weekend_1PM_27 with Dissolve(0.5)
    MC "{color=#808080}*Should I even say something? I think I would just make things worse.*{/color}"
    MC "{color=#808080}*Jennifer went surprisingly defensive about Isabella's swimsuit...*{/color}"
    scene Jennifer_weekend_1PM_28 with Dissolve(0.5)
    Jennifer "Now get out of here both of you. You are pissing me off."
    scene Jennifer_weekend_1PM_29 with Dissolve(0.5)
    Isabella "Yeah, yeah, whatever."
    scene Jennifer_weekend_1PM_30 with Dissolve(0.5)
    Isabella "Let's get out of here, [MC]."
    scene Jennifer_weekend_1PM_31 with Dissolve(0.5)
    MC "Mhm, right behind you."
    scene Jennifer_weekend_1PM_32 with Dissolve(0.5)
    Jennifer "[MC_upper]!!" 
    scene Jennifer_weekend_1PM_33 with Dissolve(0.5)
    MC "My bad!"
    call stat_reward({"Isabella": {"love": 2}, "Jennifer": {"love": 2}}, return_to=None)
    $ Location = "Entrance"
    $ advance_time_or_sleep()