# -*- coding: utf-8 -*-
# python 3.8.7, Windows 10, 64 bit


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox # CHECK OUT QProgressDialog
import FindMattes as fm
import os
from os import listdir

import progressBar

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 22))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.inputLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.inputLabel.setObjectName("inputLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inputLabel)
        self.inputEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputEdit.setObjectName("inputEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 99, 391, 22))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.outputEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.outputEdit.setObjectName("outputEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.outputEdit)
        self.outputLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.outputLabel.setObjectName("outputLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.outputLabel)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(270, 69, 171, 22))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.vosEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.vosEdit.setObjectName("vosEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vosEdit)
        self.vosLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.vosLabel.setObjectName("vosLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vosLabel)
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 69, 121, 22))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ffEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.ffEdit.setObjectName("ffEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ffEdit)
        self.ffLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.ffLabel.setObjectName("ffLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ffLabel)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(140, 69, 121, 22))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lsEdit = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.lsEdit.setObjectName("lsEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lsEdit)
        self.lsLabel = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.lsLabel.setObjectName("lsLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lsLabel)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(340, 129, 81, 23))
        self.run.setObjectName("run")
        self.inputButton = QtWidgets.QToolButton(self.centralwidget)
        self.inputButton.setGeometry(QtCore.QRect(410, 10, 31, 21))
        self.inputButton.setObjectName("inputButton")
        self.outputButton = QtWidgets.QToolButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(410, 100, 31, 21))
        self.outputButton.setObjectName("outputButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # buttons
        self.run.clicked.connect(lambda: self.create_matte())
        self.inputButton.clicked.connect(lambda: self.open_input_finder())
        self.outputButton.clicked.connect(lambda: self.open_output_finder())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputEdit, self.outputEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoRoto"))
        self.inputLabel.setText(_translate("MainWindow", "Input folder:"))
        self.outputLabel.setText(_translate("MainWindow", "Output folder:"))
        self.vosLabel.setText(_translate("MainWindow", "Vertical output size:"))
        self.ffLabel.setText(_translate("MainWindow", "First frame:"))
        self.lsLabel.setText(_translate("MainWindow", "Last frame:"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.inputButton.setText(_translate("MainWindow", "..."))
        self.outputButton.setText(_translate("MainWindow", "..."))

        # My functions
    def create_matte(self):
        folderInput = self.inputEdit.text()
        folderOutput = self.outputEdit.text()
        vSize = self.vosEdit.text()

        # check if folderOutput actually exists, otherwise, create it
        if not os.path.exists(folderOutput):
            os.makedirs(folderOutput)

        # check is size is numbers only, otherwise, warn user about error
        if vSize.isdecimal():
            vSize = int(vSize)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Error: Invalid vertical output size!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        # for every image in folder (but in reality every file in folder...)
        imgList = listdir(folderInput)
        for img in imgList:
            inputName = folderInput + '/' + img

            # find lenght til imgname ends, add _autoMatte and then add the rest of the file name back
            imgNameEnd = img.find('.')
            outputName = img[:imgNameEnd] + '_autoMatte' + img[imgNameEnd:]

            outputName = folderOutput + '/' + outputName
            print(inputName, outputName, vSize)
            fm.createMatte(inputName, outputName, vSize)

            #formatting for percent
            imgNr = int(imgList.index(img))+1
            maxNr = int(len(imgList))
            percent = round(imgNr/maxNr*100)
            print(percent)

        print('done')


    def open_input_finder(self):
        folderPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.inputEdit.setText(folderPath)

        # fixing the output folder
        lastFolder = os.path.basename(folderPath)
        #outputPath = folderPath.replace(lastFolder, lastFolder + '_autoMatte')
        outputPath = self.replace_last(folderPath, lastFolder, lastFolder +'_autoMatte')
        self.outputEdit.setText(outputPath)


    def open_output_finder(self):
        folderpath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.outputEdit.setText(folderpath)


    # rpartition splits by the last part of what it is looking for
    # making it easy to change that part specifically to something else
    def replace_last(self, sourceString, oldString, newString):
        head, _separator, tail = sourceString.rpartition(oldString)
        return head + newString + tail


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
