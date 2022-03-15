"""
@File    :   WeChat-version-Android-HUAWEI-视频号查看视频.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 14:13    xyhu       8.0.19      935
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def play_video():
    driver = WeChat.driver
    WeChat.tap_once(722, 2546, 808, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="视频号"]')
    el1.click()
    time.sleep(2)
    WeChat.swipe_up(20)
    time.sleep(5)


play_video()
