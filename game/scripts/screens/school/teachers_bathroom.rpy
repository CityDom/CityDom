screen TeachersBathroomScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/TeachersBathroom.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/TeachersBathroom evening.png"
    if is_night_hour(calendar.Hours):
        add "SchoolSubplace/TeachersBathroom night.png"