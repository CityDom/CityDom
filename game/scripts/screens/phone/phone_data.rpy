# Conversation data and phone emoji assets.

init python:
    SPEAKER_LEFT = "left"
    SPEAKER_RIGHT = "right"

    def msg_text(speaker, text):
        return {"speaker": speaker, "text": text}

    def msg_image(speaker, image):
        return {"speaker": speaker, "image": image}

    def msg_emoji(speaker, emoji):
        return {"speaker": speaker, "emoji": emoji}

    def build_conversations():
        return {
            "Jennifer": [
                msg_text(SPEAKER_LEFT, "Hey, [MC], don't forget to lock the door when you leave for school."),
                msg_text(SPEAKER_RIGHT, "Ok, mom, you told me ten times already."),
                msg_text(SPEAKER_LEFT, "And don't be late!!!"),
                msg_text(SPEAKER_LEFT, "If I get another call from your teacher, you will be in big trouble"),
                msg_text(SPEAKER_RIGHT, "Yeah, I get it, I won't be late!"),
            ],
            "Isabella": [
                msg_text(SPEAKER_LEFT, "Hey, my dear big brother, what are you doing on this wonderful day?"),
                msg_text(SPEAKER_RIGHT, "What do u want?"),
                msg_text(SPEAKER_LEFT, "Ohhh, c'mon, why do you always assume that I want something?"),
                msg_text(SPEAKER_RIGHT, "Because you do, now tell me what you want."),
                msg_text(SPEAKER_LEFT, "Can I play a game on your PC? it doesn't work on mine"),
                msg_text(SPEAKER_RIGHT, "No"),
                msg_text(SPEAKER_LEFT, "Ohhh, c'mon, I won't get any virus this time!"),
                msg_text(SPEAKER_RIGHT, "Last time I fixed it for like a week, Isa, you're not touching my pc"),
                msg_text(SPEAKER_LEFT, "Screw you!"),
            ],
            "Claire": [
                msg_text(SPEAKER_RIGHT, "Hey, Claire, how are you?"),
                msg_text(SPEAKER_RIGHT, "Jennifer told me to ask you if you will be watching a movie with us tonight."),
                msg_text(SPEAKER_RIGHT, "Hey, Claire, are you coming to the movie night?"),
                msg_text(SPEAKER_RIGHT, "We are waiting for you!"),
            ],
        }

    def maria_scarlet_photo_lingerie_messages():
        return [
            msg_text(SPEAKER_LEFT, "Just send me that damn image already..."),
            msg_text(SPEAKER_RIGHT, "New phone, who s this?"),
            msg_text(SPEAKER_LEFT, "Stop playing dumb and send me that shit"),
            msg_text(SPEAKER_LEFT, "I made that whole scene for nothing..."),
            msg_image(SPEAKER_RIGHT, "images/ArtClass/DuringClass_Scene/DuringArtClass_Scene202.webp"),
            msg_emoji(SPEAKER_LEFT, "{image=noway_face_emoji}"),
            msg_text(SPEAKER_LEFT, "Wait what"),
            msg_text(SPEAKER_RIGHT, "What?"),
            msg_text(SPEAKER_LEFT, "How tf did you get such a good shot?"),
            msg_text(SPEAKER_LEFT, "It looks like you re in there with her"),
            msg_text(SPEAKER_RIGHT, "I have my own secrets"),
            msg_text(SPEAKER_LEFT, "..."),
        ]

    def maria_scarlet_photo_naked_messages():
        return [
            msg_text(SPEAKER_LEFT, "Gimme"),
            msg_text(SPEAKER_RIGHT, "What?"),
            msg_text(SPEAKER_LEFT, "what I worked for"),
            msg_text(SPEAKER_RIGHT, "oh right, mb"),
            msg_image(SPEAKER_RIGHT, "images/ArtClass/DuringClass_Scene/photo.png"),
            msg_text(SPEAKER_RIGHT, "ummmm"),
            msg_text(SPEAKER_RIGHT, "are you still there?"),
            msg_text(SPEAKER_RIGHT, "no reaction at all?"),
            msg_emoji(SPEAKER_LEFT, "{image=noway_face_emoji}{image=noway_face_emoji}{image=noway_face_emoji}"),
            msg_text(SPEAKER_LEFT, "Don't send this to anyone else"),
            msg_text(SPEAKER_LEFT, "I'm pretty sure you can get to prison or some shit like that for this"),
            msg_text(SPEAKER_RIGHT, "Of course I won't, you think I'm dumb?"),
            msg_text(SPEAKER_LEFT, "...."),
            msg_text(SPEAKER_LEFT, "yes"),
            msg_text(SPEAKER_RIGHT, "So? You didn't tell me, do u like the picture?"),
            msg_text(SPEAKER_LEFT, "hoyl fk, are u stupid? It's hot af!"),
            msg_text(SPEAKER_LEFT, "She did't see you, right?"),
            msg_text(SPEAKER_RIGHT, "She did while I was checking out the photo to see that it was alright"),
            msg_text(SPEAKER_RIGHT, "But she doesn't know I took it."),
            msg_text(SPEAKER_LEFT, "SHE DID?!"),
            msg_text(SPEAKER_LEFT, "Didn't she go nuts on you?"),
            msg_text(SPEAKER_RIGHT, "Ofc she did, but I was just \"staying there\""),
            msg_text(SPEAKER_RIGHT, "so it's not my fault"),
            msg_text(SPEAKER_RIGHT, "but she started yelling and goingn nuts while still naked, like face to face with me"),
            msg_text(SPEAKER_LEFT, "WHAT?"),
            msg_text(SPEAKER_RIGHT, "yeah, that's what I'm saying"),
            msg_text(SPEAKER_RIGHT, "she didn't even realize we were face to face, she told me to turn around after a bit"),
            msg_text(SPEAKER_RIGHT, "I'm telling you, that + changing in the room right next to us"),
            msg_text(SPEAKER_RIGHT, "She has to be some kind of nympho"),
            msg_text(SPEAKER_LEFT, "wtf is a nympho"),
            msg_text(SPEAKER_RIGHT, "....."),
            msg_text(SPEAKER_RIGHT, "ummm, a girl that likes to be naked in public... I think"),
            msg_text(SPEAKER_LEFT, "hmmm, idk, she might be I guess..."),
            msg_text(SPEAKER_LEFT, "It is a bit weird to be changing like that, now that I think about it"),
            msg_text(SPEAKER_RIGHT, "What do u say? Do u think we could black mail her with the image?"),
            msg_text(SPEAKER_LEFT, "Are you fucking stupid? Shut the fuck up!"),
            msg_text(SPEAKER_LEFT, "Don't talk about shit like that in messages"),
            msg_text(SPEAKER_RIGHT, "Geez, ok, chill, you're such a scaredy cat"),
            msg_text(SPEAKER_LEFT, "I gotta go, don't do anything dumb with that photo, okay?"),
            msg_text(SPEAKER_RIGHT, "Ummm..."),
            msg_text(SPEAKER_LEFT, "!!!!!!!!!!!!!"),
            msg_text(SPEAKER_LEFT, "Beat your dick all u want on it, just don't share it, UDNERSTOOD?"),
            msg_text(SPEAKER_RIGHT, "Udnerstood, udnerstood"),
            msg_text(SPEAKER_LEFT, "..."),
        ]

    def maria_add_to_group_chat_messages():
        return [
            msg_text(SPEAKER_RIGHT, "We are waiting for you!"),
            msg_text(SPEAKER_RIGHT, "Don't keep us waiting too long!"),
        ]

default conversations = build_conversations()

image face_with_open_mouth_small = Transform("images/emojis/face_with_open_mouth.png", zoom=1.2)
image noway_face_emoji = Transform("images/emojis/noway_face.png", zoom=1.2)
