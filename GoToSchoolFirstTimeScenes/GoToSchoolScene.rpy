label GoToForTheFirstTimeSchoolScene:
    scene GoToSchoolFirstScenes1 with Dissolve(0.5)
    Isabella "Come on already, Claire is going to throw a fit again!"
    scene GoToSchoolFirstScenes2 with Dissolve(0.5)
    McMom "You heard her, come on, put you shoes on."
    McMom "Isn't this your first day at this new school? You don't want to be late!"
    scene GoToSchoolFirstScenes3 with Dissolve(0.5)
    McMom "Close that gate, [MC], and come on, you don't want to be late at your first day!"
    MC "I'm coming, I'm coming, geez, we aren't even that late, it's still early."
    scene GoToSchoolFirstScenes4 with Dissolve(0.5)
    Isabella "That's what I kept saying, always on such a hurry..."
    scene GoToSchoolFirstScenes5 with Dissolve(0.5)
    Clair "Yeah... with the way mom is driving, we are already late like 3 hours."
    Clair "So get your asses in here already and stop complaining!"
    scene GoToSchoolFirstScenes6 with Dissolve(0.5)
    McMom "Are you ready kids? I hope you didn't forget anything."
    McMom "It's too late to go and get it now."
    scene GoToSchoolFirstScenes7 with Dissolve(0.5)
    MC "Are you sure it's okay to not have a backpack with me?"
    MC "Or at least a notebook or a pen?"
    scene GoToSchoolFirstScenes8 with Dissolve(0.5)
    Isabella "I already told you that you don't need anything, the school provides you with everything you need."
    Isabella "So stop worrying so much. What you don't believe me?"
    scene GoToSchoolFirstScenes9 with Dissolve(0.5)
    MC "I'm sorry, Isa, but your track record of being right on things isn't the best."
    MC "I'm just trying to make sure."
    scene GoToSchoolFirstScenes10 with Dissolve(0.5)
    Isabella "What do you mean by that?!"
    Isabella "I'm always right on things!"
    scene GoToSchoolFirstScenes11 with Dissolve(0.5)
    Clair "As much as I hate to admit it, [MC] is right."
    Clair "You get things right for a staggering amount of one out of a hundred times."
    scene GoToSchoolFirstScenes12 with Dissolve(0.5)
    Isabella "Since when did you start taking his side?"
    Isabella "Did you two become best friends all of a sudde-"
    scene GoToSchoolFirstScenes13 with Dissolve(0.5)
    Clair "Buuuuut, this is the one out of those a hundred times surprisingly."
    Clair "So yeah, she's right, you don't have to bring anything to school."
    Clair "So you could stop crying now."
    scene GoToSchoolFirstScenes14 with Dissolve(0.5)
    McMom "Stop fighting kids! This is not the time to put stress on [MC]!"
    McMom "It's his first day, he is just nervous."
    scene GoToSchoolFirstScenes15 with Dissolve(0.5)
    Clair "Then just drive already!"
    $ firstPosition = closer0
    $ MCclose = False
    $ isHandOnThigh = False
    $ isHandOnTits = False
    $ isHandOnMouth = False
    $ annoyed_counter = 0
    $ love_counter = 0
    $ reachButtonsActive = False
    $ hintLocationsActive = False
    $ default_mouse = "default"
    $ lastHandLocation = "thigh"
    call screen GoToSchoolFirstTimeScreen

label GoToSchoolScene:
    scene GoToSchoolFirstScenes1 with Dissolve(0.5)
    Isabella "Come on already, Claire is going to throw a fit again!"
    scene GoToSchoolFirstScenes2 with Dissolve(0.5)
    McMom "You heard her, come on, put you shoes on."
    scene GoToSchoolFirstScenes3 with Dissolve(0.5)
    McMom "Close that gate, [MC], and hurry up, we're going to be late!"
    MC "I'm coming, I'm coming, geez, we aren't even that late, it's still early."
    scene GoToSchoolFirstScenes4 with Dissolve(0.5)
    Isabella "That's what I kept saying, always on such a hurry..."
    scene GoToSchoolFirstScenes5 with Dissolve(0.5)
    Clair "Yeah... with the way mom is driving, we are already late like 3 hours."
    Clair "So get your asses in here already and stop complaining!"
    scene GoToSchoolFirstScenes6 with Dissolve(0.5)
    McMom "Are you ready kids? I hope you didn't forget anything."
    McMom "It's too late to go and get it now."
    scene GoToSchoolFirstScenes7 with Dissolve(0.5)
    MC "Yeah, we're ready..."
    $ firstPosition = closer0
    $ MCclose = False
    $ isHandOnThigh = False
    $ isHandOnTits = False
    $ isHandOnMouth = False
    $ annoyed_counter = 0
    $ love_counter = 0
    $ reachButtonsActive = False
    $ hintLocationsActive = False
    $ default_mouse = "default"
    $ lastHandLocation = "thigh"
    call screen GoToSchoolFirstTimeScreen