from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from os import walk, mkdir
import configparser

class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        loadUi('UI/About.ui', self)
