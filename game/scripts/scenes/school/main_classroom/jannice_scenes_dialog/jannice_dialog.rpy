
label JanniceClassroomScene:
    scene JanniceScene1 with Dissolve(0.5)
    MC "Hey, Miss Thompson"
    scene JanniceScene2 with Dissolve(0.5)
    Jannice "Is there a problem, [MC]?"
    jump first_menu

label first_menu:
    scene JanniceScene1 with Dissolve(0.5)
    menu:
        "Talk":
            jump janniceTalk_menu
        "Leave":
            MC "There is no problem, sorry for bothering you."
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")

label janniceTalk_menu:
    menu:
        "What do you think about me?":
            scene JanniceScene3 with Dissolve(0.5)
            MC "I wanted to ask you, what do you think about me?"
            scene JanniceScene4 with Dissolve(0.5)
            Jannice "Well, you just moved to this class, so there isn't much to go off."
            Jannice "But keep doing your homework and don't be late and you should be good."
            scene JanniceScene3 with Dissolve(0.5)
            MC "{color=#808080}*Ughh... that's not what I was referring to...*"
            jump first_menu
        "Compliment":
            if JanniceComplimentWatched:
                MC "{color=#808080}*I already complimented her*"
                jump first_menu
            scene JanniceScene5 with Dissolve(0.5)
            MC "I just wanted to tell you that you look amazing today, Miss Thompson"
            scene JanniceScene6 with Dissolve(0.5)
            Jannice "Compliments won't raise your grades [MC]."
            Jannice "Now go back to your seat, class is about to start"
            $ JanniceComplimentWatched = True
            call stat_reward({"Jannice": {"love": 2}}, return_to=None)
            jump first_menu
        "Pervert compliment":
            if JannicePervComplimentWatched:
                MC "{color=#808080}*I already complimented her*"
                jump first_menu          
            scene JanniceScene7 with Dissolve(0.5)
            MC "There is no problem, Miss Thompson, I was just admiring your boobs."
            MC "They look really good today."
            scene JanniceScene9 with Dissolve(0.5)
            Jannice "This is no way to talk to a teacher, [MC]!!"
            Jannice "Enjoy your time in detention today, go to your seat!"
            call stat_reward({"Jannice": {"love": -5, "corruption": 2}}, return_to=None)
            $ JannicePervComplimentWatched = True
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")
        "Insult":
            if JanniceInsultWatched:
                MC "{color=#808080}*I already insulted her*"
                jump first_menu         
            scene JanniceScene11 with Dissolve(0.5)
            MC "I just wanted to ask if you are okay, Miss Thompson."
            scene JanniceScene10 with Dissolve(0.5)
            Jannice "Uhhh, yeah, I'm fine, why are you asking?"
            scene JanniceScene12 with Dissolve(0.5)
            MC "You just seem to have gained some weight lately, are you sure you are alright?"
            scene JanniceScene13 with Dissolve(0.5)
            Jannice "I'm fine, [MC], go back to your seat right now! You have detention!!"
            call stat_reward({"Jannice": {"love": -5, "corruption": -5}}, return_to=None)
            $ JanniceInsultWatched = True
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")
        "Leave":
            MC "I have to go Miss Thompson, sorry for bothering you."
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")
