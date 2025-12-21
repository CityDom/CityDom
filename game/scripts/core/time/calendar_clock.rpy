# Global instance
default default_calendar_hour = 6
default default_calendar_hours = 6
default default_calendar_days = 1
default default_calendar_day = 0
default default_calendar_month = 0

default calendar = Calendar()

init python:
    DAY_START_HOUR = 0
    DAY_END_HOUR = 20
    DAY_HOURS_COUNT = DAY_END_HOUR - DAY_START_HOUR + 1

    SCHOOL_START_HOUR = 6
    SCHOOL_END_HOUR = 12
    SCHOOL_PERIODS_PER_HOUR = 2

    class Calendar(object):
        def __init__(self):
            self.Hour = default_calendar_hour
            self.Hours = default_calendar_hours
            self.Days = default_calendar_days
            self.Day = int(default_calendar_day)
            self.Month = default_calendar_month
            self.Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            self.WeekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            self.period_index = 0
            self._day_advanced_flag = False

        @property
        def Output(self):
            return f"{self.WeekDays[self.Day]} {str(self.Hours).zfill(2)}:00"

        def is_school_hours(self, hour=None):
            if hour is None:
                hour = self.Hours
            return SCHOOL_START_HOUR <= hour < SCHOOL_END_HOUR

        def AddTime(self, Hours):
            self.advance_hours(Hours)

        def advance_hours(self, hours):
            hours = int(hours)
            if hours <= 0:
                return
            for _ in range(hours):
                prev_hour = self.Hours
                day_advanced = self._advance_one_hour()
                self._sync_school_clock_after_hour(prev_hour, self.Hours, day_advanced)
            hud_refresh()

        def advance_school_periods(self, periods=1):
            periods = int(periods)
            if periods <= 0:
                return
            for _ in range(periods):
                if not self.is_school_hours():
                    break
                if school_clock.is_last_period():
                    break
                prev_period = school_clock.period
                school_clock.advance_periods(1)
                if school_clock.period != prev_period and school_clock.period % SCHOOL_PERIODS_PER_HOUR == 0:
                    self._advance_one_hour()
            self.update_period_index()
            hud_refresh()

        def align_school_period_to_class(self):
            if not self.is_school_hours():
                return
            if school_clock.IsBreak:
                self.advance_school_periods(1)
        
        def sync_from_school_clock(self, round_break=False):
            offset = school_clock.START_HOUR - SCHOOL_START_HOUR
            if round_break:
                odd_period = (school_clock.period % SCHOOL_PERIODS_PER_HOUR) != 0
                if odd_period:
                    if school_clock.is_last_period():
                        self.Hours = SCHOOL_END_HOUR
                        self.update_period_index()
                        hud_refresh()
                        return
                    school_clock.advance_periods(1)
            self.Hours = school_clock.hour - offset
            self.update_period_index()
            hud_refresh()

        def get_current_hour(self):
            return self.Hours

        def advance_to_next_day(self):
            if not hasattr(self, "_day_advanced_flag"):
                self._day_advanced_flag = False
            if self._day_advanced_flag:
                self._day_advanced_flag = False
            else:
                self.Day = int(self.Day) + 1
                if self.Day > 6:
                    self.Day = 0
                self.Days += 1
                if self.Days == self.MonthDays[self.Month]:
                    self.Month += 1
                    self.Days = 0
                if self.Month > 11:
                    self.Month = 0
            self.Hours = DAY_START_HOUR
            self.update_period_index()
            school_clock.reset()

        def update_period_index(self):
            if 12 <= self.Hours < 16:
                self.period_index = 1
            elif 16 <= self.Hours < 24:
                self.period_index = 2
            else:
                self.period_index = 0

        def update_sub_place_data(self):
            self.update_period_index()

        def _advance_one_hour(self):
            if not hasattr(self, "_day_advanced_flag"):
                self._day_advanced_flag = False
            self.Hours += 1
            day_advanced = False
            if self.Hours > DAY_END_HOUR:
                self.Hours = DAY_START_HOUR
                self.Day += 1
                self.Days += 1
                day_advanced = True
                self._day_advanced_flag = True
            if self.Day > 6:
                self.Day = 0
            if self.Days == self.MonthDays[self.Month]:
                self.Month += 1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0
            self.update_period_index()
            if day_advanced:
                school_clock.reset()
                renpy.call("SleepEvent")
            return day_advanced

        def _sync_school_clock_after_hour(self, prev_hour, new_hour, day_advanced):
            if day_advanced or new_hour == SCHOOL_START_HOUR:
                school_clock.reset()
                return
            if self.is_school_hours(new_hour):
                school_clock.advance_periods(SCHOOL_PERIODS_PER_HOUR)
                
    class Event:
        def __init__(self, start_hour, end_hour, day, location, block, is_active, screen_name=None):
            self.start_hour = start_hour
            self.end_hour = end_hour
            self.day = day
            self.location = location
            self.block = block
            self.is_active = is_active
            self.screen_name = screen_name

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

