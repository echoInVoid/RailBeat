from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

from HomeWidget import HomeWidget

def main():
    app = QApplication(sys.argv)
    mainWid = QMainWindow()
    mainWid.setFixedSize(600,800)
    homeWid = HomeWidget()
    homeWid.setupUi(QWidget(mainWid))
    mainWid.show()
    homeWid.HomeWidget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()