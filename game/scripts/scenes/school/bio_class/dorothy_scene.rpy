init python:
    define_images("Dorothy_Scene", "BioClass/Dorothy", "Dorothy_Scene", 60)

label BioClass_Dorothy_Scene:
    if Watched_BioClass_Dorothy_Scene:
        MC "{color=#808080}*I already talked to her...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Dorothy_Scene = True
        scene Dorothy_Scene1 with Dissolve(0.5)
        MC "Hey, Dorothy, what's up? What are you writing now?"
        scene Dorothy_Scene2 with Dissolve(0.5)
        Dorothy "I almost finished the homework that we got. I spent all my time reading last night and I forgot about it."
        Dorothy "And as class president, I can't show my face without my homework done."
        scene Dorothy_Scene3 with Dissolve(0.5)
        MC "We had homework?"
        scene Dorothy_Scene4 with Dissolve(0.5)
        Dorothy "Yes, [MC], we had homework. We always have."
        scene Dorothy_Scene5 with Dissolve(0.5)
        Dorothy "And you should seriously start doing it."
        Dorothy "The class's reputation is my reputation as well."
        Dorothy "And I don't want the teachers to think I'm not capable of doing my job! What if they replace me?!"
        scene Dorothy_Scene6 with Dissolve(0.5)
        MC "Yeah, yeah, I'll do it, don't worry about it."
        scene Dorothy_Scene7 with Dissolve(0.5)
        MC "And why do you worry about that? There is no girl in this school who would do a better job than you, let alone in this class."
        scene Dorothy_Scene8 with Dissolve(0.5)
        Dorothy "...."
        MC "Anyway, what are you drawing there? That looks so cool!"
        Dorothy "...."
        scene Dorothy_Scene9 with Dissolve(0.5)
        MC "Huh? Dorothy? Helloooo!"
        scene Dorothy_Scene8 with Dissolve(0.5)
        Dorothy "Huh..."
        scene Dorothy_Scene10 with Dissolve(0.5)
        Dorothy "Oh, what? Yeah, right, the drawing. What's with it?"
        scene Dorothy_Scene11 with Dissolve(0.5)
        MC "It's really cool! Did you make it? Can I have a closer look?"
        scene Dorothy_Scene12 with Dissolve(0.5)
        Dorothy "Uhhh, yeah, sure."
        scene Dorothy_Scene13 with Dissolve(0.5)
        MC "Really? Thanks!"
        scene Dorothy_Scene14 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene Dorothy_Scene17 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene Dorothy_Scene15 with Dissolve(1)
        Dorothy "{size=25}Oh, I thought you'd just take the notebook closer to you...{/size}" 
        scene Dorothy_Scene16 with Dissolve(0.5)
        MC "What?"
        scene Dorothy_Scene18 with Dissolve(0.5)
        Dorothy "N-nothing, here you go."
        scene Dorothy_Scene19 with Dissolve(0.5)
        Dorothy "You can have a closer look."
        scene Dorothy_Scene20 with Dissolve(0.5)
        MC "Daaaaamn, I didn't know you could draw that well! This looks amazing!"
        scene Dorothy_Scene21 with Dissolve(0.5)
        Dorothy "Well... Miss Petal always speaks highly of me."
        Dorothy "But she grades my work right after yours, and by that time, you always get her mad enough to tell you to get out of the class."
        Dorothy "I don't even know what you're doing. Do you really draw that badly?"
        scene Dorothy_Scene22 with Dissolve(0.5)
        MC "Eh, me and Miss Petal like different art styles."
        MC "But I'm sure she'll grow to like it!"
        scene Dorothy_Scene23 with Dissolve(0.5)
        MC "Maybe I can show it to you at some point, and you can grade me as well."
        MC "With how good you draw, maybe you could give me some advice!"
        scene Dorothy_Scene24 with Dissolve(0.5)
        Dorothy "Yeah, sure, I'd like that, especially if it will help you with your grades!"
        scene Dorothy_Scene25 with Dissolve(0.5)
        MC "Nice, it's a deal!"
        MC "Okay then, I'll leave you to it. I'll try to cop- uh, um, do the homework as well before the class starts!"
        scene Dorothy_Scene26 with Dissolve(0.5)
        Dorothy "Okay, [MC], good luck!"
        call stat_reward({"Dorothy": {"love": 2, "corruption": 2}})
