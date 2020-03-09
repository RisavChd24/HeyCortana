from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser as w
import time
opera_path = '#path of web browser'

def talktoMe(audio) :
    tts = gTTS(text=audio)
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

def mic(x) :
    r = sr.Recognizer()
    with sr.Microphone() as source :
         audio = r.listen(source)
         com = r.recognize_google(audio)
    return(com)

def web_browse(d):
    r = sr.Recognizer()
    with sr.Microphone() as source :
         talktoMe("which website to be opened rishabh")
         
         while 1 :
              audio = r.listen(source)
              if audio :
                  break
         talktoMe("heard")
    text = r.recognize_google(audio)
    talktoMe('I AM SEARCHING' + text + '!')
    f_text = 'https://www.google.co.in/search?q=' + text
    w.get(opera_path).open(f_text)
    
def ready_to_comply(a) :
    c = 3
    while c != 4 :
          talktoMe("READY TO COMPLY !")
          f = 4
          command = mic(f)
          talktoMe('you said' + command + '!')
          if command == "leave" or command == "quit" or command == "stop" :
              break
          if command == "web" or command == "web browse" or command == "net" :
             e = 4
             web_browse(e)


talktoMe("HEY ! I am CORTANA")
b = 'der'
ready_to_comply(b)

