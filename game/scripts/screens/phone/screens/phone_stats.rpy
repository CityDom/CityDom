screen StatsScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background stats_background

        if CharacterSelectionIsShowing == True:

            if selected_character == "Jennifer":
                
                add "CharStats/jenniferFront.png" xpos 120 ypos 41
                add "CharStats/jenniferBack.png" xpos 1526 ypos 41
                add "Levels/[Jennifer_level].png" xpos 1110 ypos 480
                text Jennifer_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Jennifer_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Jennifer_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Jennifer_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Jennifer_love == 20 and Jennifer_Obedience == 20 and Jennifer_Corruption == 20 and Jennifer_level == Jennifer_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)
            
            
            elif selected_character == "Claire":
                add "CharStats/ClaireFront.png" xpos 63 ypos 60
                add "CharStats/ClaireBack.png" xpos 1460 ypos 60
                add "Levels/[Claire_level].png" xpos 1110 ypos 480
                text Claire_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Claire_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Claire_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Claire_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Claire_love == 20 and Claire_Obedience == 20 and Claire_Corruption == 20 and Claire_level == Claire_maxLevel:
                    text "Max progression reached" xpos 1005 ypos 615 size 30 color "#FF0000"
                else:
                    use character_progress_bar(selected_character)

            elif selected_character == "Isabella":
                add "CharStats/isabellaFront.png" xpos 90 ypos 60
                add "CharStats/isabellaBack.png" xpos 1510 ypos 60
                
                add "Levels/[Isabella_level].png" xpos 1110 ypos 480
                text Isabella_Info1 xpos 600 ypos 800 size 35 color "#000000" xsize 700 ysize 100
                text "[Isabella_Corruption]" xpos 890 ypos 600 size 50 color '#000000'
                text "[Isabella_Obedience]" xpos 870 ypos 510 size 50 color '#000000'
                text "[Isabella_love]" xpos 735 ypos 420 size 50 color '#000000'
                if Isabella_love == 20 and Isabella_Obedience == 20 and Isabella_Corruption == 20 and Isabella_level == Isabella_maxLevel:
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

            # Button to go to the selected character's schedule scree'
            imagebutton:
                xpos 1353  # Adjust position as needed
                ypos 770  # Adjust position as needed, ensuring it doesn't overlap with other button'
                auto "schedule_%s.png"
                action [Show("ScheduleScreen"),
                        SetVariable("CharacterSelectionIsShowing", False)]
                sensitive selected_character is not None

            # Button to go to the selected character's body scree'
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
                SetVariable("selected_character", "Jennifer"), 
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
