# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tkinter import messagebox, filedialog
import requests
import time
import random
import tkinter
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import ctypes
import base64
import os
import sys
import cgitb
import ctypes
from qfluentwidgets import *
from qframelesswindow import *
from qfluentwidgets import FluentIcon as FIF
from configparser import *

VERSION = "v3.0-FluentUI"
FILEDIR = "C:/DouyinCatcher"

# 创建图标
douyinIcon = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABMLAAATCwAAAAAAAAAAAAAAAAAAAAAAIAAAAK8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA7wAAAL8AAAAgAAAAAAAAACAAAADvAAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAO8AAAAgAAAAvwAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BQAQ/woAIP8KACD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAALAAAADvAAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8KACD/MgCg/0YA3/9QAP//UAD//1AA//9LAO//LQCQ/woAIP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/OSBw/62Q7//ez///7+/v///////p3///yK///3xA//9QAP//UAD//yMAcP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/4CAgP///////////////////////////////////////////9O///9mIP//UAD//ygAgP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP+ankD///////////////////////////////////////////////////////Tv//9mIP//UAD//x4AX/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/aW0A/+3vz////////////////////////f7f//f8gP/1+2D/9/1///3+3////////////+nf//9mIP//RgDf/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/x4fAP/0+0D//////////////////////97fz/+JjSD/eH0A/7S7AP/w+gD/8foQ/+zuv////////////72f//9QAP//HgBf/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/eH0A//j8kP////////////////+9n///CgAg/wAAAP8AAAD/AAAA/zw/AP/h6gD/8vog////////////9O///1sQ//8yAJ//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/DywD/+f2g////////////9O///1EQ3/8AAAD/AAAA/wAAAP8AAAD/AAAA/2ltAP/w+gD/+/6/////////////fED//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/+HqAP/q7aD///////////+ykP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/Hh8A//D6AP/7/r////////////+ccP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//j8kP///////////6eA//9QAP//CgAg/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/h6gD/9PtQ////////////07///1AA//8yAJ//AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6/////////////p4D//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/6WsAP/w+gD//f7f////////////fED//1AA//88AL//GQBQ/woAIP8KACD/AAAA//D6AP/7/r////////////+ngP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Wl0A//D6AP/2/GD////////////07///qID//1sQ//9QAP//WxD//zIAn/8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/0toA//D6AP/4/Y////////////////////////////+RYP//MgCf/wAAAP/w+gD/+/6/////////////p4D//zwAv/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8eHwD/0toA//D6AP/4/Y///////////////////////5Fg//8yAJ//AAAA//D6AP/7/r////////////+ngP//PAC//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8eHwD/0toA//D6AP/z+0D/+/6/////////////kWD//zIAn/8AAAD/8PoA//v+v////////////6eA//88AL//AAAA/wAAAP8UAED/LQCQ/zwAv/9BAM//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8PEAD/eH0A/+HqAP/w+gD/8foQ//L7MP9rXlD/DwAw/wAAAP/w+gD/+/6/////////////p4D//zwAv/8eAGD/ckDf/51v//+9n///nW///1AA//8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/DxAA/zw/AP9aXgD/aW0A/x4fAP8AAAD/AAAA//D6AP/7/r////////////+ngP//jWDv/+nf//////////////////+9n///UAD//wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////+nf/////////////////////////////72f//9QAP//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6/////////////////////////////////////////////sp/P/zcAr/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/7/r//////////////////////////////////+v6v/+PrIP94fQD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v////////////////////////////52ff/8eHwD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+/6///////////////////////+Tf7//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/7/r//////////////////so///xQAQP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/8PoA//v+v/////////////Tv//9WEO//AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP/w+gD/+v6v//3+3//9/t//t5/f/zcAr/8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAADvAAAArwAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA//D6AP/w+gD/8PoA//D6AP94fQD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAL8AAAAgAAAA7wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAADvAAAAIAAAAAAAAAAgAAAAvwAAAO8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAArwAAACAAAAAAgAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAE='
if not os.path.exists(FILEDIR):
    os.mkdir(FILEDIR)
f = open(FILEDIR + "/DouyinIcon.ico", "wb")
f.write(base64.b64decode(douyinIcon))
f.close()

# 消息框初始化
root = tkinter.Tk()
root.withdraw()
root.title("Douyin Catcher Messagebox Component")
root.iconbitmap(FILEDIR + "/DouyinIcon.ico")


# Win11云母效果
def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


if isWin11():
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dycatcher")
sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')

if not os.path.exists(FILEDIR + "/config.ini"):
    f = open(FILEDIR + "/config.ini", "w")
    f.write('''[browser]
type = Microsoft Edge
hide = 1

[download]
path = downloads
mode = auto

[UI]
mica = 1
theme = auto

''')
    f.close()

conf = ConfigParser()
conf.read(FILEDIR + "/config.ini", encoding="utf-8")
config = {}
for i in conf.sections():
    for j in conf.options(i):
        try:
            config[j] = conf.getboolean(i, j)
        except:
            config[j] = conf.get(i, j)

# 创建文件夹
if not os.path.exists(config["path"]):
    os.mkdir(config["path"])

DARKQSS = '''Widget > QLabel {
    font: 24px 'Segoe UI', 'Microsoft YaHei';
}

Widget {
    border-left: 1px solid rgb(29, 29, 29);
    background-color: rgb(39, 39, 39);
}


Window {
    background-color: rgb(32, 32, 32);
}

MSFluentTitleBar, CustomTitleBar {
    background-color: transparent;
}

MSFluentTitleBar > QLabel,
Widget > QLabel,
CustomTitleBar > QLabel {
    color: white;
}


MSFluentTitleBar>QLabel#titleLabel, CustomTitleBar>QLabel#titleLabel {
    background: transparent;
    font: 13px 'Segoe UI';
    padding: 0 4px
}



MinimizeButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-hoverBackgroundColor: rgba(255, 255, 255, 26);
    qproperty-pressedColor: white;
    qproperty-pressedBackgroundColor: rgba(255, 255, 255, 51)
}


MaximizeButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-hoverBackgroundColor: rgba(255, 255, 255, 26);
    qproperty-pressedColor: white;
    qproperty-pressedBackgroundColor: rgba(255, 255, 255, 51)
}

CloseButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
}
'''

LIGHTQSS = '''
Widget > QLabel {
    font: 24px 'Segoe UI', 'Microsoft YaHei';
}

Widget {
    border-left: 1px solid rgb(229, 229, 229);
    background-color: rgb(249, 249, 249);
}

Window {
    background-color: rgb(243, 243, 243);
}

MSFluentTitleBar > QLabel#titleLabel, CustomTitleBar > QLabel#titleLabel {
    background: transparent;
    font: 13px 'Segoe UI';
    padding: 0 4px
}
'''


def changeVal(sec, opt, val):
    conf.set(sec, opt, val)
    config[opt] = val
    with open(FILEDIR + "/config.ini", "w") as f:
        conf.write(f)


class MicaWindow(Window):

    def __init__(self):
        super().__init__()
        self.setTitleBar(MSFluentTitleBar(self))
        if isWin11():
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())


# 抓取线程
class Catch(QThread):
    messageboxShow = pyqtSignal(str, str, str, int)
    log = pyqtSignal(str)
    resultList = pyqtSignal(str)
    end = pyqtSignal(list, str, bool)
    dialogShow = pyqtSignal()

    # 自动检测
    def checkType(self, browser):
        time.sleep(1)
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
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e), 7000)
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
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e), 7000)
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
                # self.messageboxShow.emit("retry", "抖音短视频爬取工具",
                #                         "需要验证码。请在打开的窗口中进行验证码识别后点击“重试”。\n如果窗口没有验证码，则也请点击“重试”。\n若点击“取消”，则将会结束本操作。",
                #                         -1)
                self.dialogShow.emit()

            else:
                self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                         "需要验证码，请先关闭”隐藏浏览器“然后重试。\n本操作已自动终止。", 7000)
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
                self.messageboxShow.emit("error", "抖音短视频爬取工具", "爬取失败。\n这可能是由于你没有选择正确的格式。",
                                         5000)
                browser.close()
                self.end.emit([], "", False)
                return
        else:
            if self.checkType(browser) == 0:
                self.getPic(browser)
            elif self.checkType(browser) == -1:
                self.needVerify(browser)
            else:
                self.messageboxShow.emit("error", "抖音短视频爬取工具", "爬取失败。\n这可能是由于你没有选择正确的格式。",
                                         5000)
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
            self.messageboxShow.emit("error", "抖音短视频爬取工具", "链接解析失败，请检查链接是否正确", 5000)
            self.end.emit([], "", False)
            return
        self.log.emit("Parse URL: " + self.link)
        try:
            html = requests.get(self.link)
            reditList = html.history
            lastDirect = reditList[-1].headers["location"]
        except:
            self.log.emit("Error during directing URL")
            self.messageboxShow.emit("error", "抖音短视频爬取工具", "链接解析失败，请检查链接是否正确", 5000)
            self.end.emit([], "", False)
            return
        self.log.emit("Parsing URL Direct to " + lastDirect)
        if self.head:
            self.messageboxShow.emit("info", "抖音短视频爬取工具", "正在爬取，可能需要一段时间。", 10000)
        else:
            self.messageboxShow.emit("warning", "抖音短视频爬取工具",
                                     "正在打开浏览器。\n打开浏览器后，请不要进行任何操作（验证码操作除外）。", 10000)
        try:
            mode = ["Chrome", "Edge", "Firefox", "Ie", "Safari"]
            option = eval("webdriver." + mode[self.method] + "Options()")
            if self.head:
                option.add_argument('--headless')
            try:
                browser = eval("webdriver." + mode[self.method] + "(options=option)")
            except Exception as e:
                self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                         "没有找到指定的浏览器，请尝试安装该浏览器或切换浏览器。\n\n错误信息: " + str(e),
                                         7000)
                self.end.emit([], "", False)
                return
            browser.get(lastDirect)
            # self.log.emit("User-Agent: " + str(browser.get('http://httpbin.org/user-agent')))
            self.log.emit("Browser Opened")
            self.log.emit("")
            self.modeOperation(browser)
        except Exception as e:
            self.messageboxShow.emit("error", "抖音短视频爬取工具",
                                     "发生错误。浏览器可能已经被关闭。\n\n错误信息: " + str(e), 7000)
            self.end.emit([], "", False)
            return


# 下载器
class Downloader(QThread):
    messageboxShow = pyqtSignal(str, str, str, str)
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
            root = config["path"].strip("/") + "/Images_" + str(time.time()).replace(".", "")
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
            self.messageboxShow.emit("download", "抖音短视频爬取工具",
                                     "图片下载完成，文件位于" + root + "！\n感谢您的使用！", root)
        else:
            self.links = self.links[0]
            root = config["path"].strip("/") + "/"
            file_name = "Video_" + str(time.time()).replace(".", "") + ".mp4"
            self.log.emit("Downloading video " + file_name)
            urllib.request.urlretrieve(self.links, root + file_name)
            self.log.emit("Video " + file_name + " finished!")
            self.log.emit("")
            self.log.emit("All files finished!")
            self.progressBar.emit(100)
            self.messageboxShow.emit("download", "抖音短视频爬取工具",
                                     "视频下载完成，文件位于" + config["path"].strip("/") + "/" + str(
                                         file_name) + "！\n感谢您的使用！",
                                     config["path"].strip("/"))
        self.end.emit()


class RetryMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel("操作中断")
        self.bodyLabel = BodyLabel(
            "可能需要验证码。请在打开的窗口中进行验证码识别后点击“重试”。\n如果窗口没有验证码，则也请点击“重试”。\n若点击“取消”，则将会结束本操作。",
            self)
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.bodyLabel)
        self.yesButton.setText('重试')
        self.cancelButton.setText('取消')


@InfoBarManager.register('Custom')
class CustomInfoBarManager(InfoBarManager):
    """ Custom info bar manager """

    def _pos(self, infoBar: InfoBar, parentSize=None):
        p = infoBar.parent()
        parentSize = parentSize or p.size()

        # the position of first info bar
        x = (parentSize.width() - infoBar.width()) // 2
        y = (parentSize.height() - infoBar.height()) // 2

        # get the position of current info bar
        index = self.infoBars[p].index(infoBar)
        for bar in self.infoBars[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, infoBar: InfoBar):
        pos = self._pos(infoBar)
        return QPoint(pos.x(), pos.y() - 16)


class MainUi(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"Main")
        font = QFont()
        font.setFamily(u"DengXian")
        font.setPointSize(10)
        self.setFont(font)
        # self.setStyleSheet(u"")
        self.TitleLabel = TitleLabel(self)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(20, 40, 211, 41))
        self.CaptionLabel = CaptionLabel(self)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setGeometry(QRect(20, 80, 171, 16))
        self.CaptionLabel_2 = CaptionLabel(self)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setGeometry(QRect(20, 470, 431, 31))
        self.CaptionLabel_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.PrimaryPushButton = PrimaryPushButton(self)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.setGeometry(QRect(20, 400, 161, 31))
        self.StrongBodyLabel = StrongBodyLabel(self)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(20, 450, 500, 31))
        self.StrongBodyLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 110, 331, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BodyLabel = BodyLabel(self.verticalLayoutWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.verticalLayout.addWidget(self.BodyLabel)

        self.LineEdit = LineEdit(self.verticalLayoutWidget)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMinimumSize(QSize(0, 20))

        self.verticalLayout.addWidget(self.LineEdit)

        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 280, 331, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BodyLabel_2 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.verticalLayout_2.addWidget(self.BodyLabel_2)

        self.RadioButton = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton.setObjectName(u"RadioButton")
        self.RadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.RadioButton)

        self.RadioButton_2 = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton_2.setObjectName(u"RadioButton_2")

        self.verticalLayout_2.addWidget(self.RadioButton_2)

        self.RadioButton_3 = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton_3.setObjectName(u"RadioButton_3")

        self.verticalLayout_2.addWidget(self.RadioButton_3)

        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 190, 331, 71))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BodyLabel_3 = BodyLabel(self.gridLayoutWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout.addWidget(self.BodyLabel_3, 0, 0, 1, 1)

        self.ComboBox = ComboBox(self.gridLayoutWidget)
        self.ComboBox.setObjectName(u"ComboBox")
        self.ComboBox.addItems(["Chrome", "Microsoft Edge", "Firefox", "IE", "Safari"])

        self.gridLayout.addWidget(self.ComboBox, 1, 0, 1, 1)

        self.CheckBox = CheckBox(self.gridLayoutWidget)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setChecked(True)

        self.gridLayout.addWidget(self.CheckBox, 1, 1, 1, 1)

        self.ListWidget_2 = ListWidget(self)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        QListWidgetItem(self.ListWidget_2)
        self.ListWidget_2.setObjectName(u"ListWidget_2")
        self.ListWidget_2.setGeometry(QRect(380, 140, 321, 251))
        self.ListWidget_2.setFrameShape(QFrame.StyledPanel)
        self.ListWidget_2.setFrameShadow(QFrame.Sunken)
        self.ListWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ListWidget_2.setMovement(QListView.Static)
        self.ListWidget_2.setViewMode(QListView.ListMode)
        self.horizontalLayoutWidget_4 = QWidget(self)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(380, 400, 321, 34))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PushButton = PushButton(self.horizontalLayoutWidget_4)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout_4.addWidget(self.PushButton)

        self.PushButton_2 = PushButton(self.horizontalLayoutWidget_4)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.horizontalLayout_4.addWidget(self.PushButton_2)

        self.PrimaryPushButton_2 = PrimaryPushButton(self.horizontalLayoutWidget_4)
        self.PrimaryPushButton_2.setObjectName(u"PrimaryPushButton_2")

        self.horizontalLayout_4.addWidget(self.PrimaryPushButton_2)

        self.ProgressBar = ProgressBar(self)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(380, 440, 321, 4))
        self.ProgressBar.setValue(0)
        self.ProgressBar.setUseAni(True)
        self.StrongBodyLabel_2 = StrongBodyLabel(self)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        self.StrongBodyLabel_2.setGeometry(QRect(390, 110, 113, 19))

        self.catchThread = Catch()
        self.PrimaryPushButton.clicked.connect(self.catch)
        self.catchThread.messageboxShow.connect(self.msgShow)
        self.catchThread.resultList.connect(self.listAppend)
        self.catchThread.log.connect(self.log)
        self.catchThread.dialogShow.connect(self.dialogShow)
        self.source = []
        self.fType = ""
        self.catchThread.end.connect(self.catchEnd)
        self.PrimaryPushButton_2.clicked.connect(self.download)
        self.downloadThread = Downloader()
        self.downloadThread.messageboxShow.connect(self.msgShow)
        self.downloadThread.log.connect(self.log)
        self.downloadThread.progressBar.connect(self.progress)
        self.downloadThread.end.connect(self.downloadEnd)
        self.PushButton.clicked.connect(self.selectAll)
        self.PushButton_2.clicked.connect(self.selectNone)
        self.logState = True
        self.catchNums = "A"
        self.catchTime = 0.5
        self.cType = "A"
        self.RadioButton.clicked.connect(self.changeAuto)
        self.RadioButton_2.clicked.connect(self.changeVideo)
        self.RadioButton_3.clicked.connect(self.changePic)
        self.PrimaryPushButton_2.setEnabled(False)
        self.PushButton.setEnabled(False)
        self.PushButton_2.setEnabled(False)
        self.ListWidget_2.setEnabled(False)
        self.ListWidget_2.setSelectionMode(QAbstractItemView.NoSelection)

        self.CheckBox.setChecked(config["hide"])
        self.ComboBox.setText(config["type"])
        self.ComboBox.setCurrentText(config["type"])
        if config["mode"] == "video":
            self.RadioButton_2.setChecked(True)
        elif config["mode"] == "pic":
            self.RadioButton_3.setChecked(True)
        self.ComboBox.currentTextChanged.connect(self.changeBrowser)
        self.CheckBox.clicked.connect(self.changeHide)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Douyin Catcher", None))
        self.CaptionLabel.setText(
            QCoreApplication.translate("Form", u"\u6296\u97f3\u89c6\u9891\u722c\u53d6\u5de5\u5177", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form",
                                                               u"\u6b64\u7a0b\u5e8f\u4ec5\u4f9b\u5b66\u4e60\u4ea4\u6d41\u4f7f\u7528\uff0c\u89c6\u9891/\u56fe\u96c6\u8457\u4f5c\u6743\u5f52\u5c5e\u4e8e\u539f\u4f5c\u8005\u3002\u4e25\u7981\u7528\u4e8e\u975e\u6cd5\u7528\u9014\u3002",
                                                               None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u6267\u884c", None))
        self.StrongBodyLabel.setText(
            QCoreApplication.translate("Form", u"Author: HShiDianLu. | Version " + VERSION, None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u94fe\u63a5", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
        self.RadioButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.RadioButton_2.setText(QCoreApplication.translate("Form", u"\u89c6\u9891", None))
        self.RadioButton_3.setText(QCoreApplication.translate("Form", u"\u56fe\u96c6", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u6d4f\u89c8\u5668", None))
        self.CheckBox.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u6d4f\u89c8\u5668", None))

        __sortingEnabled = self.ListWidget_2.isSortingEnabled()
        self.ListWidget_2.setSortingEnabled(False)
        self.ListWidget_2.setSortingEnabled(__sortingEnabled)

        self.PushButton.setText(QCoreApplication.translate("Form", u"\u5168\u9009", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u5168\u4e0d\u9009", None))
        self.PrimaryPushButton_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.StrongBodyLabel_2.setText(
            QCoreApplication.translate("Form", u"\u89c6\u9891/\u56fe\u7247\u5217\u8868", None))

    # retranslateUi

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

    def changeBrowser(self):
        changeVal("browser", "type", self.ComboBox.currentText())

    def changeHide(self):
        if self.CheckBox.isChecked():
            changeVal("browser", "hide", "1")
        else:
            changeVal("browser", "hide", "0")

    # 抓取
    def catch(self):
        self.ProgressBar.setValue(0)
        self.PrimaryPushButton.setEnabled(False)
        self.PrimaryPushButton_2.setEnabled(False)
        self.PushButton.setEnabled(False)
        self.PushButton_2.setEnabled(False)
        self.ListWidget_2.setEnabled(False)
        self.ListWidget_2.clear()
        self.catchThread.setPat(self.LineEdit.text(), self.cType, self.CheckBox.isChecked(),
                                self.ComboBox.currentIndex())
        self.log("NoHead: " + str(self.CheckBox.isChecked()))
        self.log("Browser: " + self.ComboBox.currentText() + " (" + str(self.ComboBox.currentIndex()) + ")")
        self.catchThread.start()

    def dialogShow(self):
        w = RetryMessageBox(self)
        self.catchThread.setAskBoxReturn(w.exec())

    # 消息显示
    def msgShow(self, boxType, title, message, dur=5000):
        if boxType == "error":
            InfoBar.error(
                title='',
                content=message,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=dur,
                parent=self
            )
        elif boxType == "warning":
            InfoBar.warning(
                title='',
                content=message,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=dur,
                parent=self
            )
        elif boxType == "info":
            InfoBar.info(
                title='',
                content=message,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=dur,
                parent=self
            )
        elif boxType == "success":
            InfoBar.success(
                title='',
                content=message,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=dur,
                parent=self
            )

        # 已弃用
        elif boxType == "retry":
            option = tkinter.messagebox.askretrycancel(title, message)
            self.catchThread.setAskBoxReturn(option)
        elif boxType == "download":
            w = InfoBar(
                icon=InfoBarIcon.INFORMATION,
                title='',
                content=message,
                orient=Qt.Vertical,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=-1,
                parent=self
            )

            pb = PushButton('打开文件夹')
            w.addWidget(pb)
            pb.clicked.connect(lambda link: QDesktopServices.openUrl(QUrl.fromLocalFile(dur)))
            w.show()

    # 日志
    # ChangeLog：UI更新日志没地方塞，print直接输出
    def log(self, message):
        print(time.asctime() + " | " + message)
        # self.listWidget_2.addItem(time.asctime() + " | " + message)
        # self.listWidget_2.setCurrentRow(self.listWidget_2.count() - 1)

    # 添加列表
    def listAppend(self, info):
        self.ListWidget_2.addItem(info)
        self.ListWidget_2.setEnabled(True)

    # 爬取结束回调
    def catchEnd(self, source, cType, refreshList):
        self.source = source
        self.fType = cType
        # self.pushButton_4.setEnabled(True)
        self.PrimaryPushButton.setEnabled(True)
        if refreshList:
            self.PrimaryPushButton_2.setEnabled(True)
            if self.fType == "P":
                self.PushButton.setEnabled(True)
                self.PushButton_2.setEnabled(True)
                self.ListWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
                # tkinter.messagebox.showinfo("抖音短视频爬取工具",
                #                            "抓取完成！请在右边的列表中选择你需要的图片，并点击“下载”按钮来下载。")
                self.msgShow("success", "抖音短视频爬取工具",
                             "抓取完成！请在右边的列表中选择你需要的图片，并点击“下载”按钮来下载。", 7000)
            else:
                self.ListWidget_2.setCurrentRow(0)
                self.ListWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
                # tkinter.messagebox.showinfo("抖音短视频爬取工具",
                #                            "抓取完成！请在右边的列表中选择你需要的图片，并点击“下载”按钮来下载。")
                self.msgShow("success", "抖音短视频爬取工具",
                             "抓取完成！请在右边的列表中选择你需要的图片，并点击“下载”按钮来下载。", 7000)

    # 下载
    def download(self):
        selects = []
        links = []
        self.ProgressBar.setValue(0)
        self.PrimaryPushButton_2.setEnabled(False)
        for i in self.ListWidget_2.selectedIndexes():
            selects.append(i.row())
            links.append(self.source[i.row()])
        self.log("ListWidget CurrentItem(s): " + str(selects))
        if not selects:
            self.log("No such selects")
            # tkinter.messagebox.showerror("抖音短视频爬取工具", "请先选择要下载的项！")
            self.msgShow("error", "抖音短视频爬取工具", "请先选择要下载的项！")
            self.PrimaryPushButton_2.setEnabled(True)
            return
        self.downloadThread.setTask(links, self.fType)
        self.downloadThread.start()
        self.log("Downloader started")

    # 下载完成回调
    def downloadEnd(self):
        self.PrimaryPushButton_2.setEnabled(True)

    # 刷新进度
    def progress(self, val):
        self.ProgressBar.setValue(int(val))

    # 全选
    def selectAll(self):
        total = self.ListWidget_2.count()
        for i in range(total):
            item = self.ListWidget_2.item(i)
            item.setSelected(True)

    # 全不选
    def selectNone(self):
        total = self.ListWidget_2.count()
        for i in range(total):
            item = self.ListWidget_2.item(i)
            item.setSelected(False)


class SettingUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"Setting")
        # self.resize(723, 515)
        font = QFont()
        font.setFamily(u"DengXian")
        font.setPointSize(10)
        self.setFont(font)
        # self.setStyleSheet(u"")
        self.TitleLabel = TitleLabel(self)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(20, 40, 211, 41))
        self.CaptionLabel = CaptionLabel(self)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setGeometry(QRect(20, 80, 171, 16))
        self.CaptionLabel_2 = CaptionLabel(self)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setGeometry(QRect(20, 470, 431, 31))
        self.CaptionLabel_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.StrongBodyLabel = StrongBodyLabel(self)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(20, 450, 500, 31))
        self.StrongBodyLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 200, 331, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BodyLabel_2 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.verticalLayout_2.addWidget(self.BodyLabel_2)

        self.RadioButton = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton.setObjectName(u"RadioButton")
        self.RadioButton.setChecked(False)

        self.verticalLayout_2.addWidget(self.RadioButton)

        self.RadioButton_2 = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton_2.setObjectName(u"RadioButton_2")

        self.verticalLayout_2.addWidget(self.RadioButton_2)

        self.RadioButton_3 = RadioButton(self.verticalLayoutWidget_2)
        self.RadioButton_3.setObjectName(u"RadioButton_3")
        self.RadioButton_3.setChecked(True)

        self.verticalLayout_2.addWidget(self.RadioButton_3)

        self.gridLayoutWidget_2 = QWidget(self)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 110, 331, 71))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LineEdit = LineEdit(self.gridLayoutWidget_2)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMinimumSize(QSize(0, 20))
        self.LineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.LineEdit, 1, 0, 1, 1)

        self.BodyLabel_4 = BodyLabel(self.gridLayoutWidget_2)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.gridLayout_2.addWidget(self.BodyLabel_4, 0, 0, 1, 1)

        self.ToolButton = ToolButton(self.gridLayoutWidget_2)
        self.ToolButton.setObjectName(u"ToolButton")
        self.ToolButton.setIcon(FIF.MORE)

        self.gridLayout_2.addWidget(self.ToolButton, 1, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 320, 226, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BodyLabel_3 = BodyLabel(self.verticalLayoutWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.verticalLayout.addWidget(self.BodyLabel_3)

        self.SwitchButton = SwitchButton(self.verticalLayoutWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")

        self.verticalLayout.addWidget(self.SwitchButton)

        self.LineEdit.setText(config["path"])
        if config["theme"] == "dark":
            self.RadioButton_2.setChecked(True)
        elif config["theme"] == "light":
            self.RadioButton.setChecked(True)
        self.SwitchButton.setChecked(config["mica"])

        self.RadioButton.clicked.connect(self.changeLight)
        self.RadioButton_2.clicked.connect(self.changeDark)
        self.RadioButton_3.clicked.connect(self.changeAuto)
        self.ToolButton.clicked.connect(self.changeDir)
        self.showState = False
        self.SwitchButton.checkedChanged.connect(self.changeMica)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Douyin Catcher", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.CaptionLabel.setText(
            QCoreApplication.translate("Form", u"\u8c03\u6574\u7a0b\u5e8f\u8fd0\u884c\u65b9\u5f0f", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form",
                                                               u"\u6b64\u7a0b\u5e8f\u4ec5\u4f9b\u5b66\u4e60\u4ea4\u6d41\u4f7f\u7528\uff0c\u89c6\u9891/\u56fe\u96c6\u8457\u4f5c\u6743\u5f52\u5c5e\u4e8e\u539f\u4f5c\u8005\u3002\u4e25\u7981\u7528\u4e8e\u975e\u6cd5\u7528\u9014\u3002",
                                                               None))
        self.StrongBodyLabel.setText(
            QCoreApplication.translate("Form", u"Author: HShiDianLu. | Version " + VERSION, None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u4e3b\u9898\u989c\u8272", None))
        self.RadioButton.setText(QCoreApplication.translate("Form", u"浅色", None))
        self.RadioButton_2.setText(QCoreApplication.translate("Form", u"深色", None))
        self.RadioButton_3.setText(QCoreApplication.translate("Form", u"\u8ddf\u968f\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u6587\u4ef6\u5939", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form",
                                                            u"\u5728 Windows 11 \u7cfb\u7edf\u4e0a\u542f\u7528\u4e91\u6bcd\u6548\u679c",
                                                            None))
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))

    # retranslateUi

    def changeMica(self):
        if self.SwitchButton.isChecked():
            changeVal("UI", "mica", "1")
        else:
            changeVal("UI", "mica", "0")
        self.showRestart()

    def changeDir(self):
        file = tkinter.filedialog.askdirectory(title="请选择下载文件夹")
        if file:
            self.changeVal("download", "path", file, False)
            self.LineEdit.setText(file)

    def changeDark(self):
        changeVal("UI", "theme", "dark")
        self.showRestart()

    def changeLight(self):
        changeVal("UI", "theme", "light")
        self.showRestart()

    def changeAuto(self):
        changeVal("UI", "theme", "auto")
        self.showRestart()

    def showRestart(self):
        if not self.showState:
            InfoBar.warning(
                title='需要重启',
                content="需要重新启动程序以应用更改。",
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=-1,
                parent=self
            )
            self.showState = True


class InfoUi(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"Info")
        font = QFont()
        font.setFamily(u"DengXian")
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet(u"")
        self.TitleLabel = TitleLabel(self)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(20, 40, 211, 41))
        self.CaptionLabel = CaptionLabel(self)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setGeometry(QRect(20, 80, 171, 16))
        self.BodyLabel = BodyLabel(self)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setGeometry(QRect(20, 100, 621, 31))
        self.ElevatedCardWidget = ElevatedCardWidget(self)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.ElevatedCardWidget.setGeometry(QRect(20, 140, 681, 111))
        self.BodyLabel_5 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        self.BodyLabel_5.setGeometry(QRect(10, 50, 251, 19))
        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(10, 30, 251, 19))
        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        self.BodyLabel_4.setGeometry(QRect(10, 80, 511, 19))
        self.StrongBodyLabel_3 = StrongBodyLabel(self.ElevatedCardWidget)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setGeometry(QRect(10, 10, 113, 19))
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        self.ElevatedCardWidget_2.setGeometry(QRect(20, 270, 681, 61))
        self.BodyLabel_9 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")
        self.BodyLabel_9.setGeometry(QRect(10, 30, 251, 19))
        self.StrongBodyLabel_5 = StrongBodyLabel(self.ElevatedCardWidget_2)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setGeometry(QRect(10, 10, 113, 19))
        self.ToolButton = ToolButton(self.ElevatedCardWidget_2)
        self.ToolButton.setObjectName(u"ToolButton")
        self.ToolButton.setGeometry(QRect(630, 14, 38, 32))
        self.ElevatedCardWidget_3 = ElevatedCardWidget(self)
        self.ElevatedCardWidget_3.setObjectName(u"ElevatedCardWidget_3")
        self.ElevatedCardWidget_3.setGeometry(QRect(20, 350, 681, 81))
        self.StrongBodyLabel_6 = StrongBodyLabel(self.ElevatedCardWidget_3)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setGeometry(QRect(10, 10, 113, 19))
        self.BodyLabel_10 = BodyLabel(self.ElevatedCardWidget_3)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")
        self.BodyLabel_10.setGeometry(QRect(60, 40, 51, 31))
        self.CaptionLabel_2 = CaptionLabel(self.ElevatedCardWidget_3)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setGeometry(QRect(430, 30, 231, 21))
        self.CaptionLabel_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.CaptionLabel_3 = CaptionLabel(self.ElevatedCardWidget_3)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setGeometry(QRect(430, 50, 231, 21))
        self.CaptionLabel_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.ToolButton_2 = ToolButton(self.ElevatedCardWidget_3)
        self.ToolButton_2.setObjectName(u"ToolButton_2")
        self.ToolButton_2.setGeometry(QRect(10, 40, 38, 32))

        self.ToolButton.setIcon(FIF.GITHUB)
        self.ToolButton_2.setIcon(FIF.GITHUB)
        self.ToolButton.clicked.connect(self.openFluentGitHub)
        self.ToolButton_2.clicked.connect(self.openGitHub)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Douyin Catcher", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"DouyinCatcher", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form",
                                                          u"DouyinCatcher\u662f\u4e00\u6b3e\u53ef\u4ee5\u5c06\u6296\u97f3\u77ed\u89c6\u9891\u4e0a\u7684\u89c6\u9891/\u56fe\u7247\u65e0\u6c34\u5370\u4e0b\u8f7d\u5230\u672c\u5730\u7684\u5f00\u6e90\u3001\u5b8c\u5168\u514d\u8d39\u7684\u5de5\u5177\u3002",
                                                          None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"Version: " + VERSION, None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"Author: HShiDianLu.", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form",
                                                            u"\u6b64\u7a0b\u5e8f\u4ec5\u4f9b\u5b66\u4e60\u4ea4\u6d41\u4f7f\u7528\uff0c\u89c6\u9891/\u56fe\u96c6\u8457\u4f5c\u6743\u5f52\u5c5e\u4e8e\u539f\u4f5c\u8005\u3002\u4e25\u7981\u7528\u4e8e\u975e\u6cd5\u7528\u9014\u3002",
                                                            None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u4fe1\u606f", None))
        self.BodyLabel_9.setText(
            QCoreApplication.translate("Form", u"PyQt-Fluent-Widgets \u63d0\u4f9bUI\u754c\u9762", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u7279\u522b\u9e23\u8c22", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5f00\u6e90", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Form", u"GitHub", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"Licensed under The MIT License", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"Copyright \u00a9 2023 by HShiDianLu.", None))

    # retranslateUi

    def openFluentGitHub(self):
        QDesktopServices.openUrl(QUrl("https://github.com/zhiyiYo/PyQt-Fluent-Widgets"))

    def openGitHub(self):
        QDesktopServices.openUrl(QUrl("https://github.com/XiaoShen2020/DouyinCatcher"))


class CustomTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 10)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))


if config["mica"]:
    WindowType = MicaWindow
else:
    WindowType = FramelessWindow


class MenuUi(WindowType):

    def __init__(self):
        super().__init__()
        if not config["mica"]:
            self.setTitleBar(CustomTitleBar(self))

        # use dark theme mode
        # setTheme(Theme.DARK)

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True)
        self.stackWidget = QStackedWidget(self)

        # create sub interface
        self.searchInterface = MainUi()
        self.aboutInterface = InfoUi()
        self.settingInterface = SettingUi()

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

        self.titleBar.raise_()
        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)

    def initNavigation(self):
        # enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        self.addSubInterface(self.searchInterface, FIF.DOWNLOAD, '首页')
        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置')
        self.addSubInterface(self.aboutInterface, FIF.INFO, '关于', NavigationItemPosition.BOTTOM)

        # !IMPORTANT: don't forget to set the default route key
        qrouter.setDefaultRouteKey(self.stackWidget, self.searchInterface.objectName())

        # set the maximum width
        # self.navigationInterface.setExpandWidth(300)

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(0)

    def initWindow(self):
        self.resize(772, 515)
        ico_path = os.path.join(os.path.dirname(__file__), FILEDIR + "/DouyinIcon.ico")
        icon = QIcon()
        icon.addPixmap(QPixmap(ico_path), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Douyin Catcher | ' + VERSION)
        self.setFixedSize(self.width(), self.height())

        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text
        )

    def setQss(self):
        if isDarkTheme():
            self.setStyleSheet(DARKQSS)
        else:
            self.setStyleSheet(LIGHTQSS)

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackWidget, widget.objectName())

    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width() - 46, self.titleBar.height())


def show_MainWindow():
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    if config["theme"] == "dark":
        setTheme(Theme.DARK)
    elif config["theme"] == "auto":
        setTheme(Theme.AUTO)
    app = QApplication(sys.argv)
    ui = MenuUi()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    show_MainWindow()
