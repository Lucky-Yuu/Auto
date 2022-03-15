"""
@File    :   WeChat-version-Android-HUAWEI-收藏.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/7 20:44   xyhu       8.0.19      55
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def collect():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="朋友圈"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ID, 'com.tencent.mm:id/jui')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="更多信息"]')
    el4.click()
    time.sleep(2)
    WeChat.tap_once(281,1980,379,2078,200)
    time.sleep(2)


collect()
