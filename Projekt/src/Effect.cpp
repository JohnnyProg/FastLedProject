#ifndef EFFECT_H
#define EFFECT_H
#include <FastLED.h>

class Effect{
    protected:
        int speed;
        int brightness;
        CRGB color;

    public:
        virtual void updateAndShow();
        virtual void changeBrightness(int b);
        virtual void changeSpeed(int s);
        virtual void changeColor(CRGB color);
};

#endif