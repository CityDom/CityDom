init python:
    define_images("Isabella_weekend_11AM_", "WeekendScenes/IsabellaScenes/11AM", "Isabella_weekend_11AM_", 100)
    renpy.image("Isabella_weekend_11AM_Video_1", Movie(play="images/WeekendScenes/IsabellaScenes/11AM/Isabella_weekend_11AM_Video_1.webm", loop=True, group="pov_group"))
label Isabella_weekend_11AM:
    scene Isabella_weekend_11AM_1 with Dissolve(0.5)
    Criss "Are you sure it's still ok to wear this swimsuits?"
    Criss "You know... now that your brother is around..."
    scene Isabella_weekend_11AM_2 with Dissolve(0.5)
    Isabella "Eh, it is what it is I guess..."
    Isabella "It's not like we're gonna get new swimsuits just because he's here."
    scene Isabella_weekend_11AM_3 with Dissolve(0.5)
    Isabella "And I'm not wearing the ugly ass one from school."
    Isabella "Just imagine we're at the beach."
    scene Isabella_weekend_11AM_4 with Dissolve(0.5)
    Criss "Yeah... I guess you're right... I'll try to chill..."
    scene Isabella_weekend_11AM_5 with Dissolve(0.5)
    Criss "Huh...?"
    scene Isabella_weekend_11AM_6 with Dissolve(0.5)
    Criss "Uhhh..."
    Isabella "What?"
    scene Isabella_weekend_11AM_7 with Dissolve(0.5)
    Isabella "Ughh... great."
    scene Isabella_weekend_11AM_8 with Dissolve(0.5)
    MC "What?"
    scene Isabella_weekend_11AM_9 with Dissolve(0.5)
    Isabella "Nothing, never mind."
    Isabella "What do you want?"
    scene Isabella_weekend_11AM_10 with Dissolve(0.5)
    MC "God damn, what the fuck, what did I do?!"
    MC "Don't tell me you're turning into Claire."
    scene Isabella_weekend_11AM_11 with Dissolve(0.5)
    Isabella "You are so dense sometimes..."
    scene Isabella_weekend_11AM_12 with Dissolve(0.5)
    Isabella "..."
    scene Isabella_weekend_11AM_13 with Dissolve(0.5)
    MC "Hmm?"
    scene Isabella_weekend_11AM_14 with Dissolve(0.5)
    MC "Uhh?"
    scene Isabella_weekend_11AM_15 with Dissolve(0.5)
    pause
    scene Isabella_weekend_11AM_16 with Dissolve(0.5)
    MC "Aaaaaaa"
    scene Isabella_weekend_11AM_17 with Dissolve(0.5)
    Isabella "Tsk..."
    scene Isabella_weekend_11AM_18 with Dissolve(0.5)
    Isabella "Sorry Crissy, [MC] was just leaving."
    scene Isabella_weekend_11AM_19 with Dissolve(0.5)
    MC "No I'm not!"
    scene Isabella_weekend_11AM_20 with Dissolve(0.5)
    IsabellaW "What the fuck are you doing?!"
    scene Isabella_weekend_11AM_21 with Dissolve(0.5)
    MC "I'm around Isa, mom and Claire all the time"
    scene Isabella_weekend_11AM_22 with Dissolve(0.5)
    MC "And back at dads I had a stepmom and two stepsisters."
    scene Isabella_weekend_11AM_26 with Dissolve(0.5)
    Isabella "Shut up already!"
    scene Isabella_weekend_11AM_23 with Dissolve(0.5)
    MC "Basically, what I'm trying to say is... I'm pretty desensitized to this..."
    scene Isabella_weekend_11AM_24 with Dissolve(0.5)
    MC "So I guess you can think of me as one of the girls."
    scene Isabella_weekend_11AM_25 with Dissolve(0.5)
    MC "But that doesn't mean that I'm the gay best friend! One of the girls is the most I'll go with."
    scene Isabella_weekend_11AM_27 with Dissolve(0.5)
    Isabella "{color=#808080}*God damn it, [MC], you're scaring her!!*"
    Criss "t-teehee…"
    scene Isabella_weekend_11AM_28 with Dissolve(0.5)
    Isabella "Huh...?"
    scene Isabella_weekend_11AM_29 with Dissolve(0.5)
    Criss "haha—hehe—stop!"
    scene Isabella_weekend_11AM_30 with Dissolve(0.5)
    Criss "It's okay, one of the girls will do just fine!"
    scene Isabella_weekend_11AM_31 with Dissolve(0.5)
    MC "Hah, glad we cleared that up."
    MC "Now, tell me what drink I can get you two."
    scene Isabella_weekend_11AM_32 with Dissolve(0.5)
    Isabella "What the fuck is happening here?"
    scene Isabella_weekend_11AM_33 with Dissolve(0.5)
    Criss "Uhhh... Anything would be nice... I don't really have a preference."
    scene Isabella_weekend_11AM_34 with Dissolve(0.5)
    MC "Perfect, soda it is."
    scene Isabella_weekend_11AM_35 with Dissolve(0.5)
    MC "And you?"
    scene Isabella_weekend_11AM_36 with Dissolve(0.5)
    Isabella "..."
    scene Isabella_weekend_11AM_37 with Dissolve(0.5)
    Isabella "A coke... and get my shades as well, please."
    scene Isabella_weekend_11AM_38 with Dissolve(0.5)
    MC "You can get 'em yourself"
    scene Isabella_weekend_11AM_39 with Dissolve(0.5)
    Isabella "Excuse me?!"
    scene Isabella_weekend_11AM_40 with Dissolve(0.5)
    MC "I'm kidding, dummy, obviously..."
    scene BlackScreen with Dissolve(0.5)
    "..."
    scene Isabella_weekend_11AM_41 with Dissolve(0.5)
    MC "You are such a stalker, you know?"
    scene Isabella_weekend_11AM_42 with Dissolve(0.5)
    Mhyrorin "Oh, c'mon, don't be a meanie!"
    Mhyrorin "You did really good back there."
    scene Isabella_weekend_11AM_43 with Dissolve(0.5)
    MC "Wait, really? You think so?"
    scene Isabella_weekend_11AM_44 with Dissolve(0.5)
    Mhyrorin "Yeah, it was straight to the point and mature."
    Mhyrorin "You didn't come off as a creep."
    scene Isabella_weekend_11AM_45 with Dissolve(0.5)
    Mhyrorin "Aaaaand... there he goes..."
    show Isabella_weekend_11AM_Video_1 with Dissolve(0.5)
    MC "I'm so fucking mature..."
    MC "HMPH, HMPH, HMPH, HMPH, HMPH, HMPH!"
    scene Isabella_weekend_11AM_46 with Dissolve(0.5)
    Mhyrorin "At this point it's my fault for not learning to not compliment you."
    call stat_reward({"Criss": {"love": 2, "corruption": 2}, "Isabella": {"love": 2}}, return_to=None)
    $ Location = "Entrance"
    $ advance_time_or_sleep()
