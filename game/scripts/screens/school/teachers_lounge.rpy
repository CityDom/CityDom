screen TeachersLoungeScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/TeachersLounge.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/TeachersLounge evening.png"
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/TeachersLounge night.png"