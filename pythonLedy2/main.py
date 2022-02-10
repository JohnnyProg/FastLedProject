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

for i in range(0, 7):
    print(p.get_device_info_by_index(i))

SPEAKERS = p.get_default_output_device_info()["hostApi"]
print(SPEAKERS)
stream=p.open(format=pyaudio.paInt16,channels=2,rate=RATE,input=True,
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

# print("* recording")
#
# frames = []
# RECORD_SECONDS = 5
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# import wave
# wf = wave.open("plik1.wav", 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

def analize_EQ(data):
    fft_v = fft(data)
    lista_real = list(fft_v.real)
    # louder_low_frequency = max(lista_real[1], lista_real[2], lista_real[3])
    louder_low_frequency = max(lista_real[1], lista_real[2])
    m = abs(louder_low_frequency)
    # bass bust
    # m = translate(m, 0, 7018200, 10, 255)
    # lower bass
    m = translate(m, 0, 4018200, 10, 400)
    return m

def analize_volume(data):
    peak=np.average(np.abs(data))*2
    # bass busted values
    # m = translate(peak, 0, 30182, 10, 400)
    # avenged sevenfold tested
    m = translate(peak, 0, 30182, 10, 800)
    # testy inne
    # m = translate(peak, 0, 20182, 10, 250)
    # m = translate(peak, 0, 15182, 10, 250)
    #     # m = m - 50
    return m

DECREASE_BRIGHTNESS_SPEED = 5
while True:
    start = time.time()
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

    # equalizer
    m = analize_EQ(data)
    # m = analize_volume(data)

    if m > true_value:
        true_value = m
    elif m < true_value:
        true_value = true_value - DECREASE_BRIGHTNESS_SPEED
    #     3
    # zauważyłem że jeżeli nowa wartość jest mniejsza o 1 to i tak zmniejaszam o więcej; trzeba będzie zacząć porównywać te wartości
    if true_value >= 255:
        true_value = 255
    if(true_value < 40):
        true_value = 40
    s = "P" + str(true_value)
    end = time.time()
    ws.send(s)
    print(true_value)
    # time.sleep(0.001)
    # print(end-start)

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



while False:
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