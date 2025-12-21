init python:
    define_images("Isabella_weekend_6AM_", "WeekendScenes/IsabellaScenes/6AM", "Isabella_weekend_6AM_", 100)

label Isabella_weekend_6AM:
    scene Isabella_weekend_6AM_1 with Dissolve(0.5)
    MC "{color=#808080}*She is still sleeping...*{/color}"
    MC "{color=#808080}*I don't think it's a good idea to wake her up...*{/color}"
    menu:
        "Wake her up":
            scene Isabella_weekend_6AM_3 with Dissolve(0.5)
            MC "{color=#808080}*Let's just hope she won't kill me for this.*{/color}"
            scene Isabella_weekend_6AM_4 with Dissolve(0.5)
            MC "Pssst... Isabella... Wake up..."
            scene Isabella_weekend_6AM_5 with Dissolve(0.5)
            Isabella "......*snore*......"
            scene Isabella_weekend_6AM_6 with Dissolve(0.5)
            MC "{color=#808080}*Yeah... No way she's waking up*{/color}"
            scene Isabella_weekend_6AM_7 with Dissolve(0.5)
            MC "{color=#808080}*But maybe that's not such a bad thing...*{/color}"
            scene Isabella_weekend_6AM_8 with Dissolve(0.5)
            menu:
                "lift her robe":
                    scene Isabella_weekend_6AM_9 with Dissolve(0.5)
                    MC "{color=#808080}*Here goes nothing...*{/color}"
                    scene Isabella_weekend_6AM_10 with Dissolve(0.5)
                    Isabella "......*snore*......"
                    scene Isabella_weekend_6AM_11 with Dissolve(0.5)
                    MC "{color=#808080}*...this is probably a bad idea.*{/color}"
                    scene Isabella_weekend_6AM_12 with Dissolve(0.5)
                    Isabella "Hmmm..."
                    scene Isabella_weekend_6AM_13 with Dissolve(0.5)
                    Isabella "{color=#808080}*What the...*{/color}"
                    scene Isabella_weekend_6AM_14 with Dissolve(0.5)
                    MC "{color=#808080}*Whistle*"
                    scene Isabella_weekend_6AM_15 with Dissolve(0.5)
                    Isabella "[MC]...?"
                    scene Isabella_weekend_6AM_16 with Dissolve(0.5)
                    MC "Oh, hey Isa! What a coincidence finding you here! Good morning!"
                    MC "Do you come here often?"
                    scene Isabella_weekend_6AM_17 with Dissolve(0.5)
                    Isabella "Ummm... yeah..."
                    Isabella "I'm calling the police."
                    scene Isabella_weekend_6AM_18 with Dissolve(0.5)
                    MC "Wait what?! Jumping straight to the police?! You're not even calling for mom first?!"
                    scene Isabella_weekend_6AM_19 with Dissolve(0.5)
                    Isabella "No thanks, I hope you know how to hold that soap bar tight."
                    scene Isabella_weekend_6AM_20 with Dissolve(0.5)
                    MC "Wait a second, hold up, we can talk about this!"
                    scene Isabella_weekend_6AM_21 with Dissolve(0.5)
                    Isabella "Let's see how you'll enjoy having a grown ass man watch you sleep!"
                    scene Isabella_weekend_6AM_22 with Dissolve(0.5)
                    MC "I was not! Wait... we can talk about this!"
                    scene Isabella_weekend_6AM_23 with Dissolve(0.5)
                    Jennifer "Yaaaawn...."
                    scene Isabella_weekend_6AM_24 with Dissolve(0.5)
                    Jennifer "Huh?"
                    scene Isabella_weekend_6AM_25 with Dissolve(0.5)
                    $ renpy.pause(0.2, hard=True)
                    scene Isabella_weekend_6AM_26 with Dissolve(0.5)
                    $ renpy.pause(0.2, hard=True)
                    scene Isabella_weekend_6AM_25 with Dissolve(0.5)
                    $ renpy.pause(0.2, hard=True)
                    scene Isabella_weekend_6AM_27 with Dissolve(0.5)
                    Jennifer "Kids, stop fighting in there!"
                    scene Isabella_weekend_6AM_28 with Dissolve(0.5)
                    IsaAndMC "WE ARE NOT FIGHTING, MOM!!!"
                    scene Isabella_weekend_6AM_29 with Dissolve(0.5)
                    Jennifer "Tsk!! Why are you two always fighting?!"
                    scene Isabella_weekend_6AM_30 with Dissolve(0.5)
                    Jennifer "IT'S 6AM, FOR GOD'S SAKE!"
                    scene Isabella_weekend_6AM_31 with Dissolve(0.5)
                    Isabella "Good morning, mommy!"
                    scene Isabella_weekend_6AM_32 with Dissolve(0.5)
                    MC "Have a wonderful start of the day, birth giver!"
                    scene Isabella_weekend_6AM_33 with Dissolve(0.5)
                    Isabella "What the hell are you saying?!"
                    scene Isabella_weekend_6AM_34 with Dissolve(0.5)
                    Jennifer "Mhmph..."
                    scene Isabella_weekend_6AM_35 with Dissolve(0.5)
                    Jennifer "....."
                    scene Isabella_weekend_6AM_36 with Dissolve(0.5)
                    Jennifer "....."
                    scene Isabella_weekend_6AM_37 with Dissolve(0.5)
                    Jennifer "Go to your room, [MC]..."
                    scene Isabella_weekend_6AM_38 with Dissolve(0.5) 
                    Jennifer "And you, Isabella, Clean your room!"
                    scene Isabella_weekend_6AM_39 with Dissolve(0.5) 
                    Isabella "Sure thing, mommy!"
                    scene Isabella_weekend_6AM_40 with Dissolve(0.5)
                    MC "As you wish, my lady!"
                    scene Isabella_weekend_6AM_34 with Dissolve(0.5)
                    Jennifer "Mhmph..."
                    scene Isabella_weekend_6AM_35 with Dissolve(0.5)
                    Jennifer "....."
                    scene Isabella_weekend_6AM_36 with Dissolve(0.5)
                    Jennifer "....."
                    scene Isabella_weekend_6AM_41 with Dissolve(0.5)
                    Jennifer "....."
                    scene Isabella_weekend_6AM_42 with Dissolve(0.5)
                    IsaAndMC "....."
                    scene Isabella_weekend_6AM_43 with Dissolve(0.5)
                    Isabella "Yeah, the pizza is armed and aggressive... And unusually short for its age..."
                    scene Isabella_weekend_6AM_44 with Dissolve(0.5)
                    MC "Wait! Stop! Are you crazy?!"
                    call stat_reward({"Isabella": {"love": -2, "corruption": 2}}, return_to=None)
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "leave":
                    MC "{color=#808080}*I better leave...*{/color}"
                    MC "{color=#808080}*She'll go crazy if she wakes up and sees me...*{/color}"
                    call stat_reward({"Isabella": {"love": 2}}, return_to=None)
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Leave her alone":
            scene Isabella_weekend_6AM_2 with Dissolve(0.5)
            MC "{color=#808080}*I should let her sleep...*{/color}"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")