image BlackScreen = "JenniferAllScenes/JenniferEvening24/BlackScreen.webp"
image WarningScreen = "WarningPage.png"
image MapImage = "HomeSubplace/map.png"
image JenniferInRoomJenniferAtHome = "JenniferAllScenes/JenniferInRoom/JenniferAtHome.png"

init 1 python:
    EVENTS = {
        # * Jennifer Events
        1: Event(0, 0, -1, "Jennifer room", "JenniferMorningEvent14", True), # Wakes up
        # 2: Event(1, 1, -1, "bathroom", "JenniferMorningEvent34", True), # Shower
        # 3: Event(2, 2, -3, "kitchen", "JenniferMorningEvent24", True), # Cooks
        4: Event(4, 4, -1, "Jennifer room", "JenniferMorningEvent44", True), # Dresses up for work
        # 5: Event(13, 13, -1, "Entrance", "JenniferEveningEvent24", True), # Gets home
        6: Event(14, 14, -1, "Jennifer room", "JenniferEveningEvent34", True), # Changes into house clothing
        # 7: Event(15, 15, -1, "kitchen", "JenniferEveningEvent44", True), # Cooks
        # 8: Event(18, 18, -1, "toilet", "JenniferNightEvent24", True), # Using the toilet
        9: Event(19, 19, -1, "Jennifer room", "JenniferNightEvent34", True), # Prays
        10: Event(20, 20, -1, "Jennifer room", "JenniferNightEvent44", True), # Sleeps

        # * Isabella Events
        11: Event(0, 0, -1, "Isabella room", "IsabellaMorningEvent14", True), # Wakes up
        12: Event(1, 1, -1, "Isabella room", "IsabellaMorningEvent34", True), # Homework
        # 13: Event(2, 2, -1, "bathroom", "IsabellaMorningEvent24", True), # Showers
        14: Event(4, 4, -1, "Isabella room", "IsabellaNoonEvent14", True), # Dresses up for school
        # 15: Event(10, 10, -1, "Entrance", "IsabellaNoonEvent24", True), # Gets home
        16: Event(11, 11, -1, "Isabella room", "IsabellaEveningEvent14", True), # Changes into house clothing
        # 17: Event(12, 12, -1, "toilet", "IsabellaNightEvent34", True), # Using the toilet
        18: Event(13, 13, -1, "Livingroom", "IsabellaEveningEvent24", True), # Watches TV
        19: Event(14, 14, -1, "Isabella room", "IsabellaEveningEvent34", True), # Makes her backpack
        20: Event(15, 15, -1, "Jennifer room", "IsabellaEveningEvent44", True), # Doing a bad thing
        21: Event(18, 18, -1, "Isabella room", "IsabellaAfterNoonEvent44", True), # Plays on the computer
        22: Event(19, 19, -1, "Isabella room", "IsabellaNightEvent44", True), # Stays on social media
        23: Event(20, 20, -1, "Isabella room", "IsabellaMidnightEvent14", True), # Sleeps

        # * Claire Events
        24: Event(0, 0, -1, "Claire room", "ClaireMorningEvent14", True), # Wakes up
        25: Event(1, 1, -1, "Livingroom", "ClaireMorningEvent24", True), # Drinks her coffee
        # 26: Event(2, 2, -1, "toilet", "ClaireMorningEvent34", True), # Using the toilet
        27: Event(4, 4, -1, "Claire room", "ClaireNoonEvent14", True), # Dresses up for school
        # 28: Event(12, 12, -1, "Entrance", "ClaireEveningEvent14", True), # Gets home
        29: Event(13, 13, -1, "Claire room", "ClaireEveningEvent24", True), # Changes into home clothing
        30: Event(14, 14, -1, "Claire room", "ClaireEveningEvent34", True), # On her phone
        31: Event(15, 15, -1, "Claire room", "ClaireEveningEvent44", True), # Homework
        # 32: Event(18, 18, -1, "bathroom", "ClaireNightEvent34", True), # Showers
        33: Event(19, 19, -1, "Livingroom", "ClaireNightEvent44", True), # Watches TV
        34: Event(20, 20, -1, "Claire room", "ClaireMidnightEvent14", True), # Sleeps

        # * Group Events
        35: Event(3, 3, -1, "Livingroom", "DinnerGroupEvent", True), # Everyone eats
        # 36: Event(5, 5, -1, "Entrance", "LeaveHomeEvent", True), # Everyone leaves for school/work
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
        68: Event(0, 24, -3, "bathroom", "BathroomEvent", True),# bathroom Screen

        69: Event(0, 24, -2, "Isabella room", "IsabellaRoomWeekendEvent", True),
        70: Event(0, 24, -2, "Jennifer room", "JenniferRoomWeekendEvent", True),
        71: Event(0, 24, -2, "Claire room", "ClaireRoomWeekendEvent", True),
        72: Event(0, 24, -3, "kitchen", "KitchenEvent", True),# Kitchen Screen
        73: Event(0, 24, -2, "Garden1", "Garden1WeekendEvent", True),# Garden1 Screen
        74: Event(0, 24, -2, "Garden2", "Garden2WeekendEvent", True),# Garden2 Screen
        74: Event(0, 24, -3, "Entrance", "EntranceEvent", True),# Garden2 Screen
    }
