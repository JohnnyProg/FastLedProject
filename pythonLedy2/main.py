# import pyaudio
# import wave
# import os
#
# defaultframes = 512
#
# class textcolors:
#     if not os.name == 'nt':
#         blue = '\033[94m'
#         green = '\033[92m'
#         warning = '\033[93m'
#         fail = '\033[91m'
#         end = '\033[0m'
#     else:
#         blue = ''
#         green = ''
#         warning = ''
#         fail = ''
#         end = ''
#
# recorded_frames = []
# device_info = {}
# useloopback = False
# recordtime = 5
#
# #Use module
#
# p = pyaudio.PyAudio()
#
# #Set default to first in list or ask Windows
# try:
#     default_device_index = p.get_default_input_device_info()
# except IOError:
#     default_device_index = -1
# print(default_device_index)
# #Select Device
# print ("1",textcolors.blue + "Available devices:\n" + textcolors.end)
# for i in range(0, p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print (textcolors.green + str(info["index"]) + textcolors.end + ": \t %s \n \t %s \n" % (info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))
#
#     if default_device_index == -1:
#         default_device_index = info["index"]
#
# #Handle no devices available
# if default_device_index == -1:
#     print (textcolors.fail + "No device available. Quitting." + textcolors.end)
#     exit()
#
# print("awdawdaw")
# #Get input or default
# device_id = int(input("Choose device [" + textcolors.blue + str(default_device_index) + textcolors.end + "]: ") or default_device_index)
# print ("")
#
# #Get device info
# print("awdawdaw")
# try:
#     device_info = p.get_device_info_by_index(device_id)
# except IOError:
#     device_info = p.get_device_info_by_index(default_device_index)
#     print (textcolors.warning + "Selection not available, using default." + textcolors.end)
# print("test123")
# #Choose between loopback or standard mode
# is_input = device_info["maxInputChannels"] > 0
# is_wasapi = (p.get_host_api_info_by_index(device_info["hostApi"])["name"]).find("WASAPI") != -1
# if is_input:
#     print (textcolors.blue + "Selection is input using standard mode.\n" + textcolors.end)
# else:
#     if is_wasapi:
#         useloopback = True;
#         print (textcolors.green + "Selection is output. Using loopback mode.\n" + textcolors.end)
#     else:
#         print (textcolors.fail + "Selection is input and does not support loopback mode. Quitting.\n" + textcolors.end)
#         # exit()
#
# recordtime = int(input("Record time in seconds [" + textcolors.blue + str(recordtime) + textcolors.end + "]: ") or recordtime)
#
# #Open stream
# channelcount = device_info["maxInputChannels"] if (device_info["maxOutputChannels"] < device_info["maxInputChannels"]) else device_info["maxOutputChannels"]
# print("dane wejsciowe", channelcount, int(device_info["defaultSampleRate"]), defaultframes, device_info['index'], useloopback)
# stream = p.open(format = pyaudio.paInt16,
#                 channels = channelcount,
#                 rate = int(device_info["defaultSampleRate"]),
#                 input = True,
#                 frames_per_buffer = defaultframes,
#                 input_device_index = device_info["index"],
#                 as_loopback = useloopback)
#
# #Start Recording
# print (textcolors.blue + "Starting..." + textcolors.end)
#
# for i in range(0, int(int(device_info["defaultSampleRate"]) / defaultframes * recordtime)):
#     recorded_frames.append(stream.read(defaultframes))
#     print (".")
#
# print (textcolors.blue + "End." + textcolors.end)
# #Stop Recording
#
# stream.stop_stream()
# stream.close()
#
# #Close module
# p.terminate()
#
# filename = input("Save as [" + textcolors.blue + "out.wav" + textcolors.end + "]: ") or "out.wav"
#
# waveFile = wave.open(filename, 'wb')
# waveFile.setnchannels(channelcount)
# waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
# waveFile.setframerate(int(device_info["defaultSampleRate"]))
# waveFile.writeframes(b''.join(recorded_frames))
# waveFile.close()




# # TODO: cool idea: https://www.youtube.com/watch?v=lU1GVVU9gLU
# # TODO: cool idea: use Fire effect and when louder create more sparks
# # TODO: cool idea: every pixel is different frequency; louder is different Hue of brightness
# # TODO: cool idea: stereo mode
# # TODO: catch system/browser sound
# # TODO: create spectrum analizer
# # TODO: analize loudness of bass frequencies
# # TODO: analize loudness of whole sound
# # TODO: if its possible do it in max 0.03 seconds
# # TODO: figure out how to send clear bytes(not char) if need more speed
# # TODO: create some protocol to first send effect type and then only new values
# # //////////////////////////////////////////////
#
import pyaudio
import numpy as np
import time
import websocket
from scipy.interpolate import interp1d
from scipy.fftpack import fft, fftfreq

print("start")
# TV
CHUNK = 2**9
RATE = 48000
# słuchawki
# CHUNK = 2**10
# RATE = 44100

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

for i in range(0, 14):
    print(p.get_device_info_by_index(i))

SPEAKERS = p.get_default_output_device_info()["hostApi"]
print("speakers: ")
print(SPEAKERS)
# TV
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK,input_device_index=9, as_loopback = True)
# Słuchawki
# stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
#               frames_per_buffer=CHUNK,input_device_index=3, as_loopback = True)
# print("dane wejsciowe", channelcount, int(device_info["defaultSampleRate"]), defaultframes, device_info['index'], useloopback)


# , input_device_index=2
print("strea opened")

ws = websocket.WebSocket(0)
print("es")
ws.connect("ws://192.168.0.129:81")
print("connected")
true_value = 40
# data_for_fft_freq = np.fromstring(stream.read(CHUNK),dtype=np.int16)

# fft_freq = fftfreq(len(data_for_fft_freq), d=1/(RATE/CHUNK))
# fft_freq = fft_freq * CHUNK
# list_fft_freq = list(fft_freq)
# print(list_fft_freq[2])
max_volume_test = 0

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
    louder_low_frequency = max(lista_real[1], lista_real[2], lista_real[3])
    # louder_low_frequency = max(lista_real[1], lista_real[2])
    # louder_low_frequency = lista_real[0]
    m = abs(louder_low_frequency)
    # bass bust
    # m = translate(m, 0, 7018200, 10, 255)
    # lower bass
    m = translate(m, 0, 4018200, 10, 400)
    # print(m)
    return m

def analize_volume(data):
    peak=np.average(np.abs(data))*2
    # bass busted values
    # m = translate(peak, 0, 30182, 10, 400)
    # avenged sevenfold tested
    m = translate(peak, 0, 30182, 10, 7000)
    # testy inne
    # m = translate(peak, 0, 20182, 10, 250)
    # m = translate(peak, 0, 15182, 10, 250)
    #     # m = m - 50
    return m

DECREASE_BRIGHTNESS_SPEED = 10
while False:
    # start = time.time()
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

    # equalizer
    # m = analize_EQ(data)
    m = analize_volume(data)

    if m > true_value:
        true_value = m
    elif m < true_value:
        true_value = true_value - DECREASE_BRIGHTNESS_SPEED
    #     3
    # zauważyłem że jeżeli nowa wartość jest mniejsza o 1 to i tak zmniejaszam o więcej; trzeba będzie zacząć porównywać te wartości
    if true_value >= 255:
        true_value = 255
    if(true_value < 20):
        true_value = 20
    s = "P" + str(true_value)
    # end = time.time()
    # time.sleep(0.07)
    ws.send(s)
    print(true_value)

    # print(end-start)

# stream.stop_stream()
# stream.close()
# p.terminate()



# dont starve

# class Day:
#     def __init__(self, day, morning, afternoon, night):
#         self.morning = morning
#         self.afternoon = afternoon
#         self.night = night
#         self.day = day
#
#     def calculateEvening(self):
#         self.afternoon = 16 - self.morning - self.night
#
#     def printTimeStamp(self):
#         print("Day: " + str(self.day) + " Morning: " + str(self.morning) + " Afternoon: " + str(self.afternoon) + " Night: " + str(self.night))
#
# days = []
#
# # day
# for i in range(1, 70):
#     days.append(Day(i, 0, 0, 0))
#
# for i in range(0, 7):
#     days[i].morning = 9
#
# for i in range (7, 14):
#     days[i].morning = 8
#
# for i in range (14, 20):
#     days[i].morning = 7
#
# for i in range (20, 26):
#     days[i].morning = 6
#
# for i in range (26, 46):
#     days[i].morning = 5
#
# for i in range (46, 49):
#     days[i].morning = 6
#
# for i in range (49, 53):
#     days[i].morning = 7
#
# for i in range (53, 56):
#     days[i].morning = 8
#
# for i in range (56, 59):
#     days[i].morning = 9
#
# for i in range (59, 61):
#     days[i].morning = 10
#
# for i in range (61, 65):
#     days[i].morning = 11
#
# for i in range (65, 69):
#     days[i].morning = 10
#
# # night
# for i in range(0, 6):
#     days[i].night = 3
#
# for i in range(6, 13):
#     days[i].night = 2
#
# for i in range(13, 18):
#     days[i].night = 3
#
# for i in range(18, 22):
#     days[i].night = 4
#
# for i in range(22, 26):
#     days[i].night = 5
#
# for i in range(26, 31):
#     days[i].night = 6
#
# for i in range(31, 35):
#     days[i].night = 5
#
# for i in range(35, 41):
#     days[i].night = 4
#
# for i in range(41, 55):
#     days[i].night = 3
#
# for i in range(55, 66):
#     days[i].night = 4
#
# for i in range(66, 69):
#     days[i].night = 3
#
# for i in range(0, 69):
#     days[i].calculateEvening()
#
# def changeSmoothlyBrightness(old, new):
#     while old > new:
#         old = old - 0.7
#         ws.send("VB" + str(old))
#         print(old)
#         time.sleep(0)
#
# input("Press Enter to continue")
# start = time.time()
# actualDay = 17 - 1
# flag1 = True
# flag2 = False
# flag3 = False
#
# while True:
#     days[actualDay].printTimeStamp()
#     end = time.time()
#     print(end - start)
#     print(days[actualDay].morning * 30)
#     if (days[actualDay].morning * 30) < end-start and flag1:
#         print("cos weszlo")
#         changeSmoothlyBrightness(250, 80)
#         flag1 = False
#         flag2 = True
#
#     if days[actualDay].morning * 30 + days[actualDay].afternoon * 30 < end - start and flag2:
#         changeSmoothlyBrightness(80, 3)
#         flag2 = False
#         flag3 = True
#
#     if 60*8 < end - start and flag3:
#         changeSmoothlyBrightness(3, 250)
#         old = 3
#         while old < 250:
#             old = old + 0.7
#             ws.send("VB" + str(old))
#             print(old)
#             time.sleep(0)
#
#         flag3 = False
#         flag1 = True
#         start = time.time()
#     time.sleep(0.1)

from PIL import Image

import d3dshot
import time

d = d3dshot.create()
d.display = d.displays[1]
for i, x in enumerate(d.displays):
    print(i, ". ",x)

# screenshot = d.screenshot()
# # d.screenshot_to_disk()
# # screenshot.show()
#
# avrColor = screenshot.resize((1, 1))
# color = avrColor.getpixel((0, 0))
# print(color)
# print(chr(color[0]), chr(color[1]),chr(color[2]))
width = 1824
height = 1026
# width = 1920
# height = 1080

widthPadding = 0
heightPadding = 0

widthAmount = 45
heightAmount = 25

aspect_ratio = 21/9


ratio_height = height
ratio_width = width

# jezeli jest bardziej kinowe niz 16/9
if aspect_ratio > 1.77:
    ratio_height = width / aspect_ratio
    difference = height - ratio_height
    heightPadding = difference / 2
    # height = ratio_height
# jezeli jest bardziej kwadratowe
else:
    ratio_width = height * aspect_ratio
    difference = width - ratio_width
    widthPadding = difference / 2
    # width = ratio_width

print(f"ratio height: {ratio_height}, ratio width: {ratio_width}")
print(f"heightPadding: {heightPadding}, widthPadding: {widthPadding}")
widthStep = int(width / widthAmount)
heightStep = int(height / heightAmount)
print(widthStep, heightStep)

sum = 0
counter = 0
import numpy as np

def calculateColorsNumpy():

    screenshot = d.screenshot()
    screenshot_numpy = np.asarray(screenshot)
    averages = []


    for x in range(widthAmount):
        new = screenshot_numpy[:heightStep,x * widthStep: (x + 1) * widthStep,:]
        m_mean = new.mean(axis=(0, 1))
        averages.append(m_mean)
    for x in range(heightAmount):
        new = screenshot_numpy[x * heightStep:(x + 1) * heightStep, -1 * widthStep:, :]
        m_mean = new.mean(axis=(0, 1))
        averages.append(m_mean)
    for x in range(widthAmount-1, -1, -1):
        new = screenshot_numpy[-1 * heightStep:, x * widthStep: (x + 1) * widthStep, :]
        m_mean = new.mean(axis=(0, 1))
        averages.append(m_mean)
    for x in range(heightAmount-1, -1, -1):
        new = screenshot_numpy[x * heightStep:(x + 1) * heightStep, :widthStep, :]
        m_mean = new.mean(axis=(0, 1))
        averages.append(m_mean)


    print(f"done in {time.perf_counter() - start_time: .5f}")
    # messag = bytearray()
    # messag.append(85)
    # for x in boxes:
    #     # color = x.getpixel((0, 0))
    #     messag.append(x[0])
    #     messag.append(x[1])
    #     messag.append(x[2])





def calculateColorPILL():

    screenshot = d.screenshot()
    boxes = []
    index = 0
    for x in range(widthAmount-1, -1, -1):
        new = screenshot.crop((x * widthStep, height - heightStep, (x+1)*widthStep, height)).resize((1, 1))
        boxes.append(new.getpixel((0,0)))

        # dst.paste(new, (x * widthStep, height - heightStep))
    for x in range(heightAmount-1, -1, -1):
        new = screenshot.crop((0, x * heightStep, widthStep, (x+1) * heightStep)).resize((1, 1))
        boxes.append(new.getpixel((0,0)))
        # dst.paste(new, (0, x * heightStep) )
    for x in range(widthAmount):
        new = screenshot.crop((x * widthStep, 0, (x+1)*widthStep, heightStep)).resize((1, 1))
        boxes.append(new.getpixel((0,0)))
        # dst.paste(new, (x * widthStep, 0))
    for x in range(heightAmount):
        new = screenshot.crop((width - widthStep, x * heightStep, width, (x + 1) * heightStep)).resize((1, 1))
        boxes.append(new.getpixel((0, 0)))
        # dst.paste(new, (width - widthStep, x * heightStep))
#
# for _ in range(10):
#     messag = bytearray()
#     messag.append(85)
#     for x in range(215):
#         # color = x.getpixel((0, 0))
#         messag.append(int(0))
#         messag.append(int(0))
#         messag.append(int(0))
#
#     ws.send(messag)

def calculateWithNumpy2():

    screenshot = d.screenshot()
    screenshot_numpy = np.asarray(screenshot)
    averages = []
    up = screenshot_numpy[:heightStep, :, :]
    down = screenshot_numpy[-1 * heightStep:, :, :]
    left = screenshot_numpy[:, : widthStep, :]
    right = screenshot_numpy[:, : -1 * widthStep, :]
    # print(f"shape of up: {type(left)}")
    up_splitted = np.array_split(up, widthStep)
    down_splitted = np.array_split(down, widthStep)
    left_splitted = np.array_split(left, heightStep)
    rigth_splitted = np.array_split(right, heightStep)
    averages.append((x.mean(axis = (0, 1)) for x in up_splitted))
    averages.append((x.mean(axis=(0, 1)) for x in down_splitted))
    averages.append((x.mean(axis=(0, 1)) for x in left_splitted))
    averages.append((x.mean(axis=(0, 1)) for x in rigth_splitted))


times = np.empty(1000)
while True:
    # start_time = time.perf_counter()
    # calculateWithNumpy2()
    # time1 = time.perf_counter() - start_time
    # times[i] = time1
    screenshot = d.screenshot()
    boxes = []
    print("alskdjalks")
    for x in range(widthAmount - 1, -1, -1):
        new = screenshot.crop((x * widthStep, height - heightStep - heightPadding, (x + 1) * widthStep, height - heightPadding)).resize((1, 1))
        boxes.append(new.getpixel((0, 0)))

        # dst.paste(new, (x * widthStep, height - heightStep))
    for x in range(heightAmount - 1, -1, -1):
        new = screenshot.crop((0, x * heightStep, widthStep, (x + 1) * heightStep)).resize((1, 1))
        boxes.append(new.getpixel((0, 0)))
        # dst.paste(new, (0, x * heightStep) )
    for x in range(widthAmount):
        new = screenshot.crop((x * widthStep, heightPadding, (x + 1) * widthStep, heightStep + heightPadding)).resize((1, 1))
        boxes.append(new.getpixel((0, 0)))
        # dst.paste(new, (x * widthStep, 0))
    for x in range(heightAmount):
        new = screenshot.crop((width - widthStep, x * heightStep, width, (x + 1) * heightStep)).resize((1, 1))
        boxes.append(new.getpixel((0, 0)))
        # dst.paste(new, (width - widthStep, x * heightStep))

    messag = bytearray()
    messag.append(85)
    for x in boxes:
        # color = x.getpixel((0, 0))
        messag.append(x[0])
        messag.append(x[1])
        messag.append(x[2])

    ws.send(messag)

    # # flag = bytes('T', 'utf-8')
    # message = bytearray()
    # flaga = 'T'
    # message.append(84)
    # message.append(color[0])
    # message.append(color[1])
    # message.append(color[2])
    # print(message)
    # # print(type(message))
    # # print(message)
    # # print(color)
    #
    # # print(s)
    # ws.send(message)

    print(boxes[59])
    # print(end - start_time)
    # sum += time.time() - start_time
    # counter += 1

print(f"average = {times.mean()}")
print(f"std = {times.std()}")

ws.close