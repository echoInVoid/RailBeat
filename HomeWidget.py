# -*- coding: utf-8 -*-

import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from settings import setting

class SongWidget(QtWidgets.QWidget):
    def __init__(self, parent, icon, name, time, highScore):
        super().__init__(parent)
        self.setFixedSize(400,100)
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(20,10,20,10)
        self.layout.setObjectName("layout")
        
        self.icon = QtGui.QImage(icon)
        self.icon = self.icon.scaled(80,80)
        self.layout.addWidget(self.icon)

        self.infoLayout = QtWidgets.QVBoxLayout(self)
        self.infoLayout.setContentsMargins(10,5,10,5)
        self.infoLayout.setObjectName("infoLayout")
        self.layout.addLayout(self.infoLayout)

        self.name = QtWidgets.QLabel(name, self)
        self.infoLayout.addWidget(self.name)
        
        self.time = QtWidgets.QLabel(time, self)
        self.infoLayout.addWidget(self.time)

        self.highScore = QtWidgets.QLabel(str(highScore), self)
        self.infoLayout.addWidget(self.highScore)

class HomeWidget:
    def setupUi(self, HomeWidget: QtWidgets.QWidget):
        self.HomeWidget = HomeWidget

        self.HomeWidget.setObjectName("HomeWidget")
        self.HomeWidget.resize(600, 800)

        self.mainLayout = QtWidgets.QVBoxLayout(self.HomeWidget)
        self.mainLayout.setContentsMargins(100, 10, 100, 50)
        self.mainLayout.setObjectName("mainLayout")

        self.title = QtWidgets.QLabel(self.HomeWidget)
        self.title.setFixedSize(400,150)
        self.title.setAutoFillBackground(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setIndent(0)
        self.title.setObjectName("title")
        self.title.setPixmap(QtGui.QPixmap(".\\res\\title.png"))
        self.mainLayout.addWidget(self.title)

        self.songsArea = QtWidgets.QScrollArea(self.HomeWidget)
        self.songsArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songsArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.songsArea.setWidgetResizable(False)
        self.songsArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.songsArea.setObjectName("songsArea")
        self.songs = QtWidgets.QWidget()
        self.songs.setObjectName("songs")
        self.songs.setFixedSize(400,610)
        self.songsLayout = QtWidgets.QVBoxLayout(self.songs)
        self.songsArea.setWidget(self.songs)
        self.mainLayout.addWidget(self.songsArea)

        self.importSong = QtWidgets.QPushButton(self.HomeWidget)
        self.importSong.setObjectName("importSong")
        self.mainLayout.addWidget(self.importSong)

        self.exit = QtWidgets.QPushButton(self.HomeWidget)
        self.exit.setObjectName("exit")
        self.mainLayout.addWidget(self.exit)

        self.retranslateUi(self.HomeWidget)
        self.HomeWidget.setStyleSheet(setting.styleSheet)
        QtCore.QMetaObject.connectSlotsByName(self.HomeWidget)

    def retranslateUi(self, HomeWidget):
        _translate = QtCore.QCoreApplication.translate
        self.HomeWidget.setWindowTitle(_translate("HomeWidget", "RailBeat"))
        self.importSong.setText(_translate("HomeWidget", "导入歌曲"))
        self.exit.setText(_translate("HomeWidget", "退出"))

    def addSong(self, filePath):
        if os.path.exists(filePath):
            songData = json.load(filePath+"\\data.json")
            songWid = SongWidget(self.songs, filePath+"\\icon.png", songData["name"], songData["time"], songData["highScore"])
            self.songsLayout.addWidget(songWid)
