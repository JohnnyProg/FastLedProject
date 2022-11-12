#include <Arduino.h> //podstawowa biblioteka
#include <FastLED.h>
#include "time.h"
#include "Counter.h"
#include "Disable.cpp"

namespace Counter {
    long GMTOFFSET;
    long GMTDAYLIGHTOFFSET;
    char* SERVERTIME;

    struct tm actualTime;
    long disableTimeInSec;
    Effect** effect;
    CRGB* leds;
    int NUM_LEDS;
    
    hw_timer_t* myTimer = NULL;
    
}

void Counter::printLocalTime() {
    if(!getLocalTime(&actualTime)) {
            Serial.println("Failed to obtain time");
        }

        Serial.println(&actualTime, "%H, %M, %S");
}

void Counter::checkIfDisableReady() {
    getLocalTime(&actualTime);
    Serial.println(actualTime.tm_sec);
    int actualTimeInSec = actualTime.tm_hour * 3600 + actualTime.tm_min * 60 + actualTime.tm_sec;
    Serial.println(actualTimeInSec);

    if (actualTimeInSec > disableTimeInSec && actualTimeInSec-disableTimeInSec < 100) {
        Effect* actualEffect = *effect;

        // actualEffect->changeBrightness(10);

        delete *effect;
        *effect = new Disable(leds, NUM_LEDS);
        // delete actualEffect;
        
        // actualEffect = new Disable(leds, NUM_LEDS);
        //effect = &actualEffect;
        disableCounter();
        Serial.println("disablewlaczane");
        }
}

void Counter::configureTimer(Effect** effect2, CRGB* leds2, int nums2) {
    effect = effect2;
    leds = leds2;
    NUM_LEDS = nums2;
    GMTOFFSET = 3600;
    GMTDAYLIGHTOFFSET = 0;
    SERVERTIME = "pool.ntp.org";
    configTime(GMTOFFSET, GMTDAYLIGHTOFFSET, SERVERTIME);
    myTimer = timerBegin(0, 160, true); // konfiguracja timera; wybor timera, prescaler i kierunek liczenia: up
    timerAttachInterrupt(myTimer, &checkIfDisableReady , true);

    timerAlarmWrite(myTimer, 10000000, true);
    printLocalTime();
}

void Counter::enableCounter() {
    timerAlarmEnable(myTimer);
}

void Counter::disableCounter() {
    timerAlarmDisable(myTimer);
}

void Counter::setDistanceTime(long x) {
    disableTimeInSec = x;
}