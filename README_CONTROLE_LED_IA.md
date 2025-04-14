
# Controle de Luz com Inteligência Artificial e ESP32

Este projeto implementa um sistema de automação residencial usando **reconhecimento de voz com IA leve**, controle físico via **ESP32** e **resposta por voz**, além de registro de comandos em log. Com ele, você pode **falar comandos como "acender a luz" ou "apagar a luz"**, e o sistema interpretará, responderá e executará o comando fisicamente via LED conectado ao ESP32.

---

## 🔧 Componentes do Projeto

- ESP32 com LED conectado (pino 2)
- Python 3 (em ambiente Linux ou virtualenv)
- Microfone para entrada de áudio
- Wi-Fi (ESP32 e computador na mesma rede)

---

## 🧠 Funcionalidades

- 🎙️ Reconhecimento de voz com `speech_recognition`
- 🧠 Interpretação de comandos com IA simples (linguagem natural)
- 🌐 Comunicação HTTP com ESP32 (`/ligar`, `/desligar`)
- 💡 Controle de LED em tempo real
- 🗣️ Resposta falada com `pyttsx3`
- 📝 Registro de comandos em log `.csv` com data e hora

---

## 📂 Estrutura do Projeto

```
📁 projeto/
├── led_ia_voz_fala.py          # Script principal com tudo integrado
├── comandos_log.csv            # Arquivo gerado com histórico de comandos
├── controle_led_webserver.ino  # Código para o ESP32 (Arduino IDE)
```

---

## 🚀 Como usar

### 1. Prepare o ESP32

1. Suba o código `controle_led_webserver.ino` pela Arduino IDE
2. Verifique o IP no monitor serial (ex: `192.168.100.166`)

### 2. Configure o Python (no PC)

```bash
sudo apt install python3-venv portaudio19-dev
python3 -m venv led-ia-env
source led-ia-env/bin/activate
pip install requests pyttsx3 SpeechRecognition pyaudio
```

### 3. Rode o script com IA e voz

```bash
python led_ia_voz_fala.py
```

---

## 🗣️ Comandos suportados

- "ligar a luz", "acender", "ligar"
- "desligar a luz", "apagar", "desligar"

---

## 📋 Log de comandos

O sistema salva automaticamente todos os comandos em `comandos_log.csv`, com a estrutura:

```
Data/Hora, Comando reconhecido, Ação enviada
2025-04-14 14:36, acenda a luz, ligar
2025-04-14 14:37, apagar tudo, desligar
```

---

## 🧩 Tecnologias utilizadas

- Python 3
- ESP32 (Arduino IDE)
- Bibliotecas: `speech_recognition`, `pyttsx3`, `requests`, `pyaudio`
- HTML interno (ESP32 WebServer)

---

## 🧠 Possíveis melhorias

- Interface gráfica com botão de voz
- Integração com Google Assistant ou Telegram
- Controle de múltiplos dispositivos (ventilador, TV etc)
- Reconhecimento de voz offline (com Vosk ou Whisper)

---

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.
Criado por [Seu Nome], 2025.
