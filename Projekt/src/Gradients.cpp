#include "Gradients.h"
#include <FastLED.h>

DEFINE_GRADIENT_PALETTE( heatmap_gp ) {
  0,     0,  0,  0,   //black
128,   255,  0,  0,   //red
224,   255,255,  0,
254,   255, 255, 255,   //bright yellow
255,   255,255,255 }; //full white

DEFINE_GRADIENT_PALETTE( rgb_pallete ) {
0, 0, 0, 255,
85, 255, 0, 0,
170, 0, 255, 0,
255, 0, 0, 255
}; //full white

DEFINE_GRADIENT_PALETTE( sunset_pallete) {
0, 255, 112, 154,
170, 254, 225, 64,
244, 255, 112, 154,
255, 255, 112, 154
};

DEFINE_GRADIENT_PALETTE( nether_pallete ) {
    0, 0, 0, 0,
    128, 100, 100, 100,
    254, 75, 30, 220,
    255, 75, 30, 220
};

DEFINE_GRADIENT_PALETTE ( red_blue_pallete) {
    0, 255, 0, 0,
    128, 0, 0, 255,
    255, 255, 0, 0
};