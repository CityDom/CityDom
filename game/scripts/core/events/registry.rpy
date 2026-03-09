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
        1: Event(0, 0, EVENT_DAY_WEEKDAY, "Jennifer room", "JenniferMorningEvent14", True, auto_trigger=False), # Wakes up
        4: Event(4, 4, EVENT_DAY_WEEKDAY, "Jennifer room", "JenniferMorningEvent44", True), # Dresses up for work
        6: Event(14, 14, EVENT_DAY_WEEKDAY, "Jennifer room", "JenniferEveningEvent34", True), # Changes into house clothing
        9: Event(19, 19, EVENT_DAY_WEEKDAY, "Jennifer room", "JenniferNightEvent34", True, auto_trigger=False), # Prays
        10: Event(20, 20, EVENT_DAY_WEEKDAY, "Jennifer room", "JenniferNightEvent44", True, auto_trigger=False), # Sleeps

        # * Jennifer Weekend (auto)
        101: Event(4, 4, EVENT_DAY_WEEKEND, "Jennifer room", "Jennifer_weekend_10AM", True, priority=10), # 10 AM
        102: Event(8, 8, EVENT_DAY_WEEKEND, "Jennifer room", "Jennifer_weekend_2PM", True, priority=10), # 2 PM

        # * Isabella Events
        11: Event(0, 0, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaMorningEvent14", True, auto_trigger=False), # Wakes up
        12: Event(1, 1, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaMorningEvent34", True, auto_trigger=False), # Homework
        14: Event(4, 4, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaNoonEvent14", True), # Dresses up for school
        16: Event(11, 11, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaEveningEvent14", True), # Changes into house clothing
        19: Event(14, 14, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaEveningEvent34", True, auto_trigger=False), # Makes her backpack
        20: Event(15, 15, EVENT_DAY_WEEKDAY, "Jennifer room", "IsabellaEveningEvent44", True, auto_trigger=False), # Doing a bad thing
        21: Event(18, 18, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaAfterNoonEvent44", True, auto_trigger=False), # Plays on the computer
        22: Event(19, 19, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaNightEvent44", True, auto_trigger=False), # Stays on social media
        23: Event(20, 20, EVENT_DAY_WEEKDAY, "Isabella room", "IsabellaMidnightEvent14", True, auto_trigger=False), # Sleeps

        # * Claire Events
        24: Event(0, 0, EVENT_DAY_WEEKDAY, "Claire room", "ClaireMorningEvent14", True, auto_trigger=False), # Wakes up
        27: Event(4, 4, EVENT_DAY_WEEKDAY, "Claire room", "ClaireNoonEvent14", True), # Dresses up for school
        29: Event(13, 13, EVENT_DAY_WEEKDAY, "Claire room", "ClaireEveningEvent24", True), # Changes into home clothing
        30: Event(14, 14, EVENT_DAY_WEEKDAY, "Claire room", "ClaireEveningEvent34", True, auto_trigger=False), # On her phone
        31: Event(15, 15, EVENT_DAY_WEEKDAY, "Claire room", "ClaireEveningEvent44", True, auto_trigger=False), # Homework
        34: Event(20, 20, EVENT_DAY_WEEKDAY, "Claire room", "ClaireMidnightEvent14", True, auto_trigger=False), # Sleeps

        # * Group Events

        # * School Events
        39: screen_event(0, 24, EVENT_DAY_WEEKDAY, "School", "SchoolEvent", True), # School Front Screen
        40: screen_event(0, 24, EVENT_DAY_WEEKDAY, "SchoolEntrance", "SchoolEntranceEvent", True), # School Entrance Screen
        41: screen_event(0, 24, EVENT_DAY_WEEKDAY, "ToiletsFront", "ToiletsFrontEvent", True), # School Entrance Screen
        42: screen_event(0, 24, EVENT_DAY_WEEKDAY, "MensToilet", "MensToiletEvent", True), # School Entrance Screen
        43: screen_event(0, 24, EVENT_DAY_WEEKDAY, "WomansToilet", "WomansToiletEvent", True), # School Entrance Screen
        44: screen_event(0, 24, EVENT_DAY_WEEKDAY, "UpTheStairs", "UpTheStairsEvent", True), # Up The Stairs Screen
        45: screen_event(0, 24, EVENT_DAY_WEEKDAY, "TeacherHall", "TeacherHallEvent", True),# Teacher Hall Screen
        46: screen_event(0, 24, EVENT_DAY_WEEKDAY, "ArtClassFront", "ArtClassFrontEvent", True),# Art Class Front Screen
        47: screen_event(0, 24, EVENT_DAY_WEEKDAY, "MedicRoomFront", "MedicRoomFrontEvent", True),# Medic Room Front Screen
        48: screen_event(0, 24, EVENT_DAY_WEEKDAY, "SchoolGymFront", "SchoolGymFrontEvent", True),# School Gym Front Screen
        49: screen_event(0, 24, EVENT_DAY_WEEKDAY, "InsideSchoolGym", "InsideSchoolGymEvent", True),# Inside School Gym Screen
        50: screen_event(0, 24, EVENT_DAY_WEEKDAY, "BackYard", "BackYardEvent", True),# BackYard Screen
        51: screen_event(0, 24, EVENT_DAY_WEEKDAY, "SchoolPool", "SchoolPoolEvent", True),# SchoolPool Screen
        52: screen_event(0, 24, EVENT_DAY_WEEKDAY, "TeachersBathroom", "TeachersBathroomEvent", True),# TeachersBathroom Screen
        53: screen_event(0, 24, EVENT_DAY_WEEKDAY, "PrincipalOffice", "PrincipalOfficeEvent", True),# PrincipalOffice Screen
        54: screen_event(0, 24, EVENT_DAY_WEEKDAY, "TeachersLounge", "TeachersLoungeEvent", True),# TeachersLounge Screen
        55: screen_event(0, 24, EVENT_DAY_WEEKDAY, "MainClassroom", "MainClassroomEvent", True),# MainClassroom Screen
        56: screen_event(0, 24, EVENT_DAY_WEEKDAY, "NurseRoom", "NurseRoomEvent", True),# NurseRoom Screen
        57: screen_event(0, 24, EVENT_DAY_WEEKDAY, "ArtClass", "ArtClassEvent", True),# NurseRoom Screen
        58: screen_event(0, 24, EVENT_DAY_WEEKDAY, "SchoolLibrary", "SchoolLibraryEvent", True),# SchoolLibrary Screen
        60: screen_event(0, 24, EVENT_DAY_WEEKDAY, "MannersClass", "MannersClassEvent", True),# Manners Class Screen
        159: Event(0, 24, EVENT_DAY_WEEKDAY, "MannersClass", "MannersClassWrapper", True, condition=can_trigger_manners_event, priority=20),
        61: screen_event(0, 24, EVENT_DAY_WEEKDAY, "BioClass", "BioClassEvent", True),# Bio Class Screen
        62: screen_event(0, 24, EVENT_DAY_WEEKDAY, "Gym", "GymEvent", True),# Bio Class Screen
        63: screen_event(0, 24, EVENT_DAY_WEEKDAY, "GymLockerRoomFront", "GymLockerRoomFrontEvent", True),# Bio Class Screen
        64: screen_event(0, 24, EVENT_DAY_WEEKDAY, "GirlsLockerRoom", "GirlsLockerRoomEvent", True),# Bio Class Screen
        160: Event(0, 24, EVENT_DAY_WEEKDAY, "GirlsLockerRoom", "BeforeGymClass_FromInside_Scene", True, condition=can_trigger_before_gym_class_event, priority=30),

        # * House screens
        65: screen_event(0, 24, EVENT_DAY_WEEKDAY, "Housefront", "HousefrontEvent", True),# Housefront Screen
        66: screen_event(0, 24, EVENT_DAY_ANY, "HouseToilet", "HouseToiletEvent", True),# HouseToilet Screen
        67: screen_event(0, 24, EVENT_DAY_WEEKDAY, "Livingroom", "LivingroomEvent", True),# LivingRoom Screen
        68: screen_event(0, 24, EVENT_DAY_ANY, "Bathroom", "BathroomEvent", True),# Bathroom Screen

        72: screen_event(0, 24, EVENT_DAY_ANY, "Kitchen", "KitchenEvent", True),# Kitchen Screen
        73: screen_event(0, 24, EVENT_DAY_WEEKEND, "Garden1", "Garden1WeekendEvent", True),# Garden1 Screen
        74: screen_event(0, 24, EVENT_DAY_WEEKEND, "Garden2", "Garden2WeekendEvent", True),# Garden2 Screen
        75: screen_event(0, 24, EVENT_DAY_ANY, "Entrance", "EntranceEvent", True),# Garden2 Screen

        # * House auto events (toilet/bathroom)
        201: Event(2, 2, EVENT_DAY_WEEKDAY, "HouseToilet", "ClaireMorningEvent34", True, priority=10),
        202: Event(12, 12, EVENT_DAY_WEEKDAY, "HouseToilet", "IsabellaNightEvent34", True, priority=10),
        203: Event(18, 18, EVENT_DAY_WEEKDAY, "HouseToilet", "Jennifer_weekend_7AM", True, priority=10),
        204: Event(1, 1, EVENT_DAY_WEEKEND, "HouseToilet", "Jennifer_weekend_7AM", True, priority=10),
        211: Event(1, 1, EVENT_DAY_WEEKDAY, "Bathroom", "JenniferMorningEvent34", True, priority=10),
        212: Event(2, 2, EVENT_DAY_WEEKDAY, "Bathroom", "IsabellaMorningEvent24", True, priority=10),
        213: Event(18, 18, EVENT_DAY_WEEKDAY, "Bathroom", "ClaireNightEvent34", True, priority=10),
        214: Event(1, 1, EVENT_DAY_WEEKEND, "Bathroom", "Claire_weekend_7AM", True, priority=10),
    }
