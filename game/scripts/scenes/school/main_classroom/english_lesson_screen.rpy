default MariaLoveCounter = 0
default MariaAnnoyedCounter = 0
default MariaHandOnTitsPlacements = "EnglishClassScreen/MariaHandOff1.png"
default MariaHandOnTitsShown = "EnglishClassScreen/MariaHandOn1.png"
default MariaHandOnTits1 = "EnglishClassScreen/MariaHandOn1.png"
default MariaHandOnTits2 = "EnglishClassScreen/MariaHandOn2.png"
default MariaHandOnTits3 = "EnglishClassScreen/MariaHandOn3.png"
default MariaHandOffTitsShown = "EnglishClassScreen/MariaHandOff1.png"
default MariaHandOffTits1 = "EnglishClassScreen/MariaHandOff1.png"
default MariaHandOffTits2 = "EnglishClassScreen/MariaHandOff2.png"
default MariaHandOffTits3 = "EnglishClassScreen/MariaHandOff3.png"
default MariaFace = "EnglishClassScreen/MariaFace1.png"
default MariaFace1 = "EnglishClassScreen/MariaFace1.png"
default MariaFace2 = "EnglishClassScreen/MariaFace2.png"
default MariaFace3 = "EnglishClassScreen/MariaFace3.png"
default Maria_HandsIsOnTits = False
default Maria_hintLocationsActive = False
default Pen_or_Maria_Hints = False

init python:
    def Maria_toggle_hint_locations():
        global Maria_hintLocationsActive
        Maria_hintLocationsActive = not Maria_hintLocationsActive 

    def Toggle_Pen_or_Maria_Hints_Function():
        global Pen_or_Maria_Hints
        Pen_or_Maria_Hints = not Pen_or_Maria_Hints         

    def MariaToggleHandOnTits():
        global MariaHandOnTitsPlacements, MariaHandOnTitsShown, MariaHandOffTitsShown, Maria_HandsIsOnTits
        if MariaHandOnTitsPlacements == MariaHandOnTits1 or MariaHandOnTitsPlacements == MariaHandOnTits2 or MariaHandOnTitsPlacements == MariaHandOnTits3:
            if MariaLoveCounter < 30:
                MariaHandOffTitsShown = MariaHandOffTits1
            elif MariaLoveCounter < 70:
                MariaHandOffTitsShown = MariaHandOffTits2
            else:
                MariaHandOffTitsShown = MariaHandOffTits3
            MariaHandOnTitsPlacements = MariaHandOffTitsShown
            Maria_HandsIsOnTits = False
        else:
            if MariaLoveCounter < 30:
                MariaHandOnTitsShown = MariaHandOnTits1
            elif MariaLoveCounter < 70:
                MariaHandOnTitsShown = MariaHandOnTits2
            else:
                MariaHandOnTitsShown = MariaHandOnTits3
            MariaHandOnTitsPlacements = MariaHandOnTitsShown
            Maria_HandsIsOnTits = True
        renpy.transition(Dissolve(0.5))
        renpy.redraw(None, 0)
        
    def MariaUpdateCounters():
        global MariaAnnoyedCounter, MariaLoveCounter, MariaHandOnTitsPlacements, MariaHandOnTitsShown, MariaHandOffTitsShown, MariaFace, Maria_HandsIsOnTits
        if MariaLoveCounter < 100:  # Stop updating annoyed_counter if love_counter is 100
            if Maria_HandsIsOnTits:
                MariaAnnoyedCounter = min(100, MariaAnnoyedCounter + 0.4)
                MariaLoveCounter = min(100, MariaLoveCounter + 0.3)
            else:
                MariaAnnoyedCounter = max(0, MariaAnnoyedCounter - 0.5)
                MariaLoveCounter = max(0, MariaLoveCounter - 0.2)

        # Check if counters reach their limits
        if MariaAnnoyedCounter >= 100:
            MariaFinishLessonFail()
            return
        # elif MariaAnnoyedCounter >= 100:
        #     MariaFinishLessonFail()
        #     return

        # Update the hand images based on the current counters
        if Maria_HandsIsOnTits:
            if MariaLoveCounter < 30:
                MariaHandOnTitsPlacements = MariaHandOnTits1
            elif MariaLoveCounter < 70:
                MariaHandOnTitsPlacements = MariaHandOnTits2
            else:
                MariaHandOnTitsPlacements = MariaHandOnTits3
        else:
            if MariaLoveCounter < 30:
                MariaHandOnTitsPlacements = MariaHandOffTits1
            elif MariaLoveCounter < 70:
                MariaHandOnTitsPlacements = MariaHandOffTits2
            else:
                MariaHandOnTitsPlacements = MariaHandOffTits3

        if MariaLoveCounter < 30:
            MariaFace = MariaFace1
        elif MariaLoveCounter < 70:
            MariaFace = MariaFace2
        else:
            MariaFace = MariaFace3

        renpy.restart_interaction()

    def MariaFinishLessonSuccess():
        global MariaLoveCounter, MariaAnnoyedCounter, MariaHandOnTitsPlacements, Maria_HandsIsOnTits
        MariaLoveCounter = 0
        MariaAnnoyedCounter = 0
        MariaHandOnTitsPlacements = MariaHandOffTits1
        Maria_HandsIsOnTits = False
        Maria_hintLocationsActive = False
        renpy.hide_screen("MariaInEnglishClassScreen")
        renpy.jump("MariaFinishLessonSuccess")

    def MariaFinishLessonFail():
        global MariaLoveCounter, MariaAnnoyedCounter, MariaHandOnTitsPlacements, Maria_HandsIsOnTits
        MariaLoveCounter = 0
        MariaAnnoyedCounter = 0
        MariaHandOnTitsPlacements = MariaHandOffTits1
        Maria_HandsIsOnTits = False
        Maria_hintLocationsActive = False
        renpy.hide_screen("MariaInEnglishClassScreen")
        renpy.jump("AfterEnglishLessonFail")

    def MariaResetMinigame():
        global MariaLoveCounter, MariaAnnoyedCounter, MariaHandOnTitsPlacements, Maria_HandsIsOnTits
        MariaLoveCounter = 0
        MariaAnnoyedCounter = 0
        MariaHandOnTitsPlacements = MariaHandOffTits1
        Maria_HandsIsOnTits = False
        Maria_hintLocationsActive = False


screen EnglishLessonScreen:
    add "EnglishClassScreen/background.png"
    
    imagebutton:
        hover "EnglishClassScreen/MariaButton_hover.png"
        idle "EnglishClassScreen/MariaButton_idle.png"
        xpos 0
        ypos 250
        action [Function(MariaResetMinigame), Hide("EnglishLessonScreen"), Show("MariaInEnglishClassScreen")]
        focus_mask True
    
    imagebutton:
        hover "EnglishClassScreen/Pen_hover.png"
        idle "EnglishClassScreen/Pen_idle.png"
        xpos 1333
        ypos 490
        action [Hide("EnglishLessonScreen"), Jump("DropPenScene")]
        focus_mask True

    imagebutton:
        auto "CarMinigame/hintIcon_%s.png" xpos 1720 ypos 1000
        action Function(Toggle_Pen_or_Maria_Hints_Function)

    if Pen_or_Maria_Hints:
        add "ClickHereHint.png" xpos 1290 ypos 520
        add "ClickHereHint.png" xpos 0 ypos 500

screen MariaInEnglishClassScreen:
    frame:
        background MariaHandOnTitsPlacements

        imagebutton:
            auto "EnglishClassScreen/Tit_%s.png" xpos 680 ypos 700
            action Function(MariaToggleHandOnTits)
    
    add MariaFace xpos 1490 ypos 10
    add faceFrame xpos 1490 ypos 10

    # Display Annoyed Counter
    vbox:
        xpos 1460
        ypos 10
        add "CarMinigame/annoyed_counter_empty.png"
        add "CarMinigame/annoyed_counter_full.png" size (25, (MariaAnnoyedCounter / 75.0) * -300)  # Adjust size as needed
        add "CarMinigame/annoyed_icon.png" xpos 1461 ypos 385

    # Display Love Counter
    vbox:
        xpos 1430
        ypos 10
        add "CarMinigame/love_counter_empty.png"
        add "CarMinigame/love_counter_full.png" size (25, (MariaLoveCounter / 75.0) * -300)
        add "CarMinigame/love_icon.png" xpos 1431 ypos 385

    add "CarMinigame/annoyed_icon.png" xpos 1461 ypos 385
    add "CarMinigame/love_icon.png" xpos 1431 ypos 385

    if MariaLoveCounter >= 100:
        imagebutton:
            auto "EnglishClassScreen/finish_%s.png"
            xpos 160
            ypos 950
            action Function(MariaFinishLessonSuccess)
            focus_mask True

    imagebutton:
        auto "EnglishClassScreen/skip_%s.png"
        xpos 100
        ypos 950
        action Function(MariaFinishLessonSuccess)
        focus_mask True
        at bump

    if Maria_hintLocationsActive:
        add hintLocation xpos 700 ypos 720

    imagebutton:
        auto "CarMinigame/hintIcon_%s.png" xpos 20 ypos 950
        action Function(Maria_toggle_hint_locations)

    # Timer to update counters every 0.1 seconds
    timer 0.1 repeat True action Function(MariaUpdateCounters)
