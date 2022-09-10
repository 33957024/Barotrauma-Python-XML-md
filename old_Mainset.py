from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QComboBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from os import walk, mkdir
import configparser
from PyQt5.QtGui import QFontDatabase
from sys import argv, exit
from xml.etree.ElementTree import (
    Element, SubElement, ElementTree
)


class MainWindows(QMainWindow):
    def __init__(self):
        # 设置config.ini配置文件
        config = configparser.ConfigParser()
        # TODO:我觉得这里的版本号可以自动生成的
        config['run'] = {
            'initialization': '0',
            'version': '1.0.4'
        }
        config['path'] = {
            'game_path': 'None',
            'vanilla_path': 'None'
        }
        config.write(open('./config.ini', 'w', encoding='utf-8'))
        # 自定义字体导入
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')
        super(MainWindows, self).__init__()
        loadUi('UI/old-Main-window.ui', self)
        self.write_id = '0'
        self.write_name = '0'
        self.write_lang = 'a'
        self.write_about = '0'
        self.make_fabricatortime = '0'
        self.make_fabricator = 'a'
        self.make_deconstructor = '0'

    # 变量阵列
    def write_name(self, text):
        print("Name输入内容:" + text)
        self.write_name = text

    def write_id(self, text):
        print("Id输入内容为" + text)
        self.write_id = text

    def write_lang(self, text):
        print("Lang输入内容为" + text)
        self.write_lang = text

    def write_about(self, text):
        print("About输入内容为" + text)
        self.write_about = text

    def make_fabricatortime(self, text):
        self.make_fabricatortime = text

    def make_fabricator(self, text):
        self.make_fabricator = text

    def make_deconstructor(self, text):
        self.make_deconstructor = text

    # lang界面功能
    def write(self):
        if self.write_name != '0' and self.write_id != '0' and self.write_about != '0' and self.write_lang != '0':
            print('生成完成')
            with open('./ModFile/' + self.write_lang, 'a', encoding='utf-8') as B:
                B.write(
                    '\n' + '<entityname.' + self.write_id + '>' + self.write_name + '</entityname.' + self.write_id + '>'
                )
                B.write(
                    '\n' + '<entitydescription.' + self.write_id + '>' + self.write_about + '</entitydescription.' + self.write_id + '>'
                )
        else:
            Debug.bug('内容为空')
            Debug.show()
            print('内容有空，拒绝访问')

    def autofile(self):
        tree = ElementTree(file='./ModFile/Mods.xml')
        root = tree.getroot()
        SubElement(root, 'Items')
        SubElement(root[0], 'Mod')
        pass

    def make(self):
        pass
        tree = ElementTree(file='./ModFile/Mods.xml')
        root = tree.getroot()
        SubElement(root, 'Item')
        SubElement(root[0], 'Mod')
        root[0].attrib['name'] = Name
        root[0].attrib['Identifier'] = Identifier
        tree.write('./ModFile/Mods.xml')

    def aboutwindow(self):
        About.show()

    def read(self):
        # TODO: 这个模块将成为以后泛用路径读取的基础
        tree = ElementTree(file='./ModFile/filelist.xml')
        a = tree.findall('Item')
        for path in a:
            for name, path in path.attrib.items():
                print(path)


# 提供About窗口
class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        loadUi('UI/About.ui', self)
        config = configparser.ConfigParser()
        config_name = './config.ini'
        config.read(config_name, encoding='utf-8')
        version = config.get('run', 'version')
        self.label_2.setText(version)


# 提供Debug窗口
class Debug(QDialog):
    def __init__(self):
        super(Debug, self).__init__()
        loadUi('UI/Debug.ui', self)

    def bug(self, bug):
        text = '出现异常\n' + 'bug是' + bug + '\n请检查是否出现忘记输入，错误输入等原因\n如果非人为操作请在GitHub反馈给我'
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    About = AboutWindow()
    Debug = Debug()
    Main.show()
    exit(app.exec_())
