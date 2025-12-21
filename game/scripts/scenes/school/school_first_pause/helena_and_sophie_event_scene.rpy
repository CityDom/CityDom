init python:
    define_images("HelenaAndSophieEventScene", "SchoolFirstPause/HelenaAndSophieEventScene", "HelenaAndSophieEventScene", 60)

label HelenaAndSophieFirstPauseScene:
    scene HelenaAndSophieEventScene1 with Dissolve(0.5)
    MC "Hey girls!"
    scene HelenaAndSophieEventScene2 with Dissolve(0.5)
    Helena "Hey, [MC]!!"
    Sophie "Heeeey!"
    scene HelenaAndSophieEventScene3 with Dissolve(0.5)
    Helena "Whatcha doin'?"
    scene HelenaAndSophieEventScene4 with Dissolve(0.5)
    menu:
        "Talk":
            MC "I'm just walking around, trying to learn the school better."
            MC "How about you?"
            scene HelenaAndSophieEventScene3 with Dissolve(0.5)
            Helena "Well, nothing special, just walking around, loosening our legs a little. The chairs in class are killing me!"
            scene HelenaAndSophieEventScene5 with Dissolve(0.5)
            Helena "Listening to Sophie complain about the school uniform for the millionth time."
            scene HelenaAndSophieEventScene6 with Dissolve(0.5)
            Sophie "But it's true! We dress like we are in church school!"
            Sophie "And the skin can hardly breath in them, not to talk about these ugly skirts."
            scene HelenaAndSophieEventScene7 with Dissolve(0.5)
            MC "Who is making the dress code?"
            MC "Can't you just bring it up to them?"
            scene HelenaAndSophieEventScene8 with Dissolve(0.5)
            Sophie "It's the school counselors, she is dead set on it!"
            scene HelenaAndSophieEventScene9 with Dissolve(0.5)
            Helena "It's actually the principal."
            scene HelenaAndSophieEventScene8 with Dissolve(0.5)
            Sophie "Yeah, that's what I said, the principal!"
            scene HelenaAndSophieEventScene10 with Dissolve(0.5)
            MC "I don't know, I think they look alright."
            scene HelenaAndSophieEventScene8 with Dissolve(0.5)
            Sophie "What do you mean they look alright?!"
            scene HelenaAndSophieEventScene11 with Dissolve(0.5)
            Sophie "Look at this! My chest looks like it's about to pop off"
            scene HelenaAndSophieEventScene12 with Dissolve(0.5)
            Helena "Hmmm... you're right"
            scene HelenaAndSophieEventScene13 with Dissolve(0.5)
            Helena "Mine are pretty stiff as well... this shirt is doing its best to compress them..."
            scene HelenaAndSophieEventScene14 with Dissolve(0.5)
            Sophie "See?! I told you! This uniform sucks!"
            scene HelenaAndSophieEventScene15 with Dissolve(0.5)
            $ Maria_Report_Helena = True
            $ Maria_Report_Sophie = True
            menu:
                "Check for yourself":
                    MC "Hmmmmm... I don't know... let me check as well."
                    scene HelenaAndSophieEventScene16 with Dissolve(0.5)
                    Sophie "Absolutely not!! "
                    scene HelenaAndSophieEventScene17 with Dissolve(0.5)
                    Helena "I think you got a bit too comfortable with this conversation, [MC]!"
                    Helena "We're going to class, see ya!"
                    call stat_reward({"Helena": {"love": -5, "corruption": 2}, "Sophie": {"love": -5, "corruption": 2}}, return_to=None)
                    $ advance_time_or_sleep()
                "Agree with them":
                    MC "You girls are right, and it's a shame to have them compressed."
                    scene HelenaAndSophieEventScene18 with Dissolve(0.5)
                    MC "You should be able to walk around in something that doesn't constrain your beauty!"
                    MC "I will see what I can do about it!"
                    scene HelenaAndSophieEventScene19 with Dissolve(0.5)
                    Sophie "Really?! That would be awesome!"
                    scene HelenaAndSophieEventScene20 with Dissolve(0.5)
                    Helena "Uhhh, yeah, I'm not sure if it's possible..."
                    Helena "But thank you for trying!"
                    scene HelenaAndSophieEventScene18 with Dissolve(0.5)
                    MC "Alright girls, see you around then!"
                    scene HelenaAndSophieEventScene19 with Dissolve(0.5)
                    Sophie "Byeee!"
                    scene HelenaAndSophieEventScene20 with Dissolve(0.5)
                    Helena "See ya!"
                    call stat_reward({"Helena": {"love": 2}, "Sophie": {"love": 2}}, return_to=None)
                    $ advance_time_or_sleep()
        "Leave":
            MC "I was just passing by, see you in class!"
            scene HelenaAndSophieEventScene3 with Dissolve(0.5)
            Helena "Okay, see you!"
            $ renpy.call("GameLoop")

