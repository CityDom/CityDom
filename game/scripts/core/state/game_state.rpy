# Variables for controlling UI elements
default ShowSublocationIcons = True
default timeIcon = 0
default Location = "Entrance"
default old_scene = ""
default LastLocation = ""
default Location_img = ""
default LocationID = 0
default LocationEntryFrom = None
default LocationEntryTime = None
default ShowPhone = False
default ShowInventory = False
default ShowChoseCharacterScreen = False
default setBackgroundPhoto = "WallpaperPreview_Default.png"
default previewImage = "WallpaperPreview_Default.png"
default showWallpaperScreen = False
default showWallpaperPreview = False
default blueHUD = False
default ShowMhyrorinButton = False
default ShowCallForSidebar = False
default canDownload = False
default saveAsBackgroundCheck = False
default backFromBackgroundPreview = False
default backFromBackgroundSave = False
default skip_time_button_enabled = True

# Variables for controlling character stats screens
default ShowConversationScreen = False
default Messanger = False
default StatScreenShown = False
default ShouldSeeSwitchSceneButton = False
default persistent.intro_scene_played = False
default scroll_to_bottom_requested = False
default MapScreenShown = False
default StatsScreenShown = False
default stats_background = "ChooseCharacterStats.png"
default FirstTimeInGymClass = False


# default CharFront = "CharStats/jenniferFront.png"
# default CharBack = "CharStats/jenniferBack.png"
# default CharLVL = "Levels/[Jennifer_level].png"
# default CharInfo = "[Jennifer_Info1]"
# default CharCorruption = "[Jennifer_Corruption]"
# default CharObedience = "[Jennifer_Obedience]"
# default CharLove = "[Jennifer_love]"
# default MaxProgressReached = False
# Scale image and assign to variable
image house = im.Scale("JenniferBody.png", 1920, 1080)

############ MOM STATS #################################################################################
default Jennifer_Corruption = 0
default Jennifer_Obedience = 0
default Jennifer_love = 0
default Jennifer_level = 1
default Jennifer_maxLevel = 1

############ Isabella STATS #################################################################################
default Isabella_Corruption = 0
default Isabella_Obedience = 0
default Isabella_love = 0
default Isabella_level = 1
default Isabella_maxLevel = 1

############ Claire STATS #################################################################################
default Claire_Corruption = 0
default Claire_Obedience = 0
default Claire_love = 0
default Claire_level = 1
default Claire_maxLevel = 1

############ Maria STATS #################################################################################
default Maria_Corruption = 0
default Maria_Obedience = 0
default Maria_love = 0
default Maria_level = 1
default Maria_maxLevel = 1

############ Alis STATS #################################################################################
default Alis_Corruption = 0
default Alis_Obedience = 0
default Alis_love = 0
default Alis_level = 1
default Alis_maxLevel = 1

############ Sophie STATS #################################################################################
default Sophie_Corruption = 0
default Sophie_Obedience = 0
default Sophie_love = 0
default Sophie_level = 1
default Sophie_maxLevel = 1

############ Lola STATS #################################################################################
default Lola_Corruption = 0
default Lola_Obedience = 0
default Lola_love = 0
default Lola_level = 1
default Lola_maxLevel = 1

############ Selina STATS #################################################################################
default Selina_Corruption = 0
default Selina_Obedience = 0
default Selina_love = 0
default Selina_level = 1
default Selina_maxLevel = 1

############ Helena STATS #################################################################################
default Helena_Corruption = 0
default Helena_Obedience = 0
default Helena_love = 0
default Helena_level = 1
default Helena_maxLevel = 1

############ Dorothy STATS #################################################################################
default Dorothy_Corruption = 0
default Dorothy_Obedience = 0
default Dorothy_love = 0
default Dorothy_level = 1
default Dorothy_maxLevel = 1

############ Leya STATS #################################################################################
default Leya_Corruption = 0
default Leya_Obedience = 0
default Leya_love = 0
default Leya_level = 1
default Leya_maxLevel = 1

############ Greta STATS #################################################################################
default Greta_Corruption = 0
default Greta_Obedience = 0
default Greta_love = 0
default Greta_level = 1
default Greta_maxLevel = 1

############ Jannice STATS #################################################################################
default Jannice_Corruption = 0
default Jannice_Obedience = 0
default Jannice_love = 0
default Jannice_level = 1
default Jannice_maxLevel = 1

############ Criss STATS #################################################################################
default Criss_Corruption = 0
default Criss_Obedience = 0
default Criss_love = 0
default Criss_level = 1
default Criss_maxLevel = 1

############ Luna STATS #################################################################################
default Luna_Corruption = 0
default Luna_Obedience = 0
default Luna_love = 0
default Luna_level = 1
default Luna_maxLevel = 1

############ Angeline STATS #################################################################################
default Angeline_Corruption = 0
default Angeline_Obedience = 0
default Angeline_love = 0
default Angeline_level = 1
default Angeline_maxLevel = 1

############ Scarlet STATS #################################################################################
default Scarlet_Corruption = 0
default Scarlet_Obedience = 0
default Scarlet_love = 0
default Scarlet_level = 1
default Scarlet_maxLevel = 1

############ Anna STATS #################################################################################
default Anna_Corruption = 0
default Anna_Obedience = 0
default Anna_love = 0
default Anna_level = 1
default Anna_maxLevel = 1

############ Emma STATS #################################################################################
default Emma_Corruption = 0
default Emma_Obedience = 0
default Emma_love = 0
default Emma_level = 1
default Emma_maxLevel = 1

############ Asako STATS #################################################################################
default Asako_Corruption = 0
default Asako_Obedience = 0
default Asako_love = 0
default Asako_level = 1
default Asako_maxLevel = 1

############ Rose STATS #################################################################################
default Rose_Corruption = 0
default Rose_Obedience = 0
default Rose_love = 0
default Rose_level = 1
default Rose_maxLevel = 1

############ Tanya STATS #################################################################################
default Tanya_Corruption = 0
default Tanya_Obedience = 0
default Tanya_love = 0
default Tanya_level = 1
default Tanya_maxLevel = 1

############ Sandra STATS #################################################################################
default Sandra_Corruption = 0
default Sandra_Obedience = 0
default Sandra_love = 0
default Sandra_level = 1
default Sandra_maxLevel = 1

# NVL characters are used for the phone texting
# define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
# define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
define config.mouse = {}
define config.mouse['reach'] = [("gui/reachCursor.png", 0, 0)]
define config.mouse['default'] = [("gui/defaultCursor.png", 0, 0)]
#define config.auto_movie_channel = True

init python:
    config.quit_action = ShowMenu("custom_quit_screen")
    renpy.config.movie_channel = None
    renpy.image("GoToSchoolMovieBackground1", Movie(play="Images/CarMinigame/CarMinigameDefaultBackground.webm", loop=True, group="pov_group"))

default GoToSchoolMovieBackground = Movie(play="images/CarMinigame/CarMinigameDefaultBackground.webm", channel="_movie_88")
default poolBackground = Movie(play="images/SchoolSubplace/Pool.webm", channel="_movie_93")
default faceMovie1 = Movie(play="images/CarMinigame/face1.webm", channel="_movie_89")
default faceMovie2 = Movie(play="images/CarMinigame/face2.webm", channel="_movie_90")
default faceMovie3 = Movie(play="images/CarMinigame/face3.webm", channel="_movie_91")
default faceMovie5 = Movie(play="images/CarMinigame/face5.webm", channel="_movie_92")
default firstPosition = "CarMinigame/DefaultPosition.webp"
default closer0 = "CarMinigame/DefaultPosition.webp"
default closer1 = "CarMinigame/Closer1.webp"
default closer2 = "CarMinigame/Closer2.webp"
default closer2_2 = "CarMinigame/Closer2_2.webp"
default closer2_3 = "CarMinigame/Closer2_3.webp"
default handOnThigh1 = "CarMinigame/HandOnThigh1.webp"
default handOnThigh2 = "CarMinigame/HandOnThigh2.webp"
default handOnThigh3 = "CarMinigame/HandOnThigh3.webp"
default handOnTits1 = "CarMinigame/HandOnTits1.webp"
default handOnTits2 = "CarMinigame/HandOnTits2.webp"
default handOnMouth1 = "CarMinigame/HandOnMouth1.webp"
default LapViewHandOn = "CarMinigame/LapViewHandOn.webp"
default LapViewHandOff = "CarMinigame/LapViewHandOff.webp"
default TitsViewHandOn = "CarMinigame/TitsViewHandOn.webp"
default TitsViewHandOff = "CarMinigame/TitsViewHandOff.webp"
default MouthViewHandOn = "CarMinigame/MouthViewHandOn.webp"
default MouthViewHandOff = "CarMinigame/MouthViewHandOff.webp"
default faceFrame = "CarMinigame/faceFrame.png"
default reachIcon = "CarMinigame/reach_%s.png"
default hintLocation = "CarMinigame/hintLocation.png"
default reachButtonsActive = False
default hintLocationsActive = False
default MCclose = False
default annoyed_counter = 0
default love_counter = 0
default max_annoyed = 100
default max_love = 100
default counter_timer = None
default isHandOnThigh = False
default isHandOnTits = False
default isHandOnMouth = False
default lastHandLocation = "thigh"
default is_school_time = False
default beenToSchoolOnce = False
default workInProgress = "work-in-progress.png"
default seenSandraBackstory = False

################################################################################################ chara report

default Maria_Report_Alis = False
default Maria_Report_Sophie = False
default Maria_Report_AnnaAndEmma_tits = False
default Maria_Report_AnnaAndEmma_ass = False
default Maria_Report_AnnaAndEmma = False
default Maria_Report_Criss = False
default Maria_Report_Criss_Kissed = False
default Maria_Report_Criss_didnt_Kissed = False
default Maria_Report_Isabella = False
default Maria_Report_Isabella_Kissed_Criss = False
default Maria_Report_Isabella_didnt_Kiss_Criss = False
default Maria_Report_Dorothy = False
default Maria_Report_Greta = False
default Maria_Report_Helena = False
default Maria_Report_Lola = False
default Maria_Report_Lola_Grabbed_tit = False
default Maria_Report_Lola_didnt_Grabbed_tit = False
default Maria_Report_Leya = False
default Maria_Report_Leya_Gymnastic = False
default Maria_Report_Leya_and_Lola_Naked = False
default Maria_Report_Selina = False

################################################################################################ class watched
default CrissClassroomSceneWatched = False
default AlisClassroomSceneWatched = False
default AnnaEmmaClassroomSceneWatched = False
default DorothyClassroomSceneWatched = False
default GretaClassroomSceneWatched = False
default HelenaClassroomSceneWatched = False
default IsabellaClassroomSceneWatched = False
default JanniceComplimentWatched = False
default JannicePervComplimentWatched = False
default JanniceInsultWatched = False
default LeyaClassroomSceneWatched = False
default LolaClassroomSceneWatched = False
default MariaClassroomSceneWatched = False
default SelinaClassroomSceneWatched = False
default SophieClassroomSceneWatched = False

################################################################################################ manners asked
default Sandra_apologized = False
default Sandra_saluted = False
default Sandra_asked_for_something = False
