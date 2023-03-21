#ifndef TRAIN_H
#define TRAIN_H

#include "Effect.cpp"
#include <FastLED.h>
#include <list>

class Train : public Effect {
    int distance;
    std::list<CRGB> colors;
    CRGB* leds;
    const int NUM_LEDS;
    int border = 0;

public:
    Train(int speed, int brightness, int distance, CRGB* leds, int num_leds)
        : NUM_LEDS(num_leds)
    {
        this->brightness = brightness;
        if (brightness == 0)
            brightness = 3;
        //this->brightness = b;
        std::list<CRGB>::iterator p = colors.begin();
        while(p != colors.end()) {
            p->maximizeBrightness();
            int howLow = 256 - brightness;
            p->fadeLightBy(howLow);
            p++;
        }
        
        this->speed = speed;
        this->distance = distance;
        this->leds = leds;
    };
    ~Train() {
        
    }
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
        for (int i = 0; i < NUM_LEDS; i++) {
            if (i < border) {
                leds[i] = colors.front();
            } else {
                leds[i] = colors.back();
            }
        }
        border++;
        if (border == NUM_LEDS) {
            border = 0;
            CRGB tem = colors.front();
            colors.pop_front();
            colors.push_back(tem);
        }
        FastLED.show();
        Serial.print(speed);
        delay(speed);
        Serial.print("wykonal sie delay");
    }

    void changeSpeed(int speed)
    {
        this->speed = speed;
    }

    void changeBrightness(int b) {
        if (b == 0)
            b = 3;
        //this->brightness = b;
        std::list<CRGB>::iterator p = colors.begin();
        while(p != colors.end()) {
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

    }

    void changeColor(CRGB a) {
        this->color = a;
    }
    void sendPayload(uint8_t* payload) {}
};

#endif