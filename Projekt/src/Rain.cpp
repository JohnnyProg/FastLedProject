#ifndef RAIN_H
#define RAIN_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>
#include <ctime>

class Rain : public Effect
{
    CRGB* leds;
    const int NUM_LEDS;

public:
    Rain(int brightness,int speed, CRGB color, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        srand( time( NULL ) );
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
        this->color = color;
    };

    ~Rain() {
        
    }

    virtual void updateAndShow()
    {
        int liczba;
        for (int i = 0; i < 20; i++) {
            liczba = std::rand() % NUM_LEDS;
            leds[liczba] = color;
        }
        
        fadeToBlackBy(leds, NUM_LEDS, 15);
        // for(int i = 0; i < 8; i++) {
        //     blur1d(leds, NUM_LEDS, 64);
        // }
        blur1d(leds, NUM_LEDS, 64);
        delay(speed);
        FastLED.show();
    }

    void setSpeed(int speed)
    {
        this->speed = speed;
    }

    virtual void changeBrightness(int b) {
        if (b == 0)
            b = 3;
        //this->brightness = b;
        color.maximizeBrightness();
        int howLow = 256 - b;
        color.fadeLightBy(howLow);
    }

    virtual void changeSpeed(int s) {
        speed = s;
    }
    virtual void changeColor(CRGB a) {
        this->color = a;
    }
    void sendPayload(uint8_t* payload) {}
};

#endif