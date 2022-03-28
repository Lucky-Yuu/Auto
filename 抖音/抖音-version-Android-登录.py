'''
@File    :   抖音-version-Android-登录.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/25 14:49   xyhu       20.0.0      None
'''
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin
import 抖音_Devices as Devices


def login():
    DouYin.desired_caps['noReset'] = False
    driver = webdriver.Remote(DouYin.server, DouYin.desired_caps)
    time.sleep(5)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="同意"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.Button[@text="始终允许"]')
    el2.click()
    time.sleep(2)
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25, 20)
    time.sleep(3)
    TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="我，按钮"]')
    el3.click()
    time.sleep(3)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="密码登录"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入手机号"]')
    el5.send_keys(Devices.douyin_account['username'])
    el6 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入密码"]')
    el6.send_keys(Devices.douyin_account['password'])
    el7 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="未选中"]')
    el7.click()
    time.sleep(1)
    el8 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="登录"]')
    el8.click()
    time.sleep(3)


login()
