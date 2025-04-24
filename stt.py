import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("SPEAK")
    try:
        audio = r.listen(source)
        print("RECOGNIZING")
        text = r.recognize_google(audio)
        print("You said:", text)

    except sr.UnknownValueError:
        print("COULD NOT UNDERSTAND AUDIO")
