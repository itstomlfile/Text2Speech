# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import Text2Speech as tts
import os, webbrowser

while 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    try:
        input = r.recognize_google(audio) # recognize speech using Google Speech Recognition

        #print("You said " + input)

        if input == "Thanos" or input == "Fanos":
            output = "Your mum is so fat, Thanos had to snap twice"
        elif input == "hello" or input == "hi":
            output = "Your voice is sexy as fuck, boy"
        elif input == "beans":
            output = "Get ready, for the fattest beans in town"
            webbrowser.open ('https://www.google.com/search?q=beans&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjGotzYhYfiAhVBcBQKHf0ODooQ_AUIDigB&biw=3072&bih=1586')
        elif input == "Exit" or input == "Quit" or input == "exit" or input == "quit":
            exit(0)
    except sr.UnknownValueError: # speech is unintelligible
        #print("Could not understand audio")
        output = "Please say something you sexy ass mother fucker"

    #print(output)
    file = tts.generateFile(output)
    tts.play(file)