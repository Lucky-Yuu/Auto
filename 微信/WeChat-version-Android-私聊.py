"""
@File    :   WeChat-version-Android-HUAWEI-私聊.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:39     xyhu       8.0.19      01
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def send_msg():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')#此处填接收人昵称
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发消息"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ID, 'com.tencent.mm:id/b4a')
    el3.send_keys("你好")
    el4 = driver.find_element(By.ID, "com.tencent.mm:id/b8k")
    el4.click()
    time.sleep(2)


send_msg()
