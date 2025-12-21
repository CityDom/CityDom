init python:
    define_images("DropPenScene", "EnglishClassScreen/DropPenScene", "DropPenScene", 50)

label DropPenScene:
    scene DropPenScene1 with Dissolve(0.5)
    MC "{color=#808080}*Miss Thompson is coming this way...*"
    MC "{color=#808080}*Maybe I could try something...*"
    scene DropPenScene2 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    scene DropPenScene3 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    scene DropPenScene4 with Dissolve(0.5)
    MC "Damn it, I dropped my pen."
    scene DropPenScene6 with Dissolve(0.5)
    Jannice "Watch your language [MC], and be more careful, I could've tripped on that pencil."
    scene DropPenScene5 with Dissolve(0.5)
    MC "Sorry, Miss Thompson..."
    scene DropPenScene7 with Dissolve(0.5)
    MC "{color=#808080}*Should I slap it?*"
    menu:
        "Slap it":
            scene DropPenScene8 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene DropPenScene10 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene DropPenScene9 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene DropPenScene11 with Dissolve(0.5)
            Jannice "GHAAH!!!"
            scene DropPenScene12 with Dissolve(0.5)
            Jannice "Care to explain yourself mister?!"
            Jannice "And you better have a very good explanation!!!"
            scene DropPenScene13 with Dissolve(0.5)
            MC "Oh my god, Miss Thompson, I'm so sorry, a huge bug was on you."
            MC "It was about to jump on me and I got scared, I'm so sorry!!"
            scene DropPenScene12 with Dissolve(0.5)
            Jannice "And I'm supposed to believe that?!?!"
            scene DropPenScene14 with Dissolve(0.5)
            Maria "{color=#808080}*Tsk... This kid really wanna get expelled...*"
            Maria "{color=#808080}*Out of everyone in here, he tried his luck with Miss Thompson*"
            Maria "{color=#808080}*I guess I gotta join the performance*"
            scene DropPenScene15 with Dissolve(0.5)
            Maria "[MC] is telling the truth, Miss Thompson!"
            Maria "I saw it too, I was the one who told him to squash it, I got scared!"
            Maria "It's my fault, I'm sorry!"
            scene DropPenScene16 with Dissolve(0.5)
            Jannice "Yeah, sure, and I'm supposed to believe that?! Since when are you awake in my class?!"
            scene DropPenScene17 with Dissolve(0.5)
            Maria "{color=#808080}*Tsk... she got me...*"
            scene DropPenScene18 with Dissolve(0.5)
            MC "I promise we are telling the truth, Miss Thompson!"
            scene DropPenScene19 with Dissolve(0.5)
            MC "Look!"
            scene DropPenScene20 with Dissolve(0.5)
            Jannice "Oh my god, it you were telling the truth."
            scene DropPenScene21 with Dissolve(0.5)
            Jannice "Throw it right now [MC], it's disgusting!"
            Jannice "And you have detention!"
            scene DropPenScene22 with Dissolve(0.5)
            MC "Wait what?! but-"
            scene DropPenScene23 with Dissolve(0.5)
            Jannice "No buts!"
            scene DropPenScene24 with Dissolve(0.5)
            Maria "Wait, she actually had a bug on her? I could've sworn you were bullshitting."
            scene DropPenScene25 with Dissolve(0.5)
            MC "I was. It's a fake bug, I keep it in any case."
            scene DropPenScene26 with Dissolve(0.5)
            Maria "Haha, that's pretty smart."
            Maria "But why do you seem upset?"
            scene DropPenScene27 with Dissolve(0.5)
            MC "Because it won't work on you now."
            scene DropPenScene28 with Dissolve(0.5)
            Jannice "Everybody stop talking and pay attention."
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}*An hour goes by.*"
            scene DropPenScene29 with Dissolve(0.5)
            Jannice "And that's all for today!"
            Jannice "Make sure to do your homework!"
            scene DropPenScene30 with Dissolve(0.5)
            Jannice "See you after the break!"
            $ Location = "mainclassroom"
            call stat_reward({"Jannice": {"love": -5, "corruption": 2}, "Maria": {"love": 2, "corruption": 2, "obedience": 2}}, show_black=False, return_to=None)
            $ advance_time_or_sleep()
        "Don't":
            scene DropPenScene31 with Dissolve(0.5)
            Jannice "Take your pen [MC]."
            scene DropPenScene32 with Dissolve(0.5)
            MC "Thank you, Miss Thompson!"
            scene DropPenScene23 with Dissolve(0.5)
            Jannice "Alright, so, as I was saying!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}*An hour goes by.*"
            scene DropPenScene29 with Dissolve(0.5)
            Jannice "And that's all for today!"
            Jannice "Make sure to do your homework!"
            scene DropPenScene30 with Dissolve(0.5)
            Jannice "See you after the break!"
            call stat_reward({"Jannice": {"love": 2}}, show_black=False, return_to=None)
            $ Location = "mainclassroom"
            $ advance_time_or_sleep()
