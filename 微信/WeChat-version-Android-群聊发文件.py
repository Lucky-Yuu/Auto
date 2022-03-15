"""
@File    :   WeChat-version-Android-HUAWEI-群聊发文件.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 15:39    xyhu       8.0.20      775
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def group_send_file():
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
    driver.swipe(877, 2183,455,2183,20)
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="文件"]')
    el4.click()
    time.sleep(2)
    el5=driver.find_element(By.ID, 'com.tencent.mm:id/f5')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="收藏中的文件"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.ID, 'com.tencent.mm:id/fc1')
    el7.click()
    time.sleep(2)
    el8 = driver.find_element(By.ID, 'com.tencent.mm:id/em')
    el8.click()
    time.sleep(2)

group_send_file()
