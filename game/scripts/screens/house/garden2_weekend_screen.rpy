screen Garden2WeekendScreen():
    if is_day_hour(calendar.Hours):
        add "HomeSubplace/garden2.png"
    elif is_evening_hour(calendar.Hours):
        add "HomeSubplace/garden2 evening.png"
    elif is_night_hour(calendar.Hours):
        add "HomeSubplace/garden2 night.png"
