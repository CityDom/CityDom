init python:
    define_images("GretaPauseScene", "SchoolFirstPause/GretaEventScene", "GretaPauseScene", 60)

label GretaFirstPauseScene:
    scene GretaPauseScene1 with Dissolve(0.5)
    MC "Hey Greta, what are you doing? The bell rung."
    "........."
    MC "Gretaaaaaa!"
    scene GretaPauseScene2 with Dissolve(0.5)
    Greta "Oh, hey [MC], sorry, I didn't notice you."
    Greta "I was so focused I didn't even realize you were there."
    Greta "Do you need help with something?"
    scene GretaPauseScene3 with Dissolve(0.5)
    MC "No? Why do you assume I need help with something?"
    scene GretaPauseScene2 with Dissolve(0.5)
    Greta "Because you don't usually speak to me unless you need help with something."
    scene GretaPauseScene3 with Dissolve(0.5)
    MC "{color=#808080}*Damn... she picked up on that, she's smarter than I thought.*"
    scene GretaPauseScene2 with Dissolve(0.5)
    Greta "So? What do you need?"
    jump GretaFirstPauseMenu
label GretaFirstPauseMenu:    
    scene GretaPauseScene4 with Dissolve(0.5)
    menu:
        "What do you think about me?":
            MC "Well, since I just transferred here, I wanted to ask you, what do you think about me?"
            scene GretaPauseScene5 with Dissolve(0.5)
            Greta "Ummm.. well... as you said, you just moved here, so I didn't got the chance to form that much of an opinion."
            Greta "But Selina seems to hate you really much."
            Greta "So we can't really chat when she's around."
            scene GretaPauseScene4 with Dissolve(0.5)
            MC "Oh... I understand..."
            jump GretaFirstPauseMenu
        "Chat":
            menu:
                "Talk":
                    scene GretaPauseScene15 with Dissolve(0.5)
                    MC "I was curious why you were still studying, the class ended."
                    MC "Don't tell me we have an exam coming up."
                    scene GretaPauseScene16 with Dissolve(0.5)
                    Greta "Uhhhh... no...."
                    Greta "I just have a bit of a harder time keeping up with everyone."
                    Greta "So I have to put in some extra effort."
                    scene GretaPauseScene17 with Dissolve(0.5)
                    MC "What do you mean? You have good grades, even higher than mine!"
                    scene GretaPauseScene18 with Dissolve(0.5)
                    Greta "That's because you don't study at all, [MC], and you skip school."
                    Greta "And despite all of that you still have passing grades. If I was doing that I would have only ones and twos."
                    Greta "And Selina still has way higher grades than me..."
                    scene GretaPauseScene19 with Dissolve(0.5)
                    MC "Ohhh, c'mon, you don't have to compare to her, she was just born a genius."
                    scene GretaPauseScene20 with Dissolve(0.5)
                    Greta "You're wrong... I have to... I have to get good grades and get a job as soon as possible."
                    Greta "I have to help my family however I can."
                    scene GretaPauseScene21 with Dissolve(0.5)
                    MC "Why aren't you asking Selina for a bit of help, you two seem to be good friends."
                    scene GretaPauseScene22 with Dissolve(0.5)
                    Greta "I could never do that! I know people think I stick around her for money but that's not true at all!"
                    Greta "She is like an idol to me, and I'm trying to learn from her example. I try to be just like her."
                    scene GretaPauseScene23 with Dissolve(0.5)
                    MC "Well... then maybe I can help you!"
                    scene GretaPauseScene24 with Dissolve(0.5)
                    Greta "No, no, no! I couldn't possibly accept something like that!"
                    Greta "I'm sorry if what I said came around as begging for money, but that's not what I meant at all!"
                    Greta "I really try to earn what I can fair and square!"
                    Greta "So if you don't need anything else, I will go back at learning!"
                    call stat_reward({"Greta": {"love": 2}}, show_black=False, return_to="GretaFirstPauseMenu")
                "Compliment":
                    MC "Well, since I got the moment and its just the two of us, I wanted to tell you that you looked really nice today!"
                    scene GretaPauseScene6 with Dissolve(0.5)
                    Greta "..."
                    Greta "......"
                    MC "Uhhh... did I say something wrong? Are you ok?"
                    scene GretaPauseScene7 with Dissolve(0.5)
                    Greta "Ohhh, no, no, it's just that... nobody told me that before..."
                    Greta "Thank you!"
                    scene GretaPauseScene8 with Dissolve(0.5)
                    MC "Whaaaat??? Really? Come on, stop joking, there is no chance nobody told you that before!"
                    scene GretaPauseScene9 with Dissolve(0.5)
                    Greta "It... It's true..."
                    scene GretaPauseScene10 with Dissolve(0.5)
                    Greta "Ummmm, anyway, I have to go back to studying, is there something else that you need help with?"
                    call stat_reward({"Greta": {"love": 5}}, show_black=False, return_to="GretaFirstPauseMenu")
                "Pervert Compliment":
                    scene GretaPauseScene11 with Dissolve(0.5)
                    MC "I just wanted to let you know that you look really hot today!"
                    MC "And your tits look amazing!"
                    scene GretaPauseScene12 with Dissolve(0.5)
                    Greta "I really don't need to hear that, [MC]!"
                    Greta "I thought you actually wanted some help."
                    Greta "Now leave, I have to study!"
                    call stat_reward({"Greta": {"love": -5, "corruption": 2}}, show_black=False, return_to=None)
                    $ advance_time_or_sleep()
                "Insult":
                    scene GretaPauseScene14 with Dissolve(0.5)
                    MC "You should really lose some fat, Greta!"
                    MC "Out of this class you are the heaviest one, the other girls look way better than you."
                    scene GretaPauseScene13 with Dissolve(0.5)
                    Greta "So you just came here to bully me?"
                    Greta "I really wanted to help you."
                    Greta "At least tell me an insult that I haven't heard before!"
                    Greta "Leave already!! I have better stuff to do than to talk to you"
                    call stat_reward({"Greta": {"love": -5}}, show_black=False, return_to=None)
                    $ advance_time_or_sleep()
                "Leave":
                    jump GretaFirstPauseMenu
        "Give money":
            scene GretaPauseScene25 with Dissolve(0.5)
            MC "Here, you can have them"
            scene GretaPauseScene26 with Dissolve(0.5)
            Greta "No, no, no, [MC], you got it all wrong, please, I can't accept this money."
            Greta "I told you, I don't want to go around begging for money, I want to earn them!"
            scene GretaPauseScene27 with Dissolve(0.5)
            MC "But you are not begging for them, Greta, and you can earn them if you want."
            MC "You can do something for me. Plus you've always been nice to me ever since I came here, so you deserve it."
            scene GretaPauseScene28 with Dissolve(0.5)
            Greta "I can't, [MC]. I can't accept this much money just to give you the homework and stuff like that."
            scene GretaPauseScene27 with Dissolve(0.5)
            MC "Ok, so you want to work it harder for it?"
            scene GretaPauseScene28 with Dissolve(0.5)
            Greta "Y-yeah..."
            scene GretaPauseScene27 with Dissolve(0.5)
            MC "Then let's put some conditions on it."
            MC "You won't tell anyone that we are making this deal. Especially Selina."
            scene GretaPauseScene30 with Dissolve(0.5)
            Greta "But-"
            scene GretaPauseScene29 with Dissolve(0.5)
            MC "No buts! You said you wanted to earn this money, there you have it! Understood?!"
            scene GretaPauseScene28 with Dissolve(0.5)
            Greta "Y-yes..."
            scene GretaPauseScene29 with Dissolve(0.5)
            MC "Okay, and besides not telling anyone about the deal, you won't tell anyone what I ask you to do, understood?"
            scene GretaPauseScene28 with Dissolve(0.5)
            Greta "Yes... what do you want me to do?"
            scene GretaPauseScene30 with Dissolve(0.5)
            MC "I just want you to lift up your shirt for me."
            Greta "What do you mean lift up my shirt?!?! I won't undress for money!!"
            Greta "Do you think I'm a whore?!"
            scene GretaPauseScene31 with Dissolve(0.5)
            MC "GRETA!!"
            MC "How could you say that about yourself?!?!!"
            MC "I would never think that about you!"
            scene GretaPauseScene32 with Dissolve(0.5)
            Greta "But I learned that girls that undress themselves for money are called whores..."
            scene GretaPauseScene33 with Dissolve(0.5)
            MC "You have to listen to me Greta, you already told me that you are not the brightest girl in the world, right?"
            scene GretaPauseScene34 with Dissolve(0.5)
            Greta "Y-yeah..."
            scene GretaPauseScene35 with Dissolve(0.5)
            MC "Think about it. I can't ask you to do my homework or stuff like that because it would take a lot of your time."
            MC "And you have to focus at your study. So it has to be something quick."
            MC "But it can't be to easy for you, otherwise you will feel like you don't deserve the money."
            scene GretaPauseScene36 with Dissolve(0.5)
            MC "Plus, no one is in the class right now, so nobody would see you do it. And we already agreed that you won't tell nobody."
            MC "And I can promise you on everything I have that I won't say a word, I'm just trying to help you."
            MC "So you are not a whore for doing it, you are choosing the smartest choice. So it actually makes you smart, not a whore!"
            scene GretaPauseScene37 with Dissolve(0.5)
            Greta "Oh my God, you are right!!"
            scene GretaPauseScene38 with Dissolve(0.5)
            MC "See? I told you you are a smart girl!"
            scene GretaPauseScene39 with Dissolve(0.5)
            Greta "Hehe, thanks!"
            Greta "So what do I have to do?"
            scene GretaPauseScene40 with Dissolve(0.5)
            menu:
                "Lift up your shirt":
                    $ Maria_Report_Greta = True
                    MC "Lift up your shirt for me, that's all."
                    scene GretaPauseScene41 with Dissolve(0.5)
                    Greta "Uhhh... okay..."
                    scene GretaPauseScene42 with Dissolve(0.5)
                    Greta "Is this okay?"
                    scene GretaPauseScene43 with Dissolve(0.5)
                    MC "Oh my God, Greta, it's perfect."
                    scene GretaPauseScene44 with Dissolve(0.5)
                    MC "They are bigger than I thought!"
                    MC "But why are you wearing a sports bra?"
                    scene GretaPauseScene45 with Dissolve(0.5)
                    Greta "Normal bras are really uncomfortable... and I can't find one that fits..."
                    Greta "But can we please not talk about them. I'm felling really uncomfortable..."
                    scene GretaPauseScene46 with Dissolve(0.5)
                    MC "You shouldn't be uncomfortable at all! You look really good right now."
                    MC "You should be more proud of them, not many girls have this big of a chest. Maybe you should try wearing regular bras."
                    MC "Just look more for something that fits, it will boost your confidence a lot!"
                    scene GretaPauseScene45 with Dissolve(0.5)
                    Greta "If you say so...."
                    Greta "Can I put my shirt down now?"
                    menu:
                        "Ask to touch them":
                            MC "Can I also touch them?"
                            scene GretaPauseScene47 with Dissolve(0.5)
                            Greta "You are crossing the line [MC]!"
                            Greta "You said that it won't take long, so please leave, I have to study!"
                            call stat_reward({"Greta": {"love": -5}}, show_black=False, return_to=None)
                            $ advance_time_or_sleep()
                        "Don't":
                            MC "Yeah, you can put your shirt down."
                            scene GretaPauseScene48 with Dissolve(0.5)
                            Greta "Really?! That was all? And I get to have the money?"
                            scene GretaPauseScene49 with Dissolve(0.5)
                            MC "Yep, I told you it was a really smart choice from you, don't you feel smarter because you listened to me?"
                            scene GretaPauseScene50 with Dissolve(0.5)
                            Greta "I really do, [MC]!"
                            Greta "Thank you!"
                            scene GretaPauseScene51 with Dissolve(0.5)
                            MC "No problem, Greta, I'm glad that I can help you."
                            MC "I told you I won't keep you occupied too much, so I'll leave, you can continue your study."
                            scene GretaPauseScene50 with Dissolve(0.5)
                            Greta "You are right! I also have some time left to study, and I also made some money!"
                            Greta "See you around, [MC]!"
                            call stat_reward({"Greta": {"love": 5}}, show_black=False, return_to=None)
                            $ Greta_Obedience = Greta_Corruption + 5
                            $ Greta_Obedience = Greta_Obedience + 5
                            $ advance_time_or_sleep()
        "Leave":
            scene GretaPauseScene19 with Dissolve(0.5)
            MC "Ohhh, sorry Greta, I remember I had something to do and I'm already late."
            MC "See you later!"
            scene GretaPauseScene6 with Dissolve(0.5)
            Greta "Oh, ok.. byee!"
            $ renpy.call("GameLoop")