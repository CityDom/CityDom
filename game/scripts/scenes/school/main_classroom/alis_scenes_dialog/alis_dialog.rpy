
label AlisClassroomScene:
    if AlisClassroomSceneWatched:
        scene AlisScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")

    scene AlisScene1 with Dissolve(0.5)
    $ Maria_Report_Alis = True
    MC "Umm.. Alis?"
    scene AlisScene2 with Dissolve(0.5)
    Alis "Yes?"
    scene AlisScene3 with Dissolve(0.5)
    MC "Do you know if... uhhh... ummm..."
    scene AlisScene4 with Dissolve(0.5)
    Alis "Is there a problem? Can I help you with something?"
    scene AlisScene5 with Dissolve(0.5)
    MC "Uhhh, no it's okay..."
    scene AlisScene4 with Dissolve(0.5)
    Alis "Okay then."
    scene AlisScene1 with Dissolve(0.5)
    MC "{color=#808080}*Holy fuck... fuck, fumbled that so hard, I can't even speak to her...*"
    MC "{color=#808080}*Maria was right, she gorgeous, but she creeps me out...*"
    $ AlisClassroomSceneWatched = True
    call stat_reward({"Alis": {"love": 2}})
