# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEWTeam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from player_data import player_data
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NEWTeam(object):
    def setupUi(self, NEWTeam):

        NEWTeam.setObjectName("NEWTeam")
        NEWTeam.resize(467, 222)
        self.gridLayout = QtWidgets.QGridLayout(NEWTeam)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(NEWTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(NEWTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton = QtWidgets.QPushButton(NEWTeam)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.note = QtWidgets.QLabel(NEWTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note.setFont(font)
        self.note.setText("")
        self.note.setObjectName("note")
        self.verticalLayout.addWidget(self.note)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)

        self.retranslateUi(NEWTeam)
        QtCore.QMetaObject.connectSlotsByName(NEWTeam)

    def retranslateUi(self, NEWTeam):
        _translate = QtCore.QCoreApplication.translate
        NEWTeam.setWindowTitle(_translate("NEWTeam", "NEW Team"))
        self.label.setText(_translate("NEWTeam", "Enter team name : "))
        self.pushButton.setText(_translate("NEWTeam", "Creat Team"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEWTeam = QtWidgets.QWidget()
    ui = Ui_NEWTeam()
    ui.setupUi(NEWTeam)
    NEWTeam.show()
    sys.exit(app.exec_())

