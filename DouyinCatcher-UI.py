# -*- coding: utf-8 -*

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from PyQt5.QtCore import QThread, pyqtSignal
import cgitb
import os
import requests
import time
import tkinter
import sys
import urllib.request
from PyQt5.QtWidgets import QAbstractItemView
from selenium import webdriver
from selenium.webdriver.common.by import By
import ctypes
import base64

# 高分辨率防糊修复
QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

# 报错处理
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dycatcher")
sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')

# 创建图标
douyinIcon = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABMLAAATCwAAAAAAAAAAAAAAAAAAAAAAIAAAAK8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA7wAAAL8AAAAgAAAAAAAAACAAAADvAAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAO8AAAAgAAAAvwAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BQAQ/woAIP8KACD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAALAAAADvAAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8KACD/MgCg/0YA3/9QAP//UAD//1AA//9LAO//LQCQ/woAIP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/OSBw/62Q7//ez///7+/v///////p3///yK///3xA//9QAP//UAD//yMAcP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/4CAgP///////////////////////////////////////////9O///9mIP//UAD//ygAgP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP+ankD///////////////////////////////////////////////////////Tv//9mIP//UAD//x4AX/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/aW0A/+3vz////////////////////////f7f//f8gP/1+2D/9/1///3+3////////////+nf//9mIP//RgDf/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/x4fAP/0+0D//////////////////////97fz/+JjSD/eH0A/7S7AP/w+gD/8foQ/+zuv////////////72f//9QAP//HgBf/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/eH0A//j8kP////////////////+9n///CgAg/wAAAP8AAAD/AAAA/zw/AP/h6gD/8vog////////////9O///1sQ//8yAJ//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/DywD/+f2g////////////9O///1EQ3/8AAAD/AAAA/wAAAP8AAAD/AAAA/2ltAP/w+gD/+/6/////////////fED//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/+HqAP/q7aD///////////+ykP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/Hh8A//D6AP/7/r////////////+ccP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//j8kP///////////6eA//9QAP//CgAg/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/h6gD/9PtQ////////////07///1AA//8yAJ//AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6/////////////p4D//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/6WsAP/w+gD//f7f////////////fED//1AA//88AL//GQBQ/woAIP8KACD/AAAA//D6AP/7/r////////////+ngP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Wl0A//D6AP/2/GD////////////07///qID//1sQ//9QAP//WxD//zIAn/8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/0toA//D6AP/4/Y////////////////////////////+RYP//MgCf/wAAAP/w+gD/+/6/////////////p4D//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8eHwD/0toA//D6AP/4/Y///////////////////////5Fg//8yAJ//AAAA//D6AP/7/r////////////+ngP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8eHwD/0toA//D6AP/z+0D/+/6/////////////kWD//zIAn/8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8UAED/LQCQ/zwAv/9BAM//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8PEAD/eH0A/+HqAP/w+gD/8foQ//L7MP9rXlD/DwAw/wAAAP/w+gD/+/6/////////////p4D//zwAv/8eAGD/ckDf/51v//+9n///nW///1AA//8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/DxAA/zw/AP9aXgD/aW0A/x4fAP8AAAD/AAAA//D6AP/7/r////////////+ngP//jWDv/+nf//////////////////+9n///UAD//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////+nf/////////////////////////////72f//9QAP//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6/////////////////////////////////////////////sp/P/zcAr/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/7/r//////////////////////////////////+v6v/+PrIP94fQD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////////////////////52ff/8eHwD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6///////////////////////+Tf7//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/7/r//////////////////so///xQAQP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v/////////////Tv//9WEO//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+v6v//3+3//9/t//t5/f/zcAr/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAADvAAAArwAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/w+gD/8PoA//D6AP94fQD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAL8AAAAgAAAA7wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAADvAAAAIAAAAAAAAAAgAAAAvwAAAO8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAArwAAACAAAAAAgAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAE='
if not os.path.exists("C:/Temp"):
    os.mkdir("C:/Temp")
f = open("C:/Temp/DouyinIcon.ico", "wb")
f.write(base64.b64decode(douyinIcon))
f.close()

# 创建文件夹
if not os.path.exists("downloads"):
    os.mkdir("downloads")

# 消息框初始化
root = tkinter.Tk()
root.withdraw()
root.title("Douyin Catcher Messagebox Component")
root.iconbitmap('C:/Temp/DouyinIcon.ico')

VERSION = "v2.4"


# 抓取线程
class Catch(QThread):
    messageboxShow = pyqtSignal(str, str, str)
    log = pyqtSignal(str)
    resultList = pyqtSignal(str)
    end = pyqtSignal(list, str, bool)

    # 自动检测
    def checkType(self, browser):
        try:
            browser.find_element(By.CLASS_NAME, "xM5q7Zx1")
            return 0
        except:
            videoTags = browser.find_elements(By.TAG_NAME, "source")
            choiceSources = []
            for i in videoTags:
                choiceSources.append(str(i.get_attribute("src")))
            try:
                choiceSources[0] += " (默认)"
            except:
                return -1
            return 1

    # 抓取视频
    def getVideo(self, browser):
        self.log.emit("Mode: Video")
        try:
            videoTags = browser.find_elements(By.TAG_NAME, "source")
        except Exception as e:
            self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e))
            self.end.emit([], "", False)
            return True
        sources = []
        first = True
        for i in videoTags:
            self.log.emit("Catch Source(s): " + str(i.get_attribute("src")))
            sources.append(str(i.get_attribute("src")))
            if first:
                self.resultList.emit("(默认) " + str(i.get_attribute("src")))
            else:
                self.resultList.emit(str(i.get_attribute("src")))
            first = False
        self.log.emit("")
        browser.close()
        self.log.emit("Thread Ended. Emit ending flag...")
        self.end.emit(sources, "V", True)
        self.log.emit("Thread <CatchThread> Ended.")

    # 抓取照片
    def getPic(self, browser):
        self.log.emit("Mode: Pictures")
        try:
            pics = browser.find_elements(By.CLASS_NAME, "V5BLJkWV")
        except Exception as e:
            self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e))
            self.end.emit([], "", False)
            return True
        sources = []
        count = 1
        for i in pics:
            new = str(i.get_attribute("src"))
            self.log.emit("Catch Source(s): " + new)
            sources.append(new)
            self.resultList.emit("第" + str(count) + "张 (" + new + ")")
            count += 1
        self.log.emit("")
        browser.close()
        self.log.emit("Thread Ended. Emit ending flag...")
        self.end.emit(sources, "P", True)
        self.log.emit("Thread <CatchThread> Ended.")

    # 验证码
    # P.S. 目前不确定抖音是否还存在验证码中间页
    def needVerify(self, browser):
        ct = self.checkType(browser)
        while ct == -1:
            self.callback = None
            if not self.head:
                self.messageboxShow.emit("retry", "抖音短视频爬取工具",
                                         "需要验证码。请在打开的窗口中进行验证码识别后点击“重试”。\n如果窗口没有验证码，则也请点击“重试”。\n若点击“取消”，则将会结束本操作。")
            else:
                self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                         "需要验证码，请先关闭”隐藏浏览器“然后重试。\n本操作已自动终止。")
                self.end.emit([], "", False)
                return
            self.log.emit("Waiting for user option...")
            callbacked = False
            try:
                if self.callback == None:
                    raise Exception
            except:
                callbacked = True
            while callbacked:
                try:
                    if self.callback == None:
                        raise Exception
                    else:
                        callbacked = False
                except:
                    callbacked = True
            self.log.emit("Responded with " + str(self.callback))
            if self.callback:
                ct = self.checkType(browser)
            else:
                self.end.emit([], "", False)
                return
        self.modeOperation(browser)

    # 模式操作
    def modeOperation(self, browser):
        if self.linkType == "A":
            if self.checkType(browser) == 0:
                self.getPic(browser)
            elif self.checkType(browser) == 1:
                self.getVideo(browser)
            else:
                self.needVerify(browser)
        elif self.linkType == "V":
            if self.checkType(browser) == 1:
                self.getVideo(browser)
            elif self.checkType(browser) == -1:
                self.needVerify(browser)
            else:
                self.messageboxShow.emit("error", "抖音短视频爬取工具", "爬取失败。\n这可能是由于你没有选择正确的格式。")
                browser.close()
                self.end.emit([], "", False)
                return
        else:
            if self.checkType(browser) == 0:
                self.getPic(browser)
            elif self.checkType(browser) == -1:
                self.needVerify(browser)
            else:
                self.messageboxShow.emit("error", "抖音短视频爬取工具", "爬取失败。\n这可能是由于你没有选择正确的格式。")
                browser.close()
                self.end.emit([], "", False)
                return

    # 设置参数
    def setPat(self, link, lineType, head, method):
        self.link = link
        self.linkType = lineType
        self.head = head
        self.method = method

    # （验证码提示框）返回值设置
    def setAskBoxReturn(self, callback):
        self.callback = callback

    # 重定向&打开浏览器
    def run(self):
        self.log.emit("Original Link: " + self.link)
        try:
            self.link = self.link.split(" ")[-1]
        except:
            self.log.emit("Error during parsing URL")
            self.messageboxShow.emit("error", "抖音短视频爬取工具", "链接解析失败，请检查链接是否正确")
            self.end.emit([], "", False)
            return
        self.log.emit("Parse URL: " + self.link)
        try:
            html = requests.get(self.link)
            reditList = html.history
            lastDirect = reditList[-1].headers["location"]
        except:
            self.log.emit("Error during directing URL")
            self.messageboxShow.emit("error", "抖音短视频爬取工具", "链接解析失败，请检查链接是否正确")
            self.end.emit([], "", False)
            return
        self.log.emit("Parsing URL Direct to " + lastDirect)
        if self.head:
            self.messageboxShow.emit("info", "抖音短视频爬取工具", "正在爬取，可能需要一段时间。")
        else:
            self.messageboxShow.emit("warning", "抖音短视频爬取工具",
                                     "正在打开浏览器。\n打开浏览器后，请不要进行任何操作（验证码操作除外）。")
        try:
            mode = ["Chrome", "Edge", "Firefox", "Ie", "Safari"]
            option = eval("webdriver." + mode[self.method] + "Options()")
            if self.head:
                option.add_argument('--headless')
            try:
                browser = eval("webdriver." + mode[self.method] + "(options=option)")
            except Exception as e:
                self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                         "没有找到指定的浏览器，请尝试安装该浏览器或切换浏览器。\n\n错误信息: " + str(e))
                self.end.emit([], "", False)
                return
            browser.get(lastDirect)
            # self.log.emit("User-Agent: " + str(browser.get('http://httpbin.org/user-agent')))
            self.log.emit("Browser Opened")
            self.log.emit("")
            self.modeOperation(browser)
        except Exception as e:
            self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e))
            self.end.emit([], "", False)
            return


# 下载器
class Downloader(QThread):
    messageboxShow = pyqtSignal(str, str, str)
    log = pyqtSignal(str)
    progressBar = pyqtSignal(float)
    end = pyqtSignal()

    # 设置参数
    def setTask(self, links, cType):
        self.links = links
        self.cType = cType
        self.eachTask = 100 / len(links)
        self.percent = 0

    # 下载
    def run(self):
        if self.cType == "P":
            root = "downloads/Images_" + str(time.time()).replace(".", "")
            os.mkdir(root)
            root += "/"
            dlCount = 0
            for i in self.links:
                self.log.emit("Downloading file " + i)
                urllib.request.urlretrieve(i, root + "Image" + str(dlCount) + ".jpg")
                dlCount += 1
                self.log.emit("Done. Refresh progressbar...")
                self.percent += self.eachTask
                self.progressBar.emit(self.percent)
            self.messageboxShow.emit("info", "抖音短视频爬取工具",
                                     "图片下载完成，文件位于程序目录下" + root + "！\n感谢您的使用！")
        else:
            self.links = self.links[0]
            root = 'downloads/'
            file_name = "Video_" + str(time.time()).replace(".", "") + ".mp4"
            self.log.emit("Downloading video " + file_name)
            urllib.request.urlretrieve(self.links, root + file_name)
            self.log.emit("Video " + file_name + " finished!")
            self.log.emit("")
            self.log.emit("All files finished!")
            self.progressBar.emit(100)
            self.messageboxShow.emit("info", "抖音短视频爬取工具",
                                     "视频下载完成，文件位于程序目录下downloads/" + str(file_name) + "！\n感谢您的使用！")
        self.end.emit()


# GUI
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 445)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        Form.setFont(font)

        ico_path = os.path.join(os.path.dirname(__file__), 'C:/Temp/DouyinIcon.ico')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ico_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 60, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("c")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 80, 341, 351))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 321, 251))
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 280, 321, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 3)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(-130, -60, 971, 901))
        self.label_13.setStyleSheet("background:white;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 180, 361, 251))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 341, 221))
        self.listWidget_2.setStyleSheet("")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(410, 20, 321, 41))
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 140, 361, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DengXian")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_13.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.label_12.raise_()
        self.horizontalLayoutWidget_3.raise_()

        self.catchThread = Catch()
        self.pushButton_4.clicked.connect(self.catch)
        self.catchThread.messageboxShow.connect(self.msgShow)
        self.catchThread.resultList.connect(self.listAppend)
        self.catchThread.log.connect(self.log)
        self.source = []
        self.fType = ""
        self.catchThread.end.connect(self.catchEnd)
        self.pushButton_3.clicked.connect(self.download)
        self.downloadThread = Downloader()
        self.downloadThread.messageboxShow.connect(self.msgShow)
        self.downloadThread.log.connect(self.log)
        self.downloadThread.progressBar.connect(self.progress)
        self.downloadThread.end.connect(self.downloadEnd)
        self.pushButton.clicked.connect(self.selectAll)
        self.pushButton_2.clicked.connect(self.selectNone)
        self.logState = True
        self.catchNums = "A"
        self.catchTime = 0.5
        self.cType = "A"
        self.radioButton_4.clicked.connect(self.changeAuto)
        self.radioButton_2.clicked.connect(self.changeVideo)
        self.radioButton.clicked.connect(self.changePic)
        self.listWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        Form.setFixedSize(Form.width(), Form.height())
        Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.form = Form

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Douyin Catcher | " + VERSION))
        self.label.setText(_translate("Form", "Douyin Catcher"))
        self.label_2.setText(_translate("Form", "抖音视频爬取工具"))
        self.label_3.setText(_translate("Form", "视频链接"))
        self.label_4.setText(_translate("Form", "类型"))
        self.radioButton_4.setText(_translate("Form", "自动识别"))
        self.radioButton_2.setText(_translate("Form", "视频"))
        self.radioButton.setText(_translate("Form", "图集"))
        self.groupBox_2.setTitle(_translate("Form", "视频/图片列表"))
        self.pushButton_2.setText(_translate("Form", "全不选"))
        self.pushButton_3.setText(_translate("Form", "下载"))
        self.pushButton.setText(_translate("Form", "全选"))
        self.groupBox_3.setTitle(_translate("Form", "日志"))
        self.label_12.setText(_translate("Form", "此程序仅供学习交流使用，视频/图集著作权归属于原作者。\n"
                                                 "严禁用于非法用途。"))
        self.pushButton_4.setText(_translate("Form", "执行"))
        self.checkBox.setText(_translate("Form", "隐藏浏览器"))
        self.label_5.setText(_translate("Form", "使用浏览器"))
        self.comboBox.setItemText(0, _translate("Form", "Chrome"))
        self.comboBox.setItemText(1, _translate("Form", "Microsoft Edge"))
        self.comboBox.setItemText(2, _translate("Form", "Firefox"))
        self.comboBox.setItemText(3, _translate("Form", "IE"))
        self.comboBox.setItemText(4, _translate("Form", "Safari"))

    # 切换选项
    def changeVideo(self):
        self.cType = "V"
        self.log("Type: Video")

    def changePic(self):
        self.cType = "P"
        self.log("Type: Pictures")

    def changeAuto(self):
        self.cType = "A"
        self.log("Type: Auto")

    # 抓取
    def catch(self):
        self.progressBar.setValue(0)
        self.listWidget.clear()
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.catchThread.setPat(self.lineEdit.text(), self.cType, self.checkBox.isChecked(),
                                self.comboBox.currentIndex())
        self.log("NoHead: " + str(self.checkBox.isChecked()))
        self.log("Browser: " + self.comboBox.currentText() + " (" + str(self.comboBox.currentIndex()) + ")")
        self.catchThread.start()

    # 消息显示
    def msgShow(self, boxType, title, message):
        if boxType == "error":
            tkinter.messagebox.showerror(title, message)
        elif boxType == "warning":
            tkinter.messagebox.showwarning(title, message)
        elif boxType == "info":
            tkinter.messagebox.showinfo(title, message)
        elif boxType == "retry":
            option = tkinter.messagebox.askretrycancel(title, message)
            self.catchThread.setAskBoxReturn(option)

    # 日志
    def log(self, message):
        self.listWidget_2.addItem(time.asctime() + " | " + message)
        self.listWidget_2.setCurrentRow(self.listWidget_2.count() - 1)

    # 添加列表
    def listAppend(self, info):
        self.listWidget.addItem(info)
        self.groupBox_2.setEnabled(True)

    # 爬取结束回调
    def catchEnd(self, source, cType, refreshList):
        self.source = source
        self.fType = cType
        self.pushButton_4.setEnabled(True)
        if refreshList:
            if self.fType == "P":
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
                tkinter.messagebox.showinfo("抖音短视频爬取工具",
                                            "抓取完成！请在右边的列表中选择你需要的图片，并点击“下载”按钮来下载。")
            else:
                self.pushButton_3.setEnabled(True)
                self.listWidget.setCurrentRow(0)
                self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
                tkinter.messagebox.showinfo("抖音短视频爬取工具",
                                            "抓取完成！请在右边的列表中选择你需要的视频源，并点击“下载”按钮来下载。")

    # 下载
    def download(self):
        selects = []
        links = []
        self.progressBar.setValue(0)
        self.pushButton_3.setEnabled(False)
        for i in self.listWidget.selectedIndexes():
            selects.append(i.row())
            links.append(self.source[i.row()])
        self.log("ListWidget CurrentItem(s): " + str(selects))
        if not selects:
            self.log("No such selects")
            tkinter.messagebox.showerror("抖音短视频爬取工具", "请先选择要下载的项！")
            self.pushButton_3.setEnabled(True)
            return
        self.downloadThread.setTask(links, self.fType)
        self.downloadThread.start()
        self.log("Downloader started")

    # 下载完成回调
    def downloadEnd(self):
        self.pushButton_3.setEnabled(True)

    # 刷新进度
    def progress(self, val):
        self.progressBar.setValue(int(val))

    # 全选
    def selectAll(self):
        total = self.listWidget.count()
        for i in range(total):
            item = self.listWidget.item(i)
            item.setSelected(True)

    # 全不选
    def selectNone(self):
        total = self.listWidget.count()
        for i in range(total):
            item = self.listWidget.item(i)
            item.setSelected(False)


# 显示主窗口
def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    show_MainWindow()
