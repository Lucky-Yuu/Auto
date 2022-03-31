'''
@File    :   抖音_login_base.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/30 16:59   xyhu       20.0.0      None
'''
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
# 主设备
desired_caps = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': deviceVersion,  # 设备系统版本号
    'deviceName': deviceId,  # 设备号
    'appPackage': 'com.ss.android.ugc.aweme',  # 包名
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': False,
    'resetKeyboard': False,
    'noReset': False,  # 是否重置应用
    'newCommandTimeout': '180',
    'androidDeviceReadyTimeout': '3600'
}

driver = webdriver.Remote(server, desired_caps)
time.sleep(5)