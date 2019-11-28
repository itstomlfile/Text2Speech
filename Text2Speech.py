#!/usr/bin/python
"""
TODO: Allow last line to be processed after a black line (Remove need to press return)
"""
import time, shutil, os
from gtts import gTTS
from playsound import playsound


def generateFile(text):
    fileno = time.strftime("%Y%m%d-%H%M%S")
    fileName = "audio/file" + str(fileno) + ".mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(fileName)  # Random Files number
    return fileName


def play(file):
    playsound(file)


def deleteAudioFiles():
    path = 'audio'
    if (os.path.exists(path)):
        shutil.rmtree(path, ignore_errors=True)  # delete old directory
    os.makedirs(path)  # recreate new one
    print("Audio files cleared successfully...")
    time.sleep(1)


