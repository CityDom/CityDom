init python:
    class Place(object):
        def __init__(self, ID, x, y, name, IsActive):
            self.ID = ID
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
        ### ADDS A NEW PROPERTY
        @property
        def avatar(self):
            icon = "MapIcons/" + self.name.lower() + "_icon.png"
            return(icon)

        @property
        def rooms(self):
            return [s.name for s in get_sublocations(self.ID)]


    # Places = []
    # t = 0
    # while t < 50:
    #     Places.append(Place(t, 0, 0, "", False))
    #     t += 1

    # Places[0] = Place(0, 1000, 700, "Entrance", True)
    # Places[1] = Place(1, 200, 700, "mall", True)
    # Places[2] = Place(2, 1200, 300, "lobby", True)
    # Places[3] = Place(3, 1700, 900, "office", True)
