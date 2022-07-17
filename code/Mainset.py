from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from os import walk, mkdir
import configparser
from sys import argv, exit

class mainwindows(QMainWindow):
    def __init__(self):
        super(mainwindows, self).__init__()
        loadUi('UI/Main-window.ui', self)
        #TODO:修正变量名称
        self.AB = None
        self.AA = None
        self.AC = None
        self.AD = None
# 定义信号类型
    Name = pyqtSignal(str)
    Id = pyqtSignal(str)
    Lang = pyqtSignal(str)
    About = pyqtSignal(str)
    Write = pyqtSignal()
    AutoFile = pyqtSignal()
    AboutWindow = pyqtSignal()
    def Name(self,text):
        print("Name输入内容:" + text)
        self.AA = text
    def Id(self,text):
        print("Id输入内容为" + text)
        self.AB = text
    def Lang(self,text):
        print("Lang输入内容为" + text)
        self.AC = text
    def About(self,text):
        print("About输入内容为" + text)
        self.AD = text
    def Write(self):
        if self.AA != None and self.AB != None and self.AD != None and self.AC != None:
            print('生成完成')
            with open('./ModFile/' + self.AC, 'a', encoding='utf-8') as B:
                B.write('\n' + '<entityname.' + self.AB + '>' + self.AA + '</entityname.' + self.AB + '>')
                B.write('\n' + '<entitydescription.' + self.AB + '>' + self.AD + '</entitydescription.' + self.AB + '>')
        else:
            Debug.bug('内容为空')
            Debug.show()
            print('内容有空，拒绝访问')
    def AutoFile(self):
        config = configparser.ConfigParser()
        configname = './config.ini'
        for root, dirs, files in walk('./'):
            if 'config.ini' in files:
                print('检测到配置文件')
                config.read(configname, encoding='utf-8')
                # 读取cinfig目录下的config.ini
                file = config.get('run', 'file')
                # 判断是否需要初始化建立文件
                if file == '0':
                    mkdir('./ModFile')
                    list = {"filelist.xml", "SimplifiedChinese.xml", "English.xml", "Mods.xml"}
                    for make in list:
                        with open('./ModFile/' + make, 'w', encoding='utf-8') as A:
                            # 判断是否为语言文件,如果为true则增加语言文件的前缀
                            if make == "SimplifiedChinese.xml":
                                A.write(
                                    '<?xml version="1.0" encoding="utf-8"?>\n<infotexts language="Simplified Chinese" nowhitespace="true" translatedname="中文(简体)">')
                            if make == "English.xml":
                                A.write(
                                    '<?xml version="1.0" encoding="utf-8"?>\n<infotexts language="English" nowhitespace="false" translatedname="English">')
                            # TODO:if make == "filelist.xml":并写入内容
                            else:
                                A.write('<?xml version="1.0" encoding="utf-8"?>')
                    # 生成完成后修改配置文件
                    config.set('run', 'file', '1')
                    config.write(open(configname, 'w'))
                else:
                    print('非初始化,自动取消生成文件')
                break
            else:
                print("没有检测到配置文件，开始生成")
                config = configparser.ConfigParser()
                #TODO:我觉得这里的版本号可以自动生成的
                config['run'] = {
                    'initialization': '1',
                    'file': '0',
                    'version': '1.0.4'
                }
                config.write(open('config.ini', 'w', encoding='utf-8'))
                break
    def AboutWindow(self):
        About.show()
# 提供About窗口
class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        loadUi('UI/About.ui', self)
        config = configparser.ConfigParser()
        configname = './config.ini'
        config.read(configname, encoding='utf-8')
        version = config.get('run', 'version')
        self.label_2.setText(version)
# 提供Debug窗口
class Debug(QDialog):
    def __init__(self):
        super(Debug, self).__init__()
        loadUi('UI/Debug.ui', self)
    def bug(self,bug):
        Text = '出现异常\n' + 'bug是' + bug + '\n请检查是否出现忘记输入，错误输入等原因\n如果非人为操作请在GitHub反馈给我'
        self.label.setText(Text)
if __name__ == '__main__':
    app = QApplication(argv)
    Main = mainwindows()
    About = AboutWindow()
    Debug = Debug()
    Main.show()
    exit(app.exec_())
