screen GirlsLockerRoomScreen():
    if is_day_hour(calendar.Hours):
        add "SchoolSubplace/GirlsLockerRoom.png"
    if is_evening_hour(calendar.Hours):
        add "SchoolSubplace/GirlsLockerRoom evening.png"