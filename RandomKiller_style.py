# Form implementation generated from reading ui file 'RandomKiller_style.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RandomKiller(object):
    def setupUi(self, RandomKiller):
        RandomKiller.setObjectName("RandomKiller")
        RandomKiller.resize(630, 300)
        self.centralwidget = QtWidgets.QWidget(RandomKiller)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(-10, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(20, 90, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ResultLabel.setAutoFillBackground(True)
        self.ResultLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ResultLabel.setObjectName("ResultLabel")
        self.StartPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartPushButton.setGeometry(QtCore.QRect(40, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.StartPushButton.setFont(font)
        self.StartPushButton.setObjectName("StartPushButton")
        self.HotkeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.HotkeyLabel.setGeometry(QtCore.QRect(450, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HotkeyLabel.setFont(font)
        self.HotkeyLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.HotkeyLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.HotkeyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HotkeyLabel.setObjectName("HotkeyLabel")
        self.NextPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextPushButton.setGeometry(QtCore.QRect(220, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.NextPushButton.setFont(font)
        self.NextPushButton.setObjectName("NextPushButton")
        self.SkipPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SkipPushButton.setGeometry(QtCore.QRect(400, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SkipPushButton.setFont(font)
        self.SkipPushButton.setObjectName("SkipPushButton")
        self.ChosenNumSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ChosenNumSpinBox.setGeometry(QtCore.QRect(550, 50, 61, 31))
        self.ChosenNumSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ChosenNumSpinBox.setMinimum(1)
        self.ChosenNumSpinBox.setMaximum(6)
        self.ChosenNumSpinBox.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        self.ChosenNumSpinBox.setProperty("value", 1)
        self.ChosenNumSpinBox.setObjectName("ChosenNumSpinBox")
        self.ChosenNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChosenNumLabel.setGeometry(QtCore.QRect(460, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ChosenNumLabel.setFont(font)
        self.ChosenNumLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.ChosenNumLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.ChosenNumLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ChosenNumLabel.setObjectName("ChosenNumLabel")
        self.ImportPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportPushButton.setGeometry(QtCore.QRect(540, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ImportPushButton.setFont(font)
        self.ImportPushButton.setObjectName("ImportPushButton")
        self.SumUpTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.SumUpTitleLabel.setGeometry(QtCore.QRect(20, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SumUpTitleLabel.setFont(font)
        self.SumUpTitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SumUpTitleLabel.setObjectName("SumUpTitleLabel")
        self.SumUpNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.SumUpNumLabel.setGeometry(QtCore.QRect(80, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SumUpNumLabel.setFont(font)
        self.SumUpNumLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SumUpNumLabel.setObjectName("SumUpNumLabel")
        self.HitTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.HitTitleLabel.setGeometry(QtCore.QRect(160, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.HitTitleLabel.setFont(font)
        self.HitTitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HitTitleLabel.setObjectName("HitTitleLabel")
        self.HitNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.HitNumLabel.setGeometry(QtCore.QRect(220, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HitNumLabel.setFont(font)
        self.HitNumLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HitNumLabel.setObjectName("HitNumLabel")
        self.AliveTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.AliveTitleLabel.setGeometry(QtCore.QRect(300, 50, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AliveTitleLabel.setFont(font)
        self.AliveTitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.AliveTitleLabel.setObjectName("AliveTitleLabel")
        self.AliveNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.AliveNumLabel.setGeometry(QtCore.QRect(360, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AliveNumLabel.setFont(font)
        self.AliveNumLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.AliveNumLabel.setObjectName("AliveNumLabel")
        self.ResetPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetPushButton.setGeometry(QtCore.QRect(540, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ResetPushButton.setFont(font)
        self.ResetPushButton.setObjectName("ResetPushButton")
        RandomKiller.setCentralWidget(self.centralwidget)

        self.retranslateUi(RandomKiller)
        self.ImportPushButton.clicked.connect(RandomKiller.importList) # type: ignore
        self.StartPushButton.clicked.connect(RandomKiller.doRandom) # type: ignore
        self.NextPushButton.clicked.connect(RandomKiller.doNext) # type: ignore
        self.SkipPushButton.clicked.connect(RandomKiller.doSkip) # type: ignore
        self.ChosenNumSpinBox.valueChanged['int'].connect(RandomKiller.updateChosenNum) # type: ignore
        self.ResetPushButton.clicked.connect(RandomKiller.restart) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RandomKiller)

    def retranslateUi(self, RandomKiller):
        _translate = QtCore.QCoreApplication.translate
        RandomKiller.setWindowTitle(_translate("RandomKiller", "MainWindow"))
        self.TitleLabel.setText(_translate("RandomKiller", "不重复抽人器：抓取随机幸运儿"))
        self.ResultLabel.setText(_translate("RandomKiller", "<html><head/><body><p><span style=\" color:#595959;\">下一个幸运儿就是你！</span></p></body></html>"))
        self.StartPushButton.setText(_translate("RandomKiller", "开始抓取"))
        self.HotkeyLabel.setText(_translate("RandomKiller", "呼出 / 隐藏：Ctrl + J"))
        self.NextPushButton.setText(_translate("RandomKiller", "下一个"))
        self.SkipPushButton.setText(_translate("RandomKiller", "高抬贵手"))
        self.ChosenNumLabel.setText(_translate("RandomKiller", "抓取人数："))
        self.ImportPushButton.setText(_translate("RandomKiller", "导入名单"))
        self.SumUpTitleLabel.setText(_translate("RandomKiller", "总人数："))
        self.SumUpNumLabel.setText(_translate("RandomKiller", "NaN"))
        self.HitTitleLabel.setText(_translate("RandomKiller", "已中招："))
        self.HitNumLabel.setText(_translate("RandomKiller", "NaN"))
        self.AliveTitleLabel.setText(_translate("RandomKiller", "幸存者："))
        self.AliveNumLabel.setText(_translate("RandomKiller", "NaN"))
        self.ResetPushButton.setText(_translate("RandomKiller", "从头来过"))
