screen WomansToiletScreen():
    if 0 <= calendar.Hours <= 11:
        add "SchoolSubplace/WomansToilet.png"
    if 12 <= calendar.Hours <= 15:
        add "SchoolSubplace/WomansToilet evening.png"
    if 16 <= calendar.Hours <= 24:
        add "SchoolSubplace/WomansToilet night.png"