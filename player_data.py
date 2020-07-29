import sqlite3

from PyQt5 import QtWidgets


class player_data():

    bat = []
    bow = []
    wk = []
    ar = []
    teamName = ""
    point_used = 0
    wk_chack = 0
    cricketdb = sqlite3.connect('Fantasy_Cricket_database.db')
    cur = cricketdb.cursor()
    def NEWTeam_data():
        player_data.bat = []
        player_data.bow = []
        player_data.wk = []
        player_data.ar = []
        player_data.point_used = 0
        player_data.wk_chack = 0
        player_data.cur.execute("SELECT * FROM stats;")
        for temp in player_data.cur.fetchall():
            if temp[6] == 'BAT':
                player_data.bat.append([temp[0],temp[5],0])
            elif temp[6] == 'AR':
                player_data.ar.append([temp[0],temp[5],0])
            elif temp[6] == 'BWL':
                player_data.bow.append([temp[0],temp[5],0])
            else:
                player_data.wk.append([temp[0],temp[5],0])

    def OPENTeam_data():

        player_data.bat = []
        player_data.bow = []
        player_data.wk = []
        player_data.ar = []
        player_data.point_used = 0
        player_data.wk_chack = 0

        player_data.cur.execute("SELECT * FROM teams WHERE name==?;",(player_data.teamName,))
        playerList = []
        for temp in player_data.cur.fetchall():
            playerList.append(temp[1])

        player_data.cur.execute("SELECT * FROM stats;")
        for temp in player_data.cur.fetchall():
            if temp[0] not in playerList:
                if temp[6] == 'BAT':
                    player_data.bat.append([temp[0],temp[5],0])
                elif temp[6] == 'AR':
                    player_data.ar.append([temp[0],temp[5],0])
                elif temp[6] == 'BWL':
                    player_data.bow.append([temp[0],temp[5],0])
                else:
                    player_data.wk.append([temp[0],temp[5],0])
            else:
                if temp[6] == 'BAT':
                    player_data.point_used += temp[5]
                    player_data.bat.append([temp[0],temp[5],1])
                elif temp[6] == 'AR':
                    player_data.point_used += temp[5]
                    player_data.ar.append([temp[0],temp[5],1])
                elif temp[6] == 'BWL':
                    player_data.point_used += temp[5]
                    player_data.bow.append([temp[0],temp[5],1])
                else:
                    player_data.wk_chack = 1
                    player_data.point_used += temp[5]
                    player_data.wk.append([temp[0],temp[5],1])

    def SAVETeam_data():
        if player_data.teamName is not "":
            if player_data.wk_chack==1:
                player_data.cur.execute("DELETE FROM teams WHERE name=?;",(player_data.teamName,))
                player_data.cricketdb.commit()
                for temp in player_data.bat:
                    if temp[2]==1:
                        player_data.cur.execute("INSERT INTO teams VALUES(?,?,?);", (player_data.teamName,temp[0],temp[1]))
                for temp in player_data.bow:
                    if temp[2] == 1:
                        player_data.cur.execute("INSERT INTO teams VALUES(?,?,?);", (player_data.teamName,temp[0],temp[1]))
                for temp in player_data.wk:
                    if temp[2] == 1:
                        player_data.cur.execute("INSERT INTO teams VALUES(?,?,?);", (player_data.teamName,temp[0],temp[1]))
                for temp in player_data.ar:
                    if temp[2] == 1:
                        player_data.cur.execute("INSERT INTO teams VALUES(?,?,?);", (player_data.teamName,temp[0],temp[1]))
                player_data.cricketdb.commit()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Oops! You not select any wicket keeper')
                error_dialog.exec_()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oops! please select team')
            error_dialog.exec_()