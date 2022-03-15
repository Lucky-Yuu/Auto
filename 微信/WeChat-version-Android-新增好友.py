"""
@File    :   WeChat-version-Android-HUAWEI-新增好友.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/7 16:16   xyhu       8.0.19      17
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def add_friend():
    driver = WeChat.driver
    el1 = driver.find_element(By.ID, "com.tencent.mm:id/hyc")
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="添加朋友"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ID, "com.tencent.mm:id/j6i")
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="微信号/手机号"]')
    el4.send_keys(WeChat.new_friend_account['username'])
    el5 = driver.find_element(By.ID, "com.tencent.mm:id/j6c")
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="添加到通讯录"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.Button[@text="发送"]')
    el7.click()
    time.sleep(3)


add_friend()
