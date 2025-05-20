import pyttsx3
from gtts import gTTS
if __name__ == "__main__":
    print("Hello I am Maven , your Verbal Assistant\n")
    engine = pyttsx3.init()
    engine.say('Hello I am Maven , your Verbal Assistant. How can I help you ?')
    engine.runAndWait()
    while True:
        menu = int(input
               ("\n----------Operations----------\n"\
                "1.Speak out loud.\n" \
                "2.Change the assistant's voice.\n" \
                "3.Read from a file.\n" \
                "4.Extract text to audio file.\n" \
                "Note:Press -1 to exit\n"))
        match menu:
            case 1:
                while True:
                    x = input("\nWhat do you want to say (-1 to exit):\n")
                    if x=='-1':
                        engine.say('Hope you enjoyed interacting with me.')
                        engine.runAndWait()
                        break
                    engine.say(x)
                    engine.runAndWait()
            case 2:
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say("Voice modification is done successfully")
                engine.runAndWait()
            case 3:
                x=input("\nEnter Path to your file:\n")
                with open(x,'r') as file:
                    print("\nFile Content:")
                    content=file.read()
                    print(content)
                engine.say(content)
                engine.runAndWait()
            case 4:
                x = input("\nEnter the content to convert to audio file:\n")
                f_name=input("\nEnter the file name for the audio file :\n")
                engine.say("wait for a while till i convert it to audio file")
                engine.runAndWait()
                tts=gTTS(text=x)
                tts.save(f'{f_name}.mp3')
                print("Audio file saved successfully")
                engine.say("Audio file saved successfully")
                engine.runAndWait()
            case -1:
                engine.say("Hope you enjoyed interacting with me. Maven , signing off")
                engine.runAndWait()
                break
            case _:
                print("Invalid Input")


