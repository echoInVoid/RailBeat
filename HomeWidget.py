# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from funcs import *

class SongWidget(QtWidgets.QWidget):
    def __init__(self, parent, icon, name, time, highScore):
        super().__init__(parent)
        self.setFixedSize(380,100)
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(20,10,20,10)
        self.layout.setObjectName("layout")
        
        self.icon = QtGui.QPixmap(icon)
        self.icon = self.icon.scaled(80,80)
        self.iconLabel = QtWidgets.QLabel(self)
        self.iconLabel.setFixedSize(80,80)
        self.iconLabel.setPixmap(self.icon)
        self.layout.addWidget(self.iconLabel)

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

    def paintEvent(self, event):
        opt = QtWidgets.QStyleOption()
        # PyQt5里，QStyleOption没有init这个接口，但init跟initForm的参数一样，都是传一个窗口指针，估计PyQt5把Qt里这两个接口整合了
        opt.initFrom(self)
        p = QtGui.QPainter(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, p, self)
        super().paintEvent(event)

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
        self.songsLayout.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.songsArea.setWidget(self.songs)
        self.mainLayout.addWidget(self.songsArea)

        self.importSong = QtWidgets.QPushButton(self.HomeWidget)
        self.importSong.setObjectName("importSong")
        self.mainLayout.addWidget(self.importSong)

        self.exitBtn = QtWidgets.QPushButton(self.HomeWidget)
        self.exitBtn.clicked.connect(self.exit)
        self.exitBtn.setObjectName("exit")
        self.mainLayout.addWidget(self.exitBtn)

        self.retranslateUi(self.HomeWidget)
        self.updateSongsList(".\\songs")
        QtCore.QMetaObject.connectSlotsByName(self.HomeWidget)

    def retranslateUi(self, HomeWidget):
        _translate = QtCore.QCoreApplication.translate
        self.HomeWidget.setWindowTitle(_translate("HomeWidget", "RailBeat"))
        self.importSong.setText(_translate("HomeWidget", "导入"))
        self.exitBtn.setText(_translate("HomeWidget", "退出"))

    def exit(self):
        sys.exit(0)

    def addSong(self, filePath):
        if os.path.exists(filePath):
            songData = readSong(filePath)
            if not songData: return
            songWid = SongWidget(self.songs, filePath+"\\icon.png", songData["name"], songData["time"], songData["highscore"])
            self.songsLayout.addWidget(songWid)

    def updateSongsList(self, filePath):
        for i in self.songsLayout.children():
            i.destroy()

        for i in readSongsList(filePath):
            self.addSong(filePath+'\\'+i)
        print(self.songs.children())