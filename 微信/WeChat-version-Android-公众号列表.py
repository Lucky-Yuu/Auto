"""
@File    :   WeChat-version-Android-HUAWEI-公众号列表.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 14:08    xyhu       8.0.19      988
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def official_account():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="公众号"]')
    el1.click()


official_account()