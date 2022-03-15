"""
@File    :   WeChat-version-Android-HUAWEI-群列表.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 14:04    xyhu       8.0.19      995
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def group_list():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="群聊"]')
    el1.click()
    time.sleep(2)


group_list()