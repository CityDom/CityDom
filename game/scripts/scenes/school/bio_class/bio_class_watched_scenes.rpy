default Watched_BioClass_Anna_Emma_Scene = False
default Watched_BioClass_Dorothy_Scene = False
default Watched_BioClass_IsaCrissHelena_Scene = False
default Watched_BioClass_Lola_Leya_Scene = False
default Watched_BioClass_Maria_Scene = False
default Watched_BioClass_Selina_Greta_Scene = False
default Watched_BioClass_Sophie_Alis_Scene = False

# Define a function to reset the BioClass scene variables
init python:
    def reset_bio_class_scenes():
        global Watched_BioClass_Anna_Emma_Scene
        global Watched_BioClass_Dorothy_Scene
        global Watched_BioClass_IsaCrissHelena_Scene
        global Watched_BioClass_Lola_Leya_Scene
        global Watched_BioClass_Maria_Scene
        global Watched_BioClass_Selina_Greta_Scene
        global Watched_BioClass_Sophie_Alis_Scene
        
        Watched_BioClass_Anna_Emma_Scene = False
        Watched_BioClass_Dorothy_Scene = False
        Watched_BioClass_IsaCrissHelena_Scene = False
        Watched_BioClass_Lola_Leya_Scene = False
        Watched_BioClass_Maria_Scene = False
        Watched_BioClass_Selina_Greta_Scene = False
        Watched_BioClass_Sophie_Alis_Scene = False
