# 引用相应的包
import os
import re
import time
from appium import webdriver

'''
每次启动报错问题：
当执行adb devices时，会kill一下
adb server is out of date.  killing...
这个时候获取不到deviceid，kill结束才能获取到deviceid
每次运行一个动作后，运行下一个动作，都要重新kill
所以每次启动第一次都会报错
如果desired_caps写成固定值就不会
'''
readDeviceId = list(os.popen('adb devices').readlines())
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
server = 'http://localhost:4723/wd/hub'
# 配置参数集合
desired_caps = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': deviceVersion,  # 设备系统版本号
    'deviceName': deviceId,  # 设备号
    'appPackage': 'com.tencent.mm',  # 包名
    'appActivity': 'com.tencent.mm.ui.LauncherUI',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '60',
    'androidDeviceReadyTimeout': '3600'
}
wechat_account = {
    'username': '',  # 填写微信账号
    'password': 'fenghuo123456'  # 填写微信密码
}
new_friend_account = {
    "username": "Y1906455979"
}
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)


def get_size():
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    return (width, height)


def swipe_up(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, t)


def swipe_down(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, t)


def swipe_left(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, t)


def swipe_right(t):
    screen = get_size()
    driver.swipe(screen[0] * 0.25, screen[1] * 0.5, screen[0] * 0.75, screen[1] * 0.5, t)


def tap_once(x1, y1, x2, y2, t):
    screen = get_size()
    # p50能get到的分辨率1224*2601，非1224*2700
    driver.tap([(x1 / 1224 * screen[0], y1 / 2601 * screen[1]), (x2 / 1224 * screen[0], y2 / 2601 * screen[1])], t)
