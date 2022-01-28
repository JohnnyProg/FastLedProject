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
        MainWindow.resize(802, 424)
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
        self.horizontalLayout_2.addWidget(self.frame)
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
        self.Opcja1 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.Opcja1.setMinimumSize(QtCore.QSize(100, 40))
        self.Opcja1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Opcja1.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rbg(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rbg(85, 170, 255);\n"
"\n"
"}")
        self.Opcja1.setObjectName("Opcja1")
        self.verticalLayout_3.addWidget(self.Opcja1)
        self.Opcja2 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.Opcja2.setMinimumSize(QtCore.QSize(100, 40))
        self.Opcja2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Opcja2.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rbg(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rbg(85, 170, 255);\n"
"\n"
"}")
        self.Opcja2.setObjectName("Opcja2")
        self.verticalLayout_3.addWidget(self.Opcja2)
        self.Opcja3 = QtWidgets.QPushButton(self.Frame_Menu_Bar)
        self.Opcja3.setMinimumSize(QtCore.QSize(100, 40))
        self.Opcja3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Opcja3.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rbg(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rbg(85, 170, 255);\n"
"\n"
"}")
        self.Opcja3.setObjectName("Opcja3")
        self.verticalLayout_3.addWidget(self.Opcja3)
        self.verticalLayout_2.addWidget(self.Frame_Menu_Bar, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.Frame_Menu)
        self.Frame_Pages = QtWidgets.QFrame(self.Frame_Content_Bar)
        self.Frame_Pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_Pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Pages.setObjectName("Frame_Pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Frame_Pages)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.Frame_Pages)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.Pages_Widget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Pages_Widget.addWidget(self.page_3)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.horizontalLayout.addWidget(self.Frame_Pages)
        self.verticalLayout.addWidget(self.Frame_Content_Bar)
        self.Frame_Content_Bar.raise_()
        self.Frame_Top_Bar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Opcja1.setText(_translate("MainWindow", "Opcja 1"))
        self.Opcja2.setText(_translate("MainWindow", "Opcja 2"))
        self.Opcja3.setText(_translate("MainWindow", "Opcja 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
