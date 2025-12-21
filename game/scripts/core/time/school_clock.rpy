init python:
    class SchoolClock(object):
        START_HOUR = 12
        PERIODS_PER_HOUR = 2
        HOURS_PER_DAY = 6
        PERIODS_PER_DAY = HOURS_PER_DAY * PERIODS_PER_HOUR

        def __init__(self):
            self._period = 0

        @property
        def Output(self):
            display_hour = (self.hour - 1) % 12 + 1
            minute = 0 if self.period % 2 == 0 else 50
            return f"{display_hour}:{str(minute).zfill(2)}"

        @property
        def IsBreak(self):
            return self.period % 2 != 0 and self.hour < 17

        @property
        def period(self):
            if not hasattr(self, "_period"):
                self._period = 0
            return self._period

        @period.setter
        def period(self, value):
            value = int(value)
            self._period = max(0, min(value, self.PERIODS_PER_DAY - 1))

        @property
        def hour(self):
            if not hasattr(self, "_period"):
                self._period = 0
            return self.START_HOUR + (self._period // self.PERIODS_PER_HOUR)

        @hour.setter
        def hour(self, value):
            value = int(value)
            self._period = (value - self.START_HOUR) * self.PERIODS_PER_HOUR
            self._period = max(0, min(self._period, self.PERIODS_PER_DAY - 1))

        def AddTime(self, at_school=True):
            periods = 1 if at_school else self.PERIODS_PER_HOUR
            self.advance_periods(periods)

        def advance_periods(self, periods):
            periods = int(periods)
            if periods <= 0:
                return
            self.period = self._period + periods

        def is_last_period(self):
            return self._period >= (self.PERIODS_PER_DAY - 1)

        def reset(self):
            self._period = 0

# Initialize the school clock
default school_clock = SchoolClock()
