screen MensToiletScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/MansToilet.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/MansToilet evening.png"
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/MansToilet night.png"