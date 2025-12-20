init python:
    class TimeOfDay(object):
        def __init__(self, ID, hour, iconPhoto):
            self.ID = ID
            self.hour = hour
            self.iconPhoto = iconPhoto

    DayTime = []
    t = 1

    while t < 50:
        DayTime.append(TimeOfDay(t, 0, ""))
        t += 1
 
    DayTime[0] = TimeOfDay(0, 0, "DayTimeIcon/AfternoonIcon.png")
    DayTime[1] = TimeOfDay(1, 4, "DayTimeIcon/EveningIcon.png")
    DayTime[1] = TimeOfDay(2, 8, "DayTimeIcon/EveningIcon.png")
    DayTime[1] = TimeOfDay(3, 12, "DayTimeIcon/EveningIcon.png")
    DayTime[1] = TimeOfDay(4, 16, "DayTimeIcon/EveningIcon.png")
    DayTime[1] = TimeOfDay(5, 20, "DayTimeIcon/EveningIcon.png")

