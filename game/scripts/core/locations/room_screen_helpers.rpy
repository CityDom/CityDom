init 1 python:
    def select_room_scene(hour, events, day_bg, evening_bg, night_bg):
        if hour in events:
            return events[hour]
        if hour < EVENING_START_HOUR:
            return {"bg": day_bg}
        if hour < NIGHT_BG_START_HOUR:
            return {"bg": evening_bg}
        return {"bg": night_bg}
