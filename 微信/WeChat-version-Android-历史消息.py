"""
@File    :   WeChat-version-Android-HUAWEI-历史消息.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 11:19    xyhu       8.0.19      959
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def msg():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发消息"]')
    el2.click()
    time.sleep(2)
    WeChat.swipe_down(2000)


msg()