screen TeachersBathroomScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/TeachersBathroom.png"
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/TeachersBathroom evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/TeachersBathroom night.png"