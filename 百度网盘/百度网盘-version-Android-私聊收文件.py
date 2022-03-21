'''
@File    :   百度网盘-version-Android-私聊收文件.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/21 0021 15:42   xyhu       11.20.3     None
'''
import time
from appium import webdriver
from selenium.webdriver.common.by import By
import 百度网盘_Devices as Devices


def rec_file():
    a_driver = webdriver.Remote(Devices.server_a, Devices.desired_caps_a)
    b_driver = webdriver.Remote(Devices.server_b, Devices.desired_caps_b)
    a_el1_times = 0
    while a_el1_times < 3:
        try:
            a_el1 = a_driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_share')
            a_el1.click()
            time.sleep(2)
            break
        except:
            a_el = a_driver.find_element(By.ID, 'com.baidu.netdisk:id/iv_close')
            a_el.click()
            time.sleep(2)
            a_el1_times += 1
    a_el2 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="通讯录"]')
    a_el2.click()
    time.sleep(2)
    a_el3 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    a_el3.click()
    time.sleep(2)
    a_el4 = a_driver.find_element(By.XPATH, '//android.widget.Button[@text="分享文件"]')
    a_el4.click()
    time.sleep(2)
    b_el1_times = 0
    while b_el1_times < 3:
        try:
            b_el1 = b_driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_share')
            b_el1.click()
            time.sleep(2)
            break
        except:
            b_el = b_driver.find_element(By.ID, 'com.baidu.netdisk:id/iv_close')
            b_el.click()
            time.sleep(2)
            b_el1_times += 1
    b_el2 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="通讯录"]')
    b_el2.click()
    time.sleep(2)
    b_el3 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    b_el3.click()
    time.sleep(2)
    b_el4 = b_driver.find_element(By.XPATH, '//android.widget.Button[@text="分享文件"]')
    b_el4.click()
    time.sleep(2)
    b_el5 = b_driver.find_element(By.ID, 'com.baidu.netdisk:id/send_file_button')
    b_el5.click()
    time.sleep(2)
    b_el6 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="测试"]')
    b_el6.click()
    time.sleep(2)
    b_el7 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="测试test.txt"]')
    b_el7.click()
    time.sleep(2)
    b_el8 = b_driver.find_element(By.XPATH, '//android.widget.Button[@text="分享"]')
    b_el8.click()
    time.sleep(2)


rec_file()
