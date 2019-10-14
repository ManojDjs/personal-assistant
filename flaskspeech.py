from flask import Flask
from gtts import gTTS
import time
from playsound import playsound
import os
import grammar_check
import datetime
import pyttsx3
app = Flask(__name__)
@app.route('/')
def hello():
    def assistant():
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("Speak :")
                audio = r.listen(source, timeout=1)
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                # try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                if text.__contains__('hi'):
                    mytext = 'hai! im Aayisha. i am your personal assistant how can  help you?'
                    engine.say(mytext)
                    engine.runAndWait()
                    engine.stop()
                    # myobj = gTTS(text=mytext, lang='en', slow=False)
                    # myobj.save("welcome.mp3")
                    # # Playing the converted file
                    # # os.system("welcome.mp3")
                    # time.sleep(0.5)
                    # k = os.getcwd()
                    # playsound('welcome.mp3')
                    # os.remove(k + '/' + 'welcome.mp3')
                elif text.__contains__('today date'):
                    x = datetime.datetime.now()
                    engine.say(x)
                    engine.runAndWait()
                    engine.stop()
                    exit()
                elif text == 'bye':
                    mytext = 'take care dear.BYE'
                    engine.say(mytext)
                    engine.runAndWait()
                    engine.stop()
                    exit()
                else:
                    mytext = 'i am not trained upto that! i am sorry for that'
                    engine.say(mytext)
                    engine.runAndWait()
                    engine.stop()
                    return mytext
            except:
                engine = pyttsx3.init()
                exc = "Sorry could not recognize what you said "
                engine.say(exc)
                engine.runAndWait()
                engine.stop()
                return exc

    while True:
        k=assistant()
        return k
    # voices = engine.getProperty('voices')
    #             for voice in voices:
    #                 engine.setProperty('voice', voice.id)
    #                 engine.say('The quick brown fox jumped over the lazy dog.')
    #             engine.runAndWait()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)