import pyttsx3 
engine = pyttsx3.init()
engine.setProperty('rate', 100)
engine.setProperty('volume', 1.0)
text = input("Enter you text which has to be converted to speech")
engine.say(text)
engine.save_to_file(text,'output.wav')
engine.runAndWait()
