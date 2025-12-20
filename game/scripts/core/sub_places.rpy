init python:
    class SubPlace(object):
        def __init__(self, ID, parent, name, x, y, iconPhoto, IsActive):
            self.ID = ID
            self.parent = parent
            self.name = name
            self.IsActive = IsActive
            self.x = x
            self.y = y
            self.iconPhoto = iconPhoto

    SubLocations = []
    Places = []
    t = 0

    # How much to compress spacing between sublocation icons (1.0 = original).
    SUBLOC_POS_SCALE_X = 0.75
    SUBLOC_POS_SCALE_Y = 0.85

    # Push whole row closer to the bottom (positive values move DOWN).
    SUBLOC_BOTTOM_SHIFT = 50
    SUBLOC_RIGHT_SHIFT = 40   # pixels; + moves RIGHT, - moves LEFT

    # Fine-tune offsets (icon vs. shadow)
    SUBLOC_ICON_Y_OFFSET = 8
    SUBLOC_SHADOW_OFFSET = 3

    HOVER_ZOOM = 1.10      # how much to zoom on hover
    HOVER_DUR  = 0.08      # animation time

    while t < 500:
        SubLocations.append(SubPlace(t, -1, "",0, 0,"", False))
        Places.append(Place(t, 0, 0, "", False))
        t += 1


    Places[0] = Place(0, 1000, 700, "Entrance", True)
    Places[1] = Place(1, 200, 700, "School", True)
    #Places[2] = Place(2, 1200, 300, "lobby", True)
    #Places[3] = Place(3, 1700, 900, "office", True)

    sub_place_data = [
        (0, 0, "My room", 50, 900, "SubLocationIcons/MCBedroomIcon_%s.png", True),
        (1, 0, "Jennifer room", 230, 900, "SubLocationIcons/JenniferBedroomIcon_%s.png", True),
        (2, 0, "Isabella room", 410, 900, "SubLocationIcons/IsabellaBedroomIcon_%s.png", True),
        (3, 0, "Claire room", 590, 900, "SubLocationIcons/ClaireBedroomIcon_%s.png", True),
        (4, 0, "HouseToilet", 770, 900, "SubLocationIcons/ToiletIcon_%s.png", True),
        (5, 0, "Livingroom", 950, 900, "SubLocationIcons/livingroomIcon_%s.png", True),
        (6, 0, "Washing Room", 1130, 900, "SubLocationIcons/WashingRoomIcon_%s.png", True),
        (7, 0, "Bathroom", 1310, 900, "SubLocationIcons/Bathroom_%s.png", True),
        (8, 0, "Entrance", 1490, 900, "SubLocationIcons/Entrance_%s.png", True),
        (9, 0, "Garden1", 1670, 900, "SubLocationIcons/Garden1_%s.png", True),
        (10, 0, "Garden2", 1850, 900, "SubLocationIcons/Garden2_%s.png", True),
        (11, 0, "Housefront", 2030, 900, "SubLocationIcons/HousefrontIcon_%s.png", True),

        (10, 1, "School", 50, 900, "SchoolSubLocationIcons/School_%s.png", True),
        (11, 1, "SchoolEntrance", 230, 900, "SchoolSubLocationIcons/SchoolEntrance_%s.png", True),
        (12, 1, "ToiletsFront", 410, 900, "SchoolSubLocationIcons/ToiletsFront_%s.png", True),
        (13, 1, "UpTheStairs", 590, 900, "SchoolSubLocationIcons/UpTheStairs_%s.png", True),
        (14, 1, "TeacherHall", 770, 900, "SchoolSubLocationIcons/TeacherHall_%s.png", True),
        (15, 1, "ArtClassFront", 950, 900, "SchoolSubLocationIcons/ArtClassFront_%s.png", True),
        (16, 1, "MedicRoomFront", 1130, 900, "SchoolSubLocationIcons/MedicRoomFront_%s.png", True),
        (17, 1, "SchoolGymFront", 1310, 900, "SchoolSubLocationIcons/SchoolGymFront_%s.png", True),
        (18, 1, "InsideSchoolGym", 1490, 900, "SchoolSubLocationIcons/InsideSchoolGym_%s.png", True),
        (19, 1, "SchoolPool", 1670, 900, "SchoolSubLocationIcons/SchoolPool_%s.png", True),
    ]

    for i, data in enumerate(sub_place_data):
        SubLocations[i] = SubPlace(*data)

transform subloc_hover_zoom:
    subpixel True
    anchor (0.5, 0.5)
    on show:
        zoom 1.0
    on replace:
        zoom 1.0
    on idle:
        linear HOVER_DUR zoom 1.0
    on hover:
        linear HOVER_DUR zoom HOVER_ZOOM