"""
@File    :   WeChat-version-Android-HUAWEI-更新个人信息.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:44     xyhu       8.0.19      16
"""
import random
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def update_userinfo():
    driver = WeChat.driver
    WeChat.tap_once(1028, 2546, 1114, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.ID, "com.tencent.mm:id/l2j")
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="更多信息"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="个性签名"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.ID, 'com.tencent.mm:id/br7')
    el4.clear()
    el4.send_keys("测试test" + str(random.randint(0, 99)))
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.Button[@text="保存"]')
    el5.click()
    time.sleep(2)


update_userinfo()
