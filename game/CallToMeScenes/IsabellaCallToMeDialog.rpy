label IsabellaCallToMeDialog:
    if 5 < calendar.Hours < 10:
        MC "ISAAA!!"
        MC "ISABELLAAAAAAA!!!!"
        MC "{color=#808080}Is she fucking ignoring me again?{/color}"
        MC "{color=#808080}Oh wait, she's not, it's just that she's not home...{/color}"
        $ current_location = str(Location).lower()
        jump GameLoop
    else:
        MC "ISAAAAA!!!!!"
        MC "ISABELLAAAAAAAAAA!!!!!"
        Isabella "YEAAA, WHAT DO YOU WANT!?!"
        MC "CAN YOU COME HERE FOR A SECOND???"
        Isabella "I DON'T WANNA, COME HERE IF YOU WANT!!!"
        $ current_location = str(Location).lower()
        jump GameLoop

