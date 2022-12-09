#ifndef GRADIENTMOVING_H
#define GRADIENTMOVING_H

#include "Effect.cpp"
#include <FastLED.h>
#include "Gradients.h"

class GradientMoving : public Effect
{
    
    CRGB* leds;
    const int NUM_LEDS;
    int gradient;
    int paletteIndex;
    CRGBPalette16 myPal;

public:
    GradientMoving(int brightness, int speed, int gradient, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
        , gradient(gradient)
    {
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
        color = color;
        paletteIndex = 0;
    };
    ~GradientMoving() {
        
    }
    virtual void updateAndShow()
    {
        switch (gradient)
        {
        case 1:
            myPal = sunset_pallete;
            Serial.println("start");
            fill_palette(leds, NUM_LEDS, paletteIndex, 2, myPal, brightness, LINEARBLEND);
            break;
        case 2:
            Serial.print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            myPal = heatmap_gp;
            fill_palette(leds, NUM_LEDS, paletteIndex, 2, myPal, brightness, LINEARBLEND);
            break;
        case 3:
            Serial.print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            myPal = rgb_pallete;
            fill_palette(leds, NUM_LEDS, paletteIndex, 2, myPal, brightness, LINEARBLEND);
            break;
        case 4:
            Serial.print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            myPal = red_blue_pallete;
            fill_palette(leds, NUM_LEDS, paletteIndex, 2, myPal, brightness, LINEARBLEND);
            break;
        default:
            break;
        }

        for(int i = 0; i < 255; i++) {
                Serial.print("red: ");
                Serial.print(ColorFromPalette(myPal, i).red);
                Serial.print(" green: ");
                Serial.print(ColorFromPalette(myPal, i).green);
                Serial.print(" blue: ");
                Serial.println(ColorFromPalette(myPal, i).blue);
        }
        paletteIndex++;
        delay(speed);
        FastLED.show();
    }

    void setSpeed(int speed)
    {
        this->speed = speed;
    }

    virtual void changeBrightness(int b) {
        brightness = b;
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