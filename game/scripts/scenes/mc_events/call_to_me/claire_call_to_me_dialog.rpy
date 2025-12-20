label ClaireCallToMeDialog:
    if 5 < calendar.Hours < 13:
        MC "CLAIRE!!!"
        MC "CLAIRE, CAN YOU COME HERE FOR A SECOND??"
        MC "{color=#808080}Oh wait, she's not even home...{/color}"
        $ current_location = str(Location).lower()
        jump GameLoop
    else:
        MC "CLAIRE!!!"
        "..........."
        MC "CLAAAAAAAAAIRE!!!"
        MC "{color=#808080}I bet she hears me, but doesn't even want to answer me...{/color}"
        $ current_location = str(Location).lower()
        jump GameLoop