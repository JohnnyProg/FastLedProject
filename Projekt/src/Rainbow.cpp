#ifndef RAINBOW_H
#define RAINBOW_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>

class Rainbow : public Effect {

    int distance;
    CRGB* leds;
    const int NUM_LEDS;
    int hueBegin = 0;

public:
    Rainbow(int speed, int brightness, int distance, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        this->speed = speed;
        this->distance = distance;
        this->leds = leds;
        this->brightness = brightness;
    };
    ~Rainbow() {

    }
    virtual void updateAndShow()
    {
            for (int i = 0; i < NUM_LEDS; i++) {
                leds[i] = CHSV(hueBegin + i * distance, 255, brightness);
            }
            delay(speed);
            FastLED.show();
            hueBegin++;
        
    }


    void changeBrightness(int b)
    {
        this->brightness = b;
    }

    void changeSpeed(int s)
    {
        speed = s;
    }

    void changeColor(CRGB a)
    {
    }
    void sendPayload(uint8_t* payload) {}
};

#endif