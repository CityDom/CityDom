image BlackScreen = "JenniferAllScenes/JenniferEvening24/BlackScreen.webp"
image WarningScreen = "WarningPage.png"
image MapImage = "HomeSubplace/map.png"
image JenniferInRoomJenniferAtHome = "JenniferAllScenes/JenniferInRoom/JenniferAtHome.png"

init 1 python:
    def screen_event(start_hour, end_hour, day, location, block, is_active, auto_trigger=True, condition=None, priority=0):
        return Event(
            start_hour,
            end_hour,
            day,
            location,
            block,
            is_active,
            screen_name=get_location_screen_name(location),
            auto_trigger=auto_trigger,
            condition=condition,
            priority=priority,
        )

    EVENTS = {
        # * Jennifer Events
        1: Event(0, 0, -1, "Jennifer room", "JenniferMorningEvent14", True, auto_trigger=False), # Wakes up
        4: Event(4, 4, -1, "Jennifer room", "JenniferMorningEvent44", True), # Dresses up for work
        6: Event(14, 14, -1, "Jennifer room", "JenniferEveningEvent34", True), # Changes into house clothing
        9: Event(19, 19, -1, "Jennifer room", "JenniferNightEvent34", True, auto_trigger=False), # Prays
        10: Event(20, 20, -1, "Jennifer room", "JenniferNightEvent44", True, auto_trigger=False), # Sleeps

        # * Jennifer Weekend (auto)
        101: Event(4, 4, -2, "Jennifer room", "Jennifer_weekend_10AM", True, priority=10), # 10 AM
        102: Event(8, 8, -2, "Jennifer room", "Jennifer_weekend_2PM", True, priority=10), # 2 PM

        # * Isabella Events
        11: Event(0, 0, -1, "Isabella room", "IsabellaMorningEvent14", True, auto_trigger=False), # Wakes up
        12: Event(1, 1, -1, "Isabella room", "IsabellaMorningEvent34", True, auto_trigger=False), # Homework
        14: Event(4, 4, -1, "Isabella room", "IsabellaNoonEvent14", True), # Dresses up for school
        16: Event(11, 11, -1, "Isabella room", "IsabellaEveningEvent14", True), # Changes into house clothing
        19: Event(14, 14, -1, "Isabella room", "IsabellaEveningEvent34", True, auto_trigger=False), # Makes her backpack
        20: Event(15, 15, -1, "Jennifer room", "IsabellaEveningEvent44", True, auto_trigger=False), # Doing a bad thing
        21: Event(18, 18, -1, "Isabella room", "IsabellaAfterNoonEvent44", True, auto_trigger=False), # Plays on the computer
        22: Event(19, 19, -1, "Isabella room", "IsabellaNightEvent44", True, auto_trigger=False), # Stays on social media
        23: Event(20, 20, -1, "Isabella room", "IsabellaMidnightEvent14", True, auto_trigger=False), # Sleeps

        # * Claire Events
        24: Event(0, 0, -1, "Claire room", "ClaireMorningEvent14", True, auto_trigger=False), # Wakes up
        27: Event(4, 4, -1, "Claire room", "ClaireNoonEvent14", True), # Dresses up for school
        29: Event(13, 13, -1, "Claire room", "ClaireEveningEvent24", True), # Changes into home clothing
        30: Event(14, 14, -1, "Claire room", "ClaireEveningEvent34", True, auto_trigger=False), # On her phone
        31: Event(15, 15, -1, "Claire room", "ClaireEveningEvent44", True, auto_trigger=False), # Homework
        34: Event(20, 20, -1, "Claire room", "ClaireMidnightEvent14", True, auto_trigger=False), # Sleeps

        # * Group Events

        # * School Events
        39: screen_event(0, 24, -1, "School", "SchoolEvent", True), # School Front Screen
        40: screen_event(0, 24, -1, "SchoolEntrance", "SchoolEntranceEvent", True), # School Entrance Screen
        41: screen_event(0, 24, -1, "ToiletsFront", "ToiletsFrontEvent", True), # School Entrance Screen
        42: screen_event(0, 24, -1, "MensToilet", "MensToiletEvent", True), # School Entrance Screen
        43: screen_event(0, 24, -1, "WomansToilet", "WomansToiletEvent", True), # School Entrance Screen
        44: screen_event(0, 24, -1, "UpTheStairs", "UpTheStairsEvent", True), # Up The Stairs Screen
        45: screen_event(0, 24, -1, "TeacherHall", "TeacherHallEvent", True),# Teacher Hall Screen
        46: screen_event(0, 24, -1, "ArtClassFront", "ArtClassFrontEvent", True),# Art Class Front Screen
        47: screen_event(0, 24, -1, "MedicRoomFront", "MedicRoomFrontEvent", True),# Medic Room Front Screen
        48: screen_event(0, 24, -1, "SchoolGymFront", "SchoolGymFrontEvent", True),# School Gym Front Screen
        49: screen_event(0, 24, -1, "InsideSchoolGym", "InsideSchoolGymEvent", True),# Inside School Gym Screen
        50: screen_event(0, 24, -1, "BackYard", "BackYardEvent", True),# BackYard Screen
        51: screen_event(0, 24, -1, "SchoolPool", "SchoolPoolEvent", True),# SchoolPool Screen
        52: screen_event(0, 24, -1, "TeachersBathroom", "TeachersBathroomEvent", True),# TeachersBathroom Screen
        53: screen_event(0, 24, -1, "PrincipalOffice", "PrincipalOfficeEvent", True),# PrincipalOffice Screen
        54: screen_event(0, 24, -1, "TeachersLounge", "TeachersLoungeEvent", True),# TeachersLounge Screen
        55: screen_event(0, 24, -1, "MainClassroom", "MainClassroomEvent", True),# MainClassroom Screen
        56: screen_event(0, 24, -1, "NurseRoom", "NurseRoomEvent", True),# NurseRoom Screen
        57: screen_event(0, 24, -1, "ArtClass", "ArtClassEvent", True),# NurseRoom Screen
        58: screen_event(0, 24, -1, "SchoolLibrary", "SchoolLibraryEvent", True),# SchoolLibrary Screen
        60: screen_event(0, 24, -1, "MannersClass", "MannersClassEvent", True),# Manners Class Screen
        159: Event(0, 24, -1, "MannersClass", "MannersClassWrapper", True, condition=can_trigger_manners_event, priority=20),
        61: screen_event(0, 24, -1, "BioClass", "BioClassEvent", True),# Bio Class Screen
        62: screen_event(0, 24, -1, "Gym", "GymEvent", True),# Bio Class Screen
        63: screen_event(0, 24, -1, "GymLockerRoomFront", "GymLockerRoomFrontEvent", True),# Bio Class Screen
        64: screen_event(0, 24, -1, "GirlsLockerRoom", "GirlsLockerRoomEvent", True),# Bio Class Screen
        160: Event(0, 24, -1, "GirlsLockerRoom", "BeforeGymClass_FromInside_Scene", True, condition=can_trigger_before_gym_class_event, priority=30),

        # * House screens
        65: screen_event(0, 24, -1, "Housefront", "HousefrontEvent", True),# Housefront Screen
        66: screen_event(0, 24, -3, "HouseToilet", "HouseToiletEvent", True),# HouseToilet Screen
        67: screen_event(0, 24, -1, "Livingroom", "LivingroomEvent", True),# LivingRoom Screen
        68: screen_event(0, 24, -3, "bathroom", "BathroomEvent", True),# bathroom Screen

        72: screen_event(0, 24, -3, "kitchen", "KitchenEvent", True),# Kitchen Screen
        73: screen_event(0, 24, -2, "Garden1", "Garden1WeekendEvent", True),# Garden1 Screen
        74: screen_event(0, 24, -2, "Garden2", "Garden2WeekendEvent", True),# Garden2 Screen
        75: screen_event(0, 24, -3, "Entrance", "EntranceEvent", True),# Garden2 Screen

        # * House auto events (toilet/bathroom)
        201: Event(2, 2, -1, "HouseToilet", "ClaireMorningEvent34", True, priority=10),
        202: Event(12, 12, -1, "HouseToilet", "IsabellaNightEvent34", True, priority=10),
        203: Event(18, 18, -1, "HouseToilet", "Jennifer_weekend_7AM", True, priority=10),
        204: Event(1, 1, -2, "HouseToilet", "Jennifer_weekend_7AM", True, priority=10),
        211: Event(1, 1, -1, "Bathroom", "JenniferMorningEvent34", True, priority=10),
        212: Event(2, 2, -1, "Bathroom", "IsabellaMorningEvent24", True, priority=10),
        213: Event(18, 18, -1, "Bathroom", "ClaireNightEvent34", True, priority=10),
        214: Event(1, 1, -2, "Bathroom", "Claire_weekend_7AM", True, priority=10),
    }
