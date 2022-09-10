from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
import configparser
from PyQt5.QtGui import QFontDatabase
from sys import argv, exit
from xml.etree.ElementTree import (
    Element, SubElement, ElementTree
)
import time


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        loadUi('UI/read-window.ui', self)
        # 变量集
        self.read_combo = None
        self.read_id = None
        self.read_name = None
        self.path = r'./filelist.xml'
        self.list_2 = [
            'Submarine', 'BeaconStation', 'EnemySubmarine', 'Outpost', 'OutpostModule', 'Wreck', 'Item',
            'Character', 'Afflictions', 'BackgroundCreaturePrefabs', 'BallastFlora', 'CaveGenerationParameters',
            'Corpses', 'Decals', 'EventManagerSettings', 'Factions', 'ItemAssembly', 'Jobs',
            'LevelGenerationParameters', 'LevelObjectPrefabs', 'LocationTypes', 'MapGenerationParameters',
            'Missions', 'NPCConversations', 'NPCSets', 'Orders', 'OutpostConfig', 'Particles', 'RandomEvents',
            'RuinConfig', 'ServerExecutable', 'SkillSettings', 'Sounds', 'Structure', 'Talents', 'TalentTrees',
            'Text', 'TraitorMissions', 'UIStyle', 'UpgradeModules', 'WreckAIConfig', 'Other'
        ]
        self.e1 = None
        self.e2 = None
        # 添加自定义字体
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')

    def read_name(self, text):
        print("Name输入内容:" + text)
        self.read_name = text

    def read_id(self, text):
        print("combox2输入内容为" + text)
        self.read_id = text

    def read_combo(self, text):
        print("combox输入内容为" + text)
        self.read_combo = text

    def read(self):
        tree = ElementTree(file='./Content/preg/preg_items.xml')
        a = tree.findall('./Item')
        for b in a:
            c = b.get('name')
            print('名字:' + c)
            self.comboBox.addItem('[preg_items]'+c)
        tree = ElementTree(file='./Content/preg/toysuit/toysuit_items.xml')
        a = tree.findall('./Item')
        for b in a:
            c = b.get('name')
            print('名字:' + c)
            self.comboBox.addItem('[toysuit_items]'+c)
        self.comboBox_2.addItem('[toysuit_items]')
        self.comboBox_2.addItem('[preg_items]')
        print('配置载入完成!')

    def run(self):
        print('正在写入')
        if self.read_id == r'[toysuit_items]':
            tree = ElementTree(file=r'./Content/preg/toysuit/toysuit_items.xml')
        elif self.read_id == r'[preg_items]':
            tree = ElementTree(file=r'./Content/preg/preg_items.xml')
        else:
            print('有地方没填罢')
            pass
        a = tree.find('./Item').get('name')
        for b in a:
            if b == self.read_combo:
                b.set("name", self.read_name)
            else:
                pass
        if self.read_id == r'[toysuit_items]':
            tree.write(r'./Content/preg/toysuit/toysuit_items.xml')
        elif self.read_id == r'[preg_items]':
            tree.write(r'./Content/preg/preg_items.xml')


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    Main.show()
    exit(app.exec_())
