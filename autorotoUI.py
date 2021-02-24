# -*- coding: utf-8 -*-
# python 3.8.7, Windows 10, 64 bit


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import FindMattes as fm
from os import listdir

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 276)
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
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 200, 391, 22))
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
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 431, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.motorbike = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.motorbike.setObjectName("motorbike")
        self.gridLayout.addWidget(self.motorbike, 2, 3, 1, 1)
        self.sheep = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.sheep.setObjectName("sheep")
        self.gridLayout.addWidget(self.sheep, 3, 1, 1, 1)
        self.pottedPlant = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.pottedPlant.setObjectName("pottedPlant")
        self.gridLayout.addWidget(self.pottedPlant, 3, 0, 1, 1)
        self.person = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.person.setObjectName("person")
        self.gridLayout.addWidget(self.person, 2, 4, 1, 1)
        self.sofa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.sofa.setObjectName("sofa")
        self.gridLayout.addWidget(self.sofa, 3, 2, 1, 1)
        self.tvMonitor = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.tvMonitor.setObjectName("tvMonitor")
        self.gridLayout.addWidget(self.tvMonitor, 3, 4, 1, 1)
        self.horse = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.horse.setObjectName("horse")
        self.gridLayout.addWidget(self.horse, 2, 2, 1, 1)
        self.train = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.train.setObjectName("train")
        self.gridLayout.addWidget(self.train, 3, 3, 1, 1)
        self.diningTable = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.diningTable.setObjectName("diningTable")
        self.gridLayout.addWidget(self.diningTable, 2, 0, 1, 1)
        self.dog = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.dog.setObjectName("dog")
        self.gridLayout.addWidget(self.dog, 2, 1, 1, 1)
        self.aeroplane = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.aeroplane.setObjectName("aeroplane")
        self.gridLayout.addWidget(self.aeroplane, 0, 0, 1, 1)
        self.bicycle = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bicycle.setObjectName("bicycle")
        self.gridLayout.addWidget(self.bicycle, 0, 1, 1, 1)
        self.bird = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bird.setObjectName("bird")
        self.gridLayout.addWidget(self.bird, 0, 2, 1, 1)
        self.boat = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.boat.setObjectName("boat")
        self.gridLayout.addWidget(self.boat, 0, 3, 1, 1)
        self.bottle = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bottle.setObjectName("bottle")
        self.gridLayout.addWidget(self.bottle, 0, 4, 1, 1)
        self.bus = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.bus.setObjectName("bus")
        self.gridLayout.addWidget(self.bus, 1, 0, 1, 1)
        self.car = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.car.setObjectName("car")
        self.gridLayout.addWidget(self.car, 1, 1, 1, 1)
        self.cat = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cat.setObjectName("cat")
        self.gridLayout.addWidget(self.cat, 1, 2, 1, 1)
        self.chair = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.chair.setObjectName("chair")
        self.gridLayout.addWidget(self.chair, 1, 3, 1, 1)
        self.cow = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cow.setObjectName("cow")
        self.gridLayout.addWidget(self.cow, 1, 4, 1, 1)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(270, 170, 171, 22))
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
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 170, 121, 22))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        # Commented out, because first and last frame functionality wont be a thing for a while
        # ----------
        # self.ffEdit = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        # self.ffEdit.setObjectName("ffEdit")
        # self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ffEdit)
        # self.ffLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        # self.ffLabel.setObjectName("ffLabel")
        # self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ffLabel)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(140, 170, 121, 22))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        
        # Commented out, because first and last frame functionality wont be a thing for a while
        # ----------
        # self.lsEdit = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        # self.lsEdit.setObjectName("lsEdit")
        # self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lsEdit)
        # self.lsLabel = QtWidgets.QLabel(self.formLayoutWidget_5)
        # self.lsLabel.setObjectName("lsLabel")
        # self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lsLabel)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(340, 230, 81, 23))
        self.run.setObjectName("run")
        self.inputButton = QtWidgets.QToolButton(self.centralwidget)
        self.inputButton.setGeometry(QtCore.QRect(410, 10, 31, 21))
        self.inputButton.setObjectName("inputButton")
        self.outputButton = QtWidgets.QToolButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(410, 200, 31, 21))
        self.outputButton.setObjectName("outputButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 151, 431, 20))
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
        MainWindow.setTabOrder(self.inputEdit, self.aeroplane)
        MainWindow.setTabOrder(self.aeroplane, self.bicycle)
        MainWindow.setTabOrder(self.bicycle, self.bird)
        MainWindow.setTabOrder(self.bird, self.boat)
        MainWindow.setTabOrder(self.boat, self.bottle)
        MainWindow.setTabOrder(self.bottle, self.bus)
        MainWindow.setTabOrder(self.bus, self.car)
        MainWindow.setTabOrder(self.car, self.cat)
        MainWindow.setTabOrder(self.cat, self.chair)
        MainWindow.setTabOrder(self.chair, self.cow)
        MainWindow.setTabOrder(self.cow, self.diningTable)
        MainWindow.setTabOrder(self.diningTable, self.dog)
        MainWindow.setTabOrder(self.dog, self.horse)
        MainWindow.setTabOrder(self.horse, self.motorbike)
        MainWindow.setTabOrder(self.motorbike, self.person)
        MainWindow.setTabOrder(self.person, self.pottedPlant)
        MainWindow.setTabOrder(self.pottedPlant, self.sheep)
        MainWindow.setTabOrder(self.sheep, self.sofa)
        MainWindow.setTabOrder(self.sofa, self.train)
        MainWindow.setTabOrder(self.train, self.tvMonitor)
        MainWindow.setTabOrder(self.tvMonitor, self.outputEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoRoto"))
        self.inputLabel.setText(_translate("MainWindow", "Input folder:"))
        self.outputLabel.setText(_translate("MainWindow", "Output folder:"))
        self.motorbike.setStatusTip(_translate("MainWindow", "(64, 128, 128)"))
        self.motorbike.setText(_translate("MainWindow", "Motorbike"))
        self.sheep.setStatusTip(_translate("MainWindow", "(128, 64, 0)"))
        self.sheep.setText(_translate("MainWindow", "Sheep"))
        self.pottedPlant.setStatusTip(_translate("MainWindow", "(0, 64, 0)"))
        self.pottedPlant.setText(_translate("MainWindow", "Potted Plant"))
        self.person.setStatusTip(_translate("MainWindow", "(192, 128, 128)"))
        self.person.setText(_translate("MainWindow", "Person"))
        self.sofa.setStatusTip(_translate("MainWindow", "(0, 192, 0)"))
        self.sofa.setText(_translate("MainWindow", "Sofa"))
        self.tvMonitor.setStatusTip(_translate("MainWindow", "(0, 64, 128)"))
        self.tvMonitor.setText(_translate("MainWindow", "Tv/Monitor"))
        self.horse.setStatusTip(_translate("MainWindow", "(192, 0, 128)"))
        self.horse.setText(_translate("MainWindow", "Horse"))
        self.train.setStatusTip(_translate("MainWindow", "(128, 192, 0)"))
        self.train.setText(_translate("MainWindow", "Train"))
        self.diningTable.setStatusTip(_translate("MainWindow", "(192, 128, 0)"))
        self.diningTable.setText(_translate("MainWindow", "Dining Table"))
        self.dog.setStatusTip(_translate("MainWindow", "(64, 0, 128)"))
        self.dog.setText(_translate("MainWindow", "Dog"))
        self.aeroplane.setStatusTip(_translate("MainWindow", "(128, 0, 0)"))
        self.aeroplane.setText(_translate("MainWindow", "Aeroplane"))
        self.bicycle.setStatusTip(_translate("MainWindow", "(0, 128, 0)"))
        self.bicycle.setText(_translate("MainWindow", "Bicycle"))
        self.bird.setStatusTip(_translate("MainWindow", "(128, 128, 0)"))
        self.bird.setText(_translate("MainWindow", "Bird"))
        self.boat.setStatusTip(_translate("MainWindow", "(0, 0, 128)"))
        self.boat.setText(_translate("MainWindow", "Boat"))
        self.bottle.setStatusTip(_translate("MainWindow", "(128, 0, 128)"))
        self.bottle.setText(_translate("MainWindow", "Bottle"))
        self.bus.setStatusTip(_translate("MainWindow", "(0, 128, 128)"))
        self.bus.setText(_translate("MainWindow", "Bus"))
        self.car.setStatusTip(_translate("MainWindow", "(128, 128, 128)"))
        self.car.setText(_translate("MainWindow", "Car"))
        self.cat.setStatusTip(_translate("MainWindow", "(64, 0, 0)"))
        self.cat.setText(_translate("MainWindow", "Cat"))
        self.chair.setStatusTip(_translate("MainWindow", "(192, 0, 0)"))
        self.chair.setText(_translate("MainWindow", "Chair"))
        self.cow.setStatusTip(_translate("MainWindow", "(64, 128, 0)"))
        self.cow.setText(_translate("MainWindow", "Cow"))
        self.vosLabel.setText(_translate("MainWindow", "Vertical output size:"))
        #self.ffLabel.setText(_translate("MainWindow", "First frame:"))
        #self.lsLabel.setText(_translate("MainWindow", "Last frame:"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.inputButton.setText(_translate("MainWindow", "..."))
        self.outputButton.setText(_translate("MainWindow", "..."))

        # My functions
    def create_matte(self):
        folderInput = self.inputEdit.text()
        folderOutput = self.outputEdit.text()
        vSize = self.vosEdit.text()

        if vSize.isdecimal():
            vSize = int(vSize)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Error: Invalid vertical output size!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        # for every image in folder (but in reality every image)
        imgList = listdir(folderInput)
        for img in imgList:
            inputName = folderInput + '/' + img

            # find lenght til imgname ends, add _autoMatte and then add the rest of the file name back
            imgNameEnd = img.find('.')
            outputName = img[:imgNameEnd] + '_autoMatte' + img[imgNameEnd:]

            outputName = folderOutput + '/' + outputName
            print(inputName, outputName, vSize)
            fm.createMatte(inputName, outputName, vSize)
            print('done')

    def open_input_finder(self):
        folderpath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.inputEdit.setText(folderpath)
        self.outputEdit.setText(folderpath)

    def open_output_finder(self):
        folderpath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.outputEdit.setText(folderpath)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
