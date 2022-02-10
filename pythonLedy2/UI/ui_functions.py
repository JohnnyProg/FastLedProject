import time

import numpy as np
import websocket

from main import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt


class FunctionsUI(MainWindow):
    def nameOfClickedButton(window):
        print("aaa")
        try:
            nadawca = window.sender()
        except Exception as e:
            print(e)
        print(nadawca.text())
        print("szisz")

    def changeSizeOfWindow(window):
        if window.isMaximized():
            window.showNormal()
        else:
            window.showMaximized()

    def slideLeftMenu(window):
        width = window.ui.slide_menu_container.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        window.animation = QtCore.QPropertyAnimation(window.ui.slide_menu_container, b"maximumWidth")
        window.animation.setDuration(250)
        window.animation.setStartValue(width)
        window.animation.setEndValue(newWidth)
        window.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        window.animation.start()


class ServerConnection():

    def __init__(self):
        print("started")

    def connect(self):
        self.ws = websocket.WebSocket(0)
        print("es")
        self.ws.connect("ws://192.168.0.129:81")
        print("connected")

    def send(self, data):
        try:
            # print(data)
            self.ws.send(data)
            self.actualEffect = data
        except Exception as e:
            print(e)


class VolumeAnalizerThread(QtCore.QThread):
    def __init__(self, ws):
        QtCore.QThread.__init__(self)
        print("wykonuje się inicjator")
        self.flag1 = False
        self.CHUNK = 2 ** 10
        self.RATE = 44100
        self.true_value = 40
        self.DECREASE_BRIGHTNESS_SPEED = 5
        self.ws = ws
        import pyaudio
        p = pyaudio.PyAudio()
        print("pyaudio opened")

        for i in range(0, 7):
            print(p.get_device_info_by_index(i))

        SPEAKERS = p.get_default_output_device_info()["hostApi"]
        print(SPEAKERS)
        self.stream = p.open(format=pyaudio.paInt16, channels=2, rate=self.RATE, input=True,
                        frames_per_buffer=self.CHUNK, input_device_index=2)
        # , input_device_index=2
        print("stream opened")

    def run(self):
        print("start of run")
        while self.flag1 == True:
            start = time.time()
            data = np.fromstring(self.stream.read(self.CHUNK), dtype=np.int16)
            peak = np.average(np.abs(data)) * 2
            # bass busted values
            # m = translate(peak, 0, 30182, 10, 400)
            # avenged sevenfold tested

            m = self.translate(peak, 0, 30182, 10, 800)

            # testy inne
            # m = translate(peak, 0, 20182, 10, 250)
            # m = translate(peak, 0, 15182, 10, 250)
            #     # m = m - 50

            if m > self.true_value:
                true_value = m
            elif m < self.true_value:
                true_value = self.true_value - self.DECREASE_BRIGHTNESS_SPEED
            #     3
            # zauważyłem że jeżeli nowa wartość jest mniejsza o 1 to i tak zmniejaszam o więcej; trzeba będzie zacząć porównywać te wartości
            if true_value >= 255:
                true_value = 255
            if (true_value < 40):
                true_value = 40
            s = "P" + str(true_value)
            end = time.time()
            self.ws.send(s)
            print(true_value)
            # time.sleep(0.001)
            # print(end-start)
        print("end of run")

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return int(rightMin + (valueScaled * rightSpan))