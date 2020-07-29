# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from NEWTeam import Ui_NEWTeam
from OPENTeam import Ui_OPENTeam
from EVALUATETeam import Ui_EVALUATETeam
from player_data import player_data
import functions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 674)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.bat = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bat.setFont(font)
        self.bat.setObjectName("bat")
        self.horizontalLayout.addWidget(self.bat)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.bow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bow.setFont(font)
        self.bow.setObjectName("bow")
        self.horizontalLayout.addWidget(self.bow)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.ar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ar.setFont(font)
        self.ar.setObjectName("ar")
        self.horizontalLayout.addWidget(self.ar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.wk = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wk.setFont(font)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.point_used = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.point_used.setFont(font)
        self.point_used.setObjectName("point_used")
        self.horizontalLayout_6.addWidget(self.point_used)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.team_name = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_7.addWidget(self.team_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.players_widget_02 = QtWidgets.QListWidget(self.frame_2)
        self.players_widget_02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.players_widget_02.setObjectName("players_widget_02")
        self.verticalLayout_6.addWidget(self.players_widget_02)
        self.players_widget_02.itemDoubleClicked.connect(self.removelist2)

        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.point_available = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.point_available.setFont(font)
        self.point_available.setObjectName("point_available")
        self.horizontalLayout_5.addWidget(self.point_available)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.bat_button = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bat_button.setFont(font)
        self.bat_button.setObjectName("bat_button")
        self.horizontalLayout_4.addWidget(self.bat_button)
        self.bat_button.toggled.connect(self.bat_function)

        self.bow_button = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bow_button.setFont(font)
        self.bow_button.setObjectName("bow_button")
        self.horizontalLayout_4.addWidget(self.bow_button)
        self.bow_button.toggled.connect(self.bow_function)

        self.ar_button = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ar_button.setFont(font)
        self.ar_button.setObjectName("ar_button")
        self.horizontalLayout_4.addWidget(self.ar_button)
        self.ar_button.toggled.connect(self.ar_function)

        self.wk_button = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wk_button.setFont(font)
        self.wk_button.setObjectName("wk_button")
        self.horizontalLayout_4.addWidget(self.wk_button)
        self.wk_button.toggled.connect(self.wk_function)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.players_widget_01 = QtWidgets.QListWidget(self.frame)
        self.players_widget_01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.players_widget_01.setObjectName("players_widget_01")
        self.players_widget_01.itemDoubleClicked.connect(self.removelist1)

        self.verticalLayout_5.addWidget(self.players_widget_01)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.note = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.note.setFont(font)
        self.note.setText("")
        self.note.setObjectName("note")
        self.gridLayout.addWidget(self.note, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionNEW_Team.triggered.connect(self.newteam_function)

        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionOPEN_Team.triggered.connect(self.openteam_function)

        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.triggered.connect(self.saveteam_function)

        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEVALUATE_Team.triggered.connect(self.evaluateteam_function)

        self.menuManage_Team.addAction(self.actionNEW_Team)
        self.menuManage_Team.addAction(self.actionOPEN_Team)
        self.menuManage_Team.addAction(self.actionSAVE_Team)
        self.menuManage_Team.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.label_7.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.bat.setText(_translate("MainWindow", "##"))
        self.label_9.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.bow.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.ar.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.wk.setText(_translate("MainWindow", "##"))
        self.label_12.setText(_translate("MainWindow", "                      Points Used"))
        self.point_used.setText(_translate("MainWindow", "####"))
        self.label_15.setText(_translate("MainWindow", "                Team Name"))
        self.team_name.setText(_translate("MainWindow", "Displayed name"))
        self.label_11.setText(_translate("MainWindow", "              Points Available"))
        self.point_available.setText(_translate("MainWindow", "####"))
        self.bat_button.setText(_translate("MainWindow", "BAT"))
        self.bow_button.setText(_translate("MainWindow", "BOW"))
        self.ar_button.setText(_translate("MainWindow", "AR"))
        self.wk_button.setText(_translate("MainWindow", "WK"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def newteam_function(self):
        self.NEW_window = QtWidgets.QWidget()
        self.NEWTeamui = Ui_NEWTeam()
        self.NEWTeamui.setupUi(self.NEW_window)
        self.NEW_window.show()
        self.NEWTeamui.pushButton.clicked.connect(self.newteam_)

    def newteam_(self):
        player_data.teamName = self.NEWTeamui.lineEdit.text()
        if player_data.teamName is "":
            self.NEWTeamui.note.setText("*Pleas enter team name.")
            player_data.teamName = ""
        else:
            player_data.cur.execute("SELECT * FROM teams WHERE name==?",(player_data.teamName,))
            temp = player_data.cur.fetchone()
            if temp is not None:
                player_data.teamName = ""
                self.NEWTeamui.lineEdit.setText("")
                self.NEWTeamui.note.setText("*Team name already exist please enter different team name.")
            else:
                self.NEWTeamui.note.setText("*Team created successfully.")
                player_data.NEWTeam_data()
                self.update_detail()
                self.bat_button.setChecked(True)
                self.bow_button.setChecked(True)
                self.bat_button.setChecked(True)
                self.players_widget_02.clear()

    def openteam_function(self):
        self.OPEN_window = QtWidgets.QWidget()
        self.OPENTeamui = Ui_OPENTeam()
        self.OPENTeamui.setupUi(self.OPEN_window)
        self.OPEN_window.show()
        self.OPENTeamui.pushButton.clicked.connect(self.openteam_)

    def openteam_(self):
        player_data.teamName = self.OPENTeamui.lineEdit.text()
        if player_data.teamName is "":
            self.OPENTeamui.note.setText("*Pleas enter team name.")
            player_data.teamName = ""
        else:
            player_data.cur.execute("SELECT * FROM teams WHERE name==?",(player_data.teamName,))
            temp = player_data.cur.fetchone()
            if temp is None:
                player_data.teamName = ""
                self.OPENTeamui.lineEdit.setText("")
                self.OPENTeamui.note.setText("*Team name not exist please try again.")
            else:
                self.OPENTeamui.note.setText("*Team opened successfully.")
                player_data.OPENTeam_data()
                self.update_detail()
                self.bat_button.setChecked(True)
                self.bow_button.setChecked(True)
                self.bat_button.setChecked(True)
                self.players_widget_02.clear()
                for t in player_data.bat:
                    if t[2]==1:
                        self.players_widget_02.addItem(t[0])
                for t in player_data.bow:
                    if t[2]==1:
                        self.players_widget_02.addItem(t[0])
                for t in player_data.wk:
                    if t[2]==1:
                        self.players_widget_02.addItem(t[0])
                for t in player_data.ar:
                    if t[2]==1:
                        self.players_widget_02.addItem(t[0])

    def saveteam_function(self):
        if player_data.teamName is not "":
            if int(self.wk.text())+int(self.ar.text())+int(self.bow.text())+int(self.bat.text()) == 11:
                player_data.SAVETeam_data()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Oops! please select 11 players')
                error_dialog.exec_()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oops! please select team')
            error_dialog.exec_()

    def evaluateteam_function(self):
        self.EVALUATE_window = QtWidgets.QWidget()
        self.EVALUATETeamui = Ui_EVALUATETeam()
        self.EVALUATETeamui.setupUi(self.EVALUATE_window)
        self.EVALUATE_window.show()
        self.EVALUATETeamui.comboBox_2.currentTextChanged.connect(self.change)
        self.EVALUATETeamui.comboBox.currentTextChanged.connect(self.change_)
        self.EVALUATETeamui.pushButton.clicked.connect(self.evaluate_)

    def change(self):
        player_data.cur.execute("SELECT * FROM teams WHERE name=?;", (self.EVALUATETeamui.comboBox_2.currentText(),))
        player_ = []
        self.EVALUATETeamui.listWidget.clear()
        self.EVALUATETeamui.listWidget_2.clear()
        for temp in tuple(player_data.cur.fetchall()):
            self.EVALUATETeamui.listWidget.addItem(temp[1])
            player_.append(temp[1])
        if self.EVALUATETeamui.comboBox.currentIndex()!=0:
            for temp in player_:
                player_data.cur.execute("SELECT * FROM "+self.EVALUATETeamui.comboBox.currentText()+''' WHERE player="'''+temp+'''";''')
                self.EVALUATETeamui.listWidget_2.addItem(str(functions.score(player_data.cur.fetchone())))
        self.EVALUATETeamui.label_5.setText(' ##')

    def change_(self):
        self.EVALUATETeamui.listWidget_2.clear()
        if self.EVALUATETeamui.comboBox.currentIndex() != 0:
            player_data.cur.execute("SELECT * FROM teams WHERE name=?;", (self.EVALUATETeamui.comboBox_2.currentText(),))
            player_ = []
            for temp in tuple(player_data.cur.fetchall()):
                player_.append(temp[1])
            if self.EVALUATETeamui.comboBox_2.currentIndex() != 0:
                for temp in player_:
                    player_data.cur.execute("SELECT * FROM "+self.EVALUATETeamui.comboBox.currentText()+''' WHERE player="'''+temp+'''";''')
                    self.EVALUATETeamui.listWidget_2.addItem(str(functions.score(player_data.cur.fetchone())))
        self.EVALUATETeamui.label_5.setText(' ##')

    def evaluate_(self):
        if self.EVALUATETeamui.comboBox.currentIndex()==0:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oops! please select match.')
            error_dialog.exec_()
        elif self.EVALUATETeamui.comboBox_2.currentIndex()==0:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oops! please select team.')
            error_dialog.exec_()
        else:
            player_data.cur.execute("SELECT * FROM teams WHERE name=?;",(self.EVALUATETeamui.comboBox_2.currentText(),))
            player_ = []
            for temp in tuple(player_data.cur.fetchall()):
                player_.append(temp[1])
            score = 0
            for temp in player_:
                player_data.cur.execute("SELECT * FROM "+self.EVALUATETeamui.comboBox.currentText()+''' WHERE player="'''+temp+'''";''')
                t = functions.score(player_data.cur.fetchone())
                score += t
            self.EVALUATETeamui.label_5.setText(str(score))

    def bat_function(self):
        self.players_widget_01.clear()
        if player_data.teamName != "":
            for temp in player_data.bat:
                if temp[2]==0:
                    self.players_widget_01.addItem(temp[0])

    def bow_function(self):
        self.players_widget_01.clear()
        if player_data.teamName != "":
            for temp in player_data.bow:
                if temp[2]==0:
                    self.players_widget_01.addItem(temp[0])

    def ar_function(self):
        self.players_widget_01.clear()
        if player_data.teamName != "":
            for temp in player_data.ar:
                if temp[2]==0:
                    self.players_widget_01.addItem(temp[0])

    def wk_function(self):
        self.players_widget_01.clear()
        if player_data.teamName != "":
            for temp in player_data.wk:
                if temp[2]==0:
                    self.players_widget_01.addItem(temp[0])

    def update_detail(self):
        self.team_name.setText(player_data.teamName)
        counter = 0
        for temp in player_data.bat:
            counter += temp[2]
        self.bat.setText(str(counter))

        counter = 0
        for temp in player_data.bow:
            counter += temp[2]
        self.bow.setText(str(counter))

        counter = 0
        for temp in player_data.ar:
            counter += temp[2]
        self.ar.setText(str(counter))

        counter = 0
        for temp in player_data.wk:
            counter += temp[2]
        self.wk.setText(str(counter))

        self.point_used.setText(str(player_data.point_used))
        self.point_available.setText(str(1000-player_data.point_used))

    def removelist1(self, item):
        temp=self.players_widget_01.row(item)
        player_data.cur.execute("SELECT * FROM stats WHERE player=?;",(item.text(),))
        val = player_data.cur.fetchone()[5]
        for t in player_data.wk:
            if t[0]==item.text() and player_data.wk_chack==1:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Oops! You can select only one wicket keeper')
                error_dialog.exec_()
                break
        else:
            if val+player_data.point_used <= 1000:
                self.players_widget_01.takeItem(temp)
                self.players_widget_02.addItem(item.text())
                player_data.point_used += val
                self.point_used.setText(str(player_data.point_used))
                self.point_available.setText(str(1000 - player_data.point_used))
                for t in range(player_data.bat.__len__()):
                    if player_data.bat[t][0]==item.text():
                        player_data.bat[t][2]=1
                        break
                else:
                    for t in range(player_data.bow.__len__()):
                        if player_data.bow[t][0]==item.text():
                            player_data.bow[t][2]=1
                            break
                    else:
                        for t in range(player_data.ar.__len__()):
                            if player_data.ar[t][0]==item.text():
                                player_data.ar[t][2]=1
                                break
                        else:
                            for t in range(player_data.wk.__len__()):
                                if player_data.wk[t][0]==item.text():
                                    player_data.wk[t][2]=1
                                    player_data.wk_chack=1
                                    break
                self.update_detail()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Oops! You have only {} point'.format(1000-player_data.point_used))
                error_dialog.exec_()

    def removelist2(self, item):
        temp = self.players_widget_02.row(item)
        self.players_widget_02.takeItem(temp)
        if self.bat_button.isChecked():
            for t in player_data.bat:
                if t[0]==item.text():
                    self.players_widget_01.addItem(item.text())
                    break
        elif self.bow_button.isChecked():
                for t in player_data.bow:
                    if t[0] == item.text():
                        self.players_widget_01.addItem(item.text())
                        break
        elif self.wk_button.isChecked():
            for t in player_data.wk:
                if t[0]==item.text():
                    self.players_widget_01.addItem(item.text())
                    break
        elif self.ar_button.isChecked():
            for t in player_data.ar:
                if t[0]==item.text():
                    self.players_widget_01.addItem(item.text())
                    break
        for t in range(player_data.bat.__len__()):
            if player_data.bat[t][0] == item.text():
                player_data.bat[t][2] = 0
                player_data.point_used -= player_data.bat[t][1]
                break
        else:
            for t in range(player_data.bow.__len__()):
                if player_data.bow[t][0] == item.text():
                    player_data.bow[t][2] = 0
                    player_data.point_used -= player_data.bow[t][1]
                    break
            else:
                for t in range(player_data.ar.__len__()):
                    if player_data.ar[t][0] == item.text():
                        player_data.ar[t][2] = 0
                        player_data.point_used -= player_data.ar[t][1]
                        break
                else:
                    for t in range(player_data.wk.__len__()):
                        if player_data.wk[t][0] == item.text():
                            player_data.wk[t][2] = 0
                            player_data.point_used -= player_data.wk[t][1]
                            player_data.wk_chack=0
                            break
        self.point_used.setText(str(player_data.point_used))
        self.point_available.setText(str(1000 - player_data.point_used))
        self.update_detail()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

