init python:
    define_images("Pool_Helena_Alis_Sophie_Scene", "SwimClass/Helena_Alis_Sophie_Scene", "Pool_Helena_Alis_Sophie_Scene", 100)

label SwimClass_Helena_Alis_Sophie_Scene:
    if Watched_SwimClass_Helena_Alis_Sophie_Scene:
        scene Pool_Helena_Alis_Sophie_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to them about that...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Helena_Alis_Sophie_Scene = True
        
        scene Pool_Helena_Alis_Sophie_Scene1 with Dissolve(0.5)
        MC "Hey Helena, what are y'all doing?"
        scene Pool_Helena_Alis_Sophie_Scene2 with Dissolve(0.5)
        Helena "Oh, hey, [MC]!"
        Helena "I'm trying to convince the girls to get in the water with me, but they don't want to!"
        scene Pool_Helena_Alis_Sophie_Scene3 with Dissolve(0.5)
        Helena "Come on already! You two are so boring!"
        scene Pool_Helena_Alis_Sophie_Scene4 with Dissolve(0.5)
        Sophie "Ughhh... You don't understand, Helena."
        scene Pool_Helena_Alis_Sophie_Scene5 with Dissolve(0.5)
        Sophie "I have to get my tan to look right, I can't be here looking like a ghost!"
        scene Pool_Helena_Alis_Sophie_Scene6 with Dissolve(0.5)
        MC "Getting a tan with a swimsuit like that? I don't know about that..."
        scene Pool_Helena_Alis_Sophie_Scene7 with Dissolve(0.5)
        Sophie "Oh my god, wait! You're right, the tan lines are going to look awful from this swimsuit!"
        Sophie "What do I do?! What do I do?!"
        scene Pool_Helena_Alis_Sophie_Scene8 with Dissolve(0.5)
        Alis "Just go in the water Sophie... Or don't stay in the sun..."
        scene Pool_Helena_Alis_Sophie_Scene9 with Dissolve(0.5)
        Helena "Nice, we got one!"
        scene Pool_Helena_Alis_Sophie_Scene10 with Dissolve(0.5)
        Helena "Now let's see how we can get Alis!"
        scene Pool_Helena_Alis_Sophie_Scene11 with Dissolve(0.5)
        Helena "Come on, why don't you wanna get it?!"
        scene Pool_Helena_Alis_Sophie_Scene12 with Dissolve(0.5)
        Alis "I'll get enough water when the class starts."
        Alis "Stop insisting please..."
        scene Pool_Helena_Alis_Sophie_Scene13 with Dissolve(0.5)
        Helena "Okay, I'm sorry, I will stop..."
        scene Pool_Helena_Alis_Sophie_Scene14 with Dissolve(0.5)
        MC "Huh?! Are you giving up that fast?"
        scene Pool_Helena_Alis_Sophie_Scene15 with Dissolve(0.5)
        MC "Come on, Alis, getting in now or 5 minutes later, what's the difference?"
        scene Pool_Helena_Alis_Sophie_Scene16 with Dissolve(0.5)
        Alis "Well... If you ask that nicely, how could a shy girl like me ever refuse?"
        scene Pool_Helena_Alis_Sophie_Scene17 with Dissolve(0.5)
        MC "{color=#808080}*Ahh... shit... I might've fucked up...*"
        scene Pool_Helena_Alis_Sophie_Scene18 with Dissolve(0.5)
        Alis "What if I don't know how to swim?"
        Alis "How would you help me?"
        scene Pool_Helena_Alis_Sophie_Scene19 with Dissolve(0.5)
        Alis "What if I drown? Will you give me mouth to mouth?"
        scene Pool_Helena_Alis_Sophie_Scene20 with Dissolve(0.5)
        Alis "Would you rip off my swimsuit to help me breathe better?"
        scene Pool_Helena_Alis_Sophie_Scene21 with Dissolve(0.5)
        MC "Ummm... uhhh.... uhhh... yeah... all of that..."
        MC "But I have to go now... Miss White asked to see me..."
        MC "Uhhhhh... see you later..."
        scene Pool_Helena_Alis_Sophie_Scene22 with Dissolve(0.5)
        Alis "Well, isn't that a shame?"
        Alis "We can play together later then."
        scene Pool_Helena_Alis_Sophie_Scene23 with Dissolve(0.5)
        MC "{color=#808080}*Jesus Christ, what the fuck am I doing!?!?*"
        MC "{color=#808080}*I had it all right there!*"
        MC "{color=#808080}*Her tits squeezing on my chest.*"
        MC "{color=#808080}*Her leg tightly hugging me.*"
        MC "{color=#808080}*My dick pushing onto her.*"
        MC "{color=#808080}*Her lips two centimeters away from mine!*"
        MC "{color=#808080}*And I fumbled! I fucked up! I pussyed out!*"
        MC "{color=#808080}*What the fuck is wrong with me!? And why always with her?!*"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Helena love + 2**{color=#808080}"
        "{color=#808080}**Sophie love + 2**{color=#808080}"
        "{color=#808080}**Alis love + 2**{color=#808080}"
        $ Helena_love = Helena_love + 2
        $ Sophie_love = Sophie_love + 2
        $ Alis_love = Alis_love + 2
        $ check_and_update_character_stats("Helena")
        $ check_and_update_character_stats("Sophie")
        $ check_and_update_character_stats("Alis")
        $ renpy.call("GameLoop")
