init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("Pool_Isabella_Criss_Scene", "SwimClass/Isabella_Criss_Scene", "Pool_Isabella_Criss_Scene", 100)

label SwimClass_Isabella_Criss_Scene:
    if Watched_SwimClass_Isabella_Criss_Scene:
        scene Pool_Isabella_Criss_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her about this...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Isabella_Criss_Scene = True
        
        scene Pool_Isabella_Criss_Scene1 with Dissolve(0.5)
        Isabella "Come on, Criss, why are you such a scaredy-cat? It won't hurt!"
        scene Pool_Isabella_Criss_Scene2 with Dissolve(0.5)
        MC "Isa... stop bullying Criss, can't you see she's uncomfortable?"
        scene Pool_Isabella_Criss_Scene3 with Dissolve(0.5)
        Isabella "Oh great, here comes the party pooper, spraying explosive diarrhea all over my fun..."
        scene Pool_Isabella_Criss_Scene4 with Dissolve(0.5)
        MC "Your fun is troubling Criss, you brat."
        scene Pool_Isabella_Criss_Scene5 with Dissolve(0.5)
        Isabella "I'm just trying to help her, okay? She's scared to jump into the water."
        scene Pool_Isabella_Criss_Scene6 with Dissolve(0.5)
        Isabella "And I'm trying to give her a... ummm... uhhh... a head start!"
        scene Pool_Isabella_Criss_Scene7 with Dissolve(0.5)
        MC "Just leave her alone, Isa. She's clearly uncomfortable."
        scene Pool_Isabella_Criss_Scene8 with Dissolve(0.5)
        Isabella "Ughhh, alright, fine..."
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Criss love + 2**{color=#808080}"
        "{color=#808080}**Isabella love + 2**{color=#808080}"
        $ LilSis_love = LilSis_love + 2 
        $ Criss_love = Criss_love + 2
        $ check_and_update_character_stats("Criss")
        $ check_and_update_character_stats("LilSis")
        $ renpy.call("GameLoop")
