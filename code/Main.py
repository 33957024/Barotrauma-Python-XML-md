import sys
from PyQt5.QtCore import pyqtSignal
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
class fromMainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.AB = None
        self.AA = None
        self.AC = None
        self.AD = None
        self.setupUi(self)
    Ui_MainWindow.setupUi.Name = pyqtSignal(str)
    Ui_MainWindow.setupUi.Id = pyqtSignal(str)
    Ui_MainWindow.setupUi.Lang = pyqtSignal(str)
    Ui_MainWindow.setupUi.About = pyqtSignal(str)
    Ui_MainWindow.setupUi.Write = pyqtSignal
    Ui_MainWindow.setupUi.AutoFile = pyqtSignal
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
        print('生成完成')
        with open('./ModFile/' + self.AC, 'a', encoding='utf-8') as B:
            B.write('\n' + '<entityname.' + self.AB + '>' + self.AA + '</entityname.' + self.AB + '>')
            B.write('\n' + '<entitydescription.' + self.AB + '>' + self.AD + '</entitydescription.' + self.AB + '>')
    def AutoFile(self):
        config = configparser.ConfigParser()
        configname = './config.ini'
        for root, dirs, files in os.walk('./'):
            if 'config.ini' in files:
                print('检测到配置文件')
                config.read(configname, encoding='utf-8')
                # 读取cinfig目录下的config.ini
                file = config.get('run', 'file')
                # 判断是否需要初始化建立文件
                if file == '0':
                    os.mkdir('./ModFile')
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
                config['run'] = {
                    'initialization': '1',
                    'file': '0'
                }
                config.write(open('config.ini', 'w', encoding='utf-8'))
                break
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())