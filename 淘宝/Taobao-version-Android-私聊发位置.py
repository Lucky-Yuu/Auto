'''
@File    :   Taobao-10.10.5-Android-私聊发位置.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/18 14:47   xyhu       10.10.5     455
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def send_location():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="搜索栏"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el.click()
            time.sleep(2)
            el1_times += 1
    el2 = driver.find_element(By.ID, 'com.taobao.taobao:id/searchEdit')
    el2.send_keys("依妹儿玩具专营店")
    el3 = driver.find_element(By.XPATH, '//android.widget.Button[@text="搜索"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="店铺"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.ID, 'com.taobao.taobao:id/dynamic_container')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.LinearLayout[@content-desc="客服"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="功能面板"]')
    el7.click()
    time.sleep(2)
    el8 =driver.find_element(By.XPATH,'//android.widget.TextView[@text="位置"]')
    el8.click()
    time.sleep(2)
    el8_times = 0
    while el8_times < 3:
        try:
            el9 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发送"]')
            el9.click()
            time.sleep(2)
            break
        except:
            el10 = driver.find_element(By.XPATH, '//android.widget.Button[@text="仅使用期间允许"]')  # 第一次需授权
            el10.click()
            time.sleep(2)
            el8_times += 1


send_location()