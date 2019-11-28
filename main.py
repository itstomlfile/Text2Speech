import keyboard, time, Text2Speech as tts

def main():
    print("Input 'quit' to terminate...")
    print("Input 'clear' to remove audio files...")
    while (1):  # Loop until quit is typed
        text_to_print = input("Please enter the text you wish to be spoken: \n")
        if not text_to_print:
            # If empty line
            keyboard.press('enter')
            continue
        if (text_to_print == "quit"):
            print("Quitting the program...")
            time.sleep(1)
            quit(0)
        elif (text_to_print == "clear"):
            tts.deleteAudioFiles()
        else:
            print("Processing input...")
            file_to_play = tts.generateFile(text_to_print)
            tts.play(file_to_play)
            print("You typed: " + text_to_print)


if __name__ == "__main__":
    main()
