label start:
    $ GameIsRunning = True

    jump GameIntro
    # Game is running

    while GameIsRunning:
        label GameLoop:
            
            # Reset variables
            $ BlockToCall, clickType = "", ""
            
            # Check for events in the current location
            $ current_location = str(Location).lower()
            python:
                for event in EVENTS.values():
                    if event.is_active and event.date_check(calendar) and event.location.lower() == current_location:
                        BlockToCall = event.block

            if BlockToCall:
                $ screen_name = f"{BlockToCall.replace('Event', 'Screen')}"
                # Check if the screen exists before attempting to show it
                if renpy.has_screen(screen_name):
                    $ renpy.show_screen(screen_name)
                else:
                    # If there's no specific screen for the event, call the event block directly
                    # This assumes you have a label or function setup for handling the event by its name
                    $ renpy.call(BlockToCall)

            # Change location image if it exists
            python:
                if calendar.period_index == 1:
                    Location_img = str(Location).lower() + " evening"
                elif calendar.period_index == 2:
                    Location_img = str(Location).lower() + " night"
                else:
                    Location_img = str(Location).lower()
            if renpy.has_image(Location_img, exact=True):
                scene expression Location_img

            # ! Sad isolate event. Will look for a better solution
            if school_clock.hour == 14 and school_clock.period == 4 and Location == "MannersClass":
                if seenSandraBackstory == True:
                    $ renpy.jump("MannersClass_FromInside_Scene") 
                else:
                    $ renpy.jump("MannersClassScene") 
            if is_before_gym_swim_class() and (calendar.Day == 1 or calendar.Day == 3 or calendar.Day == 5) and Location == "GirlsLockerRoom":
                $ renpy.hide_screen("GirlsLockerRoomScreen")
                $ renpy.jump("BeforeGymClass_FromInside_Scene")
            # ! Sad isolate event. Will look for a better solution

            # Check for location change and update the location if changed
            $ new_location = renpy.call_screen("MainHud", _layer="screens")
            if new_location != Location:
                # Assuming Location is the variable holding the current location name
                $ Location = new_location

                # Hide all screens from the previous location
                python:
                    for screen_name in ALL_EVENT_SCREENS:
                        renpy.hide_screen(screen_name)

                # Then show the new location's screen
                $ new_location_screen = f"{Location}_Screen"
                if renpy.has_screen(new_location_screen):
                    $ renpy.show_screen(new_location_screen)
                else:
                    scene expression Location_img

            # Update last location
            $ LastLocation = Location
        

label variables:
    image BlackScreen = "MomAllScenes/MomEvening24/BlackScreen.webp"
    image WarningScreen = "WarningPage.png"
    image MapImage = "HomeSubplace/map.png"
    init python:
            
        EVENTS = {
            # * Mom Events
            1: Event(0, 0, -1, "Mom room", "MomMorningEvent14", True), # Wakes up
            # 2: Event(1, 1, -1, "bathroom", "MomMorningEvent34", True), # Shower
            3: Event(2, 2, -1, "kitchen", "MomMorningEvent24", True), # Cooks
            4: Event(4, 4, -1, "Mom room", "MomMorningEvent44", True), # Dresses up for work
            5: Event(13, 13, -1, "Entrance", "MomEveningEvent24", True), # Gets home
            6: Event(14, 14, -1, "Mom room", "MomEveningEvent34", True), # Changes into house clothing
            7: Event(15, 15, -1, "kitchen", "MomEveningEvent44", True), # Cooks
            # 8: Event(18, 18, -1, "toilet", "MomNightEvent24", True), # Using the toilet
            9: Event(19, 19, -1, "Mom room", "MomNightEvent34", True), # Prays
            10: Event(20, 20, -1, "Mom room", "MomNightEvent44", True), # Sleeps

            # * Isabella Events
            11: Event(0, 0, -1, "lil sis room", "LilSisMorningEvent14", True), # Wakes up
            12: Event(1, 1, -1, "lil sis room", "LilSisMorningEvent34", True), # Homework
            # 13: Event(2, 2, -1, "bathroom", "LilSisMorningEvent24", True), # Showers
            14: Event(4, 4, -1, "lil sis room", "LilSisNoonEvent14", True), # Dresses up for school
            15: Event(10, 10, -1, "Entrance", "LilSisNoonEvent24", True), # Gets home
            16: Event(11, 11, -1, "lil sis room", "LilSisEveningEvent14", True), # Changes into house clothing
            # 17: Event(12, 12, -1, "toilet", "LilSisNightEvent34", True), # Using the toilet
            18: Event(13, 13, -1, "Livingroom", "LilSisEveningEvent24", True), # Watches TV
            19: Event(14, 14, -1, "lil sis room", "LilSisEveningEvent34", True), # Makes her backpack
            20: Event(15, 15, -1, "Mom room", "LilSisEveningEvent44", True), # Doing a bad thing
            21: Event(18, 18, -1, "lil sis room", "LilSisAfterNoonEvent44", True), # Plays on the computer
            22: Event(19, 19, -1, "lil sis room", "LilSisNightEvent44", True), # Stays on social media
            23: Event(20, 20, -1, "lil sis room", "LilSisMidnightEvent14", True), # Sleeps

            # * Claire Events
            24: Event(0, 0, -1, "big sis room", "BigSisMorningEvent14", True), # Wakes up
            25: Event(1, 1, -1, "Livingroom", "BigSisMorningEvent24", True), # Drinks her coffee
            # 26: Event(2, 2, -1, "toilet", "BigSisMorningEvent34", True), # Using the toilet
            27: Event(4, 4, -1, "big sis room", "BigSisNoonEvent14", True), # Dresses up for school
            28: Event(12, 12, -1, "Entrance", "BigSisEveningEvent14", True), # Gets home
            29: Event(13, 13, -1, "big sis room", "BigSisEveningEvent24", True), # Changes into home clothing
            30: Event(14, 14, -1, "big sis room", "BigSisEveningEvent34", True), # On her phone
            31: Event(15, 15, -1, "big sis room", "BigSisEveningEvent44", True), # Homework
            # 32: Event(18, 18, -1, "bathroom", "BigSisNightEvent34", True), # Showers
            33: Event(19, 19, -1, "Livingroom", "BigSisNightEvent44", True), # Watches TV
            34: Event(20, 20, -1, "big sis room", "BigSisMidnightEvent14", True), # Sleeps

            # * Group Events
            35: Event(3, 3, -1, "Livingroom", "DinnerGroupEvent", True), # Everyone eats
            36: Event(5, 5, -1, "Entrance", "LeaveHomeEvent", True), # Everyone leaves for school/work
            37: Event(16, 16, -1, "Livingroom", "LunchGroupEvent", True), # Everybody eats part 2
            38: Event(17, 17, -1, "Livingroom", "MovieNightEvent", True), # Everyone watches TV

            # * School Events
            39: Event(0, 24, -1, "School", "SchoolEvent", True), # School Front Screen
            40: Event(0, 24, -1, "SchoolEntrance", "SchoolEntranceEvent", True), # School Entrance Screen
            41: Event(0, 24, -1, "ToiletsFront", "ToiletsFrontEvent", True), # School Entrance Screen
            42: Event(0, 24, -1, "MensToilet", "MensToiletEvent", True), # School Entrance Screen
            43: Event(0, 24, -1, "WomansToilet", "WomansToiletEvent", True), # School Entrance Screen
            44: Event(0, 24, -1, "UpTheStairs", "UpTheStairsEvent", True), # Up The Stairs Screen
            45: Event(0, 24, -1, "TeacherHall", "TeacherHallEvent", True),# Teacher Hall Screen
            46: Event(0, 24, -1, "ArtClassFront", "ArtClassFrontEvent", True),# Art Class Front Screen
            47: Event(0, 24, -1, "MedicRoomFront", "MedicRoomFrontEvent", True),# Medic Room Front Screen
            48: Event(0, 24, -1, "SchoolGymFront", "SchoolGymFrontEvent", True),# School Gym Front Screen
            49: Event(0, 24, -1, "InsideSchoolGym", "InsideSchoolGymEvent", True),# Inside School Gym Screen
            50: Event(0, 24, -1, "BackYard", "BackYardEvent", True),# BackYard Screen
            51: Event(0, 24, -1, "SchoolPool", "SchoolPoolEvent", True),# SchoolPool Screen
            52: Event(0, 24, -1, "TeachersBathroom", "TeachersBathroomEvent", True),# TeachersBathroom Screen
            53: Event(0, 24, -1, "PrincipalOffice", "PrincipalOfficeEvent", True),# PrincipalOffice Screen
            54: Event(0, 24, -1, "TeachersLounge", "TeachersLoungeEvent", True),# TeachersLounge Screen
            55: Event(0, 24, -1, "MainClassroom", "MainClassroomEvent", True),# MainClassroom Screen
            56: Event(0, 24, -1, "NurseRoom", "NurseRoomEvent", True),# NurseRoom Screen
            57: Event(0, 24, -1, "ArtClass", "ArtClassEvent", True),# NurseRoom Screen
            58: Event(0, 24, -1, "SchoolLibrary", "SchoolLibraryEvent", True),# SchoolLibrary Screen
            60: Event(0, 24, -1, "MannersClass", "MannersClassEvent", True),# Manners Class Screen
            61: Event(0, 24, -1, "BioClass", "BioClassEvent", True),# Bio Class Screen
            62: Event(0, 24, -1, "Gym", "GymEvent", True),# Bio Class Screen
            63: Event(0, 24, -1, "GymLockerRoomFront", "GymLockerRoomFrontEvent", True),# Bio Class Screen
            64: Event(0, 24, -1, "GirlsLockerRoom", "GirlsLockerRoomEvent", True),# Bio Class Screen

            # * House screens
            65: Event(0, 24, -1, "Housefront", "HousefrontEvent", True),# Housefront Screen
            66: Event(0, 24, -3, "HouseToilet", "HouseToiletEvent", True),# HouseToilet Screen
            67: Event(0, 24, -1, "Livingroom", "LivingroomEvent", True),# LivingRoom Screen
            68: Event(0, 24, -1, "bathroom", "BathroomEvent", True),# bathroom Screen

            69: Event(0, 24, -2, "lil sis room", "IsabellaRoomWeekendEvent", True),
            70: Event(0, 24, -2, "Mom room", "JenniferRoomWeekendEvent", True),
            71: Event(0, 24, -2, "big sis room", "ClaireRoomWeekendEvent", True),
            
        }
    return

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

label BigSisMidnightEvent14:
    jump BigSisMidnight14

label BigSisEveningEvent34:
    jump BigSisEvening34
    return

label BigSisEveningEvent44:
    jump BigSisEvening44
    return

label BigSisNightEvent34:
    jump BigSisNight34
    return  

label BigSisNightEvent44:
    jump BigSisNight44
    return

label BigSisEveningEvent24:
    jump BigSisEvening24
    return

label BigSisEveningEvent14:
    jump BigSisEvening14
    return    

label BigSisNoonEvent14:
    jump BigSisNoon14
    return

label BigSisMorningEvent34:
    jump BigSisMorning34
    return

label BigSisMorningEvent24:
    jump BigSisMorning24
    return    

label BigSisMorningEvent14:
    jump BigSisMorning14
    return

label LilSisEveningEvent44:
    jump LilSisEvening44
    return
    
label LilSisEveningEvent34:
    jump LilSisEvening34
    return

label LilSisMidnightEvent14:
    jump LilSisMidnight14
    return

label LilSisEveningEvent24:
    jump LilSisEvening24
    return

label LilSisNightEvent44:
    jump LilSisNight44
    return

label MovieNightEvent:
    jump MovieNightLVL1
    return

label LilSisAfterNoonEvent44:
    jump LilsisAfterNoon44
    return

label LilSisMorningEvent34:
    scene MORNING34LILSIS12
    jump LilSisMorning34

label LilSisNightEvent34:
    scene NIGHT24MOM0
    jump LilSisNight34
    return

label LilSisMorningEvent24:
    scene MORNINGS34MOM0
    jump LilSisMorning24

label LilSisMorningEvent14:
    scene MORNING14LILSIS1
    jump LilSisMorning14

label MomMorningEvent14:
    jump MomMorning14
    
label MomMorningEvent24:
    scene MORNINGS24MOM1
    MC "{color=#808080}*Oh, mom is making breakfast, let's see how she's doing*{color=#808080}"
    jump MomMorning24
    return

label MomMorningEvent34:
    scene MORNINGS34MOM0
    jump MomMorning34
    return

image MomInRoomMomAtHome = "MomAllScenes/MomInRoom/MomAtHome.png"
label MomMorningEvent44:
    scene MORNINGS44MOM0
    jump MomMorning44
    return

label MomEveningEvent24:
    scene EVENINGS24MOM32
    jump MomEvening24
    return

label MomEveningEvent34:
    scene MORNINGS44MOM0
    jump MomEvening34
    return

label MomEveningEvent44:
    scene EVENINGS44MOM0
    MC "Oh, mom is cooking dinner."
    jump MomEvening44
    return

label MomNightEvent34:
    jump MomNight34
    return

label MomNightEvent44:
    jump MomNight44
    return

label DinnerGroupEvent:
    jump DinnerEventLVL1
    return

label LilSisNoonEvent14:
    jump LilSisNoon14
    return

label LilSisNoonEvent24:
    jump LilSisNoon24
    return    
    
label LilSisEveningEvent14:
    jump LilSisEvening14
    return