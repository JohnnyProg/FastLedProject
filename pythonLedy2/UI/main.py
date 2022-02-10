
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui_main import Ui_MainWindow
from ui_functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, server):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtWidgets.QSizeGrip(self.ui.size_grip)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # global interactions
        # right top corner buttons
        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_maximize.clicked.connect(lambda: FunctionsUI.changeSizeOfWindow(self))

        def moveWindow(e):
            if self.isMaximized() == False:
                try:
                    if e.buttons() == QtCore.Qt.LeftButton:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
                except Exception as e:
                    print(e)

        self.ui.header.mouseMoveEvent = moveWindow
        self.ui.button_minimize_menu.clicked.connect(lambda: FunctionsUI.slideLeftMenu(self))


        # change of widgets
        self.ui.button_item1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.button_item2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.button_item3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # connecton to server
        self.ui.pushButton_5.clicked.connect(lambda: server.connect())
    # page 1 interactions
        # dodanie efektów do przycisków
        self.ui.button_train.clicked.connect(lambda: server.send("Etrain"))
        self.ui.button_bounce.clicked.connect(lambda: server.send("Ebounce"))
        self.ui.button_static.clicked.connect(lambda: server.send("Estatic"))
        self.ui.button_gradient.clicked.connect(lambda: server.send("Egradientmovingrgb"))  #do dokończenia
        self.ui.button_gradient_music.clicked.connect(lambda: server.send("Egradientmusic"))
        self.ui.button_full_train.clicked.connect(lambda: server.send("Efullcolor"))

        self.ui.button_rainbow.clicked.connect(lambda: server.send("Erainbow"))
        self.ui.button_rainbow_2.clicked.connect(lambda: server.send("Erainbow2"))
        self.ui.button_rain.clicked.connect(lambda: server.send("Erain"))
        self.ui.button_fire.clicked.connect(lambda: server.send("Efire"))
        self.ui.button_stroboscop.clicked.connect(lambda: server.send("Estroboscop"))

        # slidery
        # self.ui.slider_speed.sliderReleased.connect(lambda: server.send("VB" + str(self.ui.slider_speed.value())))
        self.ui.slider_speed.valueChanged.connect(lambda: server.send("VB" + str(self.ui.slider_speed.value())))
        # self.ui.slider_brightness.sliderReleased.connect(lambda: server.send("VB" + str(self.ui.slider_brightness.value())))
        self.ui.slider_brightness.valueChanged.connect(lambda: server.send("VB" + str(self.ui.slider_brightness.value())))

        self.worker = VolumeAnalizerThread(server)
        self.ui.button_search.clicked.connect(lambda: self.evt_btnStart_clicked())

        self.show()

    def evt_btnStart_clicked(self):
        print("wykonuję się")
        if self.worker.flag1 == False:
            self.worker.flag1 = True
            self.worker.start()
        else:
            self.worker.flag1 = False
        print("costam")

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    server = ServerConnection()
    window = MainWindow(server)
    sys.exit(app.exec_())