#ifndef RAINBOWFULL_H
#define RAINBOWFULL_H

#include <FastLED.h>
#include <list>
#include "Effect.cpp"

class RainbowFull : public Effect
{
    CRGB* leds;
    const int NUM_LEDS;
    int hueBegin = 0;

public:
    RainbowFull(int speed, int brightness, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
    };
    ~RainbowFull() {
        
    }
    virtual void updateAndShow()
    {
        for (int i = 0; i < NUM_LEDS; i++) {
            leds[i] = CHSV(hueBegin, 255, brightness);
        }
        delay(speed);
        FastLED.show();
        hueBegin++;
    }

    void setSpeed(int speed)
    {
        this->speed = speed;
    }

    virtual void changeBrightness(int b) {
        this->brightness = b;
    }

    virtual void changeSpeed(int s) {
        speed = s;
    }

    virtual void changeColor(CRGB a) {
    }
    void sendPayload(uint8_t* payload) {}
};

#endif