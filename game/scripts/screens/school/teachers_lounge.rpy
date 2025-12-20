screen TeachersLoungeScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/TeachersLounge.png"
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/TeachersLounge evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/TeachersLounge night.png"