import speech_recognition as sr
import datetime
# import pyttsx3


r = sr.Recognizer()

#get the default microphine
with sr.Microphone() as source:
    #listens to a command, using
    
    while True: 
      audio = r.listen(source)
      
      #Recognizes speech using google as a service
      sphinx = r.recognize_google(audio)
      google = r.recognize_google(audio)
      
      print('google: [{}]\nSphinx: {}\n\n' .format(google, sphinx))
