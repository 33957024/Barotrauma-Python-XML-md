from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase
from sys import argv, exit
from xml.etree.ElementTree import (
    ElementTree
)


class MainWindows(QMainWindow):
    def __init__(self):
        # 自定义字体导入
        self.path = None
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')
        super(MainWindows, self).__init__()
        loadUi('UI/read.ui', self)

    def file(self):
        try:
            tree = ElementTree(file=self.path)
            a = tree.findall('./Affliction')
            for path in a:
                d = path.get('name')
                print('名字:' + d)
                b = path.get('identifier')
                print('ID:' + b)
        except:
            QMessageBox.warning(self, '错误', '路径或文件有问题捏')

    def read(self):
        path, file = QFileDialog.getOpenFileName(self, '选择文件', 'C:/', '效果XML-files(*.xml)')
        self.path = path
        QMessageBox.information(self, '确认路径', path)


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    Main.show()
    exit(app.exec_())
