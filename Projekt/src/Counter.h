#ifndef COUNTER_H
#define COUNTER_H

#include "time.h"
#include <Arduino.h>
#include "Effect.cpp"
#include <FastLED.h>

namespace Counter {
    extern long GMTOFFSET;
    extern long GMTDAYLIGHTOFFSET;
    extern char* SERVERTIME;

    extern struct tm actualTime; 
    extern long disableTimeInSec;
    extern hw_timer_t* myTimer;     //tworzenie zmiennej do konfiguracji timera

    extern Effect** effect;
    extern CRGB* leds;
    extern int NUM_LEDS;

    void printLocalTime();
    void checkIfDisableReady();
    void configureTimer(Effect**, CRGB*, int);
    void enableCounter();
    void disableCounter();
    void setDistanceTime(long);
}

#endif