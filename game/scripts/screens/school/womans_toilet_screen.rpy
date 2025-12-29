screen WomansToiletScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/WomansToilet.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/WomansToilet evening.png"
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/WomansToilet night.png"