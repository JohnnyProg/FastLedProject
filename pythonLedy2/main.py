# TODO: cool idea: https://www.youtube.com/watch?v=lU1GVVU9gLU
# TODO: cool idea: use Fire effect and when louder create more sparks
# TODO: cool idea: every pixel is different frequency; louder is different Hue of brightness
# TODO: cool idea: stereo mode
# TODO: catch system/browser sound
# TODO: create spectrum analizer
# TODO: analize loudness of bass frequencies
# TODO: analize loudness of whole sound
# TODO: if its possible do it in max 0.03 seconds
# TODO: figure out how to send clear bytes(not char) if need more speed
# TODO: create some protocol to first send effect type and then only new values
# //////////////////////////////////////////////

import pyaudio
import numpy as np
import time
import websocket
from scipy.interpolate import interp1d
from scipy.fftpack import fft, fftfreq

CHUNK = 2**10
RATE = 44100

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))

p=pyaudio.PyAudio()
print("pyaudio opened")

# for i in range(0, 10):
#     print(p.get_device_info_by_index(i))

stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK, input_device_index=2)
# , input_device_index=2
print("strea opened")

ws = websocket.WebSocket(0)
print("es")
ws.connect("ws://192.168.0.129:81")
print("connected")
true_value = 40
data_for_fft_freq = np.fromstring(stream.read(CHUNK),dtype=np.int16)
fft_freq = fftfreq(len(data_for_fft_freq), d=1/(RATE/CHUNK))
fft_freq = fft_freq * CHUNK
list_fft_freq = list(fft_freq)
print(list_fft_freq[2])
max_volume_test = 0

def analize_EQ(data):
    fft_v = fft(data)
    lista_real = list(fft_v.real)
    louder_low_frequency = max(lista_real[1], lista_real[2], lista_real[3])
    m = abs(louder_low_frequency)
    # bass bust
    # m = translate(m, 0, 7018200, 10, 255)
    # lower bass
    m = translate(m, 0, 4018200, 10, 255)
    return m

def analize_volume(data):
    peak=np.average(np.abs(data))*2
    # bass busted values
    m = translate(peak, 0, 30182, 10, 400)
    # avenged sevenfold tested
    # m = translate(peak, 0, 30182, 10, 800)
    # testy inne
    # m = translate(peak, 0, 20182, 10, 800)
    # m = translate(peak, 0, 5182, 10, 1000)
    # m = m - 50
    return m

zmiennatest = 1
while True:
    start = time.time()
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

    # equalizer
    # m = analize_EQ(data)
    m = analize_volume(data)

    # peak=np.average(np.abs(data))*2
    # bass busted values
    # m = translate(peak, 0, 30182, 10, 400)
    # avenged sevenfold tested
    # m = translate(peak, 0, 30182, 10, 800)

    if m > true_value:
        true_value = m
    elif m < true_value:
        true_value = true_value - 3
    #     3

    if true_value >= 255:
        true_value = 255
    if(true_value < 40):
        true_value = 40
    s = "P" + str(true_value)
    end = time.time()
    # print(end-start)
    ws.send(s)
    print(true_value)
    # time.sleep(0.001)

stream.stop_stream()
stream.close()
p.terminate()

import d3dshot
import PIL

d = d3dshot.create()

screenshot = d.screenshot()
# d.screenshot_to_disk()
# screenshot.show()

avrColor = screenshot.resize((1, 1))
color = avrColor.getpixel((0, 0))
print(color)
print(chr(color[0]), chr(color[1]),chr(color[2]))



while True:
    start = time.time()
    screenshot = d.screenshot()
    avrColor = screenshot.resize((1, 1))
    color = avrColor.getpixel((0, 0))
    # print(color)
    # s ="T" + chr(color[0]) + chr(color[1]) + chr(color[2])
    # print(tablica)

    # flag = bytes('T', 'utf-8')
    message = bytearray()
    flaga = 'T'
    message.append(84)
    message.append(color[0])
    message.append(color[1])
    message.append(color[2])
    print(message)
    # print(type(message))
    # print(message)
    # print(color)

    # print(s)
    ws.send(message)
    # end = time.time()
    # print(end - start)


ws.close