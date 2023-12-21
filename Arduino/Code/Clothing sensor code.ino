#include <Wire.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const char* ssid = "CSE526";            // 사용하고자 하는 wifi 이름
const char* password = "swcse1971"; // 사용하고자 하는 wifi의 비밀번호
const char* serverIP = "10.124.0.5";  // 서버의 IP 주소
const int serverPort = 12000;          // 서버의 포트 번호

const int MPU_ADDR = 0x68;
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;

WiFiClient client;

unsigned long lastSendTime = 0;
const unsigned long sendInterval = 1000;  // 1초마다 한 번씩 보내도록 설정

// 함수 선언
void initSensor();
void getRawData();

void setup() {
  initSensor();
  Serial.begin(9600);
  delay(1000);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected");
  Serial.println("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  unsigned long currentTime = millis();

  // 1초마다 한 번씩 데이터 보냄
  if (currentTime - lastSendTime >= sendInterval) {
    if (!client.connected()) {
      Serial.println("Connecting to server...");
      if (client.connect(serverIP, serverPort)) {
        Serial.println("Connected to server");
      } else {
        Serial.println("Connection to server failed");
        // 연결이 실패하면 잠시 대기 후 다시 시도
        delay(3000);
        return;
      }
    }

    getRawData();

    char buffer[128];
    sprintf(buffer, "%s/%d/%d/%d/%d/%d/%d", serverIP, AcX, AcY, AcZ, GyX, GyY, GyZ);

    client.print(buffer);

    // 연결을 닫지 않고 대기
    lastSendTime = currentTime;
  }
}

// 함수 정의
void initSensor() {
  Wire.begin();
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
}

void getRawData() {
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_ADDR, 14, true);

  AcX = Wire.read() << 8 | Wire.read();
  AcY = Wire.read() << 8 | Wire.read();
  AcZ = Wire.read() << 8 | Wire.read();
  Tmp = Wire.read() << 8 | Wire.read();
  GyX = Wire.read() << 8 | Wire.read();
  GyY = Wire.read() << 8 | Wire.read();
  GyZ = Wire.read() << 8 | Wire.read();
}
