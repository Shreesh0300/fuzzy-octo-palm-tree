import datetime
import speech_recognition as sr
import pyttsx3

WAKE_UP_WORD = "hello"
RESPONSE_ON_WAKE_UP = "Hello sir,how can I help you?"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return ""
        return ""

def respond_to_query(query):
    if "time" in query:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
    elif "date" in query:
        speak(datetime.datetime.now().strftime("%B %d, %Y"))
    elif WAKE_UP_WORD in query:
        speak(RESPONSE_ON_WAKE_UP)
    else:
        speak("Im designed to tell only the time and date for now  sir")

if __name__ == "__main__":
    print("WAKEUP WORD PLEASE.")
    while True:
        user_query = listen()
        if user_query:
            respond_to_query(user_query)
            if "exit" in user_query:
                speak("Goodbye!")
                break