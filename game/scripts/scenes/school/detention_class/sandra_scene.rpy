init python:
    define_images("DetentionClass_Sandra_Scene", "DetentionClass/Sandra_Scene", "DetentionClass_Sandra_Scene", 100)

label DetentionClass_Sandra_Scene:
    scene DetentionClass_Sandra_Scene1 with Dissolve(0.5)
    MC "Hey, Miss Nadal, do you have a second?"
    scene DetentionClass_Sandra_Scene2 with Dissolve(0.5)
    Sandra "What do you want, [MC]? Detention is starting soon."
    jump SandraDetentionMenu
label SandraDetentionMenu:
    scene DetentionClass_Sandra_Scene3 with Dissolve(0.5)
    menu:
        "What do you think about me?":
            if not Watched_detention_Sandra_WDYTAM:
                $ Watched_detention_Sandra_WDYTAM = True
                MC "I wanted to ask you, what do you think about me?"
                scene DetentionClass_Sandra_Scene4 with Dissolve(0.5)
                Sandra "Haaa...?! You got some guts in you to be asking me that!"
                Sandra "What do you think?!"
                scene DetentionClass_Sandra_Scene5 with Dissolve(0.5)
                MC "Uhhh, I don't know, that's why I was asking..."
                MC "It's just that sometimes I feel like you don't want me in this class, is there something I'm doing wrong?"
                scene DetentionClass_Sandra_Scene4 with Dissolve(0.5)
                Sandra "Myeah... and that's an understatement."
                scene DetentionClass_Sandra_Scene6 with Dissolve(0.5)
                Sandra "Listen kid, it doesn't matter what you do."
                Sandra "At the end of the day, you are a man, and all men are the same."
                Sandra "Meaning, low and savage creatures that live off the backs of hard working women!"
                Sandra "So it's nothing personal."
                scene DetentionClass_Sandra_Scene7 with Dissolve(0.5)
                Sandra "When detention starts I don't wanna hear a word, so is there anything else?"
                jump SandraDetentionMenu
            else:
                MC "I already talked to her about that."
                jump SandraDetentionMenu

        "Compliment":
            if not Watched_detention_Sandra_Compliment:
                $ Watched_detention_Sandra_Compliment = True
                MC "I just wanted to thank you for teaching me to be a better man!"
                MC "In my last school, we didn't have a manners class, but now that I've been in yours, I think every school should have it!"
                MC "Especially if it's taught by someone like you! Some day I will be a man that even you would like!"
                scene DetentionClass_Sandra_Scene8 with Dissolve(0.5)
                Sandra "Hah, wouldn't that be nice. But the best you can do is be someone that I don't hate."
                Sandra "If you listen to my classes and don't act out of place you can be on the right track."
                Sandra "But talking all this sweet stuff won't raise your grade, so tell me if you need anything else."
                scene BlackScreen with Dissolve(0.5)
                "{color=#808080}**Sandra Love + 2**{color=#808080}"
                $ Sandra_love = Sandra_love + 2
                $ check_and_update_character_stats("Sandra")
                jump SandraDetentionMenu
            else:
                MC "I already talked to her about that."
                jump SandraDetentionMenu

        "Pervert compliment":
            if not Watched_detention_Sandra_PervertCompliment:
                $ Watched_detention_Sandra_PervertCompliment = True
                MC "Uhhh, regarding the manners class..."
                MC "I think I might have a few concentration problems..."
                scene DetentionClass_Sandra_Scene9 with Dissolve(0.5)
                Sandra "A man not listening to a woman speaking isn't exactly surprising to me."
                Sandra "But come on, humor me, why can't you pay attention?"
                scene DetentionClass_Sandra_Scene10 with Dissolve(0.5)
                MC "Uhhh, well... you know..."
                MC "When you're walking between benches during class..."
                scene DetentionClass_Sandra_Scene11 with Dissolve(0.5)
                MC "I can't help but notice your huge behind..."
                scene DetentionClass_Sandra_Scene12 with Dissolve(0.5)
                Sandra "This is the exact reason I went into education!"
                Sandra "All of you disgusting men can think about one thing!"
                Sandra "You just got yourself another two hours of detention!!"
                Sandra "Now get out of my face!"
                scene BlackScreen with Dissolve(0.5)
                "{color=#808080}**Sandra Love - 2**{color=#808080}"
                "{color=#808080}**Sandra Corruption + 2**{color=#808080}"
                $ Sandra_love = Sandra_love - 2
                $ Sandra_Corruption = Sandra_Corruption + 2
                $ check_and_update_character_stats("Sandra")
                $ renpy.call("GameLoop")
            else:
                MC "I already talked to her about that."
                jump SandraDetentionMenu

        "Insult":
            if not Watched_detention_Sandra_Insult:
                $ Watched_detention_Sandra_Insult = True
                MC "{color=#808080}*Uhh, as much as I'd like to do it, I don't think this is a good idea.*{color=#808080}"
                MC "{color=#808080}*She might go directly to the principal if I do that...*{color=#808080}"
                jump SandraDetentionMenu
            else:
                MC "I already talked to her about that."
                jump SandraDetentionMenu

        "Leave":
            MC "I think I actually have something to do before detention starts, sorry!"
            scene DetentionClass_Sandra_Scene7 with Dissolve(0.5)
            Sandra "Humph... don't be late!"
            $ renpy.call("GameLoop")