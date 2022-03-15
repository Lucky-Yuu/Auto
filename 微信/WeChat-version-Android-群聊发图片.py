"""
@File    :   WeChat-version-Android-HUAWEI-群聊发图片.py
@APPTYPE :   Android11

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 10:17    xyhu       8.0.19      769
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def group_send_pic():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="群聊"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')#此处填群聊名称
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ACCESSIBILITY_ID, "更多功能按钮，已折叠")
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="拍摄"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.ID, "com.tencent.mm:id/f7h")
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.Button[@text="完成"]')
    el6.click()
    time.sleep(3)


group_send_pic()
