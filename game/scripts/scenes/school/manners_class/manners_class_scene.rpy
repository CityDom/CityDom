init python:
    define_images("MannersClass", "MannersClass", "MannersClass", 130)

label MannersClass_FromInside_Scene:
    scene MannersClass32 with Dissolve(0.5)
    MariaW "Listen to me, [MC], we can't keep going this way, we can't even breathe here!"
    MariaW "We have to do something about her; if I listen to all this dumb shit anymore, I will throw up."
    scene MannersClass33 with Dissolve(0.5)
    MC_whispering "Huh? What are we supposed to do?"
    scene MannersClass32 with Dissolve(0.5)
    MariaW "I don't know... let's just not come to this class anymore."
    scene MannersClass40 with Dissolve(0.5)
    MC_whispering "Uhhh... that might not be the best idea..."
    MC_whispering "Maybe I can talk to the principal about it. I'll see what I can do."
    scene MannersClass41 with Dissolve(0.5)
    MariaW "The principal? Are you crazy?"
    MariaW "That bitch might be even more of a psycho than Miss Nadal."
    MariaW "There is no way that is gonna work!"
    scene MannersClass55 with Dissolve(0.5)
    Sandra "Are you done talking, [MC]?"
    scene MannersClass56 with Dissolve(0.5)
    MC "{color=#808080}*Fuck...*{/color}"
    scene BlackScreen with Dissolve(1)
    Sandra "Come here. NOW!"
    scene MannersClass57 with Dissolve(0.5)
    Sandra "Don't you have any kind of respect for this class?"
    scene MannersClass58 with Dissolve(0.5)
    Sandra "Any manners? Any care for the future of these girls?"
    Sandra "How dare you interrupt my class like that, disturbing the attention of these poor girls like that."
    scene MannersClass59 with Dissolve(0.5)
    Sandra "But that's okay. I will put some respect into you."
    Sandra "I will teach you some politeness, how to apologize to a woman, how to correctly salute a woman, and how to properly respect a woman!"
    scene MannersClass60 with Dissolve(0.5)
    Sandra "As it does fit today's lesson pretty well!"
    scene MannersClass61 with Dissolve(0.5)
    MC "I'm sorry, Miss Nadal. I recognize my mistakes. As I grew up with only my dad around, I didn't have a clear mother figure in my life."
    MC "So all of this is quite new to me. But I don't want to be ignorant of these things anymore."
    scene MannersClass62 with Dissolve(0.5)
    MC "Could you please first show me how to respect a woman? However I envision it, my mind would still be too ignorant to a woman's needs and feelings."
    MC "And maybe with your guidance, I could get it right without offending any ladies in this classroom."
    scene MannersClass63 with Dissolve(0.5)
    Sandra "......"
    scene MannersClass64 with Dissolve(0.5)
    Sandra "At least now I know where all this rudeness is coming from. Growing up in a house without a woman is for sure a pathway to a horrible man."
    Sandra "Fine. I will show you how to do it first."
    scene MannersClass65 with Dissolve(0.5)
    MC "Thank you, ma'am!"
    jump MannersClassChoice

label MannersClassScene:
    if seenSandraBackstory == False:
        scene MannersClass2 with Dissolve(0.5)
        MC "{color=#808080}*Huh? Why don't I hear a single voice from the inside?*{/color}"
        MC "{color=#808080}*Is this not the right class?*{/color}"
        MC "{color=#808080}*Maybe the class has already started... but it's kinda early for that.*{/color}"
        MC "{color=#808080}*Should I enter?*{/color}"
        menu:
            "Enter":
                scene MannersClass1 with Dissolve(0.5)
                MC "{color=#808080}*Oh, what, the class already started?*{/color}"
                MC "{color=#808080}*I thought I was early.*{/color}"
                scene MannersClass3 with Dissolve(0.5)
                MC "{color=#808080}*What the...*{/color}"
                MC "{color=#808080}*What the fuck happened to this class?*{/color}"
                scene MannersClass4 with Dissolve(0.5)
                MC "{color=#808080}*Never mind that now, maybe she didn't notice me...*{/color}"
                MC "{color=#808080}*Or at least doesn't care enough to pay attention to me...*{/color}"
                scene MannersClass5 with Dissolve(0.5)
                Sandra "And where exactly do you think you're going, [MC]?"
                MC "{color=#808080}*Well... shit!*{/color}"
                scene MannersClass6 with Dissolve(0.5)
                Sandra "Turn around and come here right now."
                scene MannersClass7 with Dissolve(0.5)
                Sandra "What do you think you're doing coming in class this late?!"
                Sandra "Do you not have any respect for my class? Or for any of us in here?!"
                scene MannersClass8 with Dissolve(0.5)
                MC "I'm sorry ma'am, I thought it was still break time, I tried to come five minutes early."
                scene MannersClass9 with Dissolve(0.5)
                Sandra "Five minutes early?! Is that all you have to say for yourself?!"
                scene MannersClass10 with Dissolve(0.5)
                Sandra "Can you read what it says here?! This is today's lesson! And you will be a perfect example!"
                scene MannersClass11 with Dissolve(0.5)
                Sandra "So come on, apologize for interrupting my class and my lecture. And do it properly this time!"
                scene MannersClass12 with Dissolve(0.5)
                MC "I wish to say that I am really sorry about interrupting the class by being this late."
                MC "I promise that this will never happen again, and I wish that you can forgive me!"
                scene MannersClass14 with Dissolve(0.5)
                "{color=#808080}**Everyone laughs at you.**{/color}"
                scene MannersClass13 with Dissolve(0.5)
                Sandra "Mhyeah... what can I say, that was awful."
                scene MannersClass14 with Dissolve(0.5)
                MC "{color=#808080}*Man... what the fuck is this, do I have Claire as a fucking teacher?!*{/color}"
                MC "{color=#808080}*She was mean, but not that fucking mean.*{/color}"
                scene MannersClass15 with Dissolve(0.5)
                Sandra "Ugh... that's actually pathetic, but what else can I expect from a male."
                Sandra "Just go sit already, and try to keep your mouth shut."
                scene MannersClass16 with Dissolve(0.5)
                Sandra "Okay, class. So as I was saying before I got rudely interrupted by this man..."
                scene MannersClass17 with Dissolve(0.5)
                MariaW "Nice apology sissy!"
                MariaW "I don't know if I will ever be able to, but I will try to forgive you for your sin."
                MariaW "How dare you be late to a class full of strong and ambitious women?!"
                scene MannersClass18 with Dissolve(0.5)
                $ MC_whispering = mc_name + " Whispering"
                MC_whispering "Bitch, do you see me laughing?"
                MC_whispering "What the fuck was that, I wasn't even late!"
                MC_whispering "The class starts in 5 minutes."
                scene MannersClass19 with Dissolve(0.5)
                MC_whispering "And what happened to this classroom?!"
                scene MannersClass20 with Dissolve(0.5)
                MC_whispering "I mean... I understand that she wants to push a message, but hooooly fuck."
                scene MannersClass21 with Dissolve(0.5)
                MC_whispering "This feels more like a cult."
                MC_whispering "Wait... this isn't a cult, right? You're not going to hurt me, right?"
                scene MannersClass22 with Dissolve(0.5)
                MC_whispering "Because let me tell you, I will throw hands with everybody, I don't care."
                scene MannersClass23 with Dissolve(0.5)
                MariaW "No one will jump you, dumbass, calm down."
                scene MannersClass24 with Dissolve(0.5)
                Sandra "QUIET IN THE BACK, [MC_upper]! I'M NOT TELLING YOU TWICE."
                scene MannersClass25 with Dissolve(0.5)
                MC "{color=#808080}*But I wasn't even the one talking, god damn it!*{/color}"
                scene MannersClass26 with Dissolve(0.5)
                Maria "I am really sorry, Miss Nadal, that was me talking."
                Maria "I promise I won't let it happen again!"
                scene MannersClass27 with Dissolve(0.5)
                Sandra "Of course a pathetic man would let a woman take the blame for his actions."
                Sandra "Nothing surprising here."
                scene MannersClass28 with Dissolve(0.5)
                MariaW "Tsk..."
                scene MannersClass29 with Dissolve(0.5)
                MariaW "Come closer!"
                scene MannersClass30 with Dissolve(0.5)
                $ renpy.pause(0.05, hard=True)
                scene MannersClass31 with Dissolve(0.5)
                MC_whispering "What?"
                scene MannersClass32 with Dissolve(0.5)
                MariaW "Listen to me, [MC], this bitch went completely crazy!"
                MariaW "I'm not a hundred percent sure what the fuck happened, but the girls were talking about it on the group chat; you might've seen it as well."
                scene MannersClass33 with Dissolve(0.5)
                MC_whispering "Huh? What group chat? I didn't even know we had one."
                scene MannersClass34 with Dissolve(0.5)
                MariaW "Oh, what? You're not?"
                scene MannersClass32 with Dissolve(0.5)
                MariaW "Anyway, that doesn't matter now, I will add you later."
                MariaW "The thing is, this bitch is insane; have you seen the class?! What the fuck is all of this?!"
                MariaW "And not only the class, her attitude shifted as well..."
                MariaW "I mean... not shifted... more like... worsened."
                scene MannersClass35 with Dissolve(0.5)
                MariaW "From what I understood, the principal gave her full freedom to decorate the classroom however she wants."
                MariaW "So it seems she had all of this on her mind for a reason."
                scene MannersClass36 with Dissolve(0.5)
                MC_whispering "Wait... the principal just all of a sudden agreed with all of this?"
                MariaW "It wasn't really all of a sudden."
                scene MannersClass37 with Dissolve(0.5)
                MariaW "The school apparently got sponsored by some new political party or some shit like that."
                MariaW "But I don't know any other detail; it's just some dumb shit anyway."
                scene MannersClass38 with Dissolve(0.5)
                MC_whispering "Wait, so you're not agreeing with all of this?"
                scene MannersClass39 with Dissolve(0.5)
                MariaW "Huh? What made you think I'd like any of this stuff?"
                scene MannersClass40 with Dissolve(0.5)
                MC_whispering "I don't know, maybe the red hair... the glasses..."
                scene MannersClass41 with Dissolve(0.5)
                MariaW "Do you think I'm a fucking Karen?!"
                scene MannersClass42 with Dissolve(0.5)
                MC_whispering "I didn't say that, geez. And getting this mad doesn't really help your case."
                scene MannersClass43 with Dissolve(0.5)
                MC_whispering "In any case, why is Miss Nadal so fixated on all this shit? Bad childhood, or what?"
                scene MannersClass44 with Dissolve(0.5)
                MariaW "Ugh, I really have to add you to that group chat; these bitches gossip about anything and everything."
                MariaW "Miss Nadal is Leya's mom, didn't you make the connection with the name?"
                MC_whispering "Do you think I can remember all of y'all's full names? I barely know yours."
                scene MannersClass45 with Dissolve(0.5)
                MC_whispering "Not to mention, Miss Nadal didn't pass on a single one of her genes to poor Leya. What a waste."
                scene MannersClass46 with Dissolve(0.5)
                MariaW "She actually did, if you can believe that. She used to look just like Leya... Body-wise at least... the face has nothing to do with Leya."
                MariaW "She was the best gymnast in the country when she was younger, before she became a teacher."
                scene MannersClass47 with Dissolve(0.5)
                MC_whispering "Damn... what happened? She just got hella thick and couldn't do the tricks anymore?"
                scene MannersClass48 with Dissolve(0.5)
                MariaW "Nah, she was still the best after that; she retired at the peak of her career."
                MariaW "And she didn't just get thick, she developed some condition that made her store a lot of fat on the ass and legs; I don't know what it's called."
                scene MannersClass49 with Dissolve(0.5)
                MariaW "But once she got that condition, all the media started sexualizing her. They stopped even paying attention to her career as a whole."
                MariaW "At every tournament she attended, all the cameras were on her ass, barely even filming her performance."
                scene MannersClass50 with Dissolve(0.5)
                MariaW "It all slowly piled up until she couldn't stand it anymore."
                MariaW "After that, she got heavily into all this woman power shit, changed her career to education, teaching this feminism at schools."
                scene MannersClass51 with Dissolve(0.5)
                MariaW "She led Leya on the same path as her, despite all she's been through... I guess she's hoping things will go differently for her."
                scene MannersClass52 with Dissolve(0.5)
                MC_whispering "Damn, she has quite a bit of lore behind her, huh?"
                MC_whispering "But all I needed to know is that Leya has the potential to end up looking like that. You should've told me sooner."
                scene MannersClass53 with Dissolve(0.5)
                MariaW "Ughh... that's all you got out of that? Why am I even wasting my time trying to tell you shit."
                scene MannersClass54 with Dissolve(0.5)
                MC_whispering "You don't get it, Maria, getting with Leya now is like investing in bitcoin back in 2012."
                scene MannersClass55 with Dissolve(0.5)
                Sandra "Are you done talking, [MC]?"
                scene MannersClass56 with Dissolve(0.5)
                MC "{color=#808080}*Fuck...*{/color}"
                scene BlackScreen with Dissolve(1)
                Sandra "Come here. NOW!"
                scene MannersClass57 with Dissolve(0.5)
                Sandra "Don't you have any kind of respect for this class?"
                scene MannersClass58 with Dissolve(0.5)
                Sandra "Any manners? Any care for the future of these girls?"
                Sandra "How dare you interrupt my class like that, disturbing the attention of these poor girls like that."
                scene MannersClass59 with Dissolve(0.5)
                Sandra "But that's okay. I will put some respect into you."
                Sandra "I will teach you some politeness, how to apologize to a woman, how to correctly salute a woman, and how to properly respect a woman!"
                scene MannersClass60 with Dissolve(0.5)
                Sandra "As it does fit today's lesson pretty well!"
                scene MannersClass61 with Dissolve(0.5)
                MC "I'm sorry, Miss Nadal. I recognize my mistakes. As I grew up with only my dad around, I didn't have a clear mother figure in my life."
                MC "So all of this is quite new to me. But I don't want to be ignorant of these things anymore."
                scene MannersClass62 with Dissolve(0.5)
                MC "Could you please first show me how to respect a woman? However I envision it, my mind would still be too ignorant of a woman's needs and feelings."
                MC "And maybe with your guidance, I could get it right without offending any ladies in this classroom."
                scene MannersClass63 with Dissolve(0.5)
                Sandra "......"
                scene MannersClass64 with Dissolve(0.5)
                Sandra "At least now I know where all this rudeness is coming from. Growing up in a house without a woman is for sure a pathway to a horrible man."
                Sandra "Fine. I will show you how to do it first."
                scene MannersClass65 with Dissolve(0.5)
                MC "Thank you, ma'am!"
                jump MannersClassChoice
            "Don't":
                MC "{color=#808080}*Fuck it, if I'm late to this class the teacher will go crazy, I better not enter at all.*{/color}"
                $ Location = "SchoolEntrance"
                $ renpy.call("GameLoop")

    elif seenSandraBackstory == True:
        scene MannersClass2 with Dissolve(0.5)
        MC "{color=#808080}*Huh? Why don't I hear a single voice from the inside?*{/color}"
        MC "{color=#808080}*Is this not the right class?*{/color}"
        MC "{color=#808080}*Maybe the class has already started... but it's kinda early for that.*{/color}"
        MC "{color=#808080}*Should I enter?*{/color}"
        menu:
            "Enter":
                scene MannersClass1 with Dissolve(0.5)
                MC "{color=#808080}*Oh, what, the class already started?*{/color}"
                MC "{color=#808080}*I thought I was early.*{/color}"
                scene MannersClass3 with Dissolve(0.5)
                MC "{color=#808080}*She still has all this shit on the walls...*{/color}"
                scene MannersClass4 with Dissolve(0.5)
                MC "{color=#808080}*Anyway, let's get to my chair, maybe she didn't notice me...*{/color}"
                MC "{color=#808080}*Or at least doesn't care enough to pay attention to me...*{/color}"
                scene MannersClass5 with Dissolve(0.5)
                Sandra "And where exactly do you think you're going, [MC]?"
                MC "{color=#808080}*Well... shit!*{/color}"
                scene MannersClass6 with Dissolve(0.5)
                Sandra "Turn around and come here right now."
                scene MannersClass7 with Dissolve(0.5)
                Sandra "What do you think you're doing coming in class this late?!"
                Sandra "Do you not have any respect for my class? Or for any of us in here?!"
                scene MannersClass8 with Dissolve(0.5)
                MC "I'm sorry ma'am, I thought it was still break time, I tried to come five minutes early."
                scene MannersClass9 with Dissolve(0.5)
                Sandra "Five minutes early?! Is that all you have to say for yourself?!"
                scene MannersClass10 with Dissolve(0.5)
                Sandra "Can you read what it says here?! This is today's lesson! And you will be a perfect example!"
                scene MannersClass11 with Dissolve(0.5)
                Sandra "So come on, apologize for interrupting my class and my lecture. And do it properly this time!"
                scene MannersClass12 with Dissolve(0.5)
                MC "I wish to say that I am really sorry about interrupting the class by being this late."
                MC "I promise that this will never happen again, and I wish that you can forgive me!"
                scene MannersClass14 with Dissolve(0.5)
                "{color=#808080}**Everyone laughs at you.**{/color}"
                scene MannersClass13 with Dissolve(0.5)
                Sandra "Mhyeah... what can I say, that was awful."
                scene MannersClass14 with Dissolve(0.5)
                MC "{color=#808080}*Man... what the fuck is this, do I have Claire as a fucking teacher?!*{/color}"
                MC "{color=#808080}*She was mean, but not that fucking mean.*{/color}"
                scene MannersClass15 with Dissolve(0.5)
                Sandra "Ugh... that's actually pathetic, but what else can I expect from a male."
                Sandra "Just go sit already, and try to keep your mouth shut."
                scene MannersClass16 with Dissolve(0.5)
                Sandra "Okay, class. So as I was saying before I got rudely interrupted by this man..."
                scene MannersClass17 with Dissolve(0.5)
                MariaW "Nice apology sissy!"
                MariaW "I don't know if I will ever be able to, but I will try to forgive you for your sin."
                MariaW "How dare you be late to a class full of strong and ambitious women?!"
                scene MannersClass18 with Dissolve(0.5)
                $ MC_whispering = mc_name + " Whispering"
                MC_whispering "Bitch, do you see me laughing?"
                MC_whispering "What the fuck was that, I wasn't even late!"
                MC_whispering "The class starts in five minutes."
                scene MannersClass22 with Dissolve(0.5)
                MC_whispering "Does she just hate me, or what?"
                scene MannersClass23 with Dissolve(0.5)
                MariaW "Nah, she's just completely crazy."
                scene MannersClass24 with Dissolve(0.5)
                Sandra "QUIET IN THE BACK, [MC_upper]! I'M NOT TELLING YOU TWICE."
                scene MannersClass25 with Dissolve(0.5)
                MC "{color=#808080}*But I wasn't even the one talking, god damn it!*{/color}"
                scene MannersClass26 with Dissolve(0.5)
                Maria "I am really sorry, Miss Nadal, that was me talking."
                Maria "I promise I won't let it happen again!"
                scene MannersClass27 with Dissolve(0.5)
                Sandra "Of course a pathetic man would let a woman take the blame for his actions."
                Sandra "Nothing surprising here."
                scene MannersClass28 with Dissolve(0.5)
                MariaW "Tsk..."
                scene MannersClass29 with Dissolve(0.5)
                MariaW "Come closer!"
                scene MannersClass30 with Dissolve(0.5)
                $ renpy.pause(0.05, hard=True)
                scene MannersClass31 with Dissolve(0.5)
                MC_whispering "What?"
                scene MannersClass32 with Dissolve(0.5)
                MariaW "Listen to me, [MC], this bitch went completely crazy!"
                MariaW "We have to do something about her; if I listen to all this dumb shit anymore, I will throw up."
                scene MannersClass33 with Dissolve(0.5)
                MC_whispering "Huh? What are we supposed to do?"
                scene MannersClass32 with Dissolve(0.5)
                MariaW "I don't know... let's just not come to this class anymore."
                scene MannersClass40 with Dissolve(0.5)
                MC_whispering "Uhhh... that might not be the best idea..."
                MC_whispering "Maybe I can talk to the principal about it. I'll see what I can do."
                scene MannersClass41 with Dissolve(0.5)
                MariaW "The principal? Are you crazy?"
                MariaW "That bitch might be even more of a psycho than Miss Nadal."
                MariaW "There is no way that is gonna work!"
                scene MannersClass55 with Dissolve(0.5)
                Sandra "Are you done talking, [MC]?"
                scene MannersClass56 with Dissolve(0.5)
                MC "{color=#808080}*Fuck...*{/color}"
                scene BlackScreen with Dissolve(1)
                Sandra "Come here. NOW!"
                scene MannersClass57 with Dissolve(0.5)
                Sandra "Don't you have any kind of respect for this class?"
                scene MannersClass58 with Dissolve(0.5)
                Sandra "Any manners? Any care for the future of these girls?"
                Sandra "How dare you interrupt my class like that, disturbing the attention of these poor girls like that."
                scene MannersClass59 with Dissolve(0.5)
                Sandra "But that's okay. I will put some respect into you."
                Sandra "I will teach you some politeness, how to apologize to a woman, how to correctly salute a woman, and how to properly respect a woman!"
                scene MannersClass60 with Dissolve(0.5)
                Sandra "As it does fit today's lesson pretty well!"
                scene MannersClass61 with Dissolve(0.5)
                MC "I'm sorry, Miss Nadal. I recognize my mistakes. As I grew up with only my dad around, I didn't have a clear mother figure in my life."
                MC "So all of this is quite new to me. But I don't want to be ignorant of these things anymore."
                scene MannersClass62 with Dissolve(0.5)
                MC "Could you please first show me how to respect a woman? However I envision it, my mind would still be too ignorant of a woman's needs and feelings."
                MC "And maybe with your guidance, I could get it right without offending any ladies in this classroom."
                scene MannersClass63 with Dissolve(0.5)
                Sandra "......"
                scene MannersClass64 with Dissolve(0.5)
                Sandra "At least now I know where all this rudeness is coming from. Growing up in a house without a woman is for sure a pathway to a horrible man."
                Sandra "Fine. I will show you how to do it first."
                scene MannersClass65 with Dissolve(0.5)
                MC "Thank you, ma'am!"
                jump MannersClassChoice
            "Don't":
                MC "{color=#808080}*Fuck it, if I'm late to this class the teacher will go crazy, I better not enter at all.*{/color}"
                $ renpy.call("GameLoop")

label MannersClassChoice:
    scene MannersClass77 with Dissolve(0.5)
    menu:
        "Apologize" if not Sandra_apologized:
            scene MannersClass65 with Dissolve(0.5)
            MC "I feel like first and foremost I need to learn how to properly apologize to a woman; could you please show me?"
            scene MannersClass66 with Dissolve(0.5)
            Sandra "Ugh, fine, I guess the girls will get to learn from this as well."
            scene MannersClass67 with Dissolve(0.5)
            Sandra "Alright girls, pay attention because I'm not going to do it twice!"
            scene MannersClass68 with Dissolve(0.5)
            Sandra "Before we start, keep this in mind: a girl should never apologize to a man!"
            Sandra "A girl could never be at fault for doing something to a male. What I'm doing here is just for demonstration!"
            scene MannersClass69 with Dissolve(0.5)
            Sandra "Okay, first of all, hands behind your back to show that you are passive and vulnerable."
            scene MannersClass70 with Dissolve(0.5)
            Sandra "After which, you lower your gaze to show shame and regret, to show that you are not deserving of looking the woman in the eyes."
            scene MannersClass71 with Dissolve(0.5)
            Sandra "Then you lower your whole body to show that you are under the woman, show that she is the dominant one."
            scene MannersClass72 with Dissolve(0.5)
            Sandra "Then, when you've made sure of all those things, and let her know that she is over you, you slowly raise your head."
            Sandra "And look her in the eyes to show her that you are sincere and you accept your guilt."
            scene MannersClass73 with Dissolve(0.5)
            Sandra "Now, a woman should ask for forgiveness!"
            Sandra "But a man shouldn't ever have the arrogance to ask a woman for something after he did something to her."
            scene MannersClass74 with Dissolve(0.5)
            Sandra "If you could ever gather the strength to forgive me, even if I don't deserve it, I would be deeply thankful!"
            scene MannersClass75 with Dissolve(0.5)
            Sandra "And this is basically how to do it. Of course, it depends on who you're apologizing to and so on."
            scene MannersClass76 with Dissolve(0.5)
            Sandra "What I showed you mostly applies to rude, ignorant men, like [MC] over here, and I thought he needed to learn it the most."
            scene MannersClass78 with Dissolve(0.5)
            Sandra "What other lesson do I need to put in that hard head of yours?"
            # ! Convert slowly to dogeza
            $ Sandra_apologized = True
            jump MannersClassChoice
        "Apologize" if Sandra_apologized:
            "{color=#808080}**I already asked her to show me that**{/color}"
            jump MannersClassChoice
        "Salute" if not Sandra_saluted:
            scene MannersClass79 with Dissolve(0.5)
            MC "I think saluting a woman would help me a lot; it's the first thing we do in a conversation and the first thing where I could go wrong."
            scene MannersClass80 with Dissolve(0.5)
            Sandra "Uhh... okay... I guess a man can't even do this much correctly."
            scene MannersClass81 with Dissolve(0.5)
            Sandra "You girls can pay attention as well, but I expect you to already know this much."
            Sandra "Since now we have a boy in our classroom I have to teach him as well, I can't leave students behind, so sorry if this might be boring to you."
            scene MannersClass82 with Dissolve(0.5)
            Sandra "So first of all you put on a smile, to show that you are happy to meet her."
            scene MannersClass83 with Dissolve(0.5)
            Sandra "And you do a basic gesture of waving your hand."
            scene MannersClass84 with Dissolve(0.5)
            Sandra "Waving your hand is important because it conveys friendliness and recognition."
            scene MannersClass85 with Dissolve(0.5)
            Sandra "It is believed that the gesture has roots all the way back in medieval times."
            Sandra "And it was used to demonstrate that you are unarmed and pose no threat."
            scene MannersClass86 with Dissolve(0.5)
            Sandra "So it's important to show openness and show yourself to the other person."
            Sandra "Especially for girls, who should be proud of their own body and figure, as all of them are beautiful!"
            scene MannersClass76 with Dissolve(0.5)
            Sandra "And that's pretty much the gist of it."
            scene MannersClass78 with Dissolve(0.5)
            Sandra "Anything else?"
            $ Sandra_saluted = True
            jump MannersClassChoice
        "Salute" if Sandra_saluted:
            "{color=#808080}**I already asked her to show me that**{/color}" 
            jump MannersClassChoice          
        "Ask for something" if not Sandra_asked_for_something:
            scene MannersClass79 with Dissolve(0.5)
            MC "I wanted to know how to ask something from a woman; I don't want to look too demanding or like I am entitled to a favor."
            scene MannersClass87 with Dissolve(0.5)
            Sandra "Hmm... that's surprisingly thoughtful of you, [MC]."
            Sandra "Okay, I'll show you!"
            scene MannersClass88 with Dissolve(0.5)
            Sandra "Okay, girls, pay attention."
            Sandra "I will show you how to correctly ask for something."
            scene MannersClass89 with Dissolve(0.5)
            Sandra "In general, a man should never ask something from a woman, since they already took enough from us."
            Sandra "But since they are helpless without us, they can only appeal to our kindness."
            scene MannersClass90 with Dissolve(0.5)
            Sandra "So if they are going to do it anyway, I better teach them to do it right."
            Sandra "And you girls can pay attention as well, since most of it can apply to you too."
            scene MannersClass91 with Dissolve(0.5)
            Sandra "So first of all, you should drop any kind of arrogance or entitlement that you have."
            Sandra "You have to show her that you want to ask for something, not demand it."
            Sandra "Then you have to formulate your request well; keep in mind, you are the one in need."
            scene MannersClass92 with Dissolve(0.5)
            Sandra "Do you think that... uhh... do you think that you could please give me some water?"
            scene MannersClass93 with Dissolve(0.5)
            Sandra "I know that it is rude to ask that of you, but-"
            scene MannersClass94 with Dissolve(0.5)
            Sandra "It's also adequate to show the interlocutor the need you have for said thing."
            Sandra "You need to show that you not only want it just because, but you actually need it."
            scene MannersClass95 with Dissolve(0.5)
            Sandra "I know that it is rude to ask that of you-"
            Sandra "Buh, buh, mah mouf is sho dry... mah tung too... look!"
            scene MannersClass96 with Dissolve(0.5)
            Sandra "Could you pleash, pleash lend me shome water?"
            scene MannersClass97 with Dissolve(0.5)
            Sandra "Now, if the person still refuses you, you don't continue, as it's very rude to keep trying."
            Sandra "But if you are really really desperate, as men usually are, though rarely it might apply to girls as well."
            scene MannersClass98 with Dissolve(0.5)
            Sandra "You have two choices. And I will say it now."
            Sandra "As a girl, you should never go for these two choices if you somehow end up in the awful position of asking something from a man."
            "You can either offer something in return or really beg for it."
            scene MannersClass99 with Dissolve(0.5)
            Sandra "A woman should never beg for something from a man; what I do here is a demonstration that will show you, and help [MC] to see how it's done."
            scene MannersClass100 with Dissolve(0.5)
            Sandra "Please, please lend me some water, I am really dehydrated, and I don't feel so well."
            Sandra "I promise, I will do anything for it, please!"
            scene MannersClass101 with Dissolve(0.5)
            Sandra "Anything you need, just give it to me, please!"
            scene MannersClass102 with Dissolve(0.5)
            Sandra "Ugh, that was so disgusting..."
            Sandra "But I gotta do what I gotta do to teach this generation."
            scene MannersClass103 with Dissolve(0.5)
            Sandra "And this is pretty much all there is to it."
            Sandra "Again, this explanation was more for [MC]."
            scene MannersClass76 with Dissolve(0.5)
            Sandra "But you girls can see as well what you should expect from a man."
            scene MannersClass78 with Dissolve(0.5)
            Sandra "Anything else that you think you should know? Besides everything, of course."
            $ Sandra_asked_for_something = True
            jump MannersClassChoice
        "Ask for something" if Sandra_asked_for_something:
            "{color=#808080}**I already asked her to show me that**{/color}"
            jump MannersClassChoice
        "That was all":
            scene MannersClass79 with Dissolve(0.5)
            MC "That was all, Miss Nadal, thank you very much!"
            scene MannersClass104 with Dissolve(0.5)
            Sandra "Yeah, no problem, I'm just doing my job."
            scene MannersClass105 with Dissolve(0.5)
            Sandra "Now go back to your seat. And I don't want to hear another word from you."
            scene MannersClass106 with Dissolve(0.5)
            Sandra "Okay class, we can continue."
            call stat_reward({"Sandra": {"love": 2, "corruption": 2}}, return_to=None)
            $ seenSandraBackstory = True
            $ Sandra_apologized = False
            $ Sandra_saluted = False
            $ Sandra_asked_for_something = False
            $ advance_time_or_sleep()
