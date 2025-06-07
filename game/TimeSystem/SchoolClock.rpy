init python:
    class SchoolClock(object):
        def __init__(self):
            self.hour = 12  # School starts at 12:00 PM
            self.period = 0  # Initial period

        @property
        def Output(self):
            display_hour = (self.hour - 1) % 12 + 1  # Convert 13-23 to 1-11 and 12 to 12
            minute = 0 if self.period % 2 == 0 else 50
            return f"{display_hour}:{str(minute).zfill(2)}"

        @property
        def IsBreak(self):
            return self.period % 2 != 0 and self.hour < 17  # It's break if the period is odd (i.e., something:50) and before 5 PM

        def AddTime(self, at_school=True):
            # If the player is in school, follow normal school period increments (1-2-3-4, etc.)
            if at_school:
                if self.period % 2 == 0:
                    self.period += 1  # Advance to 50 minutes
                else:
                    self.period += 1  # Advance to next hour and reset to 0 minutes
                    self.hour += 1

                # Reset the clock if it reaches 17:50
                if self.hour == 18 and self.period % 2 == 0:
                    self.reset()

            # If the player is NOT in school, skip every other period (0, 2, 4, 6, etc.)
            else:
                self.period += 2  # Skip one period (i.e., from 0 to 2, from 2 to 4, etc.)
                if self.period >= 2:
                    self.hour += 1  # Advance the hour once per 2 periods
                    self.period = 0 if self.hour == 18 else self.period  # Reset period after 17:50

                # Reset the clock at the end of the school day (6 PM)
                if self.hour >= 18:
                    self.reset()

        def reset(self):
            self.hour = 12
            self.period = 0

# Initialize the school clock
default school_clock = SchoolClock()
