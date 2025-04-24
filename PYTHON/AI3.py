import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Shreesh Kulkarni\Downloads\ecstatic-baton-456919-g9-628c52554d97.json"
import speech_recognition as sr
import vertexai
from gtts import gTTS
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel
import platform

load_dotenv()
project_id = os.getenv("ecstatic-baton-456919-g9")
region = os.getenv("asia-south1")

vertexai.init(project="ecstatic-baton-456919-g9", location="asia-south1")
model = GenerativeModel("gemini-pro")
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Speak your question...")
    try:
        audio = r.listen(source)
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)

        response = model.generate_content(text)
        ai_text = response.text
        print(f"AI Response: {ai_text}")

        tts = gTTS(text=ai_text, lang='en')
        audio_file = "ai_response.mp3"
        tts.save(audio_file)

        if platform.system() == "Windows":
            os.startfile(audio_file)
        elif platform.system() == "Darwin":
            os.system(f"open {audio_file}")
        elif platform.system() == "Linux":
            os.system(f"mpg321 {audio_file} &")
        else:
            print("Unsupported operating system for audio playback.")

        # os.remove(audio_file)  # Optional: Remove the audio file

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")