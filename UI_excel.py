# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Excel(object):
    def setupUi(self, Excel):
        Excel.setObjectName(_fromUtf8("Excel"))
        Excel.resize(777, 624)
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(_fromUtf8(":./log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Excel.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(Excel)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_addfile = QtGui.QPushButton(self.centralWidget)
        self.pushButton_addfile.setGeometry(QtCore.QRect(50, 470, 121, 51))
        self.pushButton_addfile.setObjectName(_fromUtf8("pushButton_addfile"))
        self.pushButton_adddir = QtGui.QPushButton(self.centralWidget)
        self.pushButton_adddir.setGeometry(QtCore.QRect(180, 470, 121, 51))
        self.pushButton_adddir.setObjectName(_fromUtf8("pushButton_adddir"))
        self.pushButton_start = QtGui.QPushButton(self.centralWidget)
        self.pushButton_start.setGeometry(QtCore.QRect(460, 470, 121, 51))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.pushButton_stop = QtGui.QPushButton(self.centralWidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(590, 470, 121, 51))
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.pushButton_setpath = QtGui.QPushButton(self.centralWidget)
        self.pushButton_setpath.setGeometry(QtCore.QRect(594, 100, 121, 41))
        self.pushButton_setpath.setObjectName(_fromUtf8("pushButton_setpath"))
        self.pushButton_clear = QtGui.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(490, 100, 91, 41))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setGeometry(QtCore.QRect(50, 540, 661, 61))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 160, 651, 291))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        Excel.setCentralWidget(self.centralWidget)
        self.action = QtGui.QAction(Excel)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(Excel)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(Excel)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(Excel)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.actionAbout = QtGui.QAction(Excel)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.retranslateUi(Excel)
        QtCore.QObject.connect(self.pushButton_addfile, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.addFile)
        QtCore.QObject.connect(self.pushButton_adddir, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.addDir)
        QtCore.QObject.connect(self.pushButton_start, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.startMerge)
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.close)
        QtCore.QObject.connect(self.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.clearFile)
        QtCore.QObject.connect(self.pushButton_setpath, QtCore.SIGNAL(_fromUtf8("clicked()")), Excel.setSavePath)
        QtCore.QMetaObject.connectSlotsByName(Excel)

    def retranslateUi(self, Excel):
        Excel.setWindowTitle(_translate("Excel", "Excel 合并工具 (beta1.0)", None))
        self.pushButton_addfile.setText(_translate("Excel", "添加文件", None))
        self.pushButton_adddir.setText(_translate("Excel", "添加目录", None))
        self.pushButton_start.setText(_translate("Excel", "开始合并", None))
        self.pushButton_stop.setText(_translate("Excel", "结束任务", None))
        self.pushButton_setpath.setText(_translate("Excel", "设置保存路径", None))
        self.pushButton_clear.setText(_translate("Excel", "清空", None))

        self.textBrowser.setHtml(_translate("Excel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }.time{font-weight:700;}.log{color:#666;}\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))


        # self.action.setText(_translate("Excel", "选择文件夹", None))
        # self.action_2.setText(_translate("Excel", "添加文件", None))
        # self.action_3.setText(_translate("Excel", "设置保存路径", None))
        # self.action_4.setText(_translate("Excel", "清空", None))
        # self.actionAbout.setText(_translate("Excel", "About", None))


import excel_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Excel = QtGui.QMainWindow()
    ui = Ui_Excel()
    ui.setupUi(Excel)
    Excel.show()
    sys.exit(app.exec_())
