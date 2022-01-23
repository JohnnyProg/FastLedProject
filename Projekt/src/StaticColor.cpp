#ifndef STATICCOLOR_H
#define STATICCOLOR_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>

class StaticColor : public Effect
{
    CRGB* leds;
    const int NUM_LEDS;

public:
    StaticColor(int brightness, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        this->speed = 0;
        this->leds = leds;
        this->brightness = brightness;
        color = CRGB::Red;
    };

    virtual void updateAndShow()
    {
        for (int i = 0; i < NUM_LEDS; i++) {
            leds[i] = color;
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