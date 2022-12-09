//includy efektów
#include "WebPage.h"
#include "Bouncing.cpp"
#include "Effect.cpp"
#include "Rainbow.cpp"
#include "RainbowFull.cpp"
#include "StaticColor.cpp"
#include "Train.cpp"
#include "TrainsWithManyColors.cpp"
#include "Rain.cpp"
#include "Fire.cpp"
#include "Disable.cpp"
#include "Stroboscop.cpp"
#include "GradientMoving.cpp"
#include "GradientMusic.cpp"
#include "ChangeFullColors.cpp"
#include "Tv.cpp"

#include "Counter.h"

#include <SPIFFS.h>
#include <Arduino.h> //podstawowa biblioteka
#include <ESPmDNS.h> //dns połączenie
#include <FastLED.h> //obsługa ledów !niekoniecznie musi być tutaj
#include <String>
#include <WebServer.h> //serwer webowy !musi być tutaj na ten moment
#include <WebSocketsServer.h> //web socket    !musi być tutaj na ten moment
#include <WiFi.h> //połączenie wifi !musi być tutaj na ten moment
#include <cstdlib>
#include <iostream>
#include <chrono>   //mierzenie czasu
#include "time.h"
#define LED_PIN 2
#define NUM_LEDS 260

//test strony zajebistej


int speed = 0;
int brightness = 150;
// tworzenie serwera, efektu działającego i ledów
CRGB leds[NUM_LEDS];
WebServer server;
WebSocketsServer webSocket = WebSocketsServer(81);
Effect* effect;


// obsługa komunikacji z klientem, w stronę; odbieranie danych z przeglądarki; komunikacja klient->serwer
void webSocketEvent(uint8_t num, WStype_t type, uint8_t* payload, size_t length)
{
    // Serial.println("wiadomość dotarła");
    //Serial.print(webSocket.connectedClients());
    // String str = (char*)payload;
    // Serial.println(str);
    if (type == WStype_TEXT) {
        //Serial.println(brightness);
        String str = (char*)payload;
        // Serial.println(str);
        if(str[0] == 'U') {
            effect->sendPayload(payload);
        } else if (str[0] == 'T') {
            int r = static_cast<unsigned char>(payload[1]);
            int g = static_cast<unsigned char>(payload[2]);
            int b = static_cast<unsigned char>(payload[3]);
            Serial.println("r = ");
            Serial.println(r);
            Serial.println(g);
            Serial.println(b);
            CRGB color = CRGB(r, g, b);
            effect->changeColor(color);
        } else if (str[0] == 'P') {
            brightness = (int)strtol((const char*)&payload[1], NULL, 10);
            Serial.println(brightness);
            effect->changeBrightness(brightness);
        } else if (str[0] == 'E') {
            // Serial.print("2");
            String substr = str.substring(1);

            if (substr == "train") {
                Serial.println(speed);
                delete effect;
                Serial.print("after deletion");
                Serial.print(speed);
                Train* t = new Train(speed, brightness, 6, leds, NUM_LEDS);
                t->addColor(CRGB(150, 150, 0));
                t->addColor(CRGB(0, 150, 150));
                effect = t;
            } else if (substr == "rainbow") {
                delete effect;
                effect = new Rainbow(speed, brightness, 1, leds, NUM_LEDS);
            } else if (substr == "rainbow2") {
                delete effect;
                effect = new RainbowFull(speed, brightness, leds, NUM_LEDS);
            } else if (substr == "bounce") {
                delete effect;
                effect = new Bouncing(speed, brightness, CRGB(150, 150, 0), leds, NUM_LEDS, 6);
            } else if (substr == "train2") {
                delete effect;
                TrainsWithManyColors* t = new TrainsWithManyColors(speed, brightness, 10, leds, NUM_LEDS);
                
                t->addColor(CRGB(255, 0, 0));
                t->addColor(CRGB(0, 0, 255));
                effect = t;
            } else if (substr == "static") {
                delete effect;
                Serial.print("destruktor zakonczony, zaczynanie nowego efektu");
                effect = new StaticColor(brightness, leds, NUM_LEDS);
            } else if (substr == "rain") {
                delete effect;
                effect = new Rain(brightness, speed, CRGB::Blue, leds, NUM_LEDS);
            } else if (substr == "fire") {
                delete effect;
                effect = new Fire(brightness, speed, leds, NUM_LEDS);
            } else if (substr == "disable") {
                delete effect;
                effect = new Disable(leds, NUM_LEDS);
            } else if (substr == "stroboscop") {
                delete effect;
                effect = new Stroboscop(brightness, speed, CRGB::Red, leds, NUM_LEDS);
            } else if (str.substring(1, 15) == "gradientmoving") {
                Serial.print(str.substring(15));
                
                if(str.substring(15) == "sunset") {
                  delete effect;
                  effect = new GradientMoving(brightness, speed, 1, leds, NUM_LEDS);
                }else if(str.substring(15) == "nether") {
                  delete effect;
                  effect = new GradientMoving(brightness, speed, 2, leds, NUM_LEDS);
                }  else if(str.substring(15) == "rgb") {
                  delete effect;
                  effect = new GradientMoving(brightness, speed, 3, leds, NUM_LEDS);
                } else if(str.substring(15) == "redblue") {
                  delete effect;
                  effect = new GradientMoving(brightness, speed, 4, leds, NUM_LEDS);
                }
            } else if (substr == "gradientmusic") {
                delete effect;
                effect = new GradientMusic(brightness, 1, leds, NUM_LEDS);
            } else if (substr == "fullcolor") {
                delete effect;
                ChangeFullColors* t = new ChangeFullColors(speed, brightness, leds, NUM_LEDS);
                t->addColor(CRGB(255, 0, 0));
                t->addColor(CRGB(0, 0, 255));
                effect = t;
            } else if (substr == "fullcolor2") {
                delete effect;
                ChangeFullColors* t = new ChangeFullColors(speed, brightness, leds, NUM_LEDS);
                t->addColor(CRGB(255, 0, 0));
                t->addColor(CRGB(255, 255, 0));
                t->addColor(CRGB(0, 255, 255));
                t->addColor(CRGB(0, 0, 255));
                t->addColor(CRGB(255, 0, 255));
                effect = t;
            } else if (substr == "tv") {
                delete effect;
                effect = new Tv(brightness, leds, 0, 150, NUM_LEDS);
            }
        } else if (str[0] == 'V') {
            if (str[1] == 'B') {
                brightness = (int)strtol((const char*)&payload[2], NULL, 10);
                Serial.println(brightness);
                effect->changeBrightness(brightness);
            } else if (str[1] == 'S') {
                speed = (int)strtol((const char*)&payload[2], NULL, 10);
                effect->changeSpeed(speed);
                Serial.println(speed);
            } else if (str[1] == 'C') {
                String substr = str.substring(4);
                char* p;
                int color = strtol(substr.c_str(), &p, 16);
                if (*p != 0) {
                    Serial.println("not a color");
                }
                Serial.println(color);
                CRGB a = color;
                effect->changeColor(a);
            } else if (str[1] == 'T') {
                if (str[2] == 'S'){
                    String substr1 = str.substring(3, 5);
                    String substr2 = str.substring(6, 8);
                    Serial.println(substr1);
                    Serial.println(substr2);
                    char* p;
                    int hour = strtol(substr1.c_str(), &p, 10);
                    int minute = strtol(substr2.c_str(), &p, 10);
                    
                    long timeInSeconds = hour * 3600 + minute * 60;
                    Serial.println(timeInSeconds);
                    Counter::setDistanceTime(timeInSeconds);
                    Counter::enableCounter();

                }else if (str[2] == 'D') {
                    Counter::disableCounter();
                }
            }
        }
    }
    // Serial.print("end");
}

// void onIndexRequest(AsyncWebServerRequest *request) {
//     IPAddress remote_ip = request->client()->remoteIP();
//     Serial.println("[" + remote_ip.toString() + "] HTTP get request of " + request->url());
//     request->send(SPIFFS, "/index.html", "text/html");
// }

void serveIndexFile() {
    File file = SPIFFS.open("/index.html", "r");
    server.streamFile(file, "text/html");
    file.close();
}

void serveIndexCssFile() {
    File file2 = SPIFFS.open("/css/index.css", "r");
    server.streamFile(file2, "text/css");
    file2.close();
}

void serveIndexJSFile() {
    File file = SPIFFS.open("/js/index.js", "r");
    server.streamFile(file, "text/css");
    file.close();
}

// konfiguracja serwera, websocketa, dnsa
void setupServer(std::string ssid, std::string password)
{
    WiFi.begin(ssid.c_str(), password.c_str());

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.print("connected\n");
    Serial.print("IP address: ");
    Serial.print(WiFi.localIP());

    if (!MDNS.begin("esp32")) {
        Serial.println("Error setting up MDNS responder!");
        while (1) {
            delay(1000);
        }
    }
    Serial.println("mDNS responder started");
    // server.on("/", []() {
    //     server.send_P(200, "text/html", webpage123);
    // });
    SPIFFS.begin();
    server.on("/", serveIndexFile);
    server.on("/css/index.css", serveIndexCssFile);
    server.on("/js/index.js", serveIndexJSFile);
    server.begin();
    webSocket.begin();
    webSocket.onEvent(webSocketEvent);
}

void setup()
{
    Serial.begin(115200);

    FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
    // server.start("Dom", "Kabanos1", NUM_LEDS, leds);
    // setupServer("UPC3356958", "m3sdBthjwfus");
    setupServer("UPC9453756", "Papiez2137");
    effect = new Rainbow(speed, brightness, 10, leds, NUM_LEDS);
    // effect = new StaticColor(brightness, leds, NUM_LEDS);

    Counter::configureTimer(&effect, leds, NUM_LEDS);
    // Counter::enableCounter();
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop()
{
    // auto start = std::chrono::steady_clock::now();
    webSocket.loop();
    //Serial.println("Loopwebsocketa");
    server.handleClient();
    //Serial.println("server.handleClient");
    effect->updateAndShow();
    // Serial.println("UpdateAndShow");

    //Serial.print(".");
    //Serial.println("speed w mainie ");
    //Serial.println(speed);

    // auto end = std::chrono::steady_clock::now();
    // Serial.println(std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count());
    // char c[] = "costam";
    // webSocket.broadcastTXT(c, sizeof(c));
}
