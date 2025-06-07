label LilSisScenes:
    init python:
        def define_images(variable_prefix, folder, image_prefix, count):
            for i in range(1, count + 1):
                variable_name = f"{variable_prefix}{i}"
                image_path = f"{folder}/{image_prefix}{i}.webp"
                renpy.image(variable_name, image_path)

        #Morning scenes
        define_images("MORNING14LILSIS", "LilSisAllScenes/LilSisMorning14", "LilSisMorning", 18)
        define_images("MORNING24LILSIS", "LilSisAllScenes/LilSisMorning24", "LilSisMorning", 19)
        define_images("MORNING34LILSIS", "LilSisAllScenes/LilSisMorning34", "LilSisMorning", 12)

        #Night scenes
        define_images("NIGHT34LILSIS", "LilSisAllScenes/LilSisNight34", "LilSisNight", 2)
        define_images("NIGHT44LILSIS", "LilSisAllScenes/LilSisNight44", "LilSisNight", 34)

        #Noon scenes
        define_images("NOON14LILSIS", "LilSisAllScenes/LilSisNoon14", "LilSisNoon", 11)
        define_images("NOON24LILSIS", "LilSisAllScenes/LilSisNoon24", "LilSisNoon", 16)

        #Evening scenes
        define_images("EVENING24LILSIS", "LilSisAllScenes/LilSisEvening14", "LilSisEvening", 13)
        define_images("EVENING14LILSIS", "LilSisAllScenes/LilSisEvening24", "LilSisEvening", 20)
        define_images("EVENING34LILSIS", "LilSisAllScenes/LilSisEvening34", "LilSisEvening", 25)
        define_images("EVENING44LILSIS", "LilSisAllScenes/LilSisEvening44", "LilSisEvening", 91)

        #Afternoon scenes
        define_images("AFTERNOON44LILSIS", "LilSisAllScenes/LilSisAfterNoon44", "LilSisAfterNoon", 28)

        #Midnight scenes
        define_images("MIDNIGHT14LILSIS", "LilSisAllScenes/LilSisMidnight14", "LilSisMidnight", 10)