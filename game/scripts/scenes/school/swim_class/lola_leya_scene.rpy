init python:
    define_images("Pool_Lola_Leya_Scene", "SwimClass/Lola_Leya_Scene", "Pool_Lola_Leya_Scene", 100)

label SwimClass_Lola_Leya_Scene:
    if Watched_SwimClass_Lola_Leya_Scene:
        scene Pool_Lola_Leya_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I've already talked to them about this...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Lola_Leya_Scene = True
        
        scene Pool_Lola_Leya_Scene1 with Dissolve(0.5)
        MC "Uhhh... Is Lola good at any sport?"
        scene Pool_Lola_Leya_Scene2 with Dissolve(0.5)
        Leya "Not gymnastics..."
        scene Pool_Lola_Leya_Scene3 with Dissolve(0.5)
        Lola "IT'S THE ONLY THING, OKAY?!?!"
        scene Pool_Lola_Leya_Scene4 with Dissolve(0.5)
        Lola "AND YOU CAN'T EVEN SWIM!!"
        scene Pool_Lola_Leya_Scene5 with Dissolve(0.5)
        MC "Wait, what?! You don't know how to swim?!"
        scene Pool_Lola_Leya_Scene6 with Dissolve(0.5)
        Leya "Tsk..."
        scene Pool_Lola_Leya_Scene7 with Dissolve(0.5)
        Leya "I just never put in the time to learn, okay?!"
        scene Pool_Lola_Leya_Scene8 with Dissolve(0.5)
        MC "Hmmm... That's hard to believe..."
        MC "You can't even reach the ground here, and you don't seem too scared of the water..."
        scene Pool_Lola_Leya_Scene9 with Dissolve(0.5)
        Leya "Wait, what?! What do you mean I can't reach here, am I not at the edge of the pool?!"
        scene Pool_Lola_Leya_Scene10 with Dissolve(0.5)
        MC "Ummm... You're in the middle of the pool, Leya."
        scene Pool_Lola_Leya_Scene11 with Dissolve(0.5)
        MC "......"
        MC "{color=#808080}*Maybe I shouldn't have told her that...*"
        scene Pool_Lola_Leya_Scene12 with Dissolve(0.5)
        Tanya "[MC_upper], HELP HER ALREADY!! DON'T JUST STARE HER!!"
        scene Pool_Lola_Leya_Scene13 with Dissolve(0.5)
        MC "{color=#808080}*Ughh... isn't that your job, Tanya?*"
        scene Pool_Lola_Leya_Scene14 with Dissolve(0.5)
        Lola "Oh my god, [MC], get her fast!"
        scene Pool_Lola_Leya_Scene15 with Dissolve(0.5)
        Lola "God damn it, Leya, I thought you knew what you were doing!"
        Lola "What are you doing in the middle of the pool like that?!"
        scene Pool_Lola_Leya_Scene16 with Dissolve(0.5)
        Leya "I didn't know I got all the way here, okay?"
        scene Pool_Lola_Leya_Scene17 with Dissolve(0.5)
        MC "It's okay, Leya, you're safe now, let's get you to the pool edge so you can calm down."
        scene Pool_Lola_Leya_Scene18 with Dissolve(0.5)
        Leya "Okay..."
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Lola love + 2**{color=#808080}"
        "{color=#808080}**Leya love + 2**{color=#808080}"
        $ Leya_love = Leya_love + 2 
        $ Lola_love = Lola_love + 2
        $ check_and_update_character_stats("Lola")
        $ check_and_update_character_stats("Leya")
        $ renpy.call("GameLoop")
