label BigSisScenes:
    init python:
        def define_images(variable_prefix, folder, image_prefix, count):
            for i in range(1, count + 1):
                variable_name = f"{variable_prefix}{i}"
                image_path = f"{folder}/{image_prefix}{i}.webp"
                renpy.image(variable_name, image_path)

        #Morning scenes
        define_images("MORNING14BIGSIS", "BigSisAllScenes/BigSisMorning14", "BigSisMorning", 7)
        define_images("MORNING24BIGSIS", "BigSisAllScenes/BigSisMorning24", "BigSisMorning", 7)
        define_images("MORNING34BIGSIS", "BigSisAllScenes/BigSisMorning34", "BigSisMorning", 1)

        #Noon scenes
        define_images("NOON14BIGSIS", "BigSisAllScenes/BigSisNoon14", "BigSisNoon", 15)

        #Evening scenes
        define_images("EVENING14BIGSIS", "BigSisAllScenes/BigSisEvening14", "BigSisEvening", 15)
        define_images("EVENING24BIGSIS", "BigSisAllScenes/BigSisEvening24", "BigSisEvening", 15)
        define_images("EVENING34BIGSIS", "BigSisAllScenes/BigSisEvening34", "BigSisEvening", 1)
        define_images("EVENING44BIGSIS", "BigSisAllScenes/BigSisEvening44", "BigSisEvening", 15)

        #Night scenes
        define_images("NIGHT34BIGSIS", "BigSisAllScenes/BigSisNight34", "BigSisNight", 15)
        define_images("NIGHT44BIGSIS", "BigSisAllScenes/BigSisNight44", "NIGHT44BIGSIS", 15)

        #Midnight scenes
        define_images("MIDNIGHT14BIGSIS", "BigSisAllScenes/BigSisMidnight14", "BigSisMidnight", 10)