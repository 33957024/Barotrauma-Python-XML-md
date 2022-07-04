import sys
from Mainset import mainwindows
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainwindows()
    w.show()
    sys.exit(app.exec_())
