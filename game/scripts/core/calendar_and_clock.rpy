# Global instance
default default_calendar_hour = 6
default default_calendar_hours = 6
default default_calendar_days = 1
default default_calendar_day = 0
default default_calendar_month = 0

default calendar = Calendar()

init python:
    class Calendar(object):
        def __init__(self):
            # Initialization now directly uses global default values.
            self.Hour = default_calendar_hour
            self.Hours = default_calendar_hours
            self.Days = default_calendar_days
            self.Day = int(default_calendar_day)
            self.Month = default_calendar_month
            self.Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            self.WeekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            self.period_index = 0


        @property
        def Output(self):
            return f"{self.WeekDays[self.Day]} {str(self.Hours).zfill(2)}:00"

        def AddTime(self, Hours):
            self.Hours += Hours
            if self.Hours > 20:
                self.Hours -= 21
                self.Day += 1
                self.Days += 1
            # if 20 < self.Hours < 24:
                renpy.call("SleepEvent") 
            if self.Day > 6:
                self.Day = 0
            if self.Days == self.MonthDays[self.Month]:
                self.Month += 1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0
            if self.Hours == 22:
                self.Hours += 3
            self.update_sub_place_data()
            hud_refresh()

        def get_current_hour(self):
            return self.Hours

        def advance_to_next_day(self):
            self.Day = int(self.Day) + 1
            if self.Day > 6:
                self.Day = 0

        def update_sub_place_data(self):
            sub_place_data = [
                (0, 0, "My room", 50, 900, "SubLocationIcons/MCBedroomIcon_%s.png", True),
                (1, 0, "Jennifer room", 230, 900, "SubLocationIcons/JenniferBedroomIcon_%s.png", True),
                (2, 0, "Isabella room", 410, 900, "SubLocationIcons/IsabellaBedroomIcon_%s.png", True),
                (3, 0, "Claire room", 590, 900, "SubLocationIcons/ClaireBedroomIcon_%s.png", True),
                (4, 0, "HouseToilet", 770, 900, "SubLocationIcons/ToiletIcon_%s.png", True),
                (5, 0, "Livingroom", 950, 900, "SubLocationIcons/livingroomIcon_%s.png", True),
                (6, 0, "Washing Room", 1130, 900, "SubLocationIcons/WashingRoomIcon_%s.png", True),
                (7, 0, "Bathroom", 1310, 900, "SubLocationIcons/Bathroom_%s.png", True),
                (8, 0, "Entrance", 1490, 900, "SubLocationIcons/Entrance_%s.png", True),
                (9, 0, "Garden1", 1670, 900, "SubLocationIcons/Garden1_%s.png", True),
                (10, 0, "Garden2", 1850, 900, "SubLocationIcons/Garden2_%s.png", True),
                (11, 0, "Housefront", 2030, 900, "SubLocationIcons/HousefrontIcon_%s.png", True),

                (10, 1, "School", 50, 900, "SchoolSubLocationIcons/School_%s.png", True),
                (11, 1, "SchoolEntrance", 230, 900, "SchoolSubLocationIcons/SchoolEntrance_%s.png", True),
                (12, 1, "ToiletsFront", 410, 900, "SchoolSubLocationIcons/ToiletsFront_%s.png", True),
                (13, 1, "UpTheStairs", 590, 900, "SchoolSubLocationIcons/UpTheStairs_%s.png", True),
                (14, 1, "TeacherHall", 770, 900, "SchoolSubLocationIcons/TeacherHall_%s.png", True),
                (15, 1, "ArtClassFront", 950, 900, "SchoolSubLocationIcons/ArtClassFront_%s.png", True),
                (16, 1, "MedicRoomFront", 1130, 900, "SchoolSubLocationIcons/MedicRoomFront_%s.png", True),
                (17, 1, "SchoolGymFront", 1310, 900, "SchoolSubLocationIcons/SchoolGymFront_%s.png", True),
                (18, 1, "InsideSchoolGym", 1490, 900, "SchoolSubLocationIcons/InsideSchoolGym_%s.png", True),
                (19, 1, "SchoolPool", 1670, 900, "SchoolSubLocationIcons/SchoolPool_%s.png", True),
            ]

            if 12 <= self.Hours < 16:
                self.period_index = 1
            elif 16 <= self.Hours < 24:
                self.period_index = 2
            else:
                self.period_index = 0

            for i, data in enumerate(sub_place_data):
                SubLocations[i] = SubPlace(*data)
                
    class Event:
        def __init__(self, start_hour, end_hour, day, location, block, is_active):
            self.start_hour = start_hour
            self.end_hour = end_hour
            self.day = day
            self.location = location
            self.block = block
            self.is_active = is_active

        def date_check(self, c):
            hour_within_range = self.start_hour <= c.Hours <= self.end_hour

            if self.day == -1:
                # Weekday-only
                is_correct_day = 1 <= c.Day <= 5
            elif self.day == -2:
                # Weekend-only
                is_correct_day = c.Day == 0 or c.Day == 6
            elif self.day == -3:
                # Any day
                is_correct_day = True
            else:
                # Specific calendar day
                is_correct_day = self.day == c.Days

            return hour_within_range and is_correct_day and self.is_active


        def set_inactive(self):
            self.is_active = False

        def check_location(self, location):
            return self.location.lower() == location.lower()

        def __str__(self):
            return f"Event at {self.location} from Hour {self.start_hour} to {self.end_hour}, on Day {self.day}. Block: {self.block}. Active: {self.is_active}"

    class Items(object):
        def __init__(self, name, val, weight, NoOwned, ID):
            self.name = name
            self.val = val
            self.weight = weight
            self.NoOwned = NoOwned
            self.ID = ID

        def AddItem(self):
            MaxWeight = 50
            if self.CurrentWeight + self.weight <= MaxWeight:
                self.NoOwned += 1

        @property
        def CurrentWeight(self):
            return sum(q.weight * q.NoOwned for q in Inventory)

    EVENTS = [Event(0, 0, -1, "", "", False) for _ in range(50)]
    Inventory = [Items("none", 0, 0, 0, t) for t in range(50)]


    class SceneTracker:
        def __init__(self):
            # Initialize an internal dictionary to track scenes.
            self.scenes = {}
        
        def start_scene(self, scene_id):
            # Use the internal dictionary for checking and setting scene data.
            if scene_id not in self.scenes:
                self.scenes[scene_id] = {"time_added": False}
        
        def conclude_scene(self, scene_id, hours):
            # Check the internal dictionary when concluding a scene.
            if not self.scenes[scene_id]["time_added"]:
                calendar.AddTime(hours)
                self.scenes[scene_id]["time_added"] = True

    # Initialize the scene_tracker instance of SceneTracker.
    scene_tracker = SceneTracker()
