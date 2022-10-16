import re
import shutil
import traceback
from xml.etree.ElementTree import (
    Element, SubElement, ElementTree
)
from os import chdir, walk
from sys import argv, exit

from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        loadUi('NEW_UI/copygamefile.ui', self)
        self.file = None
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')
        self.setWindowIcon(QIcon('./NEW_UI/edit.ico'))
        self.gamepath = QFileDialog.getExistingDirectory(self, '打开游戏目录', 'C:')
        if self.gamepath is not None:
            try:
                chdir(self.gamepath)
                for root, dirs, files in walk('./TempMods_Download'):
                    for main_dir in dirs:
                        retext = 'Local_\w*'
                        re_find = re.search(retext, main_dir)
                        if re_find is not None:
                            # 匹配的结果为XXX.stringw
                            self.comboBox.addItem(re_find.string)
                        else:
                            pass
                    else:
                        pass

            except:
                print(traceback.print_exc())
                QMessageBox.warning(self, '错误', '异常错误!')
        else:
            QMessageBox.warning(self, '无效路径', '文件夹路径为空!')

    def main_setfile(self, text):
        print(text)
        self.file = text

    def main_repath(self):
        self.gamepath = QFileDialog.getExistingDirectory(self, '打开游戏目录', 'C:')

    def main_copy(self):
        self.comboBox.clear()
        if self.gamepath is not None:
            try:
                chdir(self.gamepath)
                for root, dirs, files in walk('./TempMods_Download'):
                    for main_dir in dirs:
                        retext = 'Local_\w*'
                        re_find = re.search(retext, main_dir)
                        if re_find is not None:
                            # 匹配的结果为XXX.stringw
                            self.comboBox.addItem(re_find.string)
                        else:
                            pass
                    else:
                        pass

            except:
                print(traceback.print_exc())
                QMessageBox.warning(self, '错误', '异常错误!')
        else:
            QMessageBox.warning(self, '无效路径', '文件夹路径为空!')

    def main_clear(self):
        self.comboBox.clear()

    def main_run(self):
        try:
            shutil.copytree('.\\TempMods_Download\\'+self.file, '.\\LocalMods\\'+self.file)
            QMessageBox.information(self, '复制完成!', '文件已经复制')
        except:
            print(traceback.print_exc())
            QMessageBox.warning(self, '复制失败', '请检查控制台?')


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    Main.show()
    exit(app.exec_())
