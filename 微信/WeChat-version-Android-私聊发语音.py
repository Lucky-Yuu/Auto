"""
@File    :   WeChat-version-Android-HUAWEI-私聊发语音.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:40     xyhu       8.0.19      763
"""
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def send_voice():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')#此处填接收人昵称
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发消息"]')
    el2.click()
    time.sleep(2)
    try:
        el3 = driver.find_element(By.ACCESSIBILITY_ID, "切换到按住说话")
        el3.click()
        time.sleep(3)
        el4 = driver.find_element(By.ACCESSIBILITY_ID, "按住说话")
        TouchAction(driver).long_press(el4, duration=3000).wait(3000).perform()
        time.sleep(5)
    except:
        print("当前已切换为按住说话")
        el4 = driver.find_element(By.ACCESSIBILITY_ID, "按住说话")
        TouchAction(driver).long_press(el4, duration=3000).wait(3000).perform()
        time.sleep(5)


send_voice()
