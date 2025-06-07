screen MensToiletScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/MansToilet.png"
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/MansToilet evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/MansToilet night.png"