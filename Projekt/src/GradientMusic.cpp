#ifndef GRADIENTMUSIC_H
#define GRADIENTMUSIC_H

#include "Effect.cpp"
#include "Gradients.h"
#include <FastLED.h>

class GradientMusic : public Effect {

    CRGB* leds;
    const int NUM_LEDS;
    int gradient;
    int paletteIndex;
    CRGBPalette16 myPal;

public:
    GradientMusic(int brightness, int gradient, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
        , gradient(gradient)
    {
        this->leds = leds;
        this->brightness = brightness;
        color = color;
        paletteIndex = 0;
    };

    virtual void updateAndShow()
    {
        myPal = heatmap_gp;
        for (int i = 0; i < NUM_LEDS; i++) {
            leds[i] = ColorFromPalette(myPal, brightness);
        }
        delay(speed);
        FastLED.show();
    }

    void setSpeed(int speed)
    {
        this->speed = speed;
    }

    virtual void changeBrightness(int b)
    {
        brightness = b;
    }

    virtual void changeSpeed(int s)
    {
        speed = s;
    }
    virtual void changeColor(CRGB a)
    {
        this->color = a;
    }
};

#endif