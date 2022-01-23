// #ifndef SERVERCONNECTIVITY_H
// #define SERVERCONNECTIVITY_H

// #include <ESPmDNS.h>
// #include <WebServer.h>
// #include <WebSocketsServer.h>
// #include <WiFi.h>

// #include "Effect.cpp"

// #include "Bouncing.cpp"
// #include "Rainbow.cpp"
// #include "Train.cpp"

// char webpage123[] PROGMEM = R"=====(
// <html>
// <head>
// </head>
// <body onload="javascript:init()">
//   <div>
//     <input type="button" id="rainbow" onclick="rainbow();" />
//   </div>
//   <hr/>
//   <div>
//     <input type="button" id="train" onclick="train()" />
//   </div>  
//   <hr/>
//   <div>
//     <input type="button" id="bounce" onclick="bounce()" />
//   </div>  
// </body>
// </html>
// )=====";




// class ServerConnectivity {

//     // WiFiServer server;
//     int NUM_LEDS;
//     Effect* effect;
//     CRGB* leds;
//     static WebServer server;
//     WebSocketsServer webSocket = WebSocketsServer(81);

// public:
//     ServerConnectivity() { }

//     void start(std::string ssid, std::string password, int num_leds, CRGB* leds)
//     {
//         NUM_LEDS = num_leds;
//         this->leds = leds;
//         WiFi.begin(ssid.c_str(), password.c_str());

//         while (WiFi.status() != WL_CONNECTED) {
//             delay(500);
//             Serial.print(".");
//         }

//         Serial.print("connected\n");
//         Serial.print("IP address: ");
//         Serial.print(WiFi.localIP());

//         if (!MDNS.begin("esp32")) {
//             Serial.println("Error setting up MDNS responder!");
//             while (1) {
//                 delay(1000);
//             }
//         }
//         Serial.println("mDNS responder started");
//         server.on("/", []() {
//             server.send_P(200, "text/html", webpage123);
//         });
//         server.begin();
//         effect = new Rainbow(50, 10, leds, NUM_LEDS);
//     }

//     Effect* obsluga()
//     {
//         WiFiClient client = server.available(); // listen for incoming clients
//         if (client) { // if you get a client,
//             Serial.println("New Client."); // print a message out the serial port
//             String currentLine = ""; // make a String to hold incoming data from the client
//             while (client.connected()) { // loop while the client's connected
//                 if (client.available()) { // if there's bytes to read from the client,
//                     char c = client.read(); // read a byte, then
//                     Serial.write(c); // print it out the serial monitor
//                     if (c == '\n') { // if the byte is a newline character

//                         // if the current line is blank, you got two newline characters in a row.
//                         // that's the end of the client HTTP request, so send a response:
//                         if (currentLine.length() == 0) {
//                             // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
//                             // and a content-type so the client knows what's coming, then a blank line:
//                             client.println("HTTP/1.1 200 OK");
//                             client.println("Content-type:text/html");
//                             client.println();

//                             // the content of the HTTP response follows the header:
//                             client.print("Click <a href=\"/H\">here</a> to turn the LED TRAIN.<br>");
//                             client.print("Click <a href=\"/L\">here</a> to turn the LED RAINBOW.<br>");
//                             client.print("Click <a href=\"/B\">here</a> to turn the LED BOUNCING.<br>");

//                             // The HTTP response ends with another blank line:
//                             client.println();
//                             // break out of the while loop:
//                             break;
//                         } else { // if you got a newline, then clear currentLine:
//                             currentLine = "";
//                         }
//                     } else if (c != '\r') { // if you got anything else but a carriage return character,
//                         currentLine += c; // add it to the end of the currentLine
//                     }

//                     // Check to see if the client request was "GET /H" or "GET /L":
//                     if (currentLine.endsWith("GET /H")) {
//                         delete effect;
//                         Train* t = new Train(100, 30, leds, NUM_LEDS);
//                         t->addColor(CRGB(150, 150, 0));
//                         t->addColor(CRGB(0, 150, 150));
//                         effect = t;
//                     }
//                     else if (currentLine.endsWith("GET /L")) {
//                         delete effect;
//                         effect = new Rainbow(100, 5, leds, NUM_LEDS);
//                     }
//                     else if(currentLine.endsWith("GET /B")) {
//                         delete effect;
//                         effect = new Bouncing(50, CRGB(0, 150, 150), leds, NUM_LEDS, 6);
//                     }
//                 }
//             }
//             // close the connection:
//             client.stop();
//             Serial.println("Client Disconnected.");
//         }
//         return this->effect;
//     }
// };

// #endif