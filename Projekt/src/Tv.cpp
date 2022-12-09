#ifndef TV_H
#define TV_H

#include <FastLED.h>
#include "Effect.cpp"


class Tv : public Effect{
    protected:
        CRGB* leds;
        const int LEDS_BEGIN;
        const int LEDS_END;
        const int NUM_LEDS;

    public:
        Tv(int brightness, CRGB* leds, int ledsBegin, int ledsEnd, int numLeds)
        : LEDS_BEGIN(ledsBegin), LEDS_END(ledsEnd), NUM_LEDS(numLeds)
        {
            this->speed = 0;
            this->leds = leds;
            this->brightness = brightness;
            color = CRGB::Red;
            for (int i = 0; i < NUM_LEDS; i++)
            {
                leds[i] = CRGB(0, 0, 0);
            }
            
        };

        ~Tv() {

        }

        void updateAndShow() {
            // for (int i = LEDS_BEGIN; i < LEDS_END; i++) {
            //     leds[i] = color;
            // }
            // delay(speed);
            // FastLED.show();
        }
        void changeBrightness(int b) {};
        void changeSpeed(int s) {};
        void changeColor(CRGB color) {};
        void sendPayload(uint8_t* payload) {
            for (int i = 0; i < LEDS_END - LEDS_BEGIN; i++) {
                int r = static_cast<unsigned char>(payload[(i*3) + 1]);
                int g = static_cast<unsigned char>(payload[(i*3) + 2]);
                int b = static_cast<unsigned char>(payload[(i*3) + 3]);
                CRGB color = CRGB(r, g, b);
                leds[i + LEDS_BEGIN] = color;
            }
            FastLED.show();
        }
};

#endif