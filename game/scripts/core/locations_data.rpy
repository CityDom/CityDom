init -2 python:
    from collections import defaultdict

    def normalize_location_key(value):
        return str(value).strip().lower()

    class LocationDef(object):
        def __init__(self, key, name, location_id=None, screen_name=None):
            self.key = key
            self.name = name
            self.location_id = location_id
            self.screen_name = screen_name

    class SubLocationDef(object):
        def __init__(self, name, parent_id, x, y, icon_pattern, active=True, icon_size=None):
            self.name = name
            self.key = normalize_location_key(name)
            self.parent_id = parent_id
            self.x = x
            self.y = y
            self.icon_pattern = icon_pattern
            self.active = active
            self.icon_size = icon_size
            self._icon_idle = None
            self._icon_hover = None
            self._icon_idle_scaled = None
            self._icon_hover_scaled = None

        def resolve_icons(self):
            if self._icon_idle is None:
                if "%s" in self.icon_pattern:
                    self._icon_idle = self.icon_pattern % "idle"
                    self._icon_hover = self.icon_pattern % "hover"
                else:
                    self._icon_idle = self.icon_pattern
                    self._icon_hover = self.icon_pattern
            if self.icon_size:
                if self._icon_idle_scaled is None:
                    self._icon_idle_scaled = im.Scale(self._icon_idle, self.icon_size, self.icon_size)
                    self._icon_hover_scaled = im.Scale(self._icon_hover, self.icon_size, self.icon_size)
                return self._icon_idle_scaled, self._icon_hover_scaled
            return self._icon_idle, self._icon_hover

        def get_icon_size(self):
            if self.icon_size:
                return (self.icon_size, self.icon_size)
            if self._icon_idle is None:
                self.resolve_icons()
            return get_subloc_icon_size(self._icon_idle)

    _LOCATIONS = {}
    _LOCATION_ALIASES = {}
    _SUBLOCATIONS = []
    _SUBLOCATIONS_BY_PARENT = defaultdict(list)
    _SUBLOC_LAYOUT_CACHE = {}
    _SUBLOC_ICON_SIZES = {}
    SCHOOL_SUBLOC_ICON_SIZE = 110

    def register_location(name, location_id=None, screen_name=None, aliases=()):
        key = normalize_location_key(name)
        loc = LocationDef(key, name, location_id=location_id, screen_name=screen_name)
        _LOCATIONS[key] = loc
        _LOCATION_ALIASES[key] = key
        for alias in aliases:
            _LOCATION_ALIASES[normalize_location_key(alias)] = key
        return loc

    def register_sublocation(name, parent_id, x, y, icon_pattern, active=True, icon_size=None):
        subloc = SubLocationDef(name, parent_id, x, y, icon_pattern, active=active, icon_size=icon_size)
        _SUBLOCATIONS.append(subloc)
        _SUBLOCATIONS_BY_PARENT[parent_id].append(subloc)
        return subloc

    def get_location_def(name_or_key):
        key = normalize_location_key(name_or_key)
        key = _LOCATION_ALIASES.get(key, key)
        return _LOCATIONS.get(key)

    def get_location_name(name_or_key):
        loc = get_location_def(name_or_key)
        return loc.name if loc else name_or_key

    def get_location_id(name_or_key, fallback=None):
        loc = get_location_def(name_or_key)
        if loc and loc.location_id is not None:
            return loc.location_id
        return fallback

    def get_location_screen_name(name_or_key):
        loc = get_location_def(name_or_key)
        return loc.screen_name if loc else None

    def get_location_image_key(name_or_key, period_index):
        base = normalize_location_key(name_or_key)
        if period_index == 1:
            return base + " evening"
        if period_index == 2:
            return base + " night"
        return base

    def get_sublocations(parent_id):
        return tuple(_SUBLOCATIONS_BY_PARENT.get(parent_id, ()))

    def get_sublocation_layout(parent_id):
        if parent_id in _SUBLOC_LAYOUT_CACHE:
            return _SUBLOC_LAYOUT_CACHE[parent_id]
        sublocs = _SUBLOCATIONS_BY_PARENT.get(parent_id, ())
        if not sublocs:
            _SUBLOC_LAYOUT_CACHE[parent_id] = (0, 0)
            return (0, 0)
        min_x = min(s.x for s in sublocs)
        min_y = min(s.y for s in sublocs)
        _SUBLOC_LAYOUT_CACHE[parent_id] = (min_x, min_y)
        return (min_x, min_y)

    def get_subloc_icon_size(image_path):
        size = _SUBLOC_ICON_SIZES.get(image_path)
        if size is None:
            if renpy.loadable(image_path):
                size = renpy.image_size(image_path)
            else:
                size = (64, 64)
            _SUBLOC_ICON_SIZES[image_path] = size
        return size

    # House locations (LocationID = 0)
    register_location("Entrance", location_id=0, screen_name="EntranceScreen")
    register_location("Housefront", location_id=0, screen_name="HousefrontScreen", aliases=("HouseFront",))
    register_location("Garden1", location_id=0, screen_name="Garden1WeekendScreen")
    register_location("Garden2", location_id=0, screen_name="Garden2WeekendScreen")
    register_location("Livingroom", location_id=0, screen_name="LivingroomScreen")
    register_location("Kitchen", location_id=0, screen_name="KitchenScreen")
    register_location("Bathroom", location_id=0, screen_name="BathroomScreen")
    register_location("Washing Room", location_id=0)
    register_location("Hallway", location_id=0)
    register_location("HouseToilet", location_id=0, screen_name="HouseToiletScreen")
    register_location("My room", location_id=0)
    register_location("Jennifer room", location_id=0, screen_name="JenniferRoomWeekendScreen")
    register_location("Isabella room", location_id=0, screen_name="IsabellaRoomWeekendScreen")
    register_location("Claire room", location_id=0, screen_name="ClaireRoomWeekendScreen")

    # School locations (LocationID = 1)
    register_location("School", location_id=1, screen_name="SchoolScreen")
    register_location("SchoolEntrance", location_id=1, screen_name="SchoolEntranceScreen")
    register_location("ToiletsFront", location_id=1, screen_name="ToiletsFrontScreen")
    register_location("UpTheStairs", location_id=1, screen_name="UpTheStairsScreen")
    register_location("TeacherHall", location_id=1, screen_name="TeacherHallScreen")
    register_location("ArtClassFront", location_id=1, screen_name="ArtClassFrontScreen")
    register_location("MedicRoomFront", location_id=1, screen_name="MedicRoomFrontScreen")
    register_location("SchoolGymFront", location_id=1, screen_name="SchoolGymFrontScreen")
    register_location("InsideSchoolGym", location_id=1, screen_name="InsideSchoolGymScreen")
    register_location("SchoolPool", location_id=1, screen_name="SchoolPoolScreen")
    register_location("MansToilet", location_id=1, screen_name="MensToiletScreen", aliases=("MensToilet",))
    register_location("WomansToilet", location_id=1, screen_name="WomansToiletScreen")
    register_location("TeachersBathroom", location_id=1, screen_name="TeachersBathroomScreen")
    register_location("PrincipalOffice", location_id=1, screen_name="PrincipalOfficeScreen")
    register_location("TeachersLounge", location_id=1, screen_name="TeachersLoungeScreen")
    register_location("MainClassroom", location_id=1, screen_name="MainClassroomScreen")
    register_location("NurseRoom", location_id=1, screen_name="NurseRoomScreen")
    register_location("ArtClass", location_id=1, screen_name="ArtClassScreen")
    register_location("SchoolLibrary", location_id=1, screen_name="SchoolLibraryScreen")
    register_location("MannersClass", location_id=1, screen_name="MannersClassScreen")
    register_location("BioClass", location_id=1, screen_name="BioClassScreen")
    register_location("Gym", location_id=1, screen_name="GymScreen")
    register_location("GymLockerRoomFront", location_id=1, screen_name="GymLockerRoomFrontScreen")
    register_location("GirlsLockerRoom", location_id=1, screen_name="GirlsLockerRoomScreen")
    register_location("BackYard", location_id=1, screen_name="BackYardScreen", aliases=("Backyard", "Backyard1"))

    # Sublocation icons (hub row)
    register_sublocation("My room", 0, 50, 900, "SubLocationIcons/MCBedroomIcon_%s.png", True)
    register_sublocation("Jennifer room", 0, 230, 900, "SubLocationIcons/JenniferBedroomIcon_%s.png", True)
    register_sublocation("Isabella room", 0, 410, 900, "SubLocationIcons/IsabellaBedroomIcon_%s.png", True)
    register_sublocation("Claire room", 0, 590, 900, "SubLocationIcons/ClaireBedroomIcon_%s.png", True)
    register_sublocation("HouseToilet", 0, 770, 900, "SubLocationIcons/ToiletIcon_%s.png", True)
    register_sublocation("Livingroom", 0, 950, 900, "SubLocationIcons/livingroomIcon_%s.png", True)
    register_sublocation("Washing Room", 0, 1130, 900, "SubLocationIcons/WashingRoomIcon_%s.png", True)
    register_sublocation("Bathroom", 0, 1310, 900, "SubLocationIcons/Bathroom_%s.png", True)
    register_sublocation("Entrance", 0, 1490, 900, "SubLocationIcons/Entrance_%s.png", True)
    register_sublocation("Garden1", 0, 1670, 900, "SubLocationIcons/Garden1_%s.png", True)
    register_sublocation("Garden2", 0, 1850, 900, "SubLocationIcons/Garden2_%s.png", True)
    register_sublocation("Housefront", 0, 2030, 900, "SubLocationIcons/HousefrontIcon_%s.png", True)

    register_sublocation("School", 1, 50, 900, "SchoolSubLocationIcons/School_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("SchoolEntrance", 1, 230, 900, "SchoolSubLocationIcons/SchoolEntrance_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("ToiletsFront", 1, 410, 900, "SchoolSubLocationIcons/ToiletsFront_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("UpTheStairs", 1, 590, 900, "SchoolSubLocationIcons/UpTheStairs_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("TeacherHall", 1, 770, 900, "SchoolSubLocationIcons/TeacherHall_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("ArtClassFront", 1, 950, 900, "SchoolSubLocationIcons/ArtClassFront_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("MedicRoomFront", 1, 1130, 900, "SchoolSubLocationIcons/MedicRoomFront_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("SchoolGymFront", 1, 1310, 900, "SchoolSubLocationIcons/SchoolGymFront_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("InsideSchoolGym", 1, 1490, 900, "SchoolSubLocationIcons/InsideSchoolGym_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
    register_sublocation("SchoolPool", 1, 1670, 900, "SchoolSubLocationIcons/SchoolPool_%s.png", True, icon_size=SCHOOL_SUBLOC_ICON_SIZE)
