#ifndef DISABLE_H
#define DISABLE_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>
#include <ctime>

class Disable : public Effect
{
    CRGB* leds;
    const int NUM_LEDS;

public:
    Disable(CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        srand( time( NULL ) );
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
        color = color;
    };

    virtual void updateAndShow()
    {
        for (int i = 0; i < NUM_LEDS; i++)
        {
            leds[i] = CRGB(0, 0, 0);
        }
        
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