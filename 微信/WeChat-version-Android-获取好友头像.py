"""
@File    :   WeChat-version-Android-HUAWEI-获取好友头像.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 14:27    xyhu       8.0.19      928
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def friend_pic():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="头像"]')
    el2.click()
    time.sleep(2)


friend_pic()
