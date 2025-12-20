init python:
    define_images("DorothyEventScene", "SchoolFirstPause/DorothyEventScene", "DorothyEventScene", 60)

label DorothyFirstPauseScene:
    scene DorothyEventScene1 with Dissolve(0.5)
    MC "Hey Dorothy, what are you doing?"
    scene DorothyEventScene2 with Dissolve(0.5)
    Dorothy "Oh, hey, [MC]!"
    scene DorothyEventScene3 with Dissolve(0.5)
    Dorothy "I'm searching for a book for Miss Thompson, she wanted me to bring it to her."
    scene DorothyEventScene4 with Dissolve(0.5)
    MC "So you're just wasting your break looking for some book?"
    scene DorothyEventScene5 with Dissolve(0.5)
    Dorothy "Of course I do, this is what it means to be class president!"
    Dorothy "And besides, I get to find a couple of books for myself. They are quite interesting, you should try, maybe it would raise your grades up a bit."
    scene DorothyEventScene6 with Dissolve(0.5)
    MC "But I do read a lot as well! What kind of books are you into?"
    scene DorothyEventScene7 with Dissolve(0.5)
    Dorothy "Really? You do?!"
    Dorothy "Well, I read a lot of philosophy, physics studies and autobiographies!"
    Dorothy "Kant's 'Critique of Pure Wisdom', Neetchz's 'Thus Spoke Zaranthustra', and Hawkkins' 'A Short History of Time' are my favorites!"
    scene DorothyEventScene8 with Dissolve(0.5)
    MC "No way! Neetchz is along my favorites as well!"
    MC "{color=#808080}*I didn't understand a single word she just said...*"
    scene DorothyEventScene9 with Dissolve(0.5)
    Dorothy "Really?!?! I haven't found anyone else who is my age and likes Neetchz!"
    Dorothy "What else do you read?! I wan't to try it!"
    scene DorothyEventScene10 with Dissolve(0.5)
    MC "Well... I'm not sure if it's your type, so..."
    scene DorothyEventScene9 with Dissolve(0.5)
    Dorothy "It doesn't matter! Just tell me, I would love to check it out!"
    scene DorothyEventScene10 with Dissolve(0.5)
    MC "Okay... well... you can try Asanagi... or... uhhh.. ShindoL or Kei Mizuryu!"
    scene DorothyEventScene11 with Dissolve(0.5)
    Dorothy "Hmmm...They sound Japanese... Is their work translated?"
    scene DorothyEventScene12 with Dissolve(0.5)
    MC "Yeah, most of it, but I doubt you will find their work in a library, it's quite niche."
    MC "But you can try looking it up online."
    scene DorothyEventScene13 with Dissolve(0.5)
    Dorothy "Okay, I will make sure to check it out! Thank you for the recommendations!!"
    Dorothy "But now I have to find that book for Miss Thompson, so maybe we can talk about more books later!"
    scene DorothyEventScene14 with Dissolve(0.5)
    MC "Whenever you have the time, I can't wait to hear what you have to say about my recommendations!"
    MC "See you in class!"
    scene DorothyEventScene13 with Dissolve(0.5)
    Dorothy "I promise I will check them out! See ya!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**Dorothy love + 2**{color=#808080}"
    "{color=#808080}**Dorothy corruption + 2**{color=#808080}"
    "{color=#808080}**Dorothy obedience + 2**{color=#808080}"
    $ Dorothy_love = Dorothy_love + 2
    $ Dorothy_Corruption = Dorothy_Corruption + 2
    $ Dorothy_Obedience = Dorothy_Obedience + 2
    $ Maria_Report_Dorothy = True
    $ check_and_update_character_stats("Dorothy")
    $ advance_time_or_sleep()