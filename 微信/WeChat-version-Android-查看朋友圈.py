"""
@File    :   WeChat-version-Android-HUAWEI-查看朋友圈.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:36     xyhu       8.0.19      500
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def moments():
    driver = WeChat.driver
    WeChat.tap_once(722, 2546, 808, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="朋友圈"]')
    el1.click()
    time.sleep(2)
    WeChat.swipe_up(20)
    time.sleep(2)


moments()
