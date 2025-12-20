init python:
    define_images("Isabella_weekend_12PM_", "WeekendScenes/IsabellaScenes/12PM", "Isabella_weekend_12PM_", 100)
    renpy.image("Isabella_weekend_12PM_Video_1", Movie(play="images/WeekendScenes/IsabellaScenes/12PM/Isabella_weekend_12PM_Video_1.webm", loop=True, group="pov_group"))
label Isabella_weekend_12PM:
    scene Isabella_weekend_12PM_1 with Dissolve(0.5)
    Isabella "Are you sure you don't want to do it in the weekends as well?"
    Isabella "I mean, you could make much more money."
    scene Isabella_weekend_12PM_2 with Dissolve(0.5)
    Criss "That's a pretty nice way to say that you don't want me over the weekends anymore."
    scene Isabella_weekend_12PM_3 with Dissolve(0.5)
    Isabella "Girl, don't even joke around with that."
    Isabella "If you leave me a full day alone in this nuthouse I'll go crazy."
    scene Isabella_weekend_12PM_4 with Dissolve(0.5)
    Criss "Then don't ask me to work on weekends."
    scene Isabella_weekend_12PM_5 with Dissolve(0.5)
    MC "GHAAAAHHH!!"
    scene Isabella_weekend_12PM_6 with Dissolve(0.5)
    MC "What a crazy and insane coincidence. No way you two are here as well!"
    scene Isabella_weekend_12PM_7 with Dissolve(0.5)
    Isabella "Ahhh... great, a beggar."
    scene Isabella_weekend_12PM_8 with Dissolve(0.5)
    Isabella "Do you have some change, Crissy? Maybe he'll leave us alone."
    scene Isabella_weekend_12PM_9 with Dissolve(0.5)
    MC "That's pretty rude, don't you think?"
    scene Isabella_weekend_12PM_10 with Dissolve(0.5)
    Isabella "It is, I'm sorry. I think it's the glasses. I can't stop being a bitch when I have them on."
    scene Isabella_weekend_12PM_11 with Dissolve(0.5)
    MC "It's okay, I'll let it slide this time, you kinda remind me of someone else when you have them on."
    scene Isabella_weekend_12PM_12 with Dissolve(0.5)
    Isabella "I'll pretend I didn't hear that."
    scene Isabella_weekend_12PM_13 with Dissolve(0.5)
    MC "Anyway, what were you girls talking about? Or am I prying in too much?"
    scene Isabella_weekend_12PM_14 with Dissolve(0.5)
    pause
    scene Isabella_weekend_12PM_15 with Dissolve(0.5)
    Isabella "Eh, you know, just gossiping like girlies. And yeah, you're butting in too much."
    scene Isabella_weekend_12PM_16 with Dissolve(0.5)
    MC "Ahhh, I see, so you were talking about me."
    scene Isabella_weekend_12PM_17 with Dissolve(0.5)
    Isabella "Hah, big ego much? You're not thaaat important, you know?"
    scene Isabella_weekend_12PM_18 with Dissolve(0.5)
    Isabella "Crissy, dear, this new pool boy kinda sucks. Should we get a new one?"
    scene Isabella_weekend_12PM_19 with Dissolve(0.5)
    Criss "Uhhh... ummm... I-"
    scene Isabella_weekend_12PM_20 with Dissolve(0.5)
    MC "Oh, my, I'm so sorry ma'am. I'll begin right away, starting with the bottom of the pool."
    scene Isabella_weekend_12PM_21 with Dissolve(0.5)
    Isabella "Mhm, that's what I thought. I don't have all day, so get to work."
    scene Isabella_weekend_12PM_22 with Dissolve(0.5)
    Criss "Ummm... Isa? Are you sure about this?"
    scene Isabella_weekend_12PM_23 with Dissolve(0.5)
    Isabella "This is just how we banter, Criss. Of course I don't tell him to clean the pool."
    scene Isabella_weekend_12PM_24 with Dissolve(0.5)
    Criss "Yeah, I know, I'm saying that he went right under you..."
    scene Isabella_weekend_12PM_25 with Dissolve(0.5)
    MC "{color=#808080}Target acquired.*"
    scene Isabella_weekend_12PM_26 with Dissolve(0.5)
    Isabella "And I'm in a pretty compromising position too..."
    scene Isabella_weekend_12PM_27 with Dissolve(0.5)
    MC "{color=#808080}Locking in.*"
    scene Isabella_weekend_12PM_28 with Dissolve(0.5)
    Isabella "*Chuckles* I'm in danger."
    scene Isabella_weekend_12PM_29 with Dissolve(0.5)
    MC "{color=#808080}Engaging.*"
    scene Isabella_weekend_12PM_30 with Dissolve(0.5)
    Isabella "Help?"
    scene Isabella_weekend_12PM_31 with Dissolve(0.5)
    MC "{color=#808080}One thousand years of death!*"
    scene Isabella_weekend_12PM_32 with Dissolve(0.5)
    Isabella "KYAAAAAAAAAAAAAAAAAA!!!!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**You run as fast as you can**"
    "{color=#808080}**Isabella love - 5**"
    "{color=#808080}**Criss love - 2**"
    "{color=#808080}**Criss Corruption + 2**"
    "{color=#808080}**Isabella corruption + 2**"
    $ Isabella_love = Isabella_love - 5
    $ Criss_love = Criss_love - 2
    $ Criss_Corruption = Criss_Corruption + 2
    $ Isabella_Corruption = Isabella_Corruption + 2
    $ check_and_update_character_stats("Isabella")
    $ check_and_update_character_stats("Criss")
    $ Location = "Entrance"
    $ advance_time_or_sleep()
