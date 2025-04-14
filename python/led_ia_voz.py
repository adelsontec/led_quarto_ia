
import requests

def enviar_comando_para_esp32(comando):
    ip_esp32 = "192.168.100.166"
    url = f"http://{ip_esp32}/{comando}"
    try:
        resposta = requests.get(url)
        print("Resposta do ESP32:", resposta.text)
    except Exception as e:
        print("Erro ao conectar ao ESP32:", e)

def interpretar_comando(comando):
    comando = comando.lower()
    if "ligar" in comando or "acender" in comando:
        return "ligar"
    elif "desligar" in comando or "apagar" in comando:
        return "desligar"
    else:
        return "comando_desconhecido"

if __name__ == "__main__":
    while True:
        entrada = input("\nFale um comando (ou 'sair'): ")
        if entrada.lower() == "sair":
            break
        acao = interpretar_comando(entrada)
        if acao != "comando_desconhecido":
            enviar_comando_para_esp32(acao)
        else:
            print("Comando não reconhecido.")
