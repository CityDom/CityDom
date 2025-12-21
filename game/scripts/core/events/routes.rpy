label GameIntroEvent:
    jump GameIntro
    $ LoadIntro = False
    return

label LeaveHomeEvent:
    jump LeaveHomeLVL1
    return

label LunchGroupEvent:
    jump LunchEventLVL1
    return

label ClaireMidnightEvent14:
    jump ClaireMidnight14

label ClaireEveningEvent34:
    jump ClaireEvening34
    return

label ClaireEveningEvent44:
    jump ClaireEvening44
    return

label ClaireNightEvent34:
    jump ClaireNight34
    return

label ClaireNightEvent44:
    jump ClaireNight44
    return

label ClaireEveningEvent24:
    jump ClaireEvening24
    return

label ClaireEveningEvent14:
    jump ClaireEvening14
    return

label ClaireNoonEvent14:
    jump ClaireNoon14
    return

label ClaireMorningEvent34:
    jump ClaireMorning34
    return

label ClaireMorningEvent24:
    jump ClaireMorning24
    return

label ClaireMorningEvent14:
    jump ClaireMorning14
    return

label IsabellaEveningEvent44:
    jump IsabellaEvening44
    return

label IsabellaEveningEvent34:
    jump IsabellaEvening34
    return

label IsabellaMidnightEvent14:
    jump IsabellaMidnight14
    return

label IsabellaEveningEvent24:
    jump IsabellaEvening24
    return

label IsabellaNightEvent44:
    jump IsabellaNight44
    return

label MovieNightEvent:
    jump MovieNightLVL1
    return

label IsabellaAfterNoonEvent44:
    jump IsabellaAfterNoon44
    return

label IsabellaMorningEvent34:
    scene Isabella_morning34_12
    jump IsabellaMorning34

label IsabellaNightEvent34:
    scene Jennifer_night24_0
    jump IsabellaNight34
    return

label IsabellaMorningEvent24:
    scene Jennifer_morning34_0
    jump IsabellaMorning24

label IsabellaMorningEvent14:
    scene Isabella_morning14_1
    jump IsabellaMorning14

label JenniferMorningEvent14:
    jump JenniferMorning14

label JenniferMorningEvent34:
    scene Jennifer_morning34_0
    jump JenniferMorning34
    return

label JenniferMorningEvent44:
    scene Jennifer_morning44_0
    jump JenniferMorning44
    return

label JenniferEveningEvent24:
    scene Jennifer_evening24_32
    jump JenniferEvening24
    return

label JenniferEveningEvent34:
    scene Jennifer_morning44_0
    jump JenniferEvening34
    return

label JenniferNightEvent34:
    jump JenniferNight34
    return

label JenniferNightEvent44:
    jump JenniferNight44
    return

label DinnerGroupEvent:
    jump DinnerEventLVL1
    return

label IsabellaNoonEvent14:
    jump IsabellaNoon14
    return

label IsabellaNoonEvent24:
    jump IsabellaNoon24
    return

label IsabellaEveningEvent14:
    jump IsabellaEvening14
    return
