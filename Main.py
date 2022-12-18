import speech_recognition as sr
import os
from datetime import datetime
import pyjokes


def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        print("Diga alguma coisa: ")
        #Basta parar de falar que a aplicação encerra
        
        #Armazena o que foi dito
        audio = microfone.listen(source)
        
    try:
        #Passa o que foi dito para o algoritmo reconhecedor de padrões e o idioma falado
        frase = microfone.recognize_google(audio, language='pt-BR')

        #Mostra a frase que foi dita
        print("Você disse: " + frase)

        if "navegador" in frase:
            #Utilizando a biblioteca 'os' para interagir com o sistema do computador
            os.system("start opera.exe")

        elif "data" in frase:
            today = datetime.now()
            print("Hoje são: "+ today.strftime("%d/%m/%Y %H:%M"))

        elif "piada" in frase:
            print(pyjokes.get_joke())

        
    #Se a fala não for reconhecida, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

ouvir_microfone()