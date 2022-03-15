"""
@File    :   WeChat-version-Android-HUAWEI-头像.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:33     xyhu       8.0.19      164
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def headpic():
    driver = WeChat.driver
    WeChat.tap_once(1028, 2546, 1114, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.ID, "com.tencent.mm:id/l2j")
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="查看头像"]')
    el2.click()
    time.sleep(2)


headpic()
