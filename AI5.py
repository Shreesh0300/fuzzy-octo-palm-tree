import google.generativeai as genai
import os
import speech_recognition as sr

def ask_gemini(question, api_key):
    try:
        genai.configure(api_key="AIzaSyDmL9xHiegSE266lXC1RIFip3tHpmyWaqQ")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def listen_for_question():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say your question...")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        question = r.recognize_google(audio)  # Use Google Speech Recognition
        print(f"You asked: {question}")
        return question
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    api_key_env = os.environ.get("AIzaSyDmL9xHiegSE266lXC1RIFip3tHpmyWaqQ")
    api_key = api_key_env if api_key_env else "AIzaSyDmL9xHiegSE266lXC1RIFip3tHpmyWaqQ"  # Replace with your actual API key

    if not api_key:
        print("Error: Gemini API key not found. Please set the GEMINI_API_KEY environment variable or ensure the API key is correctly set.")
    else:
        spoken_question = listen_for_question()

        if spoken_question:
            answer = ask_gemini(spoken_question, api_key)

            if answer:
                print("Answer from Gemini 1.5 Flash:")
                print(answer)