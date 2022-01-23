#ifndef TRAINWITHMANYCOLORS_H
#define TRAINWITHMANYCOLORS_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>

class TrainsWithManyColors : public Effect {
    int distance;
    std::list<CRGB> colors;
    CRGB* leds;
    const int NUM_LEDS;
    long border = 0;
    int numberOfColors;

public:
    TrainsWithManyColors(int speed, int brightness, int distance, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        this->brightness = brightness;
        if (brightness == 0)
            brightness = 3;
        // this->brightness = b;
        std::list<CRGB>::iterator p = colors.begin();
        while (p != colors.end()) {
            p->maximizeBrightness();
            int howLow = 256 - brightness;
            p->fadeLightBy(howLow);
            p++;
        }

        this->speed = speed;
        this->distance = distance;
        this->leds = leds;
        numberOfColors = 0;
    };

    // virtual void updateAndShow()
    // {
    //     for (CRGB x : colors) {
    //         for (int i = 0; i < NUM_LEDS; i++) {
    //             leds[i] = x;
    //             FastLED.show();
    //             delay(100);
    //         }

    //     }
    // }

    virtual void updateAndShow()
    {
        int i = 0;
        while (i < NUM_LEDS) {
            for (CRGB x : colors) {
                for (int j = 0; j < distance; j++) {
                    if (i < NUM_LEDS) {
                        leds[(i+border)%(NUM_LEDS)] = x;
                        i++;
                    }
                }
            }
        }
        if(border % (NUM_LEDS + 5) == distance * 2) {
            border = 0;
        }
        FastLED.show();
        delay(speed);
        border++;
        /////////////////////
        //     for (int i = 0; i < NUM_LEDS; i++) {
        //         if (i < border) {
        //             leds[i] = colors.front();
        //         } else {
        //             leds[i] = colors.back();
        //         }
        //     }
        //     border++;
        //     if (border % (NUM_LEDS + 1) == 45) {
        //         border = 0;
        //         CRGB tem = colors.front();
        //         colors.pop_front();
        //         colors.push_back(tem);
        //     }
        //     FastLED.show();
        //     delay(speed);
        }

        void changeSpeed(int speed)
        {
            this->speed = speed;
        }

        void changeBrightness(int b)
        {
            if (b == 0)
                b = 3;
            // this->brightness = b;
            std::list<CRGB>::iterator p = colors.begin();
            while (p != colors.end()) {
                p->maximizeBrightness();
                int howLow = 256 - b;
                p->fadeLightBy(howLow);
                p++;
            }
        }

        void setDistance(int distance)
        {
            this->distance = distance;
        }

        void addColor(CRGB newColor)
        {
            newColor.maximizeBrightness();
            int howLow = 255 - this->brightness;
            newColor.fadeLightBy(howLow);
            colors.push_back(newColor);
            numberOfColors++;
        }

        virtual void changeColor(CRGB a) {
        }
    };

#endif