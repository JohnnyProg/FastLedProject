
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui_main import Ui_MainWindow
from ui_functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtWidgets.QSizeGrip(self.ui.size_grip)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_maximize.clicked.connect(lambda: FunctionsUI.changeSizeOfWindow(self))

        def moveWindow(e):
            print("1")
            if self.isMaximized() == False:
                print("2")
                try:
                    if e.buttons() == QtCore.Qt.LeftButton:
                        print("3")
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
                except Exception as e:
                    print(e)

        self.ui.header.mouseMoveEvent = moveWindow
        self.ui.button_minimize_menu.clicked.connect(lambda: FunctionsUI.slideLeftMenu(self))


        # change of widgets
        self.ui.button_item1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.button_item2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.button_item3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        # self.ui.button_opcja3.clicked.connect(lambda: FunctionsUI.name_of_button_clicked(self))
        #
        # self.ui.button_opcja1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        # self.ui.button_opcja2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))


        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())