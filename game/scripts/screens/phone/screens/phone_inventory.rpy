screen inventory_screen():
    frame:
        xpos 1550
        ypos 100
        background "Inventory.png"
        imagebutton:
            idle "back_idle.png"
            xpos 280  # Modify these values to place the button where you want
            ypos 30  # Modify these values to place the button where you want
            action [SetVariable("ShowInventory", False), 
                    SetVariable("ShowPhone", True)]
