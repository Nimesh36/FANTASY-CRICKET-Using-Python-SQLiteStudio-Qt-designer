# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OPENTeam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

from player_data import player_data


class Ui_OPENTeam(object):
    def setupUi(self, OPENTeam):

        self.teamName = ""

        OPENTeam.setObjectName("OPENTeam")
        OPENTeam.resize(443, 265)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(OPENTeam)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(OPENTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(OPENTeam)
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

        self.pushButton = QtWidgets.QPushButton(OPENTeam)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.note = QtWidgets.QLabel(OPENTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.note.setFont(font)
        self.note.setText("")
        self.note.setObjectName("note")
        self.verticalLayout.addWidget(self.note)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.retranslateUi(OPENTeam)
        QtCore.QMetaObject.connectSlotsByName(OPENTeam)

    def retranslateUi(self, OPENTeam):
        _translate = QtCore.QCoreApplication.translate
        OPENTeam.setWindowTitle(_translate("OPENTeam", "OPENTeam"))
        self.label.setText(_translate("OPENTeam", "Enter team name : "))
        self.pushButton.setText(_translate("OPENTeam", "Open Team"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OPENTeam = QtWidgets.QWidget()
    ui = Ui_OPENTeam()
    ui.setupUi(OPENTeam)
    OPENTeam.show()
    sys.exit(app.exec_())

