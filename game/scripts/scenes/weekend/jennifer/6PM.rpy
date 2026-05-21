init python:
    define_images("Jennifer_Weekend_6PM_", "WeekendScenes/JenniferScenes/6PM", "Jennifer_Weekend_6PM_", 100)
    
label Jennifer_Weekend_6PM:
    scene Jennifer_Weekend_6PM_1 with Dissolve(0.5)
    Jennifer "Mm-mm-mm..."
    scene Jennifer_Weekend_6PM_2 with Dissolve(0.5)
    Jennifer "Hm-hm-hm..."
    scene Jennifer_Weekend_6PM_3 with Dissolve(0.5)
    MC "I can never figure out what song this is."
    scene Jennifer_Weekend_6PM_4 with Dissolve(0.5)
    Jennifer "Haha, you wouldn't know it. You weren't even born when this song was popular."
    scene Jennifer_Weekend_6PM_5 with Dissolve(0.5)
    Jennifer "Ughhhhh."
    scene Jennifer_Weekend_6PM_6 with Dissolve(0.5)
    MC "With statements like that you'll never beat the getting old allegations."
    scene Jennifer_Weekend_6PM_7 with Dissolve(0.5)
    Jennifer "OH, so you finally admit that I'm old, huh? Okaaaaaay..."
    scene Jennifer_Weekend_6PM_8 with Dissolve(0.5)
    MC "Come on, don't play that card with me. You know I'm your biggest fan."
    scene Jennifer_Weekend_6PM_9 with Dissolve(0.5)
    Jennifer "Yeah, yeah, how could I forget it? Come here."
    scene Jennifer_Weekend_6PM_10 with Dissolve(0.5)
    MC "Ahhhh... I'm really in trouble now, aren't I?"
    scene Jennifer_Weekend_6PM_11 with Dissolve(0.5)
    Jennifer "Huh? What are you talking about?"
    scene Jennifer_Weekend_6PM_12 with Dissolve(0.5)
    Jennifer "Come here already! If people heard you talk like this, they'd think I beat you every day."
    scene Jennifer_Weekend_6PM_13 with Dissolve(0.5)
    MC "Uhhhh... and you don't?"
    scene Jennifer_Weekend_6PM_14 with Dissolve(0.5)
    Jennifer "Hihhhh-! Is that what you think?!"
    scene Jennifer_Weekend_6PM_15 with Dissolve(0.5)
    MC "No, no, no, I was just joking!"
    scene Jennifer_Weekend_6PM_16 with Dissolve(0.5)
    Jennifer "You know very well that I've never put my hands on you! I don't even know where you got that idea from!"
    scene Jennifer_Weekend_6PM_17 with Dissolve(0.5)
    MC "Uuuuu... I don't know about \"never\"... \"Never\" is a pretty strong word, don't you think?"
    scene Jennifer_Weekend_6PM_18 with Dissolve(0.5)
    Jennifer "Ah, I see what we're doing, funny guy."
    scene Jennifer_Weekend_6PM_19 with Dissolve(0.5)
    Jennifer "Then, since you got time for jokes, grab me the mop."
    scene Jennifer_Weekend_6PM_20 with Dissolve(0.5)
    Jennifer "It fell."
    scene Jennifer_Weekend_6PM_21 with Dissolve(0.5)
    MC "Uhhhh... okay..."
    scene Jennifer_Weekend_6PM_22 with Dissolve(0.5)
    MC "A bit petty don't you think?"
    scene Jennifer_Weekend_6PM_23 with Dissolve(0.5)
    Jennifer "You wouldn't want your old mom to break her back over it, would you?"
    scene Jennifer_Weekend_6PM_24 with Dissolve(0.5)
    MC "Oh, c'mon, I told you it was a jo-"
    scene Jennifer_Weekend_6PM_25 with Dissolve(0.5)
    MC "AAAAAAAGHHHHH!!!"
    scene Jennifer_Weekend_6PM_26 with Dissolve(0.5)
    Jennifer "Never call your mama old! Not even as a joke!"
    scene Jennifer_Weekend_6PM_27 with Dissolve(0.5)
    Jennifer "Mmmmmmm!"
    scene BlackScreen with Dissolve(1)
    call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
    $ Location = "garden1"
    $ advance_time_or_sleep()
