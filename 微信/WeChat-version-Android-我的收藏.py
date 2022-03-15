"""
@File    :   WeChat-version-Android-HUAWEI-我的收藏.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/8 10:18   xyhu       8.0.19      960
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def my_collect():
    driver = WeChat.driver
    WeChat.tap_once(1028, 2546, 1114, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="收藏"]')
    el1.click()
    time.sleep(2)


my_collect()
