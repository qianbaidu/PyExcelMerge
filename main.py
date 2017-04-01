# -*- coding: utf-8 -*-



from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time
import os
import xlrd
import xlwt

from UI_excel import Ui_Excel



class MainWindow(QMainWindow, Ui_Excel):

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        # QMainWindow.__init__(self, parent)
        self.fileList = []
        self.savePath = os.path.abspath('.')
        self.saveName = '%d.xls' % (time.time())
        self.setupUi(self)

    def eachDirFile(self,filepath):
            pathDir =  os.listdir(filepath)
            dirFileList = []
            for allDir in pathDir:
                child = os.path.join('%s/%s' % (filepath, allDir))
                fileType = os.path.splitext(child)
                if fileType[1] == '.xlsx' or fileType[1] == '.xls':
                    self.fileList.append(child)
                    self.log(u'添加文件:'+child+"\n")

    def addFile(self):
        fname = QFileDialog.getOpenFileName(self, '添加文件',
        'c:\\',"Image files (*.xlsx *.xls)")
        if(len(fname) > 0):
            self.fileList.append(fname)
            self.log(u'添加文件:'+fname+"\n")


    def addDir(self):
        dir = QtGui.QFileDialog.getExistingDirectory()
        if(len(dir) > 0):
            self.log(u'选择文件夹:'+dir+"\n")
            self.eachDirFile(dir)

    def log(self,str):
        logStr = '<span class="time"><font color=#000>%s</font></span><span class="log"><font color=#666>  %s</font></span>' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,str)
        self.textBrowser.append(logStr)

    def clearFile(self):
        fileList = []
        savePath = ''
        self.textBrowser.setText('')

    def setSavePath(self):
        savePathTemp = QtGui.QFileDialog.getExistingDirectory()
        if(len(savePathTemp) > 0):
            self.savePath = savePathTemp
            self.log(u'选择保存文件夹:'+self.savePath+"\n")


    def startMerge(self):
        #print('startMerge')
        thread = MergeThread(self) # 创建线程
        thread.trigger.connect(self.updateStatusLog) # 连接信号！
        self.savePathName = '%s/%s' % (self.savePath,self.saveName)

        thread.setup(self.fileList,self.savePathName) # 传递参数
        thread.start() # 启动线程

    def updateStatusLog(self,message):
        self.log(message)



class MergeThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str) # trigger传输的内容是字符串
    def __init__(self, parent=None):
        super(MergeThread, self).__init__(parent)

    def setup(self, fileArr,savePathName):
        self.fileArr = fileArr
        self.savePathName = savePathName


    def run(self): # 很多时候都必重写run方法, 线程start后自动运行
        self.merge(self.fileArr,self.savePathName)

    # def my_function(self):
    #     # Note: This is never called directly. It is called by Qt once the
    #     # thread environment has been set up.
    #     self.trigger.emit(u"线程启动了！\n")
    #     for i in range(10):
    #         time.sleep(3)
    #         self.trigger.emit(u"当前为第："+str(i)+"----\n")
    #     self.trigger.emit(u"线程结束了！\n")


    def merge(self,fileArr,savePathName):
        newFile = xlwt.Workbook()
        newExcel = newFile.add_sheet('sheet1')

        fileIndex = 0;
        lineNum = 0;
        for f in fileArr:
            #print(f)
            isFile = os.path.isfile(f)
            if isFile != True:
                continue
            fileIndex += 1
            self.trigger.emit(u"当前处理合并文件:%d %s \n" % (fileIndex,f))
            data = xlrd.open_workbook(f)   # 打开demo.xls
            table = data.sheet_by_index(0)        # 通过索引获取xls文件第0个sheet
            nrows = table.nrows
            #ncols = table.ncols

            for rownum in range(nrows):
                if lineNum >= 60000:
                    #print('合并文件行数大于60000 后续数据将被丢弃\n')
                    self.trigger.emit(u"合并文件行数大于60000 后续数据将被丢弃！\n")
                    break
                for j in range(len(table.row_values(rownum))):
                    newExcel.write(lineNum,j,table.row_values(rownum)[j])
                lineNum += 1
            newFile.save(savePathName)
        self.trigger.emit(u"合并完成 \n")
        self.trigger.emit(u'保存位置:%s \n' % (savePathName))



if __name__ == "__main__":

    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )

    app = QtGui.QApplication(sys.argv)
    ui =MainWindow()
    ui.show()
    sys.exit(app.exec_())


