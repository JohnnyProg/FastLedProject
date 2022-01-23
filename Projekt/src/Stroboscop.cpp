#ifndef STROBOSCOP_H
#define STROBOSCOP_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>
#include <ctime>

class Stroboscop : public Effect
{
    CRGB* leds;
    const int NUM_LEDS;
    bool on;

public:
    Stroboscop(int brightness,int speed, CRGB color, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        srand( time( NULL ) );
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
        color = color;
        on = true;
    };

    virtual void updateAndShow()
    {
        if(on) {
            for (int i = 0; i < NUM_LEDS; i++) {
                leds[i] = CRGB(0, 0, 0);
            }
        }else {
            for (int i = 0; i < NUM_LEDS; i++) {
                leds[i] = color;
            }
        }
        on = !on;
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
};

#endif