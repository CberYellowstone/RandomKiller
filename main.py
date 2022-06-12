import contextlib
from random import randint
from time import sleep
from yaml import CLoader as CLoader, CDumper as CDumper, load as yaml_load, dump as yaml_dump
import sys, os
import csv
import chardet
import secrets
import keyboard
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from RandomKiller_style import Ui_RandomKiller
from customClass import RandomKiller_super

def isInter(a: list, b: list) -> bool:
	return bool(list(set(a) & set(b)))

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

class suspenseThread(QThread):
    def __init__(self, parent, signal: pyqtSignal, totalList: list, finalStr: str, chosenNum: int, last: bool):
        super().__init__()
        self.signal = signal
        self.totalList = totalList
        self.finalStr = finalStr
        print(finalStr)
        self._parent = parent
        self.chosenNum = chosenNum
        self.last = last

    def run(self):
        for _ in range(13):
            sleep(0.05)
            self.signal.emit("、".join(self.totalList[randint(0, len(self.totalList) - 1)] for _ in range(self.chosenNum)))
        self.signal.emit(self.finalStr)
        if(not self.last):
            self._parent.NextPushButton.setEnabled(True); self._parent.SkipPushButton.setEnabled(True)

class RandomKiller_class(QtWidgets.QMainWindow, Ui_RandomKiller, RandomKiller_super):
    suspenseSignal = pyqtSignal(str)
    hideHotKeySignal = pyqtSignal()

    def setupUi(self, Config):
        super(RandomKiller_class, self).setupUi(Config)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{application_path}/icon/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setIconSize(QtCore.QSize(128, 128))
        Config.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        Config.setWindowOpacity(0.9)
        DesktopSize = self.screen().availableSize()
        Config.move(DesktopSize.width() * 0.3, DesktopSize.height() * 0.3)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)

    def __init__(self):
        super(RandomKiller_class, self).__init__()
        self.suspenseSignal.connect(self.changeResult)
        self.storedListFilePath = 'storedList.yml'
        self.setupUi(self)
        self.hideHotKeySignal.connect(self.swichShow)
        keyboard.add_hotkey('Ctrl + R',lambda: self.hideHotKeySignal.emit())
        self.fortSizeMapping = {1:30, 2:30, 3:30, 4:26, 5:22, 6:18}
        self.updateChosenNum()
        self.NextPushButton.setEnabled(False); self.SkipPushButton.setEnabled(False)
        self.hitList = []
        self.isStored = True
        self.readStoredList()
        self.aliveList = self.luckyList[:]
        self.updateStatus()

    def swichShow(self):
        if(self.isMinimized()):
            self.showNormal()
            return
        self.showMinimized()

    def readStoredList(self):
        if(not os.path.exists(self.storedListFilePath)):
            QtWidgets.QMessageBox.critical(self,"未发现默认文件","请导入人员名单！")
            self.isStored = False
            self.StartPushButton.setEnabled(False)
            self.luckyList = []
            return
        with open(self.storedListFilePath, 'r', encoding='utf-8') as storedListFile:
            self.luckyList = yaml_load(storedListFile, CLoader)

    def saveStoredList(self):
        with open(self.storedListFilePath, 'w', encoding='utf-8') as storedListFile:
            yaml_dump(self.luckyList, storedListFile, CDumper)

    def updateStatus(self):
        self.SumUpNumLabel.setText(str(len(self.luckyList)))
        self.AliveNumLabel.setText(str(len(self.aliveList)))
        self.HitNumLabel.setText(str(len(self.hitList)))
        if(len(self.aliveList) == 0):
            self.StartPushButton.setEnabled(False)
            self.NextPushButton.setEnabled(False)
            self.SkipPushButton.setEnabled(False)

    def updateChosenNum(self):
        self.chosenNum = self.ChosenNumSpinBox.value()
        font = QtGui.QFont()
        font.setPointSize(self.fortSizeMapping[self.chosenNum])
        self.ResultLabel.setFont(font)
        # print(self.chosenNum)

    def importList(self):
        filePath, openStatus = QtWidgets.QFileDialog.getOpenFileName(self, '选择名单', '', 'CSV(*.csv)')
        if openStatus:
            with open(filePath,mode='rb') as file:
                encoding = chardet.detect(file.read())['encoding']
            if encoding == 'None':
                QtWidgets.QMessageBox.critical(self,"编码有误","请检查文件编码！")
                return
            with open(filePath,mode='r',encoding=encoding) as csvfile:
                reader = csv.reader(csvfile)
                self.luckyList = [name[0] for name in reader]
                self.aliveList = self.luckyList[:]
            self.saveStoredList()
            self.updateStatus()
            self.StartPushButton.setEnabled(True)

    def changeResult(self, result: str):
        self.ResultLabel.setText(result)

    def generateRandomNumList(self):
        self.randomNumList = [secrets.randbelow(len(self.aliveList)) for _ in range(self.chosenNum)]
        # self.doCheck()
        self.doKill()
        # print(self.randomNumList)
        while(1):
            difference = len(self.randomNumList) - len(set(self.randomNumList))
            if(difference == 0):
                break
            baseList = list(set(self.randomNumList))
            newList = list(tuple(secrets.randbelow(len(self.aliveList)) for _ in range(difference)))
            self.randomNumList = baseList + newList

    def doRandom(self):
        self.StartPushButton.setEnabled(False)
        self.generateRandomNumList()
        self.showResult(self.randomNumList)
        self.updateStatus()

    def doNext(self):
        hits = tuple(self.aliveList[randomNum] for randomNum in self.randomNumList)
        self.hitList.extend(hits)
        for hit in hits:
            with contextlib.suppress(ValueError):
                self.aliveList.remove(hit)
        self.updateStatus()
        if(len(self.aliveList) <= self.chosenNum):
            self.showResult(self.aliveList, True)
            self.hitList.extend(self.aliveList)
            self.aliveList.clear()
            self.updateStatus()
            return
        self.generateRandomNumList()
        self.showResult(self.randomNumList)
        self.updateStatus()

    def doSkip(self):
        self.updateStatus()
        self.generateRandomNumList()
        self.showResult(self.randomNumList)
        self.updateStatus()

    def restart(self):
        self.hitList.clear()
        self.aliveList = self.luckyList[:]
        self.ResultLabel.setText("<html><head/><body><p><span style=\" color:#595959;\">下一个幸运儿就是你！</span></p></body></html>")
        self.StartPushButton.setEnabled(True)
        self.NextPushButton.setEnabled(False); self.SkipPushButton.setEnabled(False)
        self.updateStatus()

    def showResult(self, randomNumList: list, last = False):
        if(last):
            finalStr = '、'.join(randomNumList)
        else:
            finalStr = "、".join(self.aliveList[randomNum] for randomNum in randomNumList)
        self.suspenseThread = suspenseThread(self ,self.suspenseSignal, self.luckyList, finalStr, self.chosenNum, last)
        self.NextPushButton.setEnabled(False); self.SkipPushButton.setEnabled(False)
        self.suspenseThread.start()

def runGUI():
    RandomKiller_APP = QtWidgets.QApplication(sys.argv)
    RandomKiller_mainWindow = RandomKiller_class()
    RandomKiller_mainWindow.show()
    RandomKiller_APP.exec()

if __name__ == "__main__":
    runGUI()
