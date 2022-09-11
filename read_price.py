import traceback
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QFontDatabase, QIcon
from sys import argv, exit
from xml.etree.ElementTree import (
    ElementTree
)


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        loadUi('UI/read.ui', self)
        # 自定义字体导入
        self.identifier = None
        self.pricelist = []
        self.path2 = None
        self.path = None
        self.setWindowIcon(QIcon('./NEW_UI/edit.ico'))
        self.setWindowTitle('多功能行动编辑器')
        self.label_2.setText('注意：\nby:CTos\n喵~~\nV1.0.4')
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')

    def file(self):
        self.pricelist.clear()
        try:
            tree = ElementTree(file=self.path)
            tree2 = ElementTree(file=self.path2)
            a = tree.findall('./Item')
            for path in a:
                self.identifier = path.get('identifier')
                b = 'NULL'
                d = path.get('name')

                try:
                    b = path.find('Price').attrib.get('baseprice')
                except:
                    pass
                try:
                    d1 = tree2.find('entityname.' + self.identifier).text
                    b1 = tree2.find('entitydescription.' + self.identifier).text
                    name_lang = '翻译名字' + d1 + '翻译简介' + b1
                    name_file = '名字: ' + d + ' 价格: ' + b + '标识符' + path.get('identifier')
                    c = name_file + name_lang
                    self.pricelist.append(c)
                except:
                    pass

        except:
            print(traceback.print_exc())
            QMessageBox.warning(self, '错误', '路径或文件有问题捏')
        slm = QStringListModel()
        slm.setStringList(self.pricelist)
        self.listView.setModel(slm)

    def read(self):
        path, file = QFileDialog.getOpenFileName(self, '选择文件', 'C:/', '物品XML-files(*.xml)')
        self.path = path
        path2, file2 = QFileDialog.getOpenFileName(self, '选择语言', path, '语言XML-files(*.XML)')
        self.path2 = path2
        QMessageBox.information(self, '确认路径', '文件路径' + path + '\n语言路径:\n' + path2)


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    Main.show()
    exit(app.exec_())
