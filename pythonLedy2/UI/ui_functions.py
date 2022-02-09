
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

