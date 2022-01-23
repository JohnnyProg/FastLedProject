#ifndef CHANGEFULLCOLORS_H
#define CHANGEFULLCOLORS_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>
#include <iterator>

class ChangeFullColors : public Effect {
    int distance;
    std::list<CRGB> colors;
    CRGB* leds;
    const int NUM_LEDS;
    long border = 0;
    int numberOfColors;
    int ticks = 5;
    bool chooseColor = true;

public:
    ChangeFullColors(int speed, int brightness, CRGB* leds, int num_leds)
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
        auto l_front = colors.begin();
        std::advance(l_front, border);
        for (int i = 0; i < NUM_LEDS; i++) {    
            leds[i] = *l_front;
        }
        Serial.print("border = ");
        Serial.println(border);
        Serial.print("Color = ");
        Serial.println(*l_front);
        border++;
        if(border == numberOfColors) {
            border = 0;
        }

        FastLED.show();
        delay(speed * 5);
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