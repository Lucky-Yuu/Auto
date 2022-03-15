"""
@File    :   WeChat-version-Android-HUAWEI-退出.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:35     xyhu       8.0.19      03
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def logout():
    driver = WeChat.driver
    WeChat.tap_once(1028, 2546, 1114, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="设置"]')
    el1.click()
    time.sleep(2)
    WeChat.swipe_up(20)
    time.sleep(2)
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="退出"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="退出登录"]')
    el3.click()
    time.sleep(5)
    driver.close_app()
    driver.quit()


logout()
