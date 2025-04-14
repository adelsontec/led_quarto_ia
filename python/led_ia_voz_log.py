
import requests
import speech_recognition as sr
import csv
from datetime import datetime

def enviar_comando_para_esp32(comando):
    ip_esp32 = "192.168.100.166"
    url = f"http://{ip_esp32}/{comando}"
    try:
        resposta = requests.get(url)
        print("ESP32 respondeu:", resposta.text)
        return resposta.text
    except Exception as e:
        print("Erro ao conectar ao ESP32:", e)
        return "Erro"

def interpretar_comando(texto):
    texto = texto.lower()
    if "ligar" in texto or "acender" in texto:
        return "ligar"
    elif "desligar" in texto or "apagar" in texto:
        return "desligar"
    else:
        return "comando_desconhecido"

def ouvir_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale seu comando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", texto)
        return texto
    except sr.UnknownValueError:
        print("Não entendi o que foi dito.")
    except sr.RequestError as e:
        print("Erro ao se conectar com o serviço de voz:", e)
    return ""

def registrar_log(texto_original, acao):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("comandos_log.csv", "a", newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([agora, texto_original, acao])

if __name__ == "__main__":
    print("Sistema iniciado com reconhecimento de voz e registro de comandos.")
    while True:
        print("\nDiga um comando de voz ou pressione Ctrl+C para sair")
        texto = ouvir_microfone()
        if texto:
            acao = interpretar_comando(texto)
            if acao != "comando_desconhecido":
                resposta = enviar_comando_para_esp32(acao)
                registrar_log(texto, acao)
            else:
                print("Comando não reconhecido.")
                registrar_log(texto, "desconhecido")
