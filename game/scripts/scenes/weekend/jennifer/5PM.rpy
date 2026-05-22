init python:
    define_images("Jennifer_weekend_5PM_", "WeekendScenes/JenniferScenes/5PM", "Jennifer_weekend_5PM_", 100)

screen jennifer_5pm_mc_line():
    window:
        style "say_window"

        text "No, no, it's nothing, I thought I saw something." style "say_dialogue"

label Jennifer_weekend_5PM:
    scene Jennifer_weekend_5PM_1 with Dissolve(0.5)
    Jennifer "Mm-mm-mm..."
    scene Jennifer_weekend_5PM_2 with Dissolve(0.5)
    Jennifer "Hm-hm-hm..."
    scene Jennifer_weekend_5PM_3 with Dissolve(0.5)
    MC "GAAHHHHH!"
    scene Jennifer_weekend_5PM_4 with Dissolve(0.5)
    Jennifer "Oh my, honey, you startled me! I told you to stop scaring me like that!"
    scene Jennifer_weekend_5PM_5 with Dissolve(0.5)
    Jennifer "What, do I have something on me? Or why that reaction?"
    show screen jennifer_5pm_mc_line
    scene Jennifer_weekend_5PM_6 with Dissolve(0.5)
    $ renpy.pause(0.3, hard=True)
    scene Jennifer_weekend_5PM_7 with Dissolve(0.2)
    $ renpy.pause(0.3, hard=True)
    scene Jennifer_weekend_5PM_6 with Dissolve(0.2)
    $ renpy.pause(0.3, hard=True)
    scene Jennifer_weekend_5PM_7 with Dissolve(0.2)
    $ renpy.pause(0.3, hard=True)
    scene Jennifer_weekend_5PM_6 with Dissolve(0.2)
    $ renpy.pause(0.3, hard=True)
    scene Jennifer_weekend_5PM_7 with Dissolve(0.2)
    $ renpy.pause(0.3, hard=True)
    hide screen jennifer_5pm_mc_line
    scene Jennifer_weekend_5PM_8 with Dissolve(0.5)
    Jennifer "Okay honey, whatever you say..."
    scene Jennifer_weekend_5PM_10 with Dissolve(0.5)
    MC "I just came to grab some water, I won't bother you!"
    scene Jennifer_weekend_5PM_11 with Dissolve(0.5)
    Jennifer "Sure thing, grab me a cup as well, please!"
    scene Jennifer_weekend_5PM_9
    pause
    # show text "{size=60}{color=#6b0000}BLEAAAAAAHHHH{/color}{/size}":
    #     xpos 0.5
    #     xanchor 0.5
    #     ypos 0.92
    #     yanchor 1.0
    # with Dissolve(1.5)
    # pause
    # hide text
    scene Jennifer_weekend_5PM_12 with Dissolve(0.5)
    Jennifer "Eeeeeeekkkk!"
    scene Jennifer_weekend_5PM_13 with Dissolve(0.5)
    Jennifer "[MC_upper], what are you doing?!"
    scene Jennifer_weekend_5PM_14 with Dissolve(0.5)
    MC "Yes, mother?"
    scene Jennifer_weekend_5PM_15 with Dissolve(0.5)
    Jennifer "Ughhh... I must be still waking up from my nap... sorry honey."
    Jennifer "Go get you water or whatever..."
    scene BlackScreen with Dissolve(1)
    call stat_reward({"Jennifer": {"corruption": 2}}, return_to=None)
    $ Location = "Entrance"
    $ advance_time_or_sleep()
