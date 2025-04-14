
#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "A3C1_Fibra_2";
const char* password = "wuG9bpve";

const int ledPin = 2;

WebServer server(80);

void ligarLed() {
  digitalWrite(ledPin, HIGH);
  server.send(200, "text/plain", "LED LIGADO");
}

void desligarLed() {
  digitalWrite(ledPin, LOW);
  server.send(200, "text/plain", "LED DESLIGADO");
}

void notFound() {
  server.send(404, "text/plain", "Comando não encontrado");
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConectado ao Wi-Fi");
  Serial.println(WiFi.localIP());

  server.on("/ligar", ligarLed);
  server.on("/desligar", desligarLed);
  server.onNotFound(notFound);

  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

void loop() {
  server.handleClient();
}
