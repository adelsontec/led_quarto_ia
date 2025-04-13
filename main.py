import random

def interpretar_comando(comando):
    comando = comando.lower()

    palavras_ligar = ["ligar", "acender", "está escuro", "preciso de luz"]
    palavras_desligar = ["desligar", "apagar", "está claro", "não preciso de luz"]

    for palavra in palavras_ligar:
        if palavra in comando:
            return "ligar"

    for palavra in palavras_desligar:
        if palavra in comando:
            return "desligar"

    return "comando_desconhecido"


def executar_acao(acao):
    if acao == "ligar":
        print("LED do quarto LIGADO.")
    elif acao == "desligar":
        print("LED do quarto DESLIGADO.")
    else:
        print("Desculpe, não entendi o comando.")


def main():
    print("Sistema de controle de LED com IA simples.")
    while True:
        comando_usuario = input("\nDiga o que deseja fazer (ou 'sair' para encerrar): ")
        if comando_usuario.lower() == "sair":
            break
        acao = interpretar_comando(comando_usuario)
        executar_acao(acao)

if __name__ == "__main__":
    main()
  
