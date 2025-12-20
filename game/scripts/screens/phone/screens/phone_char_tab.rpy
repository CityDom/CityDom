screen character_select_screen():
    # Show the correct character tab image based on the current tab

    if CharacterSelectionIsShowing == True:
        if current_char_tab == 1:

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 591 ypos 66
                action SetVariable("selected_character", "Jennifer")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 700 ypos 65
                action SetVariable("selected_character", "Isabella")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 801 ypos 65 
                action SetVariable("selected_character", "Claire")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 900 ypos 65 
                action SetVariable("selected_character", "Maria")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1000 ypos 65 
                action SetVariable("selected_character", "Alis")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1100 ypos 65 
                action SetVariable("selected_character", "Sophie")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1200 ypos 65 
                action SetVariable("selected_character", "Lola")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 590 ypos 178 
                action SetVariable("selected_character", "Selina")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 700 ypos 178 
                action SetVariable("selected_character", "Helena")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 801 ypos 178 
                action SetVariable("selected_character", "Dorothy")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 900 ypos 178 
                action SetVariable("selected_character", "Leya")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1000 ypos 178 
                action SetVariable("selected_character", "Greta")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1100 ypos 178 
                action SetVariable("selected_character", "Jannice")
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1200 ypos 178 
                action SetVariable("selected_character", "Criss")

            if selected_character == "Jennifer":
                add "Selectedchar.png" xpos 591 ypos 66

            if selected_character == "Isabella":
                add "Selectedchar.png" xpos 696 ypos 68

            if selected_character == "Claire":
                add "Selectedchar.png" xpos 801 ypos 68

            if selected_character == "Maria":
                add "Selectedchar.png" xpos 906 ypos 68

            if selected_character == "Alis":
                add "Selectedchar.png" xpos 1011 ypos 68

            if selected_character == "Sophie":
                add "Selectedchar.png" xpos 1116 ypos 68

            if selected_character == "Lola":
                add "Selectedchar.png" xpos 1220 ypos 68

            if selected_character == "Selina":
                add "Selectedchar.png" xpos 591 ypos 184

            if selected_character == "Helena":
                add "Selectedchar.png" xpos 696 ypos 184

            if selected_character == "Dorothy":
                add "Selectedchar.png" xpos 801 ypos 184

            if selected_character == "Leya":
                add "Selectedchar.png" xpos 906 ypos 184

            if selected_character == "Greta":
                add "Selectedchar.png" xpos 1011 ypos 184

            if selected_character == "Jannice":
                add "Selectedchar.png" xpos 1116 ypos 184

            if selected_character == "Criss":
                add "Selectedchar.png" xpos 1220 ypos 184
        else:
            add "CharTab2.png" xpos 566 ypos 7
            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 591 ypos 66
                action SetVariable("selected_character", "Luna")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 700 ypos 66
                action SetVariable("selected_character", "Asako")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 801 ypos 66
                action SetVariable("selected_character", "Angeline")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 900 ypos 66
                action SetVariable("selected_character", "Scarlet")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1000 ypos 66
                action SetVariable("selected_character", "Tanya")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1100 ypos 66
                action SetVariable("selected_character", "Anna")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 1220 ypos 66
                action SetVariable("selected_character", "Emma")

            imagebutton:
                auto "CharacterSelectionInvisibleButton_%s.png" xpos 590 ypos 178
                action SetVariable("selected_character", "Sandra")

            if selected_character == "Luna":
                add "Selectedchar.png" xpos 589 ypos 66

            if selected_character == "Asako":
                add "Selectedchar.png" xpos 696 ypos 66

            if selected_character == "Angeline":
                add "Selectedchar.png" xpos 802 ypos 66

            if selected_character == "Scarlet":
                add "Selectedchar.png" xpos 906 ypos 67

            if selected_character == "Tanya":
                add "Selectedchar.png" xpos 1011 ypos 67

            if selected_character == "Anna":
                add "Selectedchar.png" xpos 1115 ypos 67

            if selected_character == "Emma":
                add "Selectedchar.png" xpos 1220 ypos 67
            
            if selected_character == "Sandra":
                add "Selectedchar.png" xpos 589 ypos 183
