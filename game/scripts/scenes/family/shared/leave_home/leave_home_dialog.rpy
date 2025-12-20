init python:
    def get_upper_name(character):
        return character.name.upper()

init python:
    define_images("LeaveHomeScene", "LeaveHomeScenes", "LeaveHomeScene", 61)

label LeaveHomeLVL1:

    scene LeaveHomeScene1
    Jennifer "Are you ready [MC]? We are leaving!"
    scene LeaveHomeScene2 with Dissolve(0.5)
    Claire "Come on already dumb ass, it's getting late!"
    Claire "Are you coming or not?!"
    scene LeaveHomeScene3 with Dissolve(0.5)
    menu:
        "Go to school with them":
            scene LeaveHomeScene4 with Dissolve(0.5)
            MC "Yeah, I'll come with you!"
            MC "I just gotta take my shoes!"
            scene LeaveHomeScene5 with Dissolve(0.5)
            Claire "Ughhhh!!! I'm in a hurry!"
            scene LeaveHomeScene6 with Dissolve(0.5)
            Claire "I'll wait in the car!"
            Claire "Y'all better hurry!"
            scene LeaveHomeScene7 with Dissolve(0.5)
            Isabella "Good job big bro!"
            scene LeaveHomeScene8 with Dissolve(0.5)
            Isabella "You somehow managed to piss her off again!"
            scene LeaveHomeScene9 with Dissolve(0.5)
            Isabella "You really have a talent for it!"
            scene LeaveHomeScene10 with Dissolve(0.5)
            MC "Shut up shortie! You are the last person to make fun of me."
            scene LeaveHomeScene11 with Dissolve(0.5)
            Isabella "Who are you calling shortie? Shortie!"
            Isabella "I'm still growing!!"
            Isabella "But look at you! Mom is towering you!"
            Isabella "And you are a man! So what is your excuse?"
            scene LeaveHomeScene12 with Dissolve(0.5)
            Jennifer "Don't listen to her [MC]!"
            Jennifer "You are still growing!"
            Jennifer "You will grow far taller than me!"
            scene LeaveHomeScene13 with Dissolve(0.5)
            Isabella "Awww, how cute! Such a mama's boy!"
            scene LeaveHomeScene14 with Dissolve(0.5)
            MC "If I start making fun of you, you will start crying in 2 seconds running for mom."
            MC "So don't try me sis!"
            scene LeaveHomeScene15 with Dissolve(0.5)
            Jennifer "You kids will both grow taller than me!"
            scene LeaveHomeScene16 with Dissolve(0.5)
            Jennifer "So stop fighting, ok?"
            scene LeaveHomeScene15 with Dissolve(0.5)
            Jennifer "Now let's go! Your sister is waiting in the car, and you know she gets mad when she waits."
            # ! maybe in the future I could add an option for MC to say "let her wait", and do something
            scene BlackScreen with Dissolve(0.5)
            if beenToSchoolOnce:
                jump GoToSchoolScene
            else:
                jump GoToForTheFirstTimeSchoolScene
            # "{color=#808080}**All three of you go to the car**{/color}"
            # "{color=#808080}*Jennifer love + 2{/color}"
            # "{color=#808080}*Isabella love + 2{/color}"
            # $ Jennifer_love = Jennifer_love + 2
            # $ Isabella_love = Isabella_love + 2
            # $ Location = "Entrance"
            # $ advance_time_or_sleep()
            # $ renpy.call("GameLoop")
        "Stay home":
            scene LeaveHomeScene4 with Dissolve(0.5)
            MC "I'm starting late today, the teacher can't come for the first hour!"
            MC "So leave without me!"
            MC "I'll take the bus or the subway!"
            scene LeaveHomeScene17 with Dissolve(0.5)
            Jennifer "Hmmm....."
            Jennifer "Okay......"
            Jennifer "I hope you are not lying about this!"
            Jennifer "You know I can call the teacher any time!"
            scene LeaveHomeScene18 with Dissolve(0.5)
            MC "Come on mom, when have I ever lied to you?"
            MC "{color=#808080}*I'm totally lying my ass of right now*{/color}"
            scene LeaveHomeScene19 with Dissolve(0.5)
            Jennifer "Ok kiddo!"
            Jennifer "And don't forget!"
            scene LeaveHomeScene20 with Dissolve(0.5)
            Jennifer "Don't talk or interact with stranger in the bus or in the subway!"
            Jennifer "And don't be late!"
            scene LeaveHomeScene21 with Dissolve(0.5)
            Jennifer "If I get another call from your teacher, you are going to have big problems"
            scene LeaveHomeScene22 with Dissolve(0.5)
            MC "Yea, yea, I get it mom!"
            MC "You can go now, you know the girls get mad when they wait in the car for you."
            scene LeaveHomeScene23 with Dissolve(0.5)
            Jennifer "Okay, sweetie, see you after work then!"
            scene LeaveHomeScene24 with Dissolve(0.5)
            MC "Okay, mom, see ya!"
            scene LeaveHomeScene25 with Dissolve(0.5)
            Jennifer "Ahh, damn!"
            scene LeaveHomeScene26 with Dissolve(0.5)
            Jennifer "I dropped my keys again!"
            scene LeaveHomeScene27 with Dissolve(0.5)
            Jennifer "Oh, there they are!"
            MC "{color=#808080}*Holy fuck, I get amazed every time I see her ass up close!*{/color}"
            scene LeaveHomeScene28 with Dissolve(0.5)
            MC "{color=#808080}*I can't get my eyes off of it.*{/color}"
            Jennifer "Ughhh... it's hard to crouch at this age!"
            scene LeaveHomeScene29 with Dissolve(0.5)
            MC "{color=#808080}*I feel like I won't be able to resist anymore*{/color}"
            scene LeaveHomeScene30 with Dissolve(0.5)
            MC "{color=#808080}*Should I risk it?*{/color}"
            menu:
                "Slap her ass":
                    scene LeaveHomeScene31 with Dissolve(0.5)
                    MC "{color=#808080}*I can't resist it. This ass is way too big to not be abused!*{/color}"
                    scene LeaveHomeScene32 with Dissolve(0.5)
                    $ renpy.pause(0.1, hard=True)
                    scene LeaveHomeScene33 with Dissolve(0.5)
                    $ renpy.pause(0.1, hard=True)
                    scene LeaveHomeScene34 with Dissolve(0.5)
                    $ renpy.pause(0.1, hard=True)
                    scene LeaveHomeScene35 with Dissolve(0.5)
                    $ renpy.pause(0.1, hard=True)
                    scene LeaveHomeScene36 with Dissolve(0.5)
                    $ renpy.pause(1, hard=True)
                    scene LeaveHomeScene37 with Dissolve(0.5)
                    Jennifer "AAAAAAAAAAAAAAAA!!!!"
                    scene LeaveHomeScene38 with Dissolve(0.5)
                    MC "{color=#808080}*That felt so fucking good.*{/color}"
                    MC "{color=#808080}*It was like slapping a big block of jelly*{/color}"
                    scene LeaveHomeScene39 with Dissolve(0.5)
                    $ MC_upper = get_upper_name(MC)
                    Jennifer "WHAT ARE YOU DOING [MC_upper]?!!?"
                    scene LeaveHomeScene40 with Dissolve(0.5)
                    MC "Oh my god, mom!!"
                    MC "{color=#808080}*My only hope is to gaslight her...*{/color}"
                    MC "I'm so sorry, you just ahd a huge spider on your butt!"
                    MC "I got scared and my first instinct was to smash it!"
                    MC "I'm so sorry if I hurt you!"
                    scene LeaveHomeScene41 with Dissolve(0.5)
                    Jennifer "That doesn't mean you have to slap me like that!"
                    Jennifer "It really hurt!"
                    Jennifer "I hope it doesn't leave a mark!"
                    scene LeaveHomeScene42 with Dissolve(0.5)
                    MC "I was just trying to protect you mom!"
                    MC "I only tried to swipe the spider."
                    MC "But it was about to jump and I panicked!"
                    scene LeaveHomeScene43 with Dissolve(0.5)
                    Jennifer "I think I also bruised my knees!"
                    Jennifer "I hope my pants didn't reap..."
                    scene LeaveHomeScene44 with Dissolve(0.5)
                    MC "They seem fine mom."
                    MC "I didn't mean to hurt you, I'm sorry!"
                    scene LeaveHomeScene45 with Dissolve(0.5)
                    Jennifer "And not only that! But the fact that you-"
                    scene LeaveHomeScene46 with Dissolve(0.5)
                    Isabella "Uhhh.... mom?"
                    Isabella "Not to rush you... but Claire is fuming..."
                    Isabella "She sent me to tell you to hurry."
                    scene LeaveHomeScene47 with Dissolve(0.5)
                    Isabella "Ummmm... did I come at a bad time?"
                    Isabella "Did something happen?"
                    scene LeaveHomeScene48 with Dissolve(0.5)
                    Jennifer "Nothing happened Isa, go back to the car."
                    Jennifer "Tell Claire that I'll come soon!"
                    scene LeaveHomeScene46 with Dissolve(0.5)
                    Isabella "Okay, mom." 
                    scene LeaveHomeScene49 with Dissolve(0.5)
                    Jennifer "Don't you think we are done with this young man!"
                    Jennifer "We will continue this conversation when I get home!"
                    MC "{color=#808080}*She always forgets it by the times she gets home*{/color}"
                    scene LeaveHomeScene50 with Dissolve(0.5)
                    Jennifer "Close the door behind me!"
                    Jennifer "And don't be late for school!"
                    Jennifer "Also don't forget to lock the door with the key after you leave!"
                    scene LeaveHomeScene51 with Dissolve(0.5)
                    MC "Okay, mom!"
                    MC "{color=#808080}*Fuck... I didn't listen to her at all...*{/color}"
                    MC "{color=#808080}*I'm still thinking about how that ass felt.*{/color}"
                    MC "{color=#808080}*Thanks god Isa came in to save me.*{/color}"
                    MC "{color=#808080}*My gaslight didn't work to well*{/color}"
                    scene BlackScreen with Dissolve(0.5)
                    "{color=#808080}***You close the door behind your mom.*{/color}"
                    "{color=#808080}***Mom love - 5*{/color}"
                    "{color=#808080}***Mom obedience + 2*{/color}"
                    "{color=#808080}***Mom corruption + 2*{/color}"
                    $ Jennifer_love = Jennifer_love - 5
                    $ Jennifer_Obedience = Jennifer_Obedience + 2
                    $ Jennifer_Corruption = Jennifer_Corruption + 2
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
                "Don't":
                    MC "{color=#808080}*Let's not try anything stupid right now...*{/color}"
                    scene LeaveHomeScene53 with Dissolve(0.5)
                    Jennifer "Aghhh, Almost there!"
                    scene LeaveHomeScene54 with Dissolve(0.5)
                    MC "Do you need any help mom?"
                    scene LeaveHomeScene55 with Dissolve(0.5)
                    Jennifer "Nope, I got them!"
                    Jennifer "I'm so clumsy sometimes..."
                    scene LeaveHomeScene57 with Dissolve(0.5)
                    Jennifer "Okay, kiddo."
                    Jennifer "Don't forget to lock the door."
                    Jennifer "And don't be late for school!"
                    scene LeaveHomeScene56 with Dissolve(0.5)
                    MC "Ok mom!"
                    scene LeaveHomeScene58 with Dissolve(0.5)
                    MC "Have an easy day at work!"
                    scene LeaveHomeScene59 with Dissolve(0.5)
                    Jennifer "Awww, you are so sweet kiddo, Thank you!"
                    Jennifer "Have a nice day at school as well!"
                    Jennifer "Bye, bye!"
                    scene LeaveHomeScene60 with Dissolve(0.5)
                    MC "Bye, bye, mom!"
                    scene LeaveHomeScene61 with Dissolve(0.5)
                    MC "{color=#808080}*Her ass was so close to my face...*{/color}"
                    MC "{color=#808080}*I don't know if I would ever get another opportunity like that...*{/color}"
                    scene BlackScreen with Dissolve(0.5)
                    "{color=#808080}*You close the door after Jennifer leaves.{/color}"
                    "{color=#808080}*Mom love + 2{/color}"
                    "{color=#808080}*Mom corruption - 2{/color}"
                    $ Jennifer_love = Jennifer_love + 2
                    $ Jennifer_Corruption = Jennifer_Corruption - 2
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()