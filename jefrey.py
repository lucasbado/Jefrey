#make a bot who listen to the user's input and reply with a random response

from ast import keyword
from email.mime import audio
from multiprocessing.connection import wait
import random 
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import keyboard

rec = sr.Recognizer()
robo = pyttsx3.init()
parar = False

# if keyboard.read_key() == "s":
#     print("Iniciando...")
while parar == False:
    with sr.Microphone() as source:
        print("Say something!")
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        res = rec.recognize_google(audio, language="pt-BR")
        print(res)

        if res == "Olá":
            robo.say("Oi, tudo bem?")
            robo.runAndWait()

            audio = rec.listen(source)
            res = rec.recognize_google(audio, language="pt-BR")
            print(res)
            while "sim" in res:
                robo.say("Fico feliz em saber que você esteja bem")
                robo.runAndWait()
                
                print("Agora, diga o que você quer fazer")
                robo.say("Agora, diga o que você quer fazer")
                robo.runAndWait() 
                audio = rec.listen(source)
                res = rec.recognize_google(audio, language="pt-BR")
                print(res)

            if "não" in res:
                robo.say("Que pena, você está mal, quer que eu ligue pra alguem?")
                robo.runAndWait()
                audio = rec.listen(source)
                res = rec.recognize_google(audio, language="pt-BR")
                print(res)
                
                if "sim" in res:
                    robo.say("Ok, ligando para contato emergencia")
                    robo.runAndWait()
                    webbrowser.open("https://www.whatsapp.com/")

                if "pesquisar" in res:
                    robo.say("O que você quer pesquisar?")
                    robo.runAndWait()
                    audio = rec.listen(source)
                    res = rec.recognize_google(audio, language="pt-BR")
                    print(res)
                    webbrowser.open("https://www.google.com/search?q=" + res)
                    robo.say("Aqui está o que eu encontrei")
                    robo.runAndWait()
                
                elif "abrir" in res:
                    robo.say("Qual o nome do arquivo?")
                    robo.runAndWait()
                    audio = rec.listen(source)
                    res = rec.recognize_google(audio, language="pt-BR")
                    print(res)
                    os.startfile(res)
                    robo.say("Aqui está o que eu encontrei")
                    robo.runAndWait()

                elif "fechar" in res:
                    robo.say("Qual o nome do arquivo?")
                    robo.runAndWait()
                    audio = rec.listen(source)
                    res = rec.recognize_google(audio, language="pt-BR")
                    print(res)
                    os.system("taskkill /f /im " + res)
                    robo.say("Aqui está o que eu encontrei")
                    robo.runAndWait()

                elif "traduzir" in res:
                    robo.say("O que você quer traduzir?")
                    robo.runAndWait()
                    audio = rec.listen(source)
                    res = rec.recognize_google(audio, language="pt-BR")
                    print(res)
                    webbrowser.open("https://translate.google.com/#pt/en/" + res)
                    robo.say("Aqui está o que eu encontrei")
                    robo.runAndWait()
                
                elif "To saindo" in res:
                    robo.say("Ok, se cuida!")
                    robo.runAndWait()
                    parar = True
                    break
                                    

            

        