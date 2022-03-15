"""
@File    :   WeChat-version-Android-HUAWEI-评论.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/7 15:53   xyhu       8.0.19      25
"""
import time
import random
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def comment():
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
    el4 = driver.find_element(By.ID, 'com.tencent.mm:id/brw')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="评论"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.ID, 'com.tencent.mm:id/m8')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="评论"]')
    el7.send_keys("测试test" + str(random.randint(0, 99)))
    time.sleep(2)
    el8 = driver.find_element(By.XPATH, '//android.widget.Button[@text="发送"]')
    el8.click()
    time.sleep(2)


comment()
