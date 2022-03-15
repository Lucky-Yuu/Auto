"""
@File    :   WeChat-version-Android-HUAWEI-私聊拨打语音通话.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 18:45    xyhu       8.0.20      519
"""
import time
from appium import webdriver
from selenium.webdriver.common.by import By

# 发送方A设备
desired_caps2 = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '11',  # 设备系统版本号
    'deviceName': 'YSE0221921000592',  # 设备号，手动填写
    'appPackage': 'com.tencent.mm',  # 包名
    'appActivity': 'com.tencent.mm.ui.LauncherUI',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '60',
    'androidDeviceReadyTimeout': '3600'
}
# 接收方B设备
desired_caps = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '10',  # 设备系统版本号
    'deviceName': 'HJS5T19506006942',  # 设备号，手动填写
    'appPackage': 'com.tencent.mm',  # 包名
    'appActivity': 'com.tencent.mm.ui.LauncherUI',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '60',
    'androidDeviceReadyTimeout': '3600'
}

server_a = 'http://localhost:4723/wd/hub'
server_b = 'http://localhost:4725/wd/hub'


def audio_call():
    a_driver = webdriver.Remote(server_a, desired_caps2)
    b_driver = webdriver.Remote(server_b, desired_caps)
    time.sleep(5)
    a_width = a_driver.get_window_size()['width']
    a_height = a_driver.get_window_size()['height']
    a_driver.tap([(416 / 1224 * a_width, 2546 / 2601 * a_height), (502 / 1224 * a_width, 2601 / 2601 * a_height)])
    a_el1 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')#此处填接收人昵称
    a_el1.click()
    time.sleep(2)
    a_el2 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="音视频通话"]')
    a_el2.click()
    time.sleep(2)
    b_width = b_driver.get_window_size()['width']
    b_height = b_driver.get_window_size()['height']
    b_driver.tap([(416 / 1224 * b_width, 2546 / 2601 * b_height), (502 / 1224 * b_width, 2601 / 2601 * b_height)])
    b_el1 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')  # 此处填发送人昵称
    b_el1.click()
    time.sleep(2)
    b_el2 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="发消息"]')
    b_el2.click()
    time.sleep(2)
    a_el3 = a_driver.find_element(By.XPATH,'//android.widget.TextView[@text="语音通话"]')
    a_el3.click()
    time.sleep(5)
    b_el3 = b_driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="接听"]')
    b_el3.click()
    time.sleep(5)
    a_el4 = a_driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="挂断"]')
    a_el4.click()
    time.sleep(3)

audio_call()