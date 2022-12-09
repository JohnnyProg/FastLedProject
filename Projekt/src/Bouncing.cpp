#ifndef BOUNCING_H
#define BOUNCING_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>

class Bouncing : public Effect {

    CRGB* leds;
    const int NUM_LEDS;
    int position;
    int width;
    bool direction;
    int test123;

public:
    Bouncing(int speed, int brightness, CRGB color, CRGB* leds, int num_leds, int width)
        : NUM_LEDS(num_leds)
    {
        if (brightness == 10)
            brightness = 10;
        //this->brightness = b;
        color.maximizeBrightness();
        int howLow = 256 - brightness;
        color.fadeLightBy(howLow);
        this->color = color;
        this->speed = speed;
        this->leds = leds;
        this->width = width;
        position = 0;
        direction = true;
    }
    ~Bouncing() {
        
    }
    virtual void updateAndShow()
    {
        for (int i = 0; i < NUM_LEDS; i++) {
            // Serial.print(width);
            // Serial.print("\n");
            if (i > (position - width) && i < (position + width)) {
                leds[i] = color;
            } else {
                leds[i] = CRGB(0, 0, 0);
            }
        }
        if (direction) {
            position++;
        } else {
            position--;
        }
        if (position > NUM_LEDS || position < 1) {
            direction = !direction;
        }
        FastLED.show();
        delay(speed);
    }

    virtual void changeBrightness(int b)
    {
        if (b == 0)
            b = 3;
        //this->brightness = b;
        color.maximizeBrightness();
        int howLow = 256 - b;
        color.fadeLightBy(howLow);
    }

    virtual void changeSpeed(int s)
    {
        this->speed = s;
    }

    virtual void changeColor(CRGB a) {
        this->color = a;
    }
    void sendPayload(uint8_t* payload) {
        
    }
};
#endif