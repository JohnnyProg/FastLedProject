#ifndef FIRE_H
#define FIRE_H

#include "Effect.cpp"
#include <FastLED.h>
#include <ctime>
#include <list>
#include "Gradients.h"

class Fire : public Effect {
    CRGB* leds;
    const int NUM_LEDS;
    int Size; // How many pixels the flame is total
    int Cooling; // Rate at which the pixels cool off
    int Sparks; // How many sparks will be attempted each frame
    int SparkHeight; // If created, max height for a spark
    int Sparking; // Probability of a spark each attempt
    bool bReversed; // If reversed we draw from 0 outwards
    bool bMirrored; // If mirrored we split and duplicate the drawing
    byte* heat;

    static const byte BlendSelf = 2;
    static const byte BlendNeighbor1 = 3;
    static const byte BlendNeighbor2 = 2;
    static const byte BlendNeighbor3 = 1;
    static const byte BlendTotal = (BlendSelf + BlendNeighbor1 + BlendNeighbor2 + BlendNeighbor3);
    CRGBPalette16 myPal = heatmap_gp;

public:
    Fire(int brightness, int speed, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        srand(time(NULL));
        this->speed = speed;
        this->leds = leds;
        this->brightness = brightness;
        color = color;

        ///////

        Size = num_leds+8;
        Cooling = 20;
        Sparks = 3;
        SparkHeight = 4;
        Sparking = 100;
        bReversed = true;
        bMirrored = true;

        if (bMirrored)
            Size = Size / 2;
        heat = new byte[num_leds+8] { 0 };
    };

    ~Fire()
    {
        Serial.print("ropoczety");
        delete[] heat;
        Serial.print("destruktor skonczony");
    }

    virtual void updateAndShow()
    {
        for (int i = 0; i < Size; i++)
            heat[i] = max(0L, heat[i] - random(0, ((Cooling * 10) / Size) + 2));

        for (int i = 0; i < Size; i++)
            heat[i] = (heat[i] * BlendSelf + heat[(i + 1) % Size] * BlendNeighbor1 + heat[(i + 2) % Size] * BlendNeighbor2 + heat[(i + 3) % Size] * BlendNeighbor3)
                / BlendTotal;

        for (int i = 0; i < Sparks; i++) {
            if (random(255) < Sparking) {
                int y = Size - 1 - random(SparkHeight);
                heat[y] =random(160, 255);
                // heat[y] =255;
            }
        } // Can roll over which actually looks good!

        for (int i = 0; i < Size; i++) {
            // CRGB color = HeatColor(heat[i]);
            CRGB color = ColorFromPalette(myPal, heat[i]);
            int j = bReversed ? (Size - i) : i;
            leds[j-0] = color;
            if(bMirrored) {
                leds[NUM_LEDS - j+0] = color;
            }
        }
        delay(speed);
        Serial.println("speed w efekcie ");
        Serial.println(speed);
        FastLED.show();
    }

    virtual void changeBrightness(int b)
    {
        Sparks = b / 33;
        if( Sparks == 0) {
            Sparks = 1;
        }
        // if (b == 0)
        //     b = 3;
        // // this->brightness = b;
        // color.maximizeBrightness();
        // int howLow = 256 - b;
        // color.fadeLightBy(howLow);
    }

    virtual void changeSpeed(int s)
    {
        speed = s;
    }
    virtual void changeColor(CRGB a)
    {
        this->color = a;
    }
    void sendPayload(uint8_t* payload) {}
};

#endif
