init python:
    define_images("Breakfast_weekend_9AM_", "WeekendScenes/BreakfastScenes/9AM", "Breakfast_weekend_9AM_", 117)

    def reset_breakfast_weekend_9am_flags_for_new_day():
        global bw9_talked_jennifer_today, bw9_complimented_jennifer_today, bw9_teased_jennifer_today
        global bw9_talked_isabella_today, bw9_complimented_isabella_today, bw9_teased_isabella_today
        global bw9_talked_claire_today, bw9_complimented_claire_today, bw9_teased_claire_today

        bw9_talked_jennifer_today = False
        bw9_complimented_jennifer_today = False
        bw9_teased_jennifer_today = False

        bw9_talked_isabella_today = False
        bw9_complimented_isabella_today = False
        bw9_teased_isabella_today = False

        bw9_talked_claire_today = False
        bw9_complimented_claire_today = False
        bw9_teased_claire_today = False

# ---------------------------
# Breakfast 9AM: daily flags
# ---------------------------
default bw9_talked_jennifer_today = False
default bw9_complimented_jennifer_today = False
default bw9_teased_jennifer_today = False

default bw9_talked_isabella_today = False
default bw9_complimented_isabella_today = False
default bw9_teased_isabella_today = False

default bw9_talked_claire_today = False
default bw9_complimented_claire_today = False
default bw9_teased_claire_today = False


# Call this ONCE when the in-game day advances (e.g., in your day rollover).


# ---------------------------
# Scene + menu hub
# ---------------------------
label Breakfast_weekend_9AM:
    scene Breakfast_weekend_9AM_1 with Dissolve(0.5)
    Isabella "So that's why I need more fruits in my diet."
    scene Breakfast_weekend_9AM_2 with Dissolve(0.5)
    Jennifer "I buy them all the time, sweetie. You just don't eat them."
    scene Breakfast_weekend_9AM_3 with Dissolve(0.5)
    Isabella "Hm, weird, I never see them."
    scene Breakfast_weekend_9AM_4 with Dissolve(0.5)
    Claire "Ugh, finally..."
    scene Breakfast_weekend_9AM_5 with Dissolve(0.5)
    Jennifer "Come here, honey, we are waiting for you."
    scene Breakfast_weekend_9AM_6 with Dissolve(0.5)
    MC "Oh, c'mon mom, you don't need to wait for me to start eating."
    scene Breakfast_weekend_9AM_7 with Dissolve(0.5)
    Jennifer "We eat together as a family. If one of us is late, we all wait."
    scene Breakfast_weekend_9AM_8 with Dissolve(0.5)
    Claire "Only he's the only one that's always late."
    scene Breakfast_weekend_9AM_9 with Dissolve(0.5)
    MC "Okay, okay, my bad, I'm still getting used to this, let's eat."
    # Drop into the reusable menu hub:
    jump Breakfast_weekend_9AM_menu


# Central menu you can jump back to after any interaction.
label Breakfast_weekend_9AM_menu:
    scene Breakfast_weekend_9AM_10 with Dissolve(0.5)
    menu:
        "Isabella":
            jump bw9_isabella_menu
        "Claire":
            jump bw9_claire_menu
        "Jennifer":
            jump bw9_jennifer_menu
        "Leave":
            # No daily resets here — they’re once-per-day, not per-visit.
            $ Location = "Entrance"
            $ renpy.call("GameLoop")


# ---------------------------
# Isabella submenu
# ---------------------------
label bw9_isabella_menu:
    scene Breakfast_weekend_9AM_10
    menu:
        "Talk" if not bw9_talked_isabella_today:
            jump bw9_isabella_talk
        "{color=#808080}Talk{/color}" if bw9_talked_isabella_today:
            MC "{color=#808080}**I already talked to her today.**{/color}"
            jump bw9_isabella_menu

        "Compliment" if not bw9_complimented_isabella_today:
            jump bw9_isabella_compliment
        "{color=#808080}Compliment{/color}" if bw9_complimented_isabella_today:
            MC "{color=#808080}**I already complimented her today.**{/color}"
            jump bw9_isabella_menu

        "Tease" if not bw9_teased_isabella_today:
            jump bw9_isabella_tease
        "{color=#808080}Tease{/color}" if bw9_teased_isabella_today:
            MC "{color=#808080}**I already teased her today.**{/color}"
            jump bw9_isabella_menu

        "Back":
            jump Breakfast_weekend_9AM_menu



# --- Isabella: TALK (your lines wired) ---
label bw9_isabella_talk:
    scene Breakfast_weekend_9AM_56 with Dissolve(0.5)
    MC "Will you go swimming later?"
    scene Breakfast_weekend_9AM_57 with Dissolve(0.5)
    Isabella "Uhhh, yeah, most likely. But I'll be with Criss, so..."
    scene Breakfast_weekend_9AM_58 with Dissolve(0.5)
    Isabella "You know how shy she gets around boys, and I don't want to make her feel uncomfortable."
    scene Breakfast_weekend_9AM_59 with Dissolve(0.5)
    MC "So you're saying I make her uncomfortable?"
    scene Breakfast_weekend_9AM_60 with Dissolve(0.5)
    Isabella "Oh, c'mon, don't be like that, you know what I mean."
    scene Breakfast_weekend_9AM_61 with Dissolve(0.5)
    MC "Yeah, yeah, I'm kidding, I get it."
    scene Breakfast_weekend_9AM_62 with Dissolve(0.5)
    MC "But I'll come by, try my luck a little."
    scene Breakfast_weekend_9AM_63 with Dissolve(0.5)
    Isabella "Heh, who would've thought, shocker."
    Isabella "But actually, maybe it would help Criss with her anxiety if you were to hang around with us."
    scene Breakfast_weekend_9AM_64 with Dissolve(0.5)
    Isabella "But don't overdo it, if you see her getting uncomfortable, just leave, okay?"
    scene Breakfast_weekend_9AM_65 with Dissolve(0.5)
    MC "..."
    scene Breakfast_weekend_9AM_66 with Dissolve(0.5)
    Isabella "Ugh, yeah, of course, I forgot who I was talking to."
    Isabella "Good luck Crissy..."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_talked_isabella_today = True
    jump bw9_isabella_menu


# --- Isabella: COMPLIMENT ---
label bw9_isabella_compliment:
    scene Breakfast_weekend_9AM_30 with Dissolve(0.5)
    Jennifer "..."
    scene Breakfast_weekend_9AM_31 with Dissolve(0.5)
    Claire "..."
    scene Breakfast_weekend_9AM_32 with Dissolve(0.5)
    Isabella "..."
    scene Breakfast_weekend_9AM_33 with Dissolve(0.5)
    MC "..."
    scene Breakfast_weekend_9AM_34 with Dissolve(0.5)
    Isabella "AAAAAAAAAAA!!"
    scene Breakfast_weekend_9AM_35 with Dissolve(0.5)
    Isabella "What the hell are you doing?!"
    scene Breakfast_weekend_9AM_36 with Dissolve(0.5)
    MC "Huh?"
    scene Breakfast_weekend_9AM_37 with Dissolve(0.5)
    MC "What do you mean what am I doing?"
    MC "I'm eating what's on my plate, and you have your feet all over it."
    MC "If you don't want that to happen, don't have them there."
    scene Breakfast_weekend_9AM_38 with Dissolve(0.5)
    Isabella "That's not how it works assface!"
    scene Breakfast_weekend_9AM_39 with Dissolve(0.5)
    Jennifer "[MC], These type of jokes are not ok."
    Jennifer "Isa is your sister and this is inappropriate!"
    scene Breakfast_weekend_9AM_40 with Dissolve(0.5)
    Isabella "HA! See, I am right, weirdo!"
    scene Breakfast_weekend_9AM_41 with Dissolve(0.5)
    Jennifer "And you shouldn't have your feet up while we're eating either."
    scene Breakfast_weekend_9AM_42 with Dissolve(0.5)
    MC "Hah, told you!"
    scene Breakfast_weekend_9AM_43 with Dissolve(0.5)
    Jennifer "It's clearly making [MC] uncomfortable."
    scene Breakfast_weekend_9AM_44 with Dissolve(0.5)
    MC "Huh? Wait a second. I didn't say that."
    scene Breakfast_weekend_9AM_45 with Dissolve(0.5)
    MC "I was just saying that if she keeps waving them around like that they might end up in my mouth."
    scene Breakfast_weekend_9AM_46 with Dissolve(0.5)
    Claire "Ugh, Isa's feet? You are such a disgusting weirdo."
    scene Breakfast_weekend_9AM_47 with Dissolve(0.5)
    Isabella "...."
    scene Breakfast_weekend_9AM_48 with Dissolve(0.5)
    MC "Huh?"
    scene Breakfast_weekend_9AM_49 with Dissolve(0.5)
    MC "They are not disgusting, what are you talking about?"
    scene Breakfast_weekend_9AM_50 with Dissolve(0.5)
    Isabella "Thank you, [mc_name[:2]]-"
    scene Breakfast_weekend_9AM_51 with Dissolve(0.5)
    Isabella "Huh?!"
    scene Breakfast_weekend_9AM_52 with Dissolve(0.5)
    MC "See? Pretty cute!"
    scene Breakfast_weekend_9AM_53 with Dissolve(0.5)
    Claire "Igh..."
    scene Breakfast_weekend_9AM_54 with Dissolve(0.5)
    Isabella "UGHHHH, let it go!"
    scene Breakfast_weekend_9AM_55 with Dissolve(0.5)
    Jennifer "Tchh—haah..."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_complimented_isabella_today = True
    jump bw9_isabella_menu


# --- Isabella: TEASE ---
label bw9_isabella_tease:
    scene Breakfast_weekend_9AM_11 with Dissolve(0.5)
    MC "So, is Criss still coming over this weekend?"
    scene Breakfast_weekend_9AM_12 with Dissolve(0.5)
    Isabella "Yep, she should come in like an hour or so."
    scene Breakfast_weekend_9AM_13 with Dissolve(0.5)
    Isabella "..."
    scene Breakfast_weekend_9AM_14 with Dissolve(0.5)
    Isabella "Why are you asking though?"
    scene Breakfast_weekend_9AM_15 with Dissolve(0.5)
    MC "..."
    scene Breakfast_weekend_9AM_16 with Dissolve(0.5)
    Jennifer "Aww, honey, did you make friends with Criss at school? She's a really nice girl!"
    scene Breakfast_weekend_9AM_17 with Dissolve(0.5)
    MC "Yep, we're really good fri-"
    scene Breakfast_weekend_9AM_18 with Dissolve(0.5)
    MC "..."
    scene Breakfast_weekend_9AM_19 with Dissolve(0.5)
    Isabella "No, he is not."
    scene Breakfast_weekend_9AM_20 with Dissolve(0.5)
    MC "Oh, come on, don't tell me you're jealous."
    scene Breakfast_weekend_9AM_21 with Dissolve(0.5)
    Isabella "Hah, in your dreams."
    Isabella "I just think you are a bad influence on her."
    scene Breakfast_weekend_9AM_22 with Dissolve(0.5)
    Jennifer "Eh-hem."
    scene Breakfast_weekend_9AM_23 with Dissolve(0.5)
    IsaAndMC "Hhh—!"
    scene Breakfast_weekend_9AM_24 with Dissolve(0.5)
    MC "Hmph!"
    scene Breakfast_weekend_9AM_25 with Dissolve(0.5)
    Isabella "Hmph!"
    scene BlackScreen with Dissolve(0.5)
    $ bw9_teased_isabella_today = True
    jump bw9_isabella_menu


# ---------------------------
# Claire submenu (stubs)
# ---------------------------
label bw9_claire_menu:
    scene Breakfast_weekend_9AM_10
    menu:
        "Talk" if not bw9_talked_claire_today:
            jump bw9_claire_talk
        "{color=#808080}Talk{/color}" if bw9_talked_claire_today:
            MC "{color=#808080}**I already talked to her today.**{/color}"
            jump bw9_claire_menu

        "Compliment" if not bw9_complimented_claire_today:
            jump bw9_claire_compliment
        "{color=#808080}Compliment{/color}" if bw9_complimented_claire_today:
            MC "{color=#808080}**I already complimented her today.**{/color}"
            jump bw9_claire_menu

        "Tease" if not bw9_teased_claire_today:
            jump bw9_claire_tease
        "{color=#808080}Tease{/color}" if bw9_teased_claire_today:
            MC "{color=#808080}**I already teased her today.**{/color}"
            jump bw9_claire_menu

        "Back":
            jump Breakfast_weekend_9AM_menu

label bw9_claire_talk:
    scene Breakfast_weekend_9AM_81 with Dissolve(0.5)
    MC "Are you going out today, Claire?"
    scene Breakfast_weekend_9AM_82 with Dissolve(0.5)
    Claire "What do you care?"
    scene Breakfast_weekend_9AM_83 with Dissolve(0.5)
    MC "Just making conversation..."
    scene Breakfast_weekend_9AM_82 with Dissolve(0.5)
    Claire "Not interested."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_talked_claire_today = True
    jump bw9_claire_menu

label bw9_claire_compliment:
    scene Breakfast_weekend_9AM_92 with Dissolve(0.5)
    MC "Are you still going to the gym later, Claire?"
    scene Breakfast_weekend_9AM_93 with Dissolve(0.5)
    Claire "..."
    scene Breakfast_weekend_9AM_94 with Dissolve(0.5)
    Claire "What do you care?"
    scene Breakfast_weekend_9AM_95 with Dissolve(0.5)
    MC "Well, you look really good, so I was thinking I could join you."
    scene Breakfast_weekend_9AM_96 with Dissolve(0.5)
    Claire "Ew. No thank you. And keep your compliments to yourself."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_complimented_claire_today = True
    jump bw9_claire_menu

label bw9_claire_tease:
    scene Breakfast_weekend_9AM_97 with Dissolve(0.5)
    MC "Uhhh.. With a face like that I'm not even going to attempt it..."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_teased_claire_today = True
    jump bw9_claire_menu


# ---------------------------
# Jennifer submenu (stubs)
# ---------------------------
label bw9_jennifer_menu:
    scene Breakfast_weekend_9AM_10
    menu:
        "Talk" if not bw9_talked_jennifer_today:
            jump bw9_jennifer_talk
        "{color=#808080}Talk{/color}" if bw9_talked_jennifer_today:
            MC "{color=#808080}**I already talked to her today.**{/color}"
            jump bw9_jennifer_menu

        "Compliment" if not bw9_complimented_jennifer_today:
            jump bw9_jennifer_compliment
        "{color=#808080}Compliment{/color}" if bw9_complimented_jennifer_today:
            MC "{color=#808080}**I already complimented her today.**{/color}"
            jump bw9_jennifer_menu

        "Tease" if not bw9_teased_jennifer_today:
            jump bw9_jennifer_tease
        "{color=#808080}Tease{/color}" if bw9_teased_jennifer_today:
            MC "{color=#808080}**I already teased her today.**{/color}"
            jump bw9_jennifer_menu

        "Back":
            jump Breakfast_weekend_9AM_menu

label bw9_jennifer_talk:
    scene Breakfast_weekend_9AM_67 with Dissolve(0.5)
    MC "So, what's the plan for today, mom?"
    scene Breakfast_weekend_9AM_68 with Dissolve(0.5)
    Jennifer "Hm?"
    scene Breakfast_weekend_9AM_69 with Dissolve(0.5)
    Jennifer "Oh, well, cleaning, laundry, groceries, the usual."
    scene Breakfast_weekend_9AM_70 with Dissolve(0.5)
    MC "Uhhh.. yeah... sounds fun."
    scene Breakfast_weekend_9AM_71 with Dissolve(0.5)
    Jennifer "Heh, I know, right?"
    scene Breakfast_weekend_9AM_72 with Dissolve(0.5)
    Jennifer "But somebody's gotta do it."
    scene Breakfast_weekend_9AM_73 with Dissolve(0.5)
    MC "Can't it be skipped today? How about I take you out somewhere nice instead?"
    scene Breakfast_weekend_9AM_74 with Dissolve(0.5)
    Jennifer "Huh?"
    scene Breakfast_weekend_9AM_75 with Dissolve(0.5)
    IsaAndClaire "Heeeehhh?"
    scene Breakfast_weekend_9AM_76 with Dissolve(0.5)
    MC "Oh, no, no, no, wait, I didn't mean it like that."
    scene Breakfast_weekend_9AM_77 with Dissolve(0.5)
    Jennifer "Are you asking your mama out on a date, kiddo?"
    scene Breakfast_weekend_9AM_78 with Dissolve(0.5)
    MC "I didn't want it to sound like th-"
    scene Breakfast_weekend_9AM_77 with Dissolve(0.5)
    Jennifer "I'll tell you what kiddo. If you help me with the chores today, we can all go out tonight, how's that sound?"
    scene Breakfast_weekend_9AM_79 with Dissolve(0.5)
    MC "{color=#808080}Ugh—there's a reason I asked just you..."
    scene Breakfast_weekend_9AM_80 with Dissolve(0.5)
    MC "Sure, mom, sounds great!"
    MC "I'll see if I have time to help you later."
    scene Breakfast_weekend_9AM_77 with Dissolve(0.5)
    Jennifer "Mhm, I'm sure you'll find the time."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_talked_jennifer_today = True
    jump bw9_jennifer_menu

label bw9_jennifer_compliment:
    scene Breakfast_weekend_9AM_84 with Dissolve(0.5)
    MC "The food is amazing, mom! You really outdid yourself."
    scene Breakfast_weekend_9AM_85 with Dissolve(0.5)
    Jennifer "Awww, thank you honey. But it's just some sandwiches, nothing special."
    scene Breakfast_weekend_9AM_86 with Dissolve(0.5)
    Isabella "He wants something, mom. It's clear since he didn't compliment my smoothies first!"
    scene Breakfast_weekend_9AM_87 with Dissolve(0.5)
    Jennifer "Well, then he might just get it, since I don't get a lot of compliments around here."
    scene Breakfast_weekend_9AM_88 with Dissolve(0.5)
    Isabella "Hmph."
    scene Breakfast_weekend_9AM_89 with Dissolve(0.5)
    Jennifer "So, c'mon, tell mama what you want."
    scene Breakfast_weekend_9AM_90 with Dissolve(0.5)
    MC "Uhhh... nothing, really, I just meant the food is good."
    scene Breakfast_weekend_9AM_91 with Dissolve(0.5)
    Jennifer "Oh, really? Well... thank you honey."
    scene BlackScreen with Dissolve(0.5)
    # $ check_and_update_character_stats("Jennifer")
    $ bw9_complimented_jennifer_today = True
    jump bw9_jennifer_menu

label bw9_jennifer_tease:
    scene Breakfast_weekend_9AM_98 with Dissolve(0.5)
    Jennifer "Yeah... I don't know... sometimes it feels like they all have something against me."
    Jennifer "Maybe I'm doing something wrong?"
    scene Breakfast_weekend_9AM_99 with Dissolve(0.5)
    Isabella "Eh, don't take them seriously, mom, everybody has their off days."
    scene Breakfast_weekend_9AM_100 with Dissolve(0.5)
    MC "Huh? What are we talking about? I missed the start."
    scene Breakfast_weekend_9AM_101 with Dissolve(0.5)
    MC "Clue me in. Who's having problems with mom?"
    scene Breakfast_weekend_9AM_102 with Dissolve(0.5)
    Isabella "Eh, some of mom's coworkers at the office."
    Isabella "They are giving her a hard time out of nowhere..."
    scene Breakfast_weekend_9AM_103 with Dissolve(0.5)
    Jennifer "I don't know... maybe I am doing something wrong..."
    Jennifer "Every time I walk past them they just stop talking and look at me weird. Rolling their eyes and stuff."
    scene Breakfast_weekend_9AM_104 with Dissolve(0.5)
    MC "Huh? That's all?"
    scene Breakfast_weekend_9AM_105 with Dissolve(0.5)
    Isabella "What do you mean, \"That's all\"?! Don't be an ass!"
    scene Breakfast_weekend_9AM_106 with Dissolve(0.5)
    Jennifer "It's okay, Isa... Maybe I complain too much."
    scene Breakfast_weekend_9AM_107 with Dissolve(0.5)
    MC "Huh? No, that's not what I meant."
    MC "I wanted to say that that's all you do?"
    scene Breakfast_weekend_9AM_108 with Dissolve(0.5)
    MC "If you ask me... It's obvious that they are jealous of you"
    scene Breakfast_weekend_9AM_109 with Dissolve(0.5)
    Jennifer "Jealous? Why would they be jealous? It's not like I do or have anything extra..."
    scene Breakfast_weekend_9AM_110 with Dissolve(0.5)
    MC "...."
    scene Breakfast_weekend_9AM_111 with Dissolve(0.5)
    MC "Because of how you look compared to them, of course."
    scene Breakfast_weekend_9AM_112 with Dissolve(0.5)
    Jennifer "What do you mean?"
    scene Breakfast_weekend_9AM_113 with Dissolve(0.5)
    MC "Well, they are probably some old and ugly frustrated women who are hitting their menopause and whose kilos are starting to double their age."
    scene Breakfast_weekend_9AM_114 with Dissolve(0.5)
    Isabella "{color=#808080}Whoa, whoa, whoa... And I thought girls were mean... Maybe I should start gossiping with him instead of Claire.{/color}"
    scene Breakfast_weekend_9AM_115 with Dissolve(0.5)
    Jennifer "Oh, honey... don't talk like that, they are not like that..."
    scene Breakfast_weekend_9AM_116 with Dissolve(0.5)
    Isabella "He kinda has a point, mom. You know how women are. They act like that at school too."
    scene Breakfast_weekend_9AM_113 with Dissolve(0.5)
    MC "And then there you are, not looking a day over 30, with a fit body and a perfect figure, reminding them of how old and ugly they are each time you pass around them."
    scene Breakfast_weekend_9AM_117 with Dissolve(0.5)
    Jennifer ".... Don't talk like that to your mother..."
    Jennifer "But thank you..."
    scene BlackScreen with Dissolve(0.5)
    $ bw9_teased_jennifer_today = True
    jump bw9_jennifer_menu



    #! ChitChat
    # scene Breakfast_weekend_9AM_26 with Dissolve(0.5)
    # Jennifer "Of course lips need SPF as well, sweetie. How do you not know that by now?"
    # scene Breakfast_weekend_9AM_27 with Dissolve(0.5)
    # Isabella "Ugh, really? But it tastes like melted crayons..."
    # scene Breakfast_weekend_9AM_28 with Dissolve(0.5)
    # Claire "Maybe don't use a shitty one? Have you ever thought of that?"
    # scene Breakfast_weekend_9AM_29 with Dissolve(0.5)
    # Isabella "They all taste the same, I don't know how you two can stand it."