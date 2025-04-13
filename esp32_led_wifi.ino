#include <WiFi.h>

const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA";

WiFiServer server(3232);
const int ledPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conectado!");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    String comando = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n') {
          comando.trim();
          if (comando == "ligar") {
            digitalWrite(ledPin, HIGH);
            client.println("LED LIGADO");
          } else if (comando == "desligar") {
            digitalWrite(ledPin, LOW);
            client.println("LED DESLIGADO");
          } else {
            client.println("Comando inválido");
          }
          comando = "";
        } else {
          comando += c;
        }
      }
    }
    client.stop();
  }
}
