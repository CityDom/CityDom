transform dissolve_transition:
    on show:
        alpha 0 
        linear 0.5 alpha 1.0 
    on hide:
        linear 0.5 alpha 0

init python:
    def finish_minigame_and_reset_success():
        # Reset all relevant variables
        global firstPosition, MCclose, isHandOnThigh, isHandOnTits, isHandOnMouth
        global annoyed_counter, love_counter, reachButtonsActive, hintLocationsActive
        global default_mouse, lastHandLocation
        
        firstPosition = "CarMinigame/DefaultPosition.webp"
        MCclose = False
        isHandOnThigh = False
        isHandOnTits = False
        isHandOnMouth = False
        annoyed_counter = 0
        love_counter = 0
        reachButtonsActive = False
        hintLocationsActive = False
        default_mouse = "default"
        lastHandLocation = "thigh"

        # Hide the current screen
        renpy.hide_screen("GoToSchoolFirstTimeScreen")

        # Jump to the new label
        renpy.jump("AfterGoToSchoolMinigameSuccess")

    def finish_minigame_and_reset_Fail():
        # Reset all relevant variables
        global firstPosition, MCclose, isHandOnThigh, isHandOnTits, isHandOnMouth
        global annoyed_counter, love_counter, reachButtonsActive, hintLocationsActive
        global default_mouse, lastHandLocation
        
        firstPosition = closer0
        MCclose = False
        isHandOnThigh = False
        isHandOnTits = False
        isHandOnMouth = False
        annoyed_counter = 0
        love_counter = 0
        reachButtonsActive = False
        hintLocationsActive = False
        default_mouse = "default"
        lastHandLocation = "thigh"

        # Hide the current screen
        renpy.hide_screen("GoToSchoolFirstTimeScreen")

        ui.close()

        # Jump to the new label
        renpy.jump("AfterGoToSchoolMinigameFail")

    def move_left():
        global firstPosition, MCclose
        if firstPosition == closer0:
            firstPosition = closer1
        elif firstPosition == closer1:
            firstPosition = closer2
            MCclose = True
        # No action if on closer2
        renpy.transition(Dissolve(1.5))
        renpy.redraw(None, 0)


    def move_right():
        global firstPosition, MCclose, isHandOnThigh, isHandOnTits, isHandOnMouth

        if MCclose == True:
            MCclose = False
            isHandOnThigh = False
            isHandOnTits = False
            isHandOnMouth = False
            firstPosition = closer1
        elif firstPosition == closer1:
            firstPosition = closer0
        renpy.transition(Dissolve(1))
        renpy.restart_interaction()
        renpy.redraw(None, 0)

    def place_hand_on(part):
        global lastHandLocation
        part_active = globals().get(f"isHandOn{part.capitalize()}", False)
        if all(not globals().get(f"isHandOn{p.capitalize()}", False) for p in ["thigh", "tits", "mouth"] if p != part.lower()):
            globals()[f"isHandOn{part.capitalize()}"] = not part_active
            lastHandLocation = part.lower()
            renpy.transition(Dissolve(0.5))
            renpy.redraw(None, 0)

    def place_hand_thigh():
        place_hand_on("thigh")

    def place_hand_tits():
        place_hand_on("tits")

    def place_hand_mouth():
        place_hand_on("mouth")

    def set_reach_cursor():
        global default_mouse, reachButtonsActive
        if reachButtonsActive == False:
            reachButtonsActive = True
            default_mouse = "reach"  # This changes the cursor globally
        else:
            reachButtonsActive = False
            default_mouse = "default"

    def toggle_hint_locations():
        global hintLocationsActive
        hintLocationsActive = not hintLocationsActive 

    def update_counters():
        global annoyed_counter, love_counter, firstPosition, isHandOnThigh, isHandOnTits, isHandOnMouth
        
        if love_counter < 100:  # Add this condition to stop updating annoyed_counter if love_counter is 100
            if isHandOnThigh == True:
                # Increment the counters more smoothly
                annoyed_counter = min(100, annoyed_counter + 0.4)
                love_counter = min(100, love_counter + 0.3)
            elif isHandOnTits == True:
                annoyed_counter = min(100, annoyed_counter + 10)
                love_counter = min(100, love_counter + 0.1)
            elif isHandOnMouth == True:
                annoyed_counter = min(100, annoyed_counter + 10)
                love_counter = min(100, love_counter + 0)
            else:
                # Decrease the counters more smoothly
                annoyed_counter = max(0, annoyed_counter - 0.4)
                love_counter = max(0, love_counter - 0.1)
        else:
            # Only update love_counter if it is less than 100
            if isHandOnThigh == True:
                love_counter = min(100, love_counter + 0.3)
            elif isHandOnTits == True:
                love_counter = min(100, love_counter + 0.1)
            elif isHandOnMouth == True:
                love_counter = min(100, love_counter + 0)
            else:
                love_counter = max(0, love_counter - 0.1)

        renpy.restart_interaction()  # To update the screen

    def update_first_position_based_on_love():
        global firstPosition, isHandOnThigh, isHandOnTits
        if isHandOnThigh == True:
            if love_counter < 30:
                firstPosition = handOnThigh1
            elif love_counter < 70:
                firstPosition = handOnThigh2
            else:
                firstPosition = handOnThigh3
        elif isHandOnTits == True:
            if annoyed_counter < 100:
                firstPosition = handOnTits1
        elif isHandOnMouth == True:
            if annoyed_counter < 100:
                firstPosition = handOnMouth1
        else:
            if 0 <= love_counter < 30:
                firstPosition = closer2
            elif 30 <= love_counter < 70:
                firstPosition = closer2_2
            else:
                firstPosition = closer2_3

screen GoToSchoolFirstTimeScreen():
    add GoToSchoolMovieBackground
    if annoyed_counter == 100:
        $ finish_minigame_and_reset_Fail()
    frame: 
        background firstPosition

        imagebutton:
            auto "CarMinigame/hintIcon_%s.png" xpos 20 ypos 950
            action Function(toggle_hint_locations)

        imagebutton:
            auto "CarMinigame/MoveLeft_%s.png"
            xpos 10
            ypos 100
            action Function(move_left)

        imagebutton:
            auto "CarMinigame/MoveRight_%s.png"
            xpos 120
            ypos 100
            action Function(move_right)

        if love_counter == 100:
            imagebutton:
                auto "CarMinigame/Finish_%s.png" xpos 160 ypos 950
                action Function(finish_minigame_and_reset_success)

        if hintLocationsActive == True:
            add hintLocation xpos 550 ypos 430
            add hintLocation xpos 520 ypos 760
            add hintLocation xpos 430 ypos 180

        imagebutton:
            auto "EnglishClassScreen/skip_%s.png"
            xpos 100
            ypos 950
            action Function(finish_minigame_and_reset_success)
            focus_mask True
            at bump

        if MCclose == True:
            if isHandOnThigh == True:
                $ update_first_position_based_on_love()
                add LapViewHandOn xpos 1490 ypos 460
            elif isHandOnTits == True:
                $ update_first_position_based_on_love()
                add TitsViewHandOn xpos 1490 ypos 460
            elif isHandOnMouth == True:
                $ update_first_position_based_on_love()
                add MouthViewHandOn xpos 1490 ypos 460
            else:
                $ update_first_position_based_on_love()
                if lastHandLocation == "thigh":
                    add LapViewHandOff xpos 1490 ypos 460
                elif lastHandLocation == "tits":
                    add TitsViewHandOff xpos 1490 ypos 460
                elif lastHandLocation == "mouth":
                    add MouthViewHandOff xpos 1490 ypos 460
            
            if isHandOnThigh == True or isHandOnTits == True or lastHandLocation == "thigh" or lastHandLocation == "tits":
                if love_counter < 30:
                    add faceMovie1 xpos 1490 ypos 10 at dissolve_transition
                elif love_counter < 70:
                    add faceMovie2 xpos 1490 ypos 10 at dissolve_transition
                else:
                    add faceMovie3 xpos 1490 ypos 10 at dissolve_transition
            elif isHandOnMouth == True:
                add faceMovie5 xpos 1490 ypos 10 at dissolve_transition
            elif isHandOnThigh == False and isHandOnTits == False and isHandOnMouth == False and lastHandLocation == "mouth":
                if love_counter < 30:
                    add faceMovie1 xpos 1490 ypos 10 at dissolve_transition
                elif love_counter < 70:
                    add faceMovie2 xpos 1490 ypos 10 at dissolve_transition
                else:
                    add faceMovie3 xpos 1490 ypos 10 at dissolve_transition
            add faceFrame xpos 1490 ypos 10


            # Display Annoyed Counter
            $ annoyed_progress_width = (annoyed_counter / 75.0) * -300 
            vbox:
                xpos 1460
                ypos 10
                add "CarMinigame/annoyed_counter_empty.png"
                add "CarMinigame/annoyed_counter_full.png" size (25, annoyed_progress_width)

            # Display Love Counter
            $ love_progress_width = (love_counter / 75.0) * -300 
            vbox:
                xpos 1430
                ypos 10
                add "CarMinigame/love_counter_empty.png"
                add "CarMinigame/love_counter_full.png" size (25, love_progress_width)

            imagebutton:
                auto "CarMinigame/reach_%s.png" xpos 20 ypos 230
                action Function(set_reach_cursor)
            add "CarMinigame/annoyed_icon.png" xpos 1461 ypos 385
            add "CarMinigame/love_icon.png" xpos 1431 ypos 385
        
            if reachButtonsActive:
                imagebutton:
                    auto "CarMinigame/reachBodyButton_%s.png" xpos 520 ypos 760 # thigh
                    action Function(place_hand_thigh)
            
            if reachButtonsActive:
                imagebutton:
                    auto "CarMinigame/reachBodyButton_%s.png" xpos 550 ypos 430 # tits
                    action Function(place_hand_tits)

            if reachButtonsActive:
                imagebutton:
                    auto "CarMinigame/reachBodyButton_%s.png" xpos 430 ypos 180 # mouth
                    action Function(place_hand_mouth)

        # Timer to update counters every 0.5 seconds regardless of position
        timer 0.1 repeat True action Function(update_counters)
