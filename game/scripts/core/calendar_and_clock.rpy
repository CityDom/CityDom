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
            self.update_period_index()
            hud_refresh()

        def get_current_hour(self):
            return self.Hours

        def advance_to_next_day(self):
            self.Day = int(self.Day) + 1
            if self.Day > 6:
                self.Day = 0

        def update_period_index(self):
            if 12 <= self.Hours < 16:
                self.period_index = 1
            elif 16 <= self.Hours < 24:
                self.period_index = 2
            else:
                self.period_index = 0

        def update_sub_place_data(self):
            # Backward-compatible alias for older call sites and tests.
            self.update_period_index()
                
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
