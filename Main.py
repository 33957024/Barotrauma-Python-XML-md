from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
import configparser
from PyQt5.QtGui import QFontDatabase, QIcon
from sys import argv, exit
from xml.etree.ElementTree import (
    Element, SubElement, ElementTree
)


# 主窗口
class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.setting_type = None
        loadUi('NEW_UI/Main.ui', self)
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')
        self.setWindowIcon(QIcon('./NEW_UI/edit.ico'))

    def Main_add(self):
        pass

    def openSet(self):
        pass

    def openEdit(self):
        Edit.show()


# 提供编辑界面
class Edit(QDialog):
    def __init__(self):
        super(Edit, self).__init__()
        self.text20 = None
        self.text10 = None
        self.text19 = None
        self.text18 = None
        self.text17 = None
        self.text16 = None
        self.text15 = None
        self.text14 = None
        self.text13 = None
        self.text12 = None
        self.text11 = None
        self.text09 = None
        self.text08 = None
        self.text07 = None
        self.text06 = None
        self.text05 = None
        self.text04 = None
        self.text03 = None
        self.text02 = None
        self.text01 = None
        self.bool = ['false', 'true']
        self.spawnType = ['Human', 'Enemy', 'Cargo', 'Corpse']
        self.filelist = [
            'Submarine', 'BeaconStation', 'EnemySubmarine', 'Outpost', 'OutpostModule', 'Wreck', 'Item',
            'Character', 'Afflictions', 'BackgroundCreaturePrefabs', 'BallastFlora', 'CaveGenerationParameters',
            'Corpses', 'Decals', 'EventManagerSettings', 'Factions', 'ItemAssembly', 'Jobs',
            'LevelGenerationParameters', 'LevelObjectPrefabs', 'LocationTypes', 'MapGenerationParameters',
            'Missions', 'NPCConversations', 'NPCSets', 'Orders', 'OutpostConfig', 'Particles', 'RandomEvents',
            'RuinConfig', 'ServerExecutable', 'SkillSettings', 'Sounds', 'Structure', 'Talents', 'TalentTrees',
            'Text', 'TraitorMissions', 'UIStyle', 'UpgradeModules', 'WreckAIConfig', 'Other'
        ]
        self.actionlist = [
            'ConversationAction', 'FireAction', 'RemoveItemAction', 'AfflictionAction', 'GiveSkillExpAction',
            'ReputationAction', 'BinaryOptionAction', 'GodModeAction', 'RNGAction', 'CheckAfflictionAction', 'GoTo',
            'SetDataAction', 'CheckDataAction', 'Label', 'SetPriceMultiplierAction', 'CheckItemAction', 'MissionAction',
            'SkillCheckAction', 'CheckMoneyAction', 'MoneyAction', 'SpawnAction', 'CheckReputationAction',
            'NPCChangeTeamAction', 'StatusEffectAction', 'TriggerEventAction', 'ClearTagAction', 'NPCFollowAction',
            'TagAction', 'UnlockPathAction', 'CombatAction', 'NPCWaitAction', 'TriggerAction', 'WaitAction'
        ]
        loadUi('NEW_UI/Edit.ui', self)
        QFontDatabase.addApplicationFont('./Font/Bender_Light.otf')
        self.setWindowTitle('多功能行动编辑器')
        self.setWindowIcon(QIcon('./NEW_UI/box.ico'))
        self.actionlist.sort()
        self.comboBox_11.addItems(self.actionlist)

    def Text_1(self, text):
        self.text01 = text

    def Text_2(self, text):
        self.text02 = text

    def Text_3(self, text):
        self.text03 = text

    def Text_4(self, text):
        self.text04 = text

    def Text_5(self, text):
        self.text05 = text

    def Text_6(self, text):
        self.text06 = text

    def Text_7(self, text):
        self.text07 = text

    def Text_8(self, text):
        self.text08 = text

    def Text_9(self, text):
        self.text09 = text

    def combo_1(self, text):
        self.text11 = text

    def combo_2(self, text):
        self.text12 = text

    def combo_3(self, text):
        self.text13 = text

    def combo_4(self, text):
        self.text14 = text

    def combo_5(self, text):
        self.text15 = text

    def combo_6(self, text):
        self.text16 = text

    def combo_7(self, text):
        self.text17 = text

    def combo_8(self, text):
        self.text18 = text

    def combo_9(self, text):
        self.text19 = text

    def father(self, text):
        self.text10 = text
        print(text)

    def edit_set(self, text):
        self.text20 = text

    def ok(self):
        # self.line_name.setPlaceholderText('内容')
        pass

    def edit_set_ok(self):
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        self.comboBox_7.clear()
        self.comboBox_8.clear()
        self.comboBox_9.clear()
        self.comboBox_10.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.comboBox_8.clear()
        self.lineEdit_9.clear()
        if self.text20 == 'ConversationAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'FireAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'RemoveItemAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'AfflictionAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'GiveSkillExpAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'ReputationAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'BinaryOptionAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'GodModeAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'RNGAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CheckAfflictionAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'GoTo':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'SetDataAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CheckDataAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'Label':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'SetPriceMultiplierAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CheckItemAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'MissionAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'SkillCheckAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CheckMoneyAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'MoneyAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'SpawnAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CheckReputationAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'NPCChangeTeamAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'StatusEffectAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'TriggerEventAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'ClearTagAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'NPCFollowAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'TagAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'UnlockPathAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'CombatAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'NPCWaitAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'TriggerAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        elif self.text20 == 'WaitAction':
            self.comboBox_2.addItems()
            self.comboBox_3.addItems()
            self.comboBox_4.addItems()
            self.comboBox_5.addItems()
            self.comboBox_6.addItems()
            self.comboBox_7.addItems()
            self.comboBox_8.addItems()
            self.comboBox_9.addItems()
            self.comboBox_10.addItems()
            self.lineEdit.setPlaceholderText('null')
            self.lineEdit_2.setPlaceholderText('null')
            self.lineEdit_3.setPlaceholderText('null')
            self.lineEdit_4.setPlaceholderText('null')
            self.lineEdit_5.setPlaceholderText('null')
            self.lineEdit_6.setPlaceholderText('null')
            self.lineEdit_7.setPlaceholderText('null')
            self.lineEdit_8.setPlaceholderText('null')
            self.lineEdit_9.setPlaceholderText('null')
        else:
            print('不应该出现这句话的，看到我请上报github')


if __name__ == '__main__':
    app = QApplication(argv)
    Main = MainWindows()
    Edit = Edit()
    Main.show()
    exit(app.exec_())
