"""
@File    :   WeChat-version-Android-HUAWEI-私聊发位置.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:44     xyhu       8.0.19      455
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def share_location():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')#此处填接收人昵称
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发消息"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ACCESSIBILITY_ID, "更多功能按钮，已折叠")
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="位置"]')
    el4.click()
    time.sleep(2)
    el5=driver.find_element(By.XPATH, '//android.widget.TextView[@text="发送位置"]')
    el5.click()
    time.sleep(3)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发送"]')
    el6.click()
    time.sleep(3)

share_location()
