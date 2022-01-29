# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 373)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Frame_Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Top_Bar.setMinimumSize(QtCore.QSize(0, 40))
        self.Frame_Top_Bar.setMaximumSize(QtCore.QSize(16777215, 45))
        self.Frame_Top_Bar.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.Frame_Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Top_Bar.setObjectName("Frame_Top_Bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Frame_Top_Bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.Frame_Top_Bar)
        self.frame.setMinimumSize(QtCore.QSize(100, 40))
        self.frame.setMaximumSize(QtCore.QSize(100, 40))
        self.frame.setStyleSheet("background-color: rgb(0, 76, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_2 = QtWidgets.QFrame(self.Frame_Top_Bar)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.Frame_Top_Bar)
        self.Frame_Content_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Content_Bar.setMinimumSize(QtCore.QSize(0, 40))
        self.Frame_Content_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_Content_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Content_Bar.setObjectName("Frame_Content_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Frame_Content_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Frame_Menu = QtWidgets.QFrame(self.Frame_Content_Bar)
        self.Frame_Menu.setMaximumSize(QtCore.QSize(100, 1080))
        self.Frame_Menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Frame_Menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Menu.setObjectName("Frame_Menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Frame_Menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Frame_Menu_Bar = QtWidgets.QFrame(self.Frame_Menu)
        self.Frame_Menu_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Menu_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Menu_Bar.setObjectName("Frame_Menu_Bar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Frame_Menu_Bar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_opcja1 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.button_opcja1.setMinimumSize(QtCore.QSize(100, 40))
        self.button_opcja1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.button_opcja1.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.button_opcja1.setObjectName("button_opcja1")
        self.verticalLayout_3.addWidget(self.button_opcja1)
        self.button_opcja2 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.button_opcja2.setMinimumSize(QtCore.QSize(100, 40))
        self.button_opcja2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.button_opcja2.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.button_opcja2.setObjectName("button_opcja2")
        self.verticalLayout_3.addWidget(self.button_opcja2)
        self.button_opcja3 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.button_opcja3.setMinimumSize(QtCore.QSize(100, 40))
        self.button_opcja3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.button_opcja3.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.button_opcja3.setObjectName("button_opcja3")
        self.verticalLayout_3.addWidget(self.button_opcja3)
        self.verticalLayout_2.addWidget(self.Frame_Menu_Bar, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.Frame_Menu)
        self.Frame_Pages = QtWidgets.QFrame(self.Frame_Content_Bar)
        self.Frame_Pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_Pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Pages.setObjectName("Frame_Pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Frame_Pages)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.Frame_Pages)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_sterowanie_dzwiekiem = QtWidgets.QLabel(self.page_1)
        self.label_sterowanie_dzwiekiem.setGeometry(QtCore.QRect(10, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_sterowanie_dzwiekiem.setFont(font)
        self.label_sterowanie_dzwiekiem.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_sterowanie_dzwiekiem.setScaledContents(False)
        self.label_sterowanie_dzwiekiem.setObjectName("label_sterowanie_dzwiekiem")
        self.button_glosnosc = QtWidgets.QPushButton(self.page_1)
        self.button_glosnosc.setGeometry(QtCore.QRect(20, 80, 91, 41))
        self.button_glosnosc.setObjectName("button_glosnosc")
        self.button_eq = QtWidgets.QPushButton(self.page_1)
        self.button_eq.setGeometry(QtCore.QRect(20, 160, 91, 41))
        self.button_eq.setObjectName("button_eq")
        self.comboBox_glosnosc_template = QtWidgets.QComboBox(self.page_1)
        self.comboBox_glosnosc_template.setGeometry(QtCore.QRect(150, 90, 101, 22))
        self.comboBox_glosnosc_template.setObjectName("comboBox_glosnosc_template")
        self.comboBox_eq_template = QtWidgets.QComboBox(self.page_1)
        self.comboBox_eq_template.setGeometry(QtCore.QRect(150, 170, 101, 22))
        self.comboBox_eq_template.setObjectName("comboBox_eq_template")
        self.Pages_Widget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_sterowanie_obrazem = QtWidgets.QLabel(self.page_3)
        self.label_sterowanie_obrazem.setGeometry(QtCore.QRect(20, 20, 151, 31))
        self.label_sterowanie_obrazem.setObjectName("label_sterowanie_obrazem")
        self.horizontalScrollBar_saturacja = QtWidgets.QScrollBar(self.page_3)
        self.horizontalScrollBar_saturacja.setGeometry(QtCore.QRect(10, 90, 160, 16))
        self.horizontalScrollBar_saturacja.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_saturacja.setObjectName("horizontalScrollBar_saturacja")
        self.horizontalScrollBar_hue = QtWidgets.QScrollBar(self.page_3)
        self.horizontalScrollBar_hue.setGeometry(QtCore.QRect(220, 90, 160, 16))
        self.horizontalScrollBar_hue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_hue.setObjectName("horizontalScrollBar_hue")
        self.graphicsView = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView.setGeometry(QtCore.QRect(460, 130, 51, 51))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(550, 130, 51, 51))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.Pages_Widget.addWidget(self.page_3)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.frame_pottom_bar = QtWidgets.QFrame(self.Frame_Pages)
        self.frame_pottom_bar.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_pottom_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pottom_bar.setObjectName("frame_pottom_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_pottom_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_pottom_bar)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_pottom_bar)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_pottom_bar)
        self.horizontalLayout.addWidget(self.Frame_Pages)
        self.verticalLayout.addWidget(self.Frame_Content_Bar)
        self.Frame_Content_Bar.raise_()
        self.Frame_Top_Bar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "connection"))
        self.button_opcja1.setText(_translate("MainWindow", "Opcja 1"))
        self.button_opcja2.setText(_translate("MainWindow", "Opcja 2"))
        self.button_opcja3.setText(_translate("MainWindow", "Opcja 3"))
        self.label_sterowanie_dzwiekiem.setText(_translate("MainWindow", "sterowanie dźwiękiem"))
        self.button_glosnosc.setText(_translate("MainWindow", "Głośność"))
        self.button_eq.setText(_translate("MainWindow", "EQ"))
        self.label_sterowanie_obrazem.setText(_translate("MainWindow", "sterowanie obrazem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
