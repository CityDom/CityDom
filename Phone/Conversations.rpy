default conversations = {
    "Jennifer": [
        {'speaker': 'left', 'text': 'Hey, [MC], don\'t forget to lock the door when you leave for school.'},
        {'speaker': 'right', 'text': 'Ok, mom, you told me ten times already.'},
        {'speaker': 'left', 'text': 'And don\'t be late!!!'},
        {'speaker': 'left', 'text': 'If I get another call from your teacher, you will be in big trouble'},
        {'speaker': 'right', 'text': 'Yeah, I get it, I won\'t be late!'},
    ],
    "Isabella": [
        {'speaker': 'left', 'text': 'Hey, my dear big brother, what are you doing on this wonderful day?'},
        {'speaker': 'right', 'text': 'What do u want?'},
        {'speaker': 'left', 'text': 'Ohhh, c\'mon, why do you always assume that I want something?'},
        {'speaker': 'right', 'text': 'Because you do, now tell me what you want.'},
        {'speaker': 'left', 'text': 'Can I play a game on your PC? it doesn\'t work on mine'},
        {'speaker': 'right', 'text': "No"},
        {'speaker': 'left', 'text': 'Ohhh, c\'mon, I won\'t get any virus this time!'},
        {'speaker': 'right', 'text': 'Last time I fixed it for like a week, Isa, you\'re not touching my pc'},
        {'speaker': 'left', 'text': 'Screw you!'},
    ],
    "Claire": [
        {'speaker': 'right', 'text': 'Hey, Claire, how are you?'},
        {'speaker': 'right', 'text': 'Mom told me to ask you if you will be watching a movie with us tonight.'},
        {'speaker': 'right', 'text': 'Hey, Claire, are you coming to the movie night?'},
        {'speaker': 'right', 'text': 'We are waiting for you!'},
    ]
}

default selected_chat = ""
default chat_names = ["Jennifer", "Isabella", "Claire"]
default current_message = {name: 0 for name in chat_names}

init python:
    def add_chat(name):
        """
        Add a new chat with an empty conversation if it doesn't already exist.
        """
        if name not in renpy.store.conversations:
            renpy.store.conversations[name] = []
        if name not in renpy.store.chat_names:
            renpy.store.chat_names.append(name)
        if name not in renpy.store.current_message:
            renpy.store.current_message[name] = 0

    def get_conversations():
        """
        Returns the current conversations.
        """
        return renpy.store.conversations

    def Maria_ScarletPhoto_Lingerie():
        """
        Add Maria's Scarlet photo lingerie conversation chunk.
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'left', 'text': 'Just send me that damn image already...'},
            {'speaker': 'right', 'text': 'New phone, who s this?'},
            {'speaker': 'left', 'text': 'Stop playing dumb and send me that shit'},
            {'speaker': 'left', 'text': 'I made that whole scene for nothing...'},
            {'speaker': 'right', 'image': 'images/ArtClass/DuringClass_Scene/DuringArtClass_Scene202.webp'},
            {'speaker': 'left', 'emoji': '{image=noway_face_emoji}'}, 
            {'speaker': 'left', 'text': 'Wait what'},
            {'speaker': 'right', 'text': 'What?'},
            {'speaker': 'left', 'text': 'How tf did you get such a good shot?'},
            {'speaker': 'left', 'text': 'It looks like you re in there with her'},
            {'speaker': 'right', 'text': 'I have my own secrets'},
            {'speaker': 'left', 'text': '...'},
        ])

    def Maria_ScarletPhoto_Naked():
        """
        Add Maria's Scarlet photo naked conversation chunk.
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'left', 'text': 'Gimme'},
            {'speaker': 'right', 'text': 'What?'},
            {'speaker': 'left', 'text': 'what I worked for'},
            {'speaker': 'right', 'text': 'oh right, mb'},
            {'speaker': 'right', 'image': 'images/ArtClass/DuringClass_Scene/photo.png'},
            {'speaker': 'right', 'text': 'ummmm'},
            {'speaker': 'right', 'text': 'are you still there?'},
            {'speaker': 'right', 'text': 'no reaction at all?'},
            {'speaker': 'left', 'text': '{image=noway_face_emoji}{image=noway_face_emoji}{image=noway_face_emoji}'},
            {'speaker': 'left', 'text': 'Don\'t send this to anyone else'},
            {'speaker': 'left', 'text': 'I\'m pretty sure you can get to prison or some shit like that for this'},
            {'speaker': 'right', 'text': 'Of course I won\'t, you think I\'m dumb?'},
            {'speaker': 'left', 'text': '....'},
            {'speaker': 'left', 'text': 'yes'},
            {'speaker': 'right', 'text': 'So? You didn\'t tell me, do u like the picture?'},
            {'speaker': 'left', 'text': 'hoyl fk, are u stupid? It\'s hot af!'},
            {'speaker': 'left', 'text': 'She did\'t see you, right?'},
            {'speaker': 'right', 'text': 'She did while I was checking out the photo to see that it was alright'},
            {'speaker': 'right', 'text': 'But she doesn\'t know I took it.'},
            {'speaker': 'left', 'text': 'SHE DID?!'},
            {'speaker': 'left', 'text': 'Didn\'t she go nuts on you?'},
            {'speaker': 'right', 'text': 'Ofc she did, but I was just \"staying there\"'},
            {'speaker': 'right', 'text': 'so it\'s not my fault'},
            {'speaker': 'right', 'text': 'but she started yelling and goingn nuts while still naked, like face to face with me'},
            {'speaker': 'left', 'text': 'WHAT?'},
            {'speaker': 'right', 'text': 'yeah, that\'s what I\'m saying'},
            {'speaker': 'right', 'text': 'she didn\'t even realize we were face to face, she told me to turn around after a bit'},
            {'speaker': 'right', 'text': 'I\'m telling you, that + changing in the room right next to us'},
            {'speaker': 'right', 'text': 'She has to be some kind of nympho'},
            {'speaker': 'left', 'text': 'wtf is a nympho'},
            {'speaker': 'right', 'text': '.....'},
            {'speaker': 'right', 'text': 'ummm, a girl that likes to be naked in public... I think'},
            {'speaker': 'left', 'text': 'hmmm, idk, she might be I guess...'},
            {'speaker': 'left', 'text': 'It is a bit weird to be changing like that, now that I think about it'},
            {'speaker': 'right', 'text': 'What do u say? Do u think we could black mail her with the image?'},
            {'speaker': 'left', 'text': 'Are you fucking stupid? Shut the fuck up!'},
            {'speaker': 'left', 'text': 'Don\'t talk about shit like that in messages'},
            {'speaker': 'right', 'text': 'Geez, ok, chill, you\'re such a scaredy cat'},
            {'speaker': 'left', 'text': 'I gotta go, don\'t do anything dumb with that photo, okay?'},
            {'speaker': 'right', 'text': 'Ummm...'},
            {'speaker': 'left', 'text': '!!!!!!!!!!!!!'},
            {'speaker': 'left', 'text': 'Beat your dick all u want on it, just don\'t share it, UDNERSTOOD?'},
            {'speaker': 'right', 'text': 'Udnerstood, udnerstood'},
            {'speaker': 'left', 'text': '...'},
        ])

    def Maria_AddToGroupChat():
        """
        Add Maria's group chat conversation chunk.
        """
        renpy.store.conversations["Maria"].extend([
            {'speaker': 'right', 'text': 'We are waiting for you!'},
            {'speaker': 'right', 'text': 'Don\'t keep us waiting too long!'},
        ])
image face_with_open_mouth_small = Transform("images/emojis/face_with_open_mouth.png", zoom=1.2)
image noway_face_emoji = Transform("images/emojis/noway_face.png", zoom=1.2)