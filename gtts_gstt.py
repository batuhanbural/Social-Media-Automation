import os
import random
import webbrowser

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def text_to_speech(**kwargs):
    read_file, myText, language = "", "", "en"
    for key, value in kwargs.items():
        if key == "text":
            myText = value
        elif key == "doc":
            read_file = open(value, "r", encoding="utf-8")
            myText = read_file.read().replace("\n", " ")
        elif key == "lang":
            language = value
        else:
            raise SyntaxError

    output = gTTS(text=myText, lang=language, slow=False)

    rand_n = random.randint(1, 10000)
    file = f"speech_text_{rand_n}.mp3"

    output.save(file)
    playsound(file)
    os.remove(file)

    try:
        read_file.close()
    except AttributeError:
        pass


def speech_to_text(ask=False, lang="en"):
    if ask:
        text_to_speech(text=ask, lang=lang)

    raw_source = sr.Recognizer()
    with sr.Microphone() as source:
        audio = raw_source.listen(source)
        voice = ""
        try:
            voice = raw_source.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            text_to_speech(text="I can't catch it!", lang="en")
        except sr.RequestError:
            text_to_speech(text="System Error!", lang="en")
        return voice


def search_on_web(querry_line):
    url = "https://www.google.com/search?q=" + querry_line
    webbrowser.get().open(url)

# How to use code basically. Code made from Darquesse...

# text_to_speech(text="What can i do for you")
# while True:
#     voice = speech_to_text(lang="en")
#     if voice == "how are you":
#         text_to_speech(text="I'm fine. What can i do for you?")
#     elif voice == "see you next time":
#         text_to_speech(text="See you later")
#         break