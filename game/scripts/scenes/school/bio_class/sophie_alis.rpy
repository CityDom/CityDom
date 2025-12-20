init python:
    import random
    import re

    def prolong_name(name):
        # Split the name into syllables (simplified splitting based on vowel-consonant patterns)
        syllables = re.findall(r'[^aeiouAEIOU]*[aeiouAEIOU]+[^aeiouAEIOU]*', name)
        
        # Check the number of syllables
        syllable_count = len(syllables)

        # Single-syllable name handling
        if syllable_count == 1:
            selected_syllable = syllables[0]
            vowel_match = re.search(r'[aeiouAEIOU]', selected_syllable)
            if vowel_match:
                vowel_position = vowel_match.start()
                prolonged_vowel = selected_syllable[vowel_position] * random.randint(3, 5)
                elongated_syllable = (selected_syllable[:vowel_position] + 
                                        prolonged_vowel + 
                                        selected_syllable[vowel_position + 1:])
                syllables[0] = elongated_syllable

        # Two-syllable name handling
        elif syllable_count == 2:
            # Elongate the first vowel in both the first and second syllables
            for i in range(2):
                selected_syllable = syllables[i]
                vowel_match = re.search(r'[aeiouAEIOU]', selected_syllable)
                if vowel_match:
                    vowel_position = vowel_match.start()
                    prolonged_vowel = selected_syllable[vowel_position] * random.randint(3, 5)
                    elongated_syllable = (selected_syllable[:vowel_position] + 
                                            prolonged_vowel + 
                                            selected_syllable[vowel_position + 1:])
                    syllables[i] = elongated_syllable

        # Three or more syllables
        elif syllable_count >= 3:
            # Elongate the first vowel in each syllable
            for i in range(syllable_count):
                selected_syllable = syllables[i]
                vowel_match = re.search(r'[aeiouAEIOU]', selected_syllable)
                if vowel_match:
                    vowel_position = vowel_match.start()
                    prolonged_vowel = selected_syllable[vowel_position] * random.randint(3, 5)
                    elongated_syllable = (selected_syllable[:vowel_position] + 
                                            prolonged_vowel + 
                                            selected_syllable[vowel_position + 1:])
                    syllables[i] = elongated_syllable

        # Reconstruct the name with the elongated syllable(s)
        prolonged_name = ''.join(syllables)
        return prolonged_name

    define_images("BioClass_Sophie_Alis_Scene", "BioClass/Sophie_Alis", "BioClass_Sophie_Alis_Scene", 70)

label BioClass_Sophie_Alis_Scene:
    if Watched_BioClass_Sophie_Alis_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Sophie_Alis_Scene = True
        $ prolonged_mc_name = prolong_name(mc_name)

        scene BioClass_Sophie_Alis_Scene1 with Dissolve(0.5)
        Alis "Okay, Sophie, this is the last one..."
        scene BioClass_Sophie_Alis_Scene2 with Dissolve(0.5)
        Alis "This should be alright..."
        scene BioClass_Sophie_Alis_Scene3 with Dissolve(0.5)
        "............."
        scene BioClass_Sophie_Alis_Scene4 with Dissolve(0.5)
        Alis "So... is it good?"
        scene BioClass_Sophie_Alis_Scene5 with Dissolve(0.5)
        Sophie "No! It's horrible!"
        scene BioClass_Sophie_Alis_Scene6 with Dissolve(0.5)
        Alis "Ughhhhh... come on already!"
        Alis "We've taken like twenty photos, you have to like at least one."
        scene BioClass_Sophie_Alis_Scene7 with Dissolve(0.5)
        Sophie "Come ooooonnnn, Alis, only one more please!"
        scene BioClass_Sophie_Alis_Scene8 with Dissolve(0.5)
        Alis "No, I told you that was the last one!"
        Alis "Find someone else to take them!"
        scene BioClass_Sophie_Alis_Scene9 with Dissolve(0.5)
        Sophie "Aughh... c'mon, who am I going to ask?"
        Sophie "Isabella is good at taking photos, but she's stuck to that skeleton."
        Sophie "And Helena is even worse at taking pictures than you."
        scene BioClass_Sophie_Alis_Scene10 with Dissolve(0.5)
        ".............."
        Sophie "HA! I got an idea!" 
        Alis "....."
        Alis "Should I be worried?"
        Sophie "I will ask... uhh.. ummm..."
        Sophie "What was his name again?"
        Alis "[MC]..."
        scene BioClass_Sophie_Alis_Scene11 with Dissolve(0.5)
        Sophie "Heeeeeyyy, [prolonged_mc_name]!"
        scene BioClass_Sophie_Alis_Scene12 with Dissolve(0.5)
        Sophie "......."
        scene BioClass_Sophie_Alis_Scene13 with Dissolve(0.5)
        Sophie "Is he ignoring me?!"
        scene BioClass_Sophie_Alis_Scene14 with Dissolve(0.5)
        Alis "I think he's just sleeping..."
        scene BioClass_Sophie_Alis_Scene15 with Dissolve(0.5)
        Sophie "Heelloooooo!!! [prolonged_mc_name]!"
        scene BioClass_Sophie_Alis_Scene16 with Dissolve(0.5)
        Sophie "Ughhhh!! Is he dead?! Why isn't he waking up?!"
        scene BioClass_Sophie_Alis_Scene17 with Dissolve(0.5)
        Alis "I don't know... maybe shake him up a little..."
        scene BioClass_Sophie_Alis_Scene18 with Dissolve(0.5)
        Sophie "Eww, no, I don't wanna touch him, he's po-"
        scene BioClass_Sophie_Alis_Scene19 with Dissolve(0.5)
        Sophie "I mean... umm... uhhh... I don't wanna scare him."
        scene BioClass_Sophie_Alis_Scene20 with Dissolve(0.5)
        Alis "You want me to wake him up for you?"
        scene BioClass_Sophie_Alis_Scene21 with Dissolve(0.5)
        Sophie "Yes, pleaaaase!! Thank youuuu!!"
        scene BioClass_Sophie_Alis_Scene22 with Dissolve(0.5)
        Alis "No problem..."
        scene BlackScreen with Dissolve(1.5)
        MC "So are you just going to sit here, giving me blue balls?"
        scene BioClass_Sophie_Alis_Scene23 with Dissolve(0.5)
        MC "Don't you have anything better to do?"
        scene BioClass_Sophie_Alis_Scene25 with Dissolve(0.5)
        Mhyrorin "Blue balls? I'm not even doing anything."
        scene BioClass_Sophie_Alis_Scene23 with Dissolve(0.5)
        MC "You don't really need to do much to give me blue balls, you know?"
        scene BioClass_Sophie_Alis_Scene24 with Dissolve(0.5)
        Mhyrorin "No, I don't, you are just sexually frustrated..."
        scene BioClass_Sophie_Alis_Scene26 with Dissolve(0.5)
        MC "Of course I am, bitch, do you ever take a look at yourself?!"
        scene BioClass_Sophie_Alis_Scene27 with Dissolve(0.5)
        Mhyrorin "Heheeee, I'm pretty hot, aren't I?"
        scene BioClass_Sophie_Alis_Scene28 with Dissolve(0.5)
        MC "Yeah... fuck you..."
        MC "I don't know if I'm more pissed off at the fact that you came into the bed with those dirty shoes on!"
        MC "Didn't they teach you any manners at the succubus school or whatever the fuck you have?"
        scene BioClass_Sophie_Alis_Scene29 with Dissolve(0.5)
        MC "Oh, okay, my bad, geez, so impulsive, god..."
        scene BioClass_Sophie_Alis_Scene30 with Dissolve(0.5)
        Mhyrorin "They are cleaner than this entire room, asshole."
        Mhyrorin "Don't call me dirty."
        scene BioClass_Sophie_Alis_Scene31 with Dissolve(0.5)
        Mhyrorin "Plus, I mostly fly, so they don't even get the chance to get dirty."
        scene BlackScreen with Dissolve(1)
        "............."
        scene BioClass_Sophie_Alis_Scene32 with Dissolve(0.5)
        MC "So..... do you wanna play some video games or something?"
        scene BioClass_Sophie_Alis_Scene33 with Dissolve(0.5)
        Mhyrorin "You have a whole butt-naked succubus in your bed, and you want to play video games?!"
        Mhyrorin "God, you're so pathetic."
        scene BioClass_Sophie_Alis_Scene34 with Dissolve(0.5)
        MC "Are you gonna suck it?"
        scene BioClass_Sophie_Alis_Scene35 with Dissolve(0.5)
        Mhyrorin "Nah..."
        scene BioClass_Sophie_Alis_Scene34 with Dissolve(0.5)
        MC "Bounce on it?"
        scene BioClass_Sophie_Alis_Scene35 with Dissolve(0.5)
        Mhyrorin "Nope!"
        scene BioClass_Sophie_Alis_Scene34 with Dissolve(0.5)
        MC "At least a boobjob?"
        scene BioClass_Sophie_Alis_Scene35 with Dissolve(0.5)
        Mhyrorin "Hell naw!"
        scene BioClass_Sophie_Alis_Scene36 with Dissolve(0.5)
        MC "Then what the fuck do you want me to do?! You are the boring one!"
        scene BioClass_Sophie_Alis_Scene37 with Dissolve(0.5)
        Mhyrorin "It's not my fault that everything you think about is video games and fucking!"
        Mhyrorin "And make a side note that I said \"thinking\", cause you're not fucking anyone!!"
        scene BioClass_Sophie_Alis_Scene38 with Dissolve(0.5)
        MC "Oh, wow, look who's talking! The almighty succubus!"
        MC "Aren't you supposed to have like an army of zombies after you? Doing whatever you want?!"
        MC "But here you are, with me, doing jack shit. And why are you even here? Haven't you said that you have \"business\" to attend to at night?!"
        MC "You ran out of people to piss off?"
        MC "And besides—"
        Mhyrorin "Listen..."
        scene BioClass_Sophie_Alis_Scene39 with Dissolve(0.5)
        Mhyrorin "[MC]..."
        scene BioClass_Sophie_Alis_Scene40 with Dissolve(0.5)
        Mhyrorin "Ever since that night..."
        scene BioClass_Sophie_Alis_Scene41 with Dissolve(0.5)
        MC "You mean the one where you almost choked to death?"
        scene BioClass_Sophie_Alis_Scene42 with Dissolve(0.5)
        Mhyrorin "Yeah... that one..."
        scene BioClass_Sophie_Alis_Scene43 with Dissolve(0.5)
        MC "Yeah, what's with it?"
        scene BioClass_Sophie_Alis_Scene44 with Dissolve(0.5)
        Mhyrorin "You should be more careful about who you're around, especially girls..."
        Mhyrorin "I can't always be close to you..."
        scene BioClass_Sophie_Alis_Scene45 with Dissolve(0.5)
        MC "Huh? What do you mean? I know some girls are crazy, but they can't be worse than you..."
        scene BioClass_Sophie_Alis_Scene44 with Dissolve(0.5)
        Mhyrorin "Well... they can be way worse than me..."
        scene BioClass_Sophie_Alis_Scene48 with Dissolve(0.5)
        Mhyrorin "Ahhhh... actually... nevermind..."
        Mhyrorin "I shouldn't be stressing you with that right now..."
        Mhyrorin "Just focus on what you have to do and I will handle the rest."
        scene BioClass_Sophie_Alis_Scene46 with Dissolve(0.5)
        MC "I mean... if you're that worried about something, just tell me..."
        scene BioClass_Sophie_Alis_Scene47 with Dissolve(0.5)
        Mhyrorin "Nah, it's okay, you'll be alright..."
        Mhyrorin "I'll make sure of it."
        scene BlackScreen with Dissolve(1.5)
        "........"
        Unknown "Wake up, love, I miss you..."
        scene BioClass_Sophie_Alis_Scene49 with Dissolve(1.5)
        MC "..... huh?"
        scene BlackScreen with Dissolve(1)
        Unknown "Don't leave me all alone, please..."
        scene BioClass_Sophie_Alis_Scene50 with Dissolve(1.5)
        "............"
        scene BioClass_Sophie_Alis_Scene51 with Dissolve(0.5)
        Alis "Let's spend some more time together!"
        scene BioClass_Sophie_Alis_Scene52 with Dissolve(1.5)
        MC "Uhhh..."
        scene BioClass_Sophie_Alis_Scene53 with Dissolve(0.5)
        Sophie "He's waking up, he's waking up!"
        scene BioClass_Sophie_Alis_Scene54 with Dissolve(0.5)
        Alis "Vorgron gath myr’zith valgur nish’zar."
        scene BioClass_Sophie_Alis_Scene55 with Dissolve(0.5)
        Sophie "He woke up! Finally!"
        scene BioClass_Sophie_Alis_Scene56 with Dissolve(0.5)
        Alis "\"Finally\", huh?"
        scene BioClass_Sophie_Alis_Scene57 with Dissolve(0.5)
        Sophie "Hey, [MC], can you help me take some photos really quick? Pleaaaaaase!"
        scene BioClass_Sophie_Alis_Scene58 with Dissolve(0.5)
        "........"
        scene BioClass_Sophie_Alis_Scene57 with Dissolve(0.5)
        Sophie "Ummm... [MC]?"
        scene BioClass_Sophie_Alis_Scene59 with Dissolve(0.5)
        $ renpy.pause(0.2, hard=True)
        scene BioClass_Sophie_Alis_Scene60 with Dissolve(0.2)
        $ renpy.pause(0.2, hard=True)
        scene BioClass_Sophie_Alis_Scene61 with Dissolve(0.2)
        $ renpy.pause(0.2, hard=True)
        scene BioClass_Sophie_Alis_Scene60 with Dissolve(0.2)
        $ renpy.pause(0.2, hard=True)
        scene BioClass_Sophie_Alis_Scene62 with Dissolve(0.2)
        MC "Huh?! What?!"
        scene BioClass_Sophie_Alis_Scene63 with Dissolve(0.5)
        Sophie "[prolonged_mc_name], hellooooooo!!"
        scene BioClass_Sophie_Alis_Scene64 with Dissolve(0.5)
        MC "Yeah, photos, sure, yeah, sorry..."
        scene BioClass_Sophie_Alis_Scene65 with Dissolve(0.5)
        Sophie "Heheee, I knew I could count on you!"
        scene BioClass_Sophie_Alis_Scene66 with Dissolve(1.5)
        Sophie "So I was thinking something like this, maybe have my back a bit more arched."
        scene BioClass_Sophie_Alis_Scene67 with Dissolve(0.5)
        MC "Hmmm... yeah, that would work, but I think the background is the problem."
        MC "These plants don't have any flowers, and the trash is right behind you."
        scene BioClass_Sophie_Alis_Scene68 with Dissolve(0.5)
        Sophie "Oh. My. God. That is so true!!! I'm so glad I thought of that!"
        scene BioClass_Sophie_Alis_Scene69 with Dissolve(0.5)
        Alis "{color=#808080}*Tsk, so annoying!*{color=#808080}"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Sophie love + 2**{color=#808080}"
        "{color=#808080}**Sophie corruption + 2**{color=#808080}"
        "{color=#808080}**Alis love + 2**{color=#808080}"
        "{color=#808080}**Alis corruption + 2**{color=#808080}"
        $ Sophie_love += 2
        $ Sophie_Corruption += 2
        $ Alis_love += 2
        $ Alis_Corruption += 2
        $ check_and_update_character_stats("Sophie")
        $ check_and_update_character_stats("Alis")
        scene BioClass_Sophie_Alis_Scene70 with Dissolve(0.5)
        Maria "............................"
        $ renpy.call("GameLoop")

