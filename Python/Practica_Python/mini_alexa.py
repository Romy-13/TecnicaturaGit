#Install SpeechRecognition with pip install SpeechRecognition
#Install pyttsx3 with pip install pyttsx3

#https://www.amazon.es/s?k=

import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()

engine = pyttsx3.init()

def talk():

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ES")
        print(f'Has dicho: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo entender lo que digiste")
        return ""

if "amazon" in talk():

    engine.say('Qué quieres comprarte en amazon')
    engine.runAndWait()
    text = talk()
    if text:
        webbrowser.open(f'https://www.amazon.es/s?k={text}')























#SpeechRecognition: 
#Esta biblioteca permite a tu programa Python reconocer y 
#transcribir voz humana en texto. Puedes usarla para crear 
#aplicaciones que respondan a comandos de voz o que 
#procesen la entrada de voz de los usuarios.

#pyttsx3: Esta es una biblioteca para síntesis de voz 
#en Python. Te permite generar voz a partir de texto, 
#lo que es útil para crear aplicaciones que pueden hablar 
#en respuesta a ciertos eventos o comandos.