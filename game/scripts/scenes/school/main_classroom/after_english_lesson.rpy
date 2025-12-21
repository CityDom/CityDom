init python:
    define_images("AfterEnglishLessonScene", "EnglishClassScreen/AfterEnglishLesson", "AfterEnglishLessonScene", 50)

label AfterEnglishLessonFail:
    scene AfterEnglishLessonScene1 with Dissolve(0.5)
    Maria "What the fuck are you doing?!"
    scene AfterEnglishLessonScene2 with Dissolve(0.5)
    MC "I'm taking advantage of a girl sleeping?"
    Maria "......"
    MC "Are you upset?"
    scene AfterEnglishLessonScene1 with Dissolve(0.5)
    Maria "I'll cut your fucking hand off."
    scene AfterEnglishLessonScene3 with Dissolve(0.5)
    MC "Understood."
    scene DropPenScene29 with Dissolve(0.5)
    Jannice "Maria! [MC]! Stop talking and pay attention!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}*An hour goes by.*"
    scene DropPenScene29 with Dissolve(0.5)
    Jannice "And that's all for today!"
    Jannice "Make sure to do your homework!"
    scene DropPenScene30 with Dissolve(0.5)
    Jannice "See you after the break!"
    call stat_reward({"Maria": {"love": -5, "corruption": -5, "obedience": -5}}, return_to=None)
    $ Location = "mainclassroom"
    $ advance_time_or_sleep()


style heart_text:
    font "arial-unicode-ms.ttf"
    size 40  # You can adjust the size as needed


label MariaFinishLessonSuccess:
    scene AfterEnglishLessonScene4 with Dissolve(0.5)
    Maria "{color=#808080}*{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️{/color}{/font}Ahhhhh{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️{/color}{/font}*"
    Maria "{color=#808080}*{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️❤️{/color}{/font}I was hoping that I was better than this, God damn it!!{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️❤️{/color}{/font}*"
    Maria "{color=#808080}*{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️❤️❤️{/color}{/font}But I'm already dripping wet!{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️❤️❤️{/color}{/font}*"
    scene AfterEnglishLessonScene5 with Dissolve(0.5)
    Maria "*What are you doing?!*"
    Maria "*I hope you did not forget our deal.*"
    Maria "*First you get some girls that we can share.*"
    Maria "*And then you can have your way with me*"
    scene AfterEnglishLessonScene6 with Dissolve(0.5)
    MC "But you seem to enjoy it."
    scene AfterEnglishLessonScene5 with Dissolve(0.5)
    Maria "Don't fuck with me [MC]."
    Maria "{color=#808080}*{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️{/color}{/font}Ahhhhh{font=dejavu_sans_oblique.ttf}{color=#FF0000}❤️❤️{/color}{/font}*"
    Maria "I'll cut your dick off!"
    scene AfterEnglishLessonScene6 with Dissolve(0.5)
    MC "Okay, sorry, Geez..."
    scene DropPenScene29 with Dissolve(0.5)
    Jannice "Maria! [MC]! Stop talking and pay attention!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}*An hour goes by.*"
    scene DropPenScene29 with Dissolve(0.5)
    Jannice "And that's all for today!"
    Jannice "Make sure to do your homework!"
    scene DropPenScene30 with Dissolve(0.5)
    Jannice "See you after the break!"
    call stat_reward({"Maria": {"love": 5, "corruption": 5, "obedience": 5}}, return_to=None)
    $ Location = "mainclassroom"
    $ advance_time_or_sleep()