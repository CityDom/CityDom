label JenniferCallToMeDialog:
    if 5 < calendar.Hours < 14:
        MC "MOOOOOOM!!"
        MC "MOOOOOOOOOOOOOOOM!!!!"
        MC "{color=#808080}*What the fuck is she doing... she usually answers me...*{/color}"
        MC "{color=#808080}*Oh wait, that's right, she's not home..*{/color}"
        $ current_location = str(Location).lower()
        jump GameLoop
    else:
        MC "MOOOOOOM!!!"
        MC "MOOOOOOOOOOOOOOOM!!!"
        Jennifer "WHAT DO YOU WANT??!?! WHY ARE YOU YELLING!?!?"
        Jennifer "IF YOU WANT SOMETHING COME HERE AND ASK!!!!"
        MC "CAN YOU COME HERE FOR A SECOND?"
        Jennifer "IF YOU WANT SOMETHING YOU COME TO ME YOUNG MAN!!!"
        Jennifer "YOU DON'T PAY ANY BILLS IN THIS HOUSE TO MAKE ME COME TO YOU FOR SOMETHING."
        MC "Tsk...."
        $ current_location = str(Location).lower()
        jump GameLoop