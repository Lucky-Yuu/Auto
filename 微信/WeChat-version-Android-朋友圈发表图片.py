"""
@File    :   WeChat-version-Android-HUAWEI-朋友圈发表图片.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:59     xyhu       8.0.19      929
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def post_moment_pic():
    driver = WeChat.driver
    WeChat.tap_once(722, 2546, 808, 2601, 20)
    time.sleep(2)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="朋友圈"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="拍照分享"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="拍摄"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.ID, "com.tencent.mm:id/f7h")
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.Button[@text="完成"]')
    el5.click()
    time.sleep(3)
    el6 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="这一刻的想法..."]')
    el6.send_keys("测试test1234")
    el7 = driver.find_element(By.XPATH,'//android.widget.Button[@text="发表"]')
    el7.click()
    time.sleep(5)


post_moment_pic()
