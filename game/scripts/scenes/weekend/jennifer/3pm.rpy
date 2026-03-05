init python:
    define_images("Jennifer_weekend_3PM_", "WeekendScenes/JenniferScenes/3PM", "Jennifer_weekend_3PM_", 100)

label Jennifer_weekend_3PM:
    scene Jennifer_weekend_3PM_1 with Dissolve(0.5)
    MC "Oh, hey mom, what are you doing?"
    scene Jennifer_weekend_3PM_2 with Dissolve(0.5)
    Jennifer "I'm for sure not tanning by the pool. So what does it look like I'm doing, {b}{i}honey{/i}{/b} ?!"
    scene Jennifer_weekend_3PM_3 with Dissolve(0.5)
    MC "Uhhh... Cleaning..."
    MC "Did I choose a bad time? I'll leave you alone if you want."
    scene Jennifer_weekend_3PM_4 with Dissolve(0.5)
    Jennifer "Actually, no, wait."
    scene Jennifer_weekend_3PM_5 with Dissolve(0.5)
    Jennifer "You came at the perfect time actually."
    scene Jennifer_weekend_3PM_6 with Dissolve(0.5)
    Jennifer "UGHHHH, my back is killing me."
    Jennifer "Do you know how to crack someone's back? I can't do it properly by myself."
    scene Jennifer_weekend_3PM_7 with Dissolve(0.5)
    MC "Uhhhh... Yeah, I think I can try. I've done it a couple of times before."
    scene Jennifer_weekend_3PM_8 with Dissolve(0.5)
    MC "Okay, just make an 'X' with your arms on your chest."
    scene Jennifer_weekend_3PM_9 with Dissolve(0.5)
    Jennifer "Like this? But I hope you're not planning to lift me up."
    Jennifer "Mommy is pretty heavy, I don't want you to hurt your back."
    scene Jennifer_weekend_3PM_10 with Dissolve(0.5)
    MC "Don't worry about it, I'm pretty strong."
    scene Jennifer_weekend_3PM_11 with Dissolve(0.5)
    MC "Plus, I don't think you're thaaaat heavy."
    scene Jennifer_weekend_3PM_12 with Dissolve(0.5)
    Jennifer "Okay, if you say so... But be careful, please."
    scene Jennifer_weekend_3PM_13 with Dissolve(0.5)
    MC "Yeah, yeah, I got it."
    scene Jennifer_weekend_3PM_14 with Dissolve(0.5)
    Jennifer "Eek! {color=#808080}*He's poking me with...*"
    scene Jennifer_weekend_3PM_15 with Dissolve(0.5)
    Jennifer "{color=#808080}*He's just trying to lift you up Jennifer, what's wrong with you, he probably didn't even realize it.*"
    scene Jennifer_weekend_3PM_16 with Dissolve(0.5)
    MC "{color=#808080}*Heh.*"
    menu:
        "grab her by the waist":
            scene Jennifer_weekend_3PM_17 with Dissolve(0.5)
            MC "Here we go, try to exhale."
            scene Jennifer_weekend_3PM_18 with Dissolve(0.5)
            Jennifer "AAAAAAAAAAAAAAAAAAAAAAAAAA!!!!"
            scene Jennifer_weekend_3PM_19 with Dissolve(0.5)
            MC "What happened to make an 'X' on your chest?"
            scene Jennifer_weekend_3PM_20 with Dissolve(0.5) 
            Jennifer "AAAAAAAAAAAAAAAA!!!!"
            scene Jennifer_weekend_3PM_21 with Dissolve(0.5) 
            MC "I heard it crack! Does it feel a bit better?"
            scene Jennifer_weekend_3PM_22 with Dissolve(0.5) 
            MC "Uhhhh.... Mom?"
            scene Jennifer_weekend_3PM_23 with Dissolve(0.5) 
            MC "{color=#808080}*Did she die...?*"
            MC "{color=#808080}*No way she fucking died, right?*"
            scene Jennifer_weekend_3PM_24 with Dissolve(0.5) 
            Jennifer "Ughhh... owwwwwww..."
            scene Jennifer_weekend_3PM_25 with Dissolve(0.5) 
            Jennifer "Yeah, it cracked..."
            scene Jennifer_weekend_3PM_26 with Dissolve(0.5) 
            MC "Sorry mom! Did I overdo it?"
            scene Jennifer_weekend_3PM_27 with Dissolve(0.5) 
            Jennifer "Hah, you think? Maybe a little."
            scene Jennifer_weekend_3PM_28 with Dissolve(0.5) 
            Jennifer "Ahhh, but I do feel a lot better. Even if it was only in my lower back."
            scene Jennifer_weekend_3PM_29 with Dissolve(0.5) 
            MC "Yeah, well, to crack it properly I do have to have my hands wrapped around you chest... so..."
            scene Jennifer_weekend_3PM_30 with Dissolve(0.5) 
            Jennifer "Oh. Well... I'll do without it."
            scene Jennifer_weekend_3PM_31 with Dissolve(0.5) 
            Jennifer "But thank you, honey! I feel a bit better now!"
            scene Jennifer_weekend_3PM_32 with Dissolve(0.5) 
            Jennifer "I'll go lay down for a bit."
            scene Jennifer_weekend_3PM_33 with Dissolve(0.5) 
            MC "Okay mom! Take care!"
            scene Jennifer_weekend_3PM_34 with Dissolve(2) 
            Jennifer "{color=#808080}*My little boy has gotten so strong...*"
            call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
            $ Location = "Entrance"
            $ advance_time_or_sleep()
        "grab her by the tits":
            scene Jennifer_weekend_3PM_35 with Dissolve(0.5) 
            MC "Here we go, try to exhale."
            Jennifer "GHAAAAAAAAAAAAAAAAAAAAA!!!!"
            scene Jennifer_weekend_3PM_36 with Dissolve(0.5) 
            Jennifer "LET GO OF ME RIGHT THIS MOMENT!!"
            scene Jennifer_weekend_3PM_37 with Dissolve(0.5)
            Jennifer "WHAT ON EARTH IS WRONG WITH YOU?!"
            scene Jennifer_weekend_3PM_38 with Dissolve(0.5)
            MC "Wha- w- what? I thought you wanted me to crack your back..."
            scene Jennifer_weekend_3PM_39 with Dissolve(0.5)
            Jennifer "For goodness sake, [MC], you can't just grab me like that! That's so inappropriate!"
            scene Jennifer_weekend_3PM_40 with Dissolve(0.5)
            MC "B-but, that's how I know how to crack a back properly..."
            scene Jennifer_weekend_3PM_41 with Dissolve(0.5)
            Jennifer "I don't even want to hear it!"
            Jennifer "And we're not done here, we're going to have a talk about this after I lay down for a bit."
            scene BlackScreen with Dissolve(1)
            "............"
            scene Jennifer_weekend_3PM_42 with Dissolve(1)
            Jennifer "For crying out loud, this kid will be the death of me..."
            call stat_reward({"Jennifer": {"love": -5, "corruption": 2}}, return_to=None)
            $ Location = "Entrance"
            $ advance_time_or_sleep()