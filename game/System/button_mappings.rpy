init python:
    default_action = [Return("bathroom"), 
        SetVariable("ShowPhone", False), 
        SetVariable("ShowInventory", False), 
        SetVariable("showWallpaperScreen", False), 
        SetVariable("Messanger", False),
        SetVariable("ShowCallForSidebar", False)]

    def create_button(image_base, xpos, ypos, return_value, time_of_day):
        """Creates button dictionary with the correct image paths based on time of day."""
        return {
            "idle": f"{image_base}_{time_of_day}_idle.png",   # Example: McDoorButton_Evening_idle.png
            "hover": f"{image_base}_{time_of_day}_hover.png", # Example: McDoorButton_Evening_hover.png
            "xpos": xpos,
            "ypos": ypos,
            "action": [Return(return_value)] + default_action[1:]
        }

    invisible_door_button_mappings = {
        # EVENING
        "washing room evening": [create_button("TransparentDoors/WashingRoomDoor", 220, 132, "bathroom", "Evening")],
        "hallway evening": [
            create_button("TransparentDoors/McDoorButton", 764, 88, "my room", "Evening"),
            create_button("TransparentDoors/LilSisRoomButton", 1117, 92, "lil sis room", "Evening"),
            create_button("TransparentDoors/BigSisRoomButton", 257, 327, "big sis room", "Evening"),
            create_button("TransparentDoors/MomDoorButton", 570, 130, "Mom room", "Evening"),
            create_button("TransparentDoors/ToiletDoor", 1414, 127, "HouseToilet", "Evening"),
            create_button("TransparentDoors/DownStairsButton", 1260, 750, "Entrance", "Evening")
        ],
        "entrance evening": [
            create_button("TransparentDoors/LivingRoomDoorButton", 3, 143, "livingroom", "Evening"),
            create_button("TransparentDoors/HallwayStairsButton", 750, 210, "hallway", "Evening"),
            create_button("TransparentDoors/BathroomDoorButton", 1482, 30, "washing room", "Evening")
        ],
        "livingroom evening": [
            create_button("TransparentDoors/KitchenDoorButton", 1120, 190, "kitchen", "Evening"),
            create_button("TransparentDoors/EntrenceDoorButton", 45, 103, "Entrance", "Evening")
        ],
        "my room evening": [create_button("TransparentDoors/MyRoomInsideDoor", 277, 158, "hallway", "Evening")],
        "big sis room evening": [create_button("TransparentDoors/BigSisRoomButtonInside", 0, 94, "hallway", "Evening")],

        # NIGHT
        "washing room night": [create_button("TransparentDoors/WashingRoomDoor", 220, 132, "bathroom", "Night")],
        "hallway night": [
            create_button("TransparentDoors/McDoorButton", 764, 88, "my room", "Night"),
            create_button("TransparentDoors/LilSisRoomButton", 1117, 92, "lil sis room", "Night"),
            create_button("TransparentDoors/BigSisRoomButton", 257, 327, "big sis room", "Night"),
            create_button("TransparentDoors/MomDoorButton", 570, 130, "Mom room", "Night"),
            create_button("TransparentDoors/ToiletDoor", 1414, 127, "HouseToilet", "Night"),
            create_button("TransparentDoors/DownStairsButton", 1260, 750, "Entrance", "Night")
        ],
        "entrance night": [
            create_button("TransparentDoors/LivingRoomDoorButton", 3, 143, "livingroom", "Night"),
            create_button("TransparentDoors/HallwayStairsButton", 750, 210, "hallway", "Night"),
            create_button("TransparentDoors/BathroomDoorButton", 1482, 30, "washing room", "Night")
        ],
        "livingroom night": [
            create_button("TransparentDoors/KitchenDoorButton", 1120, 190, "kitchen", "Night"),
            create_button("TransparentDoors/EntrenceDoorButton", 45, 103, "Entrance", "Night")
        ],
        "my room night": [create_button("TransparentDoors/MyRoomInsideDoor", 277, 158, "hallway", "Night")],
        "big sis room night": [create_button("TransparentDoors/BigSisRoomButtonInside", 0, 94, "hallway", "Night")],

        # DAY
        "washing room": [create_button("TransparentDoors/WashingRoomDoor", 220, 132, "bathroom", "Day")],
        "hallway": [
            create_button("TransparentDoors/McDoorButton", 764, 88, "my room", "Day"),
            create_button("TransparentDoors/LilSisRoomButton", 1117, 92, "lil sis room", "Day"),
            create_button("TransparentDoors/BigSisRoomButton", 257, 327, "big sis room", "Day"),
            create_button("TransparentDoors/MomDoorButton", 570, 130, "Mom room", "Day"),
            create_button("TransparentDoors/ToiletDoor", 1414, 127, "HouseToilet", "Day"),
            create_button("TransparentDoors/DownStairsButton", 1260, 750, "Entrance", "Day")
        ],
        "entrance": [
            create_button("TransparentDoors/LivingRoomDoorButton", 3, 143, "livingroom", "Day"),
            create_button("TransparentDoors/HallwayStairsButton", 750, 210, "hallway", "Day"),
            create_button("TransparentDoors/BathroomDoorButton", 1482, 30, "washing room", "Day")
        ],
        "livingroom": [
            create_button("TransparentDoors/KitchenDoorButton", 1120, 190, "kitchen", "Day"),
            create_button("TransparentDoors/EntrenceDoorButton", 45, 103, "Entrance", "Day")
        ],
        "my room": [create_button("TransparentDoors/MyRoomInsideDoor", 277, 158, "hallway", "Day")],
        "big sis room": [create_button("TransparentDoors/BigSisRoomButtonInside", 0, 94, "hallway", "Day")],
    }

    room_mappings = {
        "bathroom": "washing room",
        "washing room": "Entrance",
        "my room": "Hallway",
        "big sis room": "Hallway",
        "hallway": "Entrance",
        "mom room": "Hallway",
        "lil sis room": "Hallway",
        "livingroom": "Entrance",
        "housetoilet": "hallway",
        "kitchen": "livingroom",

        "bathroom evening": "washing room",
        "washing room evening": "Entrance",
        "my room evening": "Hallway",
        "big sis room evening": "Hallway",
        "hallway evening": "Entrance",
        "mom room evening": "Hallway",
        "lil sis room evening": "Hallway",
        "livingroom evening": "Entrance",
        "housetoilet evening": "hallway",
        "kitchen evening": "livingroom",

        "bathroom night": "washing room",
        "washing room night": "Entrance",
        "my room night": "Hallway",
        "big sis room night": "Hallway",
        "hallway night": "Entrance",
        "mom room night": "Hallway",
        "lil sis room night": "Hallway",
        "livingroom night": "Entrance",
        "housetoilet night": "hallway",
        "kitchen night": "livingroom",

        "schoolentrance": "school",
        "schoolentrance evening": "school",
        "schoolentrance night": "school",

        "manstoilet": "toiletsfront",
        "manstoilet evening": "toiletsfront",
        "manstoilet night": "toiletsfront",

        "womanstoilet": "toiletsfront",
        "womanstoilet evening": "toiletsfront",
        "womanstoilet night": "toiletsfront",

        "upthestairs": "schoolentrance",
        "upthestairs evening": "schoolentrance",
        "upthestairs night": "schoolentrance",

        "teacherhall": "upthestairs",
        "teacherhall evening": "upthestairs",
        "teacherhall night": "upthestairs",

        "artclassfront": "upthestairs",
        "artclassfront evening": "upthestairs",
        "artclassfront night": "upthestairs",

        "medicroomfront": "artclassfront",
        "medicroomfront evening": "artclassfront",
        "medicroomfront night": "artclassfront",

        "schoolgymfront": "school",
        "schoolgymfront evening": "school",
        "schoolgymfront night": "school",

        "insideschoolgym": "schoolgymfront",
        "insideschoolgym evening": "schoolgymfront",
        "insideschoolgym night": "schoolgymfront",

        "backyard": "schoolgymfront",
        "backyard1": "schoolgymfront",
        "backyard evening": "schoolgymfront",
        "backyard night": "schoolgymfront",

        "schoolpool": "schoolgymfront",
        "schoolpool evening": "schoolgymfront",
        "schoolpool night": "schoolgymfront",

        "teachersbathroom": "teacherhall",
        "teachersbathroom evening": "teacherhall",
        "teachersbathroom night": "teacherhall",

        "principaloffice": "teacherhall",
        "principaloffice evening": "teacherhall",
        "principaloffice night": "teacherhall",

        "teacherslounge": "teacherhall",
        "teacherslounge evening": "teacherhall",
        "teacherslounge night": "teacherhall",

        "mainclassroom": "artclassfront",
        "mainclassroom evening": "artclassfront",
        "mainclassroom night": "artclassfront",
        "mainclassroom empty": "artclassfront",

        "nurseroom": "medicroomfront",
        "nurseroom evening": "medicroomfront",
        "nurseroom night": "medicroomfront",

        "artclass": "artclassfront",
        "artclass evening": "artclassfront",
        "artclass night": "artclassfront",

        "schoollibrary": "medicroomfront",
        "schoollibrary evening": "medicroomfront",
        "schoollibrary night": "medicroomfront",

        "mannersclass": "schoolentrance",
        "mannersclass evening": "schoolentrance",

        "bioclass": "medicroomfront",
        "bioclass evening": "medicroomfront",
        "bioclass empty": "medicroomfront",

        "gym": "insideschoolgym",
        "gym evening": "insideschoolgym",

        "gymlockerroomfront": "insideschoolgym",
        "gymlockerroomfront evening": "insideschoolgym",

        "girlslockerroom": "gymlockerroomfront",
        "girlslockerroom evening": "gymlockerroomfront",

        "entrance": "housefront",
        "entrance evening": "housefront",
        "entrance night": "housefront",
    }
    
    time_icons = [
    ("DayTimeIcon/Morning.png", (0, 4), "Morning"),
    ("DayTimeIcon/Noon.png", (4, 8), "Noon"),
    ("DayTimeIcon/Afternoon.png", (8, 12), "Afternoon"),
    ("DayTimeIcon/Evening.png", (12, 16), "Evening"),
    ("DayTimeIcon/Night.png", (16, 20), "Night"),
    ("DayTimeIcon/Midnight.png", (20, 24), "Midnight")
]

screen door_buttons(location):
    if location in invisible_door_button_mappings:
        for button in invisible_door_button_mappings[location]:
            imagebutton:
                idle button["idle"]
                hover button["hover"]
                xpos button["xpos"]
                ypos button["ypos"]
                action button["action"]