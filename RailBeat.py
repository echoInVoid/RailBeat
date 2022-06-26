from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import os
import time
import logging as log

from HomeWidget import HomeWidget
from settings import setting

def setUp():
    if not os.path.isdir(".\\logs"): os.mkdir(".\\logs") 
    log.basicConfig(filename='.\\logs\\%s.log'%time.strftime(r"%Y%m%d-%Hh-%Mm"), level=setting.logLevel, format=setting.LOG_FORMAT, filemode='w')

    log.info("Set-Up completed.")

def main():
    setUp()
    app = QApplication(sys.argv)
    mainWid = QMainWindow()
    mainWid.setFixedSize(600,800)
    mainWid.setWindowTitle("RailBeat")
    homeWid = HomeWidget()
    homeWid.setupUi(QWidget(mainWid))
    app.setStyleSheet(setting.styleSheet)
    mainWid.show()
    homeWid.HomeWidget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()