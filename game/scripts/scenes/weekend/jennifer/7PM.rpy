init python:
    define_images("Jennifer_Weekend_7PM_", "WeekendScenes/JenniferScenes/7PM", "Jennifer_Weekend_7PM_", 200)
    for i in range(1, 8):
        renpy.image(
            "Jennifer_Weekend_7PM_Euphoria_%02d" % i,
            "WeekendScenes/JenniferScenes/7PM/Jennifer_Weekend_7PM_Euphoria_%02d.png" % i
        )
    renpy.image(
        "Jennifer_Weekend_7PM_movie_1",
        Movie(
            play="images/WeekendScenes/JenniferScenes/7PM/Jennifer_Weekend_7PM_movie_1.webm",
            loop=False,
            group="pov_group"
        )
    )
    

define sensual_dissolve = Dissolve(1.0)
define sensual_fade = Fade(0.4, 0.1, 0.8, color="#000")


transform slow_push_in:
    zoom 1.03
    xalign 0.5
    yalign 0.5
    linear 2.6 zoom 1.08


transform slow_pull_back:
    zoom 1.09
    xalign 0.5
    yalign 0.5
    linear 2.6 zoom 1.03


transform slow_pan_left:
    zoom 1.08
    xalign 0.62
    yalign 0.5
    linear 2.8 xalign 0.38


transform slow_pan_right:
    zoom 1.08
    xalign 0.38
    yalign 0.5
    linear 2.8 xalign 0.62


transform subtle_hold:
    zoom 1.04
    xalign 0.5
    yalign 0.5
    linear 2.4 zoom 1.055


transform euphoria_drift_left:
    zoom 1.18
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 0.04 alpha 1.0
    linear 0.26 zoom 1.28 xalign 0.46 yalign 0.53


transform euphoria_drift_right:
    zoom 1.18
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 0.04 alpha 1.0
    linear 0.26 zoom 1.28 xalign 0.54 yalign 0.47


transform euphoria_bloom:
    zoom 1.22
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.34 zoom 1.36


transform reveal_punch:
    zoom 1.08
    xalign 0.5
    yalign 0.5
    alpha 0.0
    xoffset 0

    linear 0.03 alpha 1.0

    parallel:
        easeout 0.25 zoom 1.0

    parallel:
        ease 0.03 xoffset 18
        ease 0.03 xoffset -18
        ease 0.04 xoffset 10
        ease 0.04 xoffset -6
        ease 0.05 xoffset 0


transform sensual_pose_left:
    zoom 1.04
    xalign 0.54
    yalign 0.5
    linear 2.0 zoom 1.10 xalign 0.46


transform sensual_pose_right:
    zoom 1.04
    xalign 0.46
    yalign 0.5
    linear 2.0 zoom 1.10 xalign 0.54


transform sensual_pose_hold:
    zoom 1.03
    xalign 0.5
    yalign 0.5
    linear 2.1 zoom 1.10


transform sensual_pose_out_left:
    zoom 1.10
    xalign 0.46
    yalign 0.5
    linear 2.0 zoom 1.04 xalign 0.54


transform sensual_pose_out_right:
    zoom 1.10
    xalign 0.54
    yalign 0.5
    linear 2.0 zoom 1.04 xalign 0.46


transform slap_aftershock:
    xalign 0.5
    yalign 0.5
    zoom 1.02
    xoffset 0
    yoffset 0
    ease 0.03 xoffset -28 yoffset 8
    ease 0.04 xoffset 22 yoffset -6
    ease 0.05 xoffset -14 yoffset 4
    ease 0.06 xoffset 8 yoffset -2
    ease 0.08 xoffset 0 yoffset 0 zoom 1.0


transform slap_star_orbit(xpos_value, ypos_value, delay_value):
    xpos xpos_value
    ypos ypos_value
    xanchor 0.5
    yanchor 0.5
    alpha 0.0
    zoom 0.65
    pause delay_value
    parallel:
        linear 0.12 alpha 1.0
        pause 1.20
        linear 0.80 alpha 0.0
    parallel:
        easeout 2.12 ypos ypos_value - 85 xpos xpos_value + 70
    parallel:
        linear 2.12 rotate 720 zoom 1.15

screen Jennifer_Weekend_7PM_BodyMap():

    modal True

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_feet_mask.png"
        action Return("feet")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_calves_mask.png"
        action Return("calves")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_thighs_mask.png"
        action Return("thighs")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_ass_mask.png"
        action Return("ass")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_back_mask.png"
        action Return("back")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_breast_mask.png"
        action Return("breast")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_arms_mask.png"
        action Return("arms")

    imagebutton:
        idle Null(1920, 1080)
        focus_mask "gui/bodymaps/jennifer_weekend_7pm/jennifer_7pm_head_mask.png"
        action Return("head")

label Jennifer_Weekend_7PM:

    scene Jennifer_Weekend_7PM_1 at slow_push_in with sensual_fade
    pause 2.4

    scene black with Dissolve(0.25)
    pause 0.15
    scene Jennifer_Weekend_7PM_2 at slow_pan_left with Dissolve(0.8)
    pause 2.3

    scene Jennifer_Weekend_7PM_3 at slow_pan_right with sensual_dissolve
    pause 2.3

    scene black with Dissolve(0.25)
    pause 0.15
    scene Jennifer_Weekend_7PM_4 at slow_pull_back with Dissolve(0.8)
    pause 2.4

    scene Jennifer_Weekend_7PM_5 at subtle_hold with sensual_dissolve
    pause 2.2

    scene Jennifer_Weekend_7PM_6 at slow_push_in with sensual_dissolve
    pause 2.5

    scene Jennifer_Weekend_7PM_7 with Dissolve(0.5)
    Mhyrorin "Grown ass man cannon balling..."
    scene Jennifer_Weekend_7PM_8 with Dissolve(0.5)
    MC "There is a higher purpose in my ways of life."
    scene Jennifer_Weekend_7PM_9 with Dissolve(0.5)
    Mhyrorin "Whatever you say... try not to break something..."
    scene Jennifer_Weekend_7PM_10 with Dissolve(0.5)
    Jennifer "...."
    scene Jennifer_Weekend_7PM_11 with Dissolve(0.5)
    Jennifer "Hmm?"
    scene Jennifer_Weekend_7PM_13 with Dissolve(0.5)
    Jennifer "GAHHH!!"
    scene Jennifer_Weekend_7PM_14 with Dissolve(0.5)
    MC "Hey mom! You finally decided to relax a bit?"
    scene Jennifer_Weekend_7PM_15 with Dissolve(0.5)
    Jennifer "Maybe the whole gentle parenting thing wasn't the best idea..."
    scene Jennifer_Weekend_7PM_16 with Dissolve(0.5)
    MC "Huh? What did you say? I didn't hear you."
    scene Jennifer_Weekend_7PM_17 with Dissolve(0.5)
    Jennifer "I said you're lucky that you're my only boy..."
    scene Jennifer_Weekend_7PM_18 with Dissolve(0.5)
    MC "\"You're lucky to have me as your only boy\"? Awww, thanks mom!"
    scene Jennifer_Weekend_7PM_19 with Dissolve(0.5)
    Jennifer "Yeah, you might still have some water in your ears..."
    scene Jennifer_Weekend_7PM_20 with Dissolve(0.5)
    MC "Oh, wait, I think I actually do! How did you know?"
    scene Jennifer_Weekend_7PM_21 with Dissolve(0.5)
    Jennifer "Mother's intuition..."
    scene Jennifer_Weekend_7PM_22 with Dissolve(0.5)
    Jennifer "Anyway..."
    scene Jennifer_Weekend_7PM_23 with Dissolve(0.5)
    Jennifer "What do you need from mommy?"
    scene Jennifer_Weekend_7PM_24 with Dissolve(0.5)
    MC "Uhhh... nothing. I just saw you relax, which is not often, so I thought we could hang out!"
    scene Jennifer_Weekend_7PM_25 with Dissolve(0.5)
    Jennifer "Hahaha, really?"
    scene Jennifer_Weekend_7PM_26 with Dissolve(0.5)
    Jennifer "Then you can help me with a little something, right?"
    scene Jennifer_Weekend_7PM_27 with Dissolve(0.5)
    MC "Uhhh... I'm in big trouble, aren't I?"
    scene Jennifer_Weekend_7PM_28 with Dissolve(0.5)
    Jennifer "Big trouble! You have to give me a massage!"
    scene Jennifer_Weekend_7PM_29 with Dissolve(0.5)
    MC "Huh?"
    scene Jennifer_Weekend_7PM_30 with Dissolve(0.5)
    Mhyrorin "Huh?"
    scene Jennifer_Weekend_7PM_31 with Dissolve(0.5)
    Jennifer "Hahahahahahaha, I knew it! The girls always hate it when I make them massage me!"
    scene Jennifer_Weekend_7PM_32 with Dissolve(0.5)
    MC "Uhhhh..."
    scene Jennifer_Weekend_7PM_34 with Dissolve(0.5)
    MC "What is happening?"
    scene Jennifer_Weekend_7PM_33 with Dissolve(0.5)
    MC "Am I at the hidden camera or something?"
    scene Jennifer_Weekend_7PM_35 with Dissolve(0.5)
    Jennifer "I'm just kidding honey, you don't have to do it. We can just relax together."
    scene Jennifer_Weekend_7PM_36 with Dissolve(0.5)
    pause 0.5
    scene Jennifer_Weekend_7PM_37 
    pause 0.1
    scene Jennifer_Weekend_7PM_36
    pause 0.1
    scene Jennifer_Weekend_7PM_37
    pause 0.1
    scene Jennifer_Weekend_7PM_36
    pause 0.1
    scene Jennifer_Weekend_7PM_37
    pause 0.1
    scene Jennifer_Weekend_7PM_36
    pause 0.1
    scene Jennifer_Weekend_7PM_37
    pause 0.1
    scene Jennifer_Weekend_7PM_36
    pause
    scene Jennifer_Weekend_7PM_38 with Dissolve(0.5)
    MC "AHHH!! NO MOM, PLEASE!! ANYTHING BUT THAT!! PLEASEEE!!"
    scene Jennifer_Weekend_7PM_39 with Dissolve(0.5)
    Jennifer "Uhhh... it's okay, I told you I was kidding..."
    scene Jennifer_Weekend_7PM_40 with Dissolve(0.5)
    MC "AHHHHHHH!!! THE AGONY!! PLEASE MOM!!!"
    scene Jennifer_Weekend_7PM_41 with Dissolve(0.5)
    Jennifer "..."
    scene Jennifer_Weekend_7PM_42 with Dissolve(0.5)
    MC "Oh mother... why hast thou forsaken me..."
    scene Jennifer_Weekend_7PM_43 with Dissolve(0.5)
    Jennifer "Hah?"
    scene Jennifer_Weekend_7PM_44 with Dissolve(0.5)
    MC "Daga shikashi…!"
    scene Jennifer_Weekend_7PM_45 with Dissolve(0.5)
    MC "A man has to face the consequences of his actions!"
    scene Jennifer_Weekend_7PM_46 with Dissolve(0.5)
    Jennifer "Where are you even learning these words from?"
    scene Jennifer_Weekend_7PM_47 with Dissolve(0.5)
    MC "I decided. I will do it!"
    scene Jennifer_Weekend_7PM_48 with Dissolve(0.5)
    Jennifer "Okay honey, don't say I forced you into it."
    scene Jennifer_Weekend_7PM_49 with Dissolve(0.5)
    Jennifer "I will sit on my stomach, okay?"
    scene Jennifer_Weekend_7PM_50 with Dissolve(0.5)
    MC "Okay, it's fine with me, that's why I was straightening the chair for you."
    scene Jennifer_Weekend_7PM_51 with Dissolve(0.5)
    MC "Is it okay like this?"
    scene Jennifer_Weekend_7PM_52 with Dissolve(0.5)
    Jennifer "Yes, honey, that's perfect, thanks!"
    scene Jennifer_Weekend_7PM_53 with Dissolve(0.5)
    MC "Do you want me to grab the lotion or something?"
    scene Jennifer_Weekend_7PM_54 with Dissolve(0.5)
    Jennifer "No, no, it's fine, I'm full of sunscreen already."
    scene Jennifer_Weekend_7PM_55 with Dissolve(0.5)
    MC "Ahan, aham, oke..."
    scene Jennifer_Weekend_7PM_56 with Dissolve(0.5)
    MC "I'll go ahead and start then..."
    scene Jennifer_Weekend_7PM_57 with Dissolve(0.5)
    jump Jennifer_Weekend_7PM_MassageChoice

label Jennifer_Weekend_7PM_MassageChoice:

    $ default_mouse = "reach"
    call screen Jennifer_Weekend_7PM_BodyMap
    $ default_mouse = "default"

    if _return == "feet":
        jump Jennifer_Weekend_7PM_Feet
    elif _return == "calves":
        jump Jennifer_Weekend_7PM_Calves
    elif _return == "thighs":
        jump Jennifer_Weekend_7PM_Thighs
    elif _return == "ass":
        jump Jennifer_Weekend_7PM_Ass
    elif _return == "back":
        jump Jennifer_Weekend_7PM_Back
    elif _return == "breast":
        jump Jennifer_Weekend_7PM_Breast
    elif _return == "arms":
        jump Jennifer_Weekend_7PM_Arms
    elif _return == "head":
        jump Jennifer_Weekend_7PM_Head

label Jennifer_Weekend_7PM_Feet:

    scene Jennifer_Weekend_7PM_58 with Dissolve(0.5)
    Jennifer "Ahhhh, that's perfect!"
    scene Jennifer_Weekend_7PM_60 with Dissolve(0.5)
    MC "...."
    scene Jennifer_Weekend_7PM_59 with Dissolve(0.5)
    MC "Soooo.... Why do you never do your pedicure?"
    scene Jennifer_Weekend_7PM_61 with Dissolve(0.5)
    MC "Isa does them all the time. I would've thought she took that from you."
    scene Jennifer_Weekend_7PM_62 with Dissolve(0.5)
    Jennifer "Ohhh, honey, I'm too old for that. Things like this are the last of my worries."
    scene Jennifer_Weekend_7PM_63 with Dissolve(0.5)
    MC "Well, don't think about it like something to worry about. You could use it as an excuse to spend some time with Isa for example."
    scene Jennifer_Weekend_7PM_64 with Dissolve(0.5)
    MC "You always say that you barely see her throughout the day."
    scene Jennifer_Weekend_7PM_65 with Dissolve(0.5)
    Jennifer "Hmmm... you know what? That's not a bad idea..."
    scene Jennifer_Weekend_7PM_66 with Dissolve(0.5)
    MC "Hah! That's a first!"
    scene Jennifer_Weekend_7PM_67 with Dissolve(0.5)
    MC "By the way, I have no idea what I'm doing here..."
    scene Jennifer_Weekend_7PM_68 with Dissolve(0.5)
    Jennifer "It doesn't matter... it feels good..."
    call stat_reward({"Jennifer": {"love": 2, "corruption": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Calves:

    scene Jennifer_Weekend_7PM_69 with Dissolve(0.5)
    MC "Is this alright?"
    scene Jennifer_Weekend_7PM_70 with Dissolve(0.5)
    Jennifer "Yes, honey. Are you sitting fine? I don't want you to be uncomfortable..."
    scene Jennifer_Weekend_7PM_71 with Dissolve(0.5)
    MC "Huh? Me? Oh, don't worry, I am sitting first row and center."
    scene Jennifer_Weekend_7PM_72 with Dissolve(0.5)
    Jennifer "Huh?"
    scene Jennifer_Weekend_7PM_73 with Dissolve(0.5)
    MC "Nothing!"
    scene Jennifer_Weekend_7PM_74 with Dissolve(0.5)
    MC "Anyway... What do-"

    scene black

    show Jennifer_Weekend_7PM_75 as glitch_img:
        xoffset -35
        yoffset 5
    pause 0.04

    show Jennifer_Weekend_7PM_74 as glitch_img:
        xoffset 25
        yoffset -5
    pause 0.03

    hide glitch_img
    pause 0.03

    show Jennifer_Weekend_7PM_75 as glitch_img:
        xoffset 45
        yoffset -8
    pause 0.04

    show Jennifer_Weekend_7PM_74 as glitch_img:
        xoffset -20
        yoffset 6
    pause 0.04

    scene Jennifer_Weekend_7PM_75 with Dissolve(0.12)
    Mhyrorin "You know what I just realized?!"
    scene Jennifer_Weekend_7PM_76 with Dissolve(0.5)
    MC "GAAAAAHHHH!!!"
    scene Jennifer_Weekend_7PM_77 with Dissolve(0.5)
    MCW "What the fuck are you doing here!?"
    scene Jennifer_Weekend_7PM_78 with Dissolve(0.5)
    Mhyrorin "You've never asked me if I wanted a massage before! Why is that?!"
    scene Jennifer_Weekend_7PM_79 with Dissolve(0.5)
    MC "Huh...?"
    scene Jennifer_Weekend_7PM_80 with Dissolve(0.5)
    MC "Bitch, are you stupid!? Couldn't this have waited until I was done here?!"
    scene Jennifer_Weekend_7PM_81 with Dissolve(0.5)
    Jennifer "What were you gonna say, honey?"
    scene Jennifer_Weekend_7PM_82 with Dissolve(0.5)
    MC "Uhhh... nothing really... I thought I saw something but it was nothing."
    scene Jennifer_Weekend_7PM_83 with Dissolve(0.5)
    MC "I'll give you a massage after this."
    MC "Or just ask me whenever, I don't mind!"
    scene Jennifer_Weekend_7PM_84 with Dissolve(0.5)
    Mhyrorin "Hmmmm..."
    scene Jennifer_Weekend_7PM_85 with Dissolve(0.5)
    Mhyrorin "Awwwwww!!! Really?!!!! You're so sweeeeet!!"

    scene black

    show Jennifer_Weekend_7PM_86 as glitch_img:
        xoffset -35
        yoffset 5
    pause 0.04

    show Jennifer_Weekend_7PM_85 as glitch_img:
        xoffset 25
        yoffset -5
    pause 0.03

    hide glitch_img
    pause 0.03

    show Jennifer_Weekend_7PM_86 as glitch_img:
        xoffset 45
        yoffset -8
    pause 0.04

    show Jennifer_Weekend_7PM_85 as glitch_img:
        xoffset -20
        yoffset 6
    pause 0.04

    scene Jennifer_Weekend_7PM_86 with Dissolve(0.12)
    MC "...."
    call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Thighs:

    scene Jennifer_Weekend_7PM_87 with Dissolve(0.5)
    MC "I'm starting to see why the girls hate this..."
    scene Jennifer_Weekend_7PM_88 with Dissolve(0.5)
    MC "Maybe this should be my punishment every time I do something bad..."
    scene Jennifer_Weekend_7PM_87 with Dissolve(0.5)
    MC "Maybe I did break that vase back then..."
    scene Jennifer_Weekend_7PM_89 with Dissolve(0.5)
    Jennifer "Hihhhhhh-! So you were the one who broke it?!"
    scene Jennifer_Weekend_7PM_90 with Dissolve(0.5)
    MC "Wait what?! No way you remember that! Really?"
    scene Jennifer_Weekend_7PM_91 with Dissolve(0.5)
    Jennifer "Hahaha, of course I remember!"
    Jennifer "You dropped it in front of me and then told me it wasn't you!"
    scene Jennifer_Weekend_7PM_92 with Dissolve(0.5)
    MC "Ohh... Uhhh... Yeah I don't remember that at all..."
    scene Jennifer_Weekend_7PM_93 with Dissolve(0.5)
    MC "It was Isa a hundred percent!"
    scene Jennifer_Weekend_7PM_94 with Dissolve(0.5)
    Jennifer "Huh?!"
    scene Jennifer_Weekend_7PM_95 with Dissolve(0.5)
    Jennifer "[MC]! Be careful with your hands! What are you doing?!"
    scene Jennifer_Weekend_7PM_96 with Dissolve(0.5)
    MC "What?"
    scene Jennifer_Weekend_7PM_97 with Dissolve(0.5)
    MC "Oh, sorry, I got lost in the conversation..."
    scene Jennifer_Weekend_7PM_95 with Dissolve(0.5)
    Jennifer "Pay more attention, okay?!"
    call stat_reward({"Jennifer": {"love": 2, "corruption": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Ass:

    scene Jennifer_Weekend_7PM_98 with Dissolve(0.5)
    MC "{color=#808080}*Ughhhh... God give me strength, give me a sign, guide me!*"
    scene Jennifer_Weekend_7PM_99 with Dissolve(0.5)
    MhyrorinDemon "What are you waiting for?! Grab it!"
    scene Jennifer_Weekend_7PM_100 with Dissolve(0.5)
    MC "{color=#808080}*Ahhh... I see... it's the voice of reason!*"
    scene Jennifer_Weekend_7PM_101 with Dissolve(0.5)
    MhyrorinDemon "Isn't this what you always wanted to do?! This is the perfect chance!"
    scene Jennifer_Weekend_7PM_102 with Dissolve(0.5)
    MhyrorinDemon "Or are you just going to bitch out?! Like the virgin loser that you are?!"
    scene Jennifer_Weekend_7PM_103 with Dissolve(0.5)
    MC "{color=#808080}*Such good arguments, it's hard to refute the logic!*"
    scene Jennifer_Weekend_7PM_104 with Dissolve(0.5)
    Mhyrorin "Did he finally lose his mind?"
    scene Jennifer_Weekend_7PM_105 with Dissolve(0.5)
    Mhyrorin "Just over her ass? Really?"
    scene Jennifer_Weekend_7PM_106 with Dissolve(0.5)
    Mhyrorin "I mean... it's huge, but still..."
    scene Jennifer_Weekend_7PM_107 with Dissolve(0.5)
    MhyrorinAngel "Wait! Listen to me!"
    scene Jennifer_Weekend_7PM_112 with Dissolve(0.5)
    MhyrorinAngel "Tsk, don't listen to that bitch... she's crazy!"
    scene Jennifer_Weekend_7PM_108 with Dissolve(0.5)
    MC "{color=#808080}*Is that...?*"
    scene Jennifer_Weekend_7PM_109 with Dissolve(0.5)
    MhyrorinAngel "Halt for but a moment my dear child!"
    scene Jennifer_Weekend_7PM_110 with Dissolve(0.5)
    MC "{color=#808080}*Damn, what do you want?! You can't change my mind now!*"
    scene Jennifer_Weekend_7PM_111 with Dissolve(1.5)
    show text "{size=60}{color=#6b0000}Fuck her brains out!{/color}{/size}":
        xpos 0.5
        xanchor 0.5
        ypos 0.92
        yanchor 1.0
    with Dissolve(0.7)
    pause
    hide text
    scene Jennifer_Weekend_7PM_113 with Dissolve(0.5)
    Jennifer "C'mon honey. what are you doing?"
    scene Jennifer_Weekend_7PM_114 with Dissolve(0.5)
    MC "Right away mom, I was thinking of where to start..."
    call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Back:
    scene Jennifer_Weekend_7PM_115 with Dissolve (0.5)
    MC "Uhhh... I don't really have a good angle for this from here..."
    scene Jennifer_Weekend_7PM_116 with Dissolve (0.5)
    Jennifer "It doesn't have to be perfect honey."
    Jennifer "Just try like that."
    scene Jennifer_Weekend_7PM_117 with Dissolve (0.5)
    MC "Okay... I'll try..."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}*Two minutes later...*"
    scene Jennifer_Weekend_7PM_118 with Dissolve (0.5)
    Jennifer "Yeah... It doesn't really feel that good..."
    scene Jennifer_Weekend_7PM_119 with Dissolve (0.5)
    MC "Sorry mom, if you want I can hop on."
    scene Jennifer_Weekend_7PM_120 with Dissolve (0.5)
    Jennifer "Hop on...?"
    scene Jennifer_Weekend_7PM_121 with Dissolve (0.5)
    Jennifer "........."
    scene Jennifer_Weekend_7PM_122 with Dissolve (0.5)
    Jennifer "You are not hopping on anything! Don't be ridiculous!"
    scene Jennifer_Weekend_7PM_123 with Dissolve (0.5)
    MC "Uhhh... Okay, I think I worded that wrong... I meant to sa-"
    scene Jennifer_Weekend_7PM_122 with Dissolve (0.5)
    Jennifer "Yeah I know what you meant! Just continue like you are already!"
    scene Jennifer_Weekend_7PM_124 with Dissolve (0.5)
    Jennifer "...."
    call stat_reward({"Jennifer": {"corruption": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Breast:
    scene BlackScreen with Dissolve (0.5)
    "{color=#808080}*10 minutes into massaging*"
    scene Jennifer_Weekend_7PM_125 with Dissolve (0.5)
    MC "{color=#808080}*So close... they are so close...*"
    scene Jennifer_Weekend_7PM_128 with Dissolve (0.5)
    MC "{color=#808080}*And she's probably asleep by now...*"
    scene Jennifer_Weekend_7PM_126 with Dissolve (0.5)
    MC "{color=#808080}*Just uhhh... just a grab... maybe a pinch... at least a poke...*"
    scene Jennifer_Weekend_7PM_127 with Dissolve (0.5)
    Mhyrorin "Wait! Don't do that!"
    scene Jennifer_Weekend_7PM_130 with Dissolve (0.5)
    MC "{color=#808080}*M-mhyro...?*"
    scene Jennifer_Weekend_7PM_129 with Dissolve (0.5)
    Mhyrorin "You know I'm not the type to cockblock, but you gotta trust me on this one."
    scene Jennifer_Weekend_7PM_131 with Dissolve (0.5)
    MC "B-but... I'm so close!"
    scene Jennifer_Weekend_7PM_132 with Dissolve (0.5)
    Mhyrorin "Listen to me! She's not sleeping! She'll get really mad! More than I can afford!"
    scene Jennifer_Weekend_7PM_133 with Dissolve (0.5)
    MC "I don't care at this point!"
    scene Jennifer_Weekend_7PM_135 with Dissolve (0.5)
    Mhyrorin "God damn it, [MC]! Now it's not the time for this shit!"
    scene Jennifer_Weekend_7PM_134 with Dissolve (0.5)
    Mhyrorin "{color=#808080}*Tsk! I'm losing him!*"
    scene Jennifer_Weekend_7PM_136 with Dissolve (0.5)
    MC "I'm sorry, but I have to do it!"
    scene Jennifer_Weekend_7PM_137 with Dissolve (0.5)
    Mhyrorin "{color=#808080}*I was hoping I wouldn't have to do this...*"
    scene Jennifer_Weekend_7PM_138 with Dissolve (0.5)
    MC "{color=#808080}*Endless bliss... here I come...*"
    scene BlackScreen with Dissolve (0.5)
    show text "{size=24}{color=#b8b8b8}heavenly chorus may be loud{/color}{/size}":
        xpos 0.985
        xanchor 1.0
        ypos 0.965
        yanchor 1.0
        alpha 0.0
        linear 0.25 alpha 0.85
    pause 1.2
    hide text with Dissolve(0.25)
    play sound "audio/Jennifer_Weekend_7PM_Euphoria_Choir.wav"
    call Jennifer_Weekend_7PM_EuphoriaMontage(fade_in=1.2)
    call Jennifer_Weekend_7PM_EuphoriaMontage
    call Jennifer_Weekend_7PM_EuphoriaMontage(fade_out=1.2)
    stop sound fadeout 0.4
    scene BlackScreen
    MC "{color=#808080}*Ahhhh... I'm ready to die now... I won't even be mad at it...*"
    scene Jennifer_Weekend_7PM_139 with Dissolve(0.18)
    pause 0.35
    scene BlackScreen with Dissolve(0.08)
    pause 0.45
    scene Jennifer_Weekend_7PM_140 with Dissolve(0.16)
    pause 0.50
    scene BlackScreen with Dissolve(0.08)
    pause 0.32
    scene Jennifer_Weekend_7PM_141 with Dissolve(0.14)
    pause 0.75
    scene BlackScreen with Dissolve(0.08)
    pause 0.22
    scene Jennifer_Weekend_7PM_142 with Dissolve(0.25)
    MC "Huh? W-w-what? Did I not just..."
    scene BlackScreen
    pause 0.1
    show Jennifer_Weekend_7PM_143 at reveal_punch
    pause
    scene Jennifer_Weekend_7PM_144 with Dissolve(0.5)
    MC "GAAHHHH!!!"
    scene Jennifer_Weekend_7PM_145 with Dissolve(0.5)
    Mhyrorin "UGHHHHHH!!!"
    scene Jennifer_Weekend_7PM_146 with Dissolve(0.5)
    MC "Y-you didn't have to... thank you..."
    scene Jennifer_Weekend_7PM_147 with Dissolve(0.5)
    Mhyrorin "... feeling better?!"
    scene Jennifer_Weekend_7PM_148 with Dissolve(0.5)
    MC "Y-yeah... a lot better..."
    scene Jennifer_Weekend_7PM_149 with Dissolve(0.5)
    Mhyrorin "Glad to hear that..."
    scene Jennifer_Weekend_7PM_150 with Dissolve(0.5)
    Mhyrorin "Hold tight."
    show Jennifer_Weekend_7PM_movie_1
    pause 0.28
    scene expression Solid("#ffffff")
    pause 1.0
    scene Jennifer_Weekend_7PM_151 with Dissolve(1.2)
    Jennifer "Everything okay, honey? Did you get tired?"
    scene Jennifer_Weekend_7PM_152 with Dissolve(0.5)
    MC "Yep, all good, don't worry..."
    call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()

label Jennifer_Weekend_7PM_Arms:

    scene Jennifer_Weekend_7PM_153 with Dissolve(0.5)
    Jennifer "Ahhh, that's perfect honey! My arms were feeling soooo heavy!"
    scene Jennifer_Weekend_7PM_154 with Dissolve(0.5)
    MC "Uhhh... aham, yep, I'm happy to hear that..."
    scene Jennifer_Weekend_7PM_155 with Dissolve(0.5)
    Jennifer "Maybe I should punish you more often. I've been far too lenient with you!"
    scene Jennifer_Weekend_7PM_156 with Dissolve(0.5)
    Jennifer "Huh?"
    scene Jennifer_Weekend_7PM_157 with Dissolve(0.5)
    Jennifer "{color=#808080}*God, Jennifer, what's wrong with you?*"
    scene Jennifer_Weekend_7PM_158 with Dissolve(0.5)
    MC "Uhhh... yeah... sure..."
    scene Jennifer_Weekend_7PM_159 with Dissolve(0.5)
    MC "I mean, ohhh, nooo, please don't!"
    scene Jennifer_Weekend_7PM_160 with Dissolve(0.5)
    MC "Huh?"
    scene Jennifer_Weekend_7PM_161 with Dissolve(0.5)
    MC "Ughhh... great..."
    scene Jennifer_Weekend_7PM_162 with Dissolve(0.5)
    MC "What now...?"
    scene Jennifer_Weekend_7PM_163 with Dissolve(0.5)
    MC "Say something... I know you're up to some shit!"
    scene Jennifer_Weekend_7PM_164 at sensual_pose_left with Dissolve(0.7)
    pause 1.35
    scene Jennifer_Weekend_7PM_165 at sensual_pose_out_right with Dissolve(0.65)
    pause 1.35
    scene Jennifer_Weekend_7PM_166 at sensual_pose_hold with Dissolve(0.65)
    pause 1.45
    scene Jennifer_Weekend_7PM_167 with Dissolve(0.5)
    MC "What the hell are you doing? Don't tell me you're in heat now, out of any other possible time..."
    scene Jennifer_Weekend_7PM_168 at sensual_pose_right with Dissolve(0.7)
    pause 1.35
    scene Jennifer_Weekend_7PM_169 at sensual_pose_out_left with Dissolve(0.65)
    pause 1.45
    scene Jennifer_Weekend_7PM_167 with Dissolve(0.5)
    MC "Wait... are you trying to..."
    scene Jennifer_Weekend_7PM_170 with Dissolve(0.5)
    MC "You really are an evil bitch. But it's not gonna work! I see you naked all day, I'm already immune to-"
    scene Jennifer_Weekend_7PM_171 with Dissolve(0.5)
    Mhyrorin "Heh..."
    scene Jennifer_Weekend_7PM_170 with Dissolve(0.5)
    MC "What are you smiling at?"
    scene Jennifer_Weekend_7PM_172 with Dissolve(0.5)
    Jennifer "GAAAHH!"
    scene Jennifer_Weekend_7PM_173 with Dissolve(0.5)
    Jennifer "AAAAAAAAAAAAAAAAAA!!"
    call stat_reward({"Jennifer": {"love": -2, "corruption": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
label Jennifer_Weekend_7PM_Head:

    scene Jennifer_Weekend_7PM_57
    MC "{color=#808080}*How the hell am I supposed to massage her head...?*"
    MC "{color=#808080}*Why did I even think of that? So stupid...*"
    jump Jennifer_Weekend_7PM_MassageChoice

label Jennifer_Weekend_7PM_EuphoriaMontage(fade_in=0.0, fade_out=0.0):

    scene black
    if fade_in > 0.0:
        show black as euphoria_fade zorder 100:
            alpha 1.0
            linear fade_in alpha 0.0
    elif fade_out > 0.0:
        show black as euphoria_fade zorder 100:
            alpha 0.0
            linear fade_out alpha 1.0

    show Jennifer_Weekend_7PM_Euphoria_01 as euphoria_img at euphoria_drift_left
    with Dissolve(0.08)
    pause 0.13
    show Jennifer_Weekend_7PM_Euphoria_02 as euphoria_img at euphoria_drift_right
    with Dissolve(0.04)
    pause 0.12
    show Jennifer_Weekend_7PM_Euphoria_03 as euphoria_img at euphoria_drift_left
    with Dissolve(0.04)
    pause 0.12
    show Jennifer_Weekend_7PM_Euphoria_04 as euphoria_img at euphoria_drift_right
    with Dissolve(0.04)
    pause 0.12
    show Jennifer_Weekend_7PM_Euphoria_05 as euphoria_img at euphoria_drift_left
    with Dissolve(0.04)
    pause 0.12
    show Jennifer_Weekend_7PM_Euphoria_06 as euphoria_img at euphoria_drift_right
    with Dissolve(0.04)
    pause 0.12
    show Jennifer_Weekend_7PM_Euphoria_07 as euphoria_img at euphoria_bloom
    with Dissolve(0.06)
    pause 0.19
    hide euphoria_img
    if fade_in > 0.0:
        hide euphoria_fade
    elif fade_out > 0.0:
        pause 0.05
    return
