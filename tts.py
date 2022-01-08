import pyttsx3
engine = pyttsx3.init()
engine.say("well done boss. how can I help you ")
engine.runAndWait()

voices = engine.getProperty('voices')       #getting details of current voice
