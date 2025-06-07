init python:
    def get_field(character, field):
        return renpy.store.__dict__.get("Show{}{}".format(character, field), False)

    def calculate_progress(character):
        # Assume character_love, character_obedience, and character_corruption are variables that store the values.
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)
        
        # Calculate total progress
        total_progress = love + obedience + corruption
        max_progress = 60  # Correctly set for full progress at 20 points for each attribute
        progress_percentage = (total_progress / max_progress) * 100
        return progress_percentage

    def toggle_char_tab():
        global current_char_tab
        if current_char_tab == 1:
            current_char_tab = 2
        else:
            current_char_tab = 1

    def check_and_update_character_stats(character):
        # Retrieve the stats
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)
        
        # Check if any of the stats are above 20, and if so, set them to 20
        if love > 20: renpy.store.__dict__[character + "_love"] = 20
        if obedience > 20: renpy.store.__dict__[character + "_Obedience"] = 20
        if corruption > 20: renpy.store.__dict__[character + "_Corruption"] = 20

        # Ensure stats do not fall below 0
        if love < 0: renpy.store.__dict__[character + "_love"] = 0
        if obedience < 0: renpy.store.__dict__[character + "_Obedience"] = 0
        if corruption < 0: renpy.store.__dict__[character + "_Corruption"] = 0

        # ! Commented for now until I will implement level ups, the level ups will be on certain scenes, so this might be moved but the functionality of the code is good
        # # Check if all stats are at max
        # if love == 20 and obedience == 20 and corruption == 20:
        #     # Increase level
        #     current_level = renpy.store.__dict__.get(character + "_level", 1)
        #     renpy.store.__dict__[character + "_level"] = current_level + 1
        #     # Reset stats for new level
        #     renpy.store.__dict__[character + "_love"] = 0
        #     renpy.store.__dict__[character + "_Obedience"] = 0
        #     renpy.store.__dict__[character + "_Corruption"] = 0


# This variable will be used to track which character's stats are currently being shown.
default selected_character = "Mom"

default CharacterSelectionIsShowing = False

screen StatsScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background stats_background

        if CharacterSelectionIsShowing == True:

            if selected_character == "Mom":
                
                add "CharStats/momFront.png" xpos 120 ypos 41
                add "CharStats/momBack.png" xpos 1526 ypos 41
                add "Levels/[Mom_level].png" xpos 1110 ypos 480
                text Mom_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Mom_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Mom_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Mom_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Mom_love == 20 and Mom_Obedience == 20 and Mom_Corruption == 20 and Mom_level == Mom_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)
            
            
            elif selected_character == "BigSis":
                add "CharStats/ClairFront.png" xpos 63 ypos 60
                add "CharStats/ClairBack.png" xpos 1460 ypos 60
                add "Levels/[BigSis_level].png" xpos 1110 ypos 480
                text BigSis_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[BigSis_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[BigSis_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[BigSis_love]" xpos 735 ypos 420 size 50 color '#000000'
                if BigSis_love == 20 and BigSis_Obedience == 20 and BigSis_Corruption == 20 and BigSis_level == BigSis_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "LilSis":
                add "CharStats/sisFront.png" xpos 90 ypos 60
                add "CharStats/sisBack.png" xpos 1510 ypos 60
                
                add "Levels/[LilSis_level].png" xpos 1110 ypos 480
                text LilSis_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[LilSis_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[LilSis_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[LilSis_love]" xpos 735 ypos 420 size 50 color '#000000'
                if LilSis_love == 20 and LilSis_Obedience == 20 and LilSis_Corruption == 20 and LilSis_level == LilSis_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Maria":
                add "CharStats/MariaFront.png" xpos 90 ypos 60
                add "CharStats/MariaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Maria_level].png" xpos 1110 ypos 480
                text Maria_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Maria_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Maria_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Maria_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Maria_love == 20 and Maria_Obedience == 20 and Maria_Corruption == 20 and Maria_level == Maria_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Alis":
                add "CharStats/AlisFront.png" xpos 90 ypos 60
                add "CharStats/AlisBack.png" xpos 1510 ypos 60
                
                add "Levels/[Alis_level].png" xpos 1110 ypos 480
                text Alis_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Alis_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Alis_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Alis_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Alis_love == 20 and Alis_Obedience == 20 and Alis_Corruption == 20 and Alis_level == Alis_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Sophie":
                add "CharStats/SophieFront.png" xpos 90 ypos 60
                add "CharStats/SophieBack.png" xpos 1510 ypos 60
                
                add "Levels/[Sophie_level].png" xpos 1110 ypos 480
                text Sophie_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Sophie_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Sophie_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Sophie_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Sophie_love == 20 and Sophie_Obedience == 20 and Sophie_Corruption == 20 and Sophie_level == Sophie_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Lola":
                add "CharStats/LolaFront.png" xpos 90 ypos 60
                add "CharStats/LolaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Lola_level].png" xpos 1110 ypos 480
                text Lola_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Lola_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Lola_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Lola_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Lola_love == 20 and Lola_Obedience == 20 and Lola_Corruption == 20 and Lola_level == Lola_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Selina":
                add "CharStats/SelinaFront.png" xpos 90 ypos 60
                add "CharStats/SelinaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Selina_level].png" xpos 1110 ypos 480
                text Selina_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Selina_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Selina_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Selina_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Selina_love == 20 and Selina_Obedience == 20 and Selina_Corruption == 20 and Selina_level == Selina_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Helena":
                add "CharStats/HelenaFront.png" xpos 90 ypos 60
                add "CharStats/HelenaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Helena_level].png" xpos 1110 ypos 480
                text Helena_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Helena_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Helena_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Helena_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Helena_love == 20 and Helena_Obedience == 20 and Helena_Corruption == 20 and Helena_level == Helena_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Dorothy":
                add "CharStats/DorothyFront.png" xpos 90 ypos 60
                add "CharStats/DorothyBack.png" xpos 1510 ypos 60
                
                add "Levels/[Dorothy_level].png" xpos 1110 ypos 480
                text Dorothy_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Dorothy_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Dorothy_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Dorothy_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Dorothy_love == 20 and Dorothy_Obedience == 20 and Dorothy_Corruption == 20 and Dorothy_level == Dorothy_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Leya":
                add "CharStats/LeyaFront.png" xpos 90 ypos 60
                add "CharStats/LeyaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Leya_level].png" xpos 1110 ypos 480
                text Leya_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Leya_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Leya_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Leya_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Leya_love == 20 and Leya_Obedience == 20 and Leya_Corruption == 20 and Leya_level == Leya_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Greta":
                add "CharStats/GretaFront.png" xpos 90 ypos 60
                add "CharStats/GretaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Greta_level].png" xpos 1110 ypos 480
                text Greta_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Greta_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Greta_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Greta_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Greta_love == 20 and Greta_Obedience == 20 and Greta_Corruption == 20 and Greta_level == Greta_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Jannice":
                add "CharStats/JanniceFront.png" xpos 90 ypos 60
                add "CharStats/JanniceBack.png" xpos 1510 ypos 60

                add "Levels/[Jannice_level].png" xpos 1110 ypos 480
                text Jannice_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Jannice_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Jannice_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Jannice_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Jannice_love == 20 and Jannice_Obedience == 20 and Jannice_Corruption == 20 and Jannice_level == Jannice_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Criss":
                add "CharStats/CrissFront.png" xpos 90 ypos 60
                add "CharStats/CrissBack.png" xpos 1510 ypos 60
                add "Levels/[Criss_level].png" xpos 1110 ypos 480
                text Criss_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Criss_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Criss_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Criss_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Criss_love == 20 and Criss_Obedience == 20 and Criss_Corruption == 20 and Criss_level == Criss_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)
        
            elif selected_character == "Luna":
                add "CharStats/LunaFront.png" xpos 90 ypos 60
                add "CharStats/LunaBack.png" xpos 1510 ypos 60
                add "Levels/[Luna_level].png" xpos 1110 ypos 480
                text Luna_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Luna_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Luna_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Luna_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Luna_love == 20 and Luna_Obedience == 20 and Luna_Corruption == 20 and Luna_level == Luna_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Angeline":
                add "CharStats/AngelineFront.png" xpos 90 ypos 60
                add "CharStats/AngelineBack.png" xpos 1510 ypos 60
                add "Levels/[Angeline_level].png" xpos 1110 ypos 480
                text Angeline_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Angeline_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Angeline_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Angeline_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Angeline_love == 20 and Angeline_Obedience == 20 and Angeline_Corruption == 20 and Angeline_level == Angeline_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Scarlet":
                add "CharStats/ScarletFront.png" xpos 90 ypos 60
                add "CharStats/ScarletBack.png" xpos 1510 ypos 60
                add "Levels/[Scarlet_level].png" xpos 1110 ypos 480
                text Scarlet_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Scarlet_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Scarlet_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Scarlet_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Scarlet_love == 20 and Scarlet_Obedience == 20 and Scarlet_Corruption == 20 and Scarlet_level == Scarlet_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Tanya":
                add "CharStats/TanyaFront.png" xpos 90 ypos 60
                add "CharStats/TanyaBack.png" xpos 1510 ypos 60
                add "Levels/[Tanya_level].png" xpos 1110 ypos 480
                text Tanya_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Tanya_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Tanya_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Tanya_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Tanya_love == 20 and Tanya_Obedience == 20 and Tanya_Corruption == 20 and Tanya_level == Tanya_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Anna":
                add "CharStats/AnnaFront.png" xpos 90 ypos 60
                add "CharStats/AnnaBack.png" xpos 1510 ypos 60
                add "Levels/[Anna_level].png" xpos 1110 ypos 480
                text Anna_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Anna_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Anna_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Anna_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Anna_love == 20 and Anna_Obedience == 20 and Anna_Corruption == 20 and Anna_level == Anna_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Emma":
                add "CharStats/EmmaFront.png" xpos 80 ypos 60
                add "CharStats/EmmaBack.png" xpos 1510 ypos 60
                add "Levels/[Emma_level].png" xpos 1110 ypos 480
                text Emma_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Emma_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Emma_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Emma_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Emma_love == 20 and Emma_Obedience == 20 and Emma_Corruption == 20 and Emma_level == Emma_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Asako":
                add "CharStats/AsakoFront.png" xpos 80 ypos 60
                add "CharStats/AsakoBack.png" xpos 1510 ypos 60
                add "Levels/[Asako_level].png" xpos 1110 ypos 480
                text Asako_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Asako_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Asako_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Asako_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Asako_love == 20 and Asako_Obedience == 20 and Asako_Corruption == 20 and Asako_level == Asako_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Sandra":
                add "CharStats/SandraFront.png" xpos 80 ypos 60
                add "CharStats/SandraBack.png" xpos 1510 ypos 60
                add "Levels/[Sandra_level].png" xpos 1110 ypos 480
                text Sandra_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Sandra_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Sandra_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Sandra_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Sandra_love == 20 and Sandra_Obedience == 20 and Sandra_Corruption == 20 and Sandra_level == Sandra_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            # Button to go to the selected character's schedule screen
            imagebutton:
                xpos 1353  # Adjust position as needed
                ypos 770  # Adjust position as needed, ensuring it doesn't overlap with other buttons
                auto "schedule_%s.png"
                action [Show("ScheduleScreen"),
                        SetVariable("CharacterSelectionIsShowing", False)]
                sensitive selected_character is not None

            # Button to go to the selected character's body screen
            imagebutton:
                xpos 1353
                ypos 870
                auto "Body_icon_%s.png"
                action [Show("CharOverviewScreen"),
                        SetVariable("CharacterSelectionIsShowing", False)]
                sensitive selected_character is not None

            imagebutton:
                xpos 1320
                ypos 110
                auto "MoveRightArrowSmaller_%s.png"
                action Function(toggle_char_tab)
            
            # Exit button
            imagebutton:
                xpos 1353
                ypos 960
                auto "Exit_%s.png"
                action [Return(LastLocation),  
                SetVariable("selected_character", "Mom"), 
                SetVariable("CharacterSelectionIsShowing", False), 
                SetVariable("StatsScreenShown", False), 
                Hide("StatsScreen"),
                Hide("character_select_screen"),
                Show("MainHud"),
                SetVariable("ShowPhone", True)]

screen character_progress_bar(character):
    $ progress = calculate_progress(character) 
    $ full_progress_bar_width = 272 
    $ progress_width = (progress / 100) * full_progress_bar_width 
    $ bar_xpos = 1030
    $ bar_ypos = 615

    add "bar/bar_empty.png":
        xpos bar_xpos
        ypos bar_ypos
    hbox:
        xsize progress_width
        add "bar/bar_full.png" size (progress_width, 40):
            xpos bar_xpos
            ypos bar_ypos
