
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui_main import Ui_MainWindow
from ui_functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Opcja3.clicked.connect(lambda: FunctionsUI.name_of_button_clicked(self))

        self.ui.Opcja1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        self.ui.Opcja2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))


        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())