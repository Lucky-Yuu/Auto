'''
@File    :   Taobao-10.10.5-Android-私聊收文字.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/17 10:27   xyhu       10.10.5     476
'''
import time
from appium import webdriver
from selenium.webdriver.common.by import By
import Taobao_Devices as Taobao

def rec_msg():
    a_driver = webdriver.Remote(Taobao.server_a, Taobao.desired_caps_a)
    b_driver = webdriver.Remote(Taobao.server_b, Taobao.desired_caps_b)
    a_el1_times = 0
    while a_el1_times < 3:
        try:
            a_el1 = a_driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            a_el1.click()
            time.sleep(2)
            break
        except:
            a_el2 = a_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            a_el2.click()
            time.sleep(2)
            a_el1_times += 1
    a_el3 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    a_el3.click()
    time.sleep(2)
    a_el4 = a_driver.find_element(By.XPATH, '//android.view.View[@content-desc="A测试"]')
    a_el4.click()
    time.sleep(2)
    a_el5 = a_driver.find_element(By.XPATH, '//android.view.View[@content-desc="发消息"]')
    a_el5.click()
    time.sleep(2)
    b_el1_times = 0
    while b_el1_times < 3:
        try:
            b_el1 = b_driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            b_el1.click()
            time.sleep(2)
            break
        except:
            b_el2 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            b_el2.click()
            time.sleep(2)
            b_el1_times += 1
    b_el3 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    b_el3.click()
    time.sleep(2)
    b_el4 = b_driver.find_element(By.XPATH, '//android.view.View[@content-desc="A测试"]')
    b_el4.click()
    time.sleep(2)
    b_el5 = b_driver.find_element(By.XPATH, '//android.view.View[@content-desc="发消息"]')
    b_el5.click()
    time.sleep(2)
    b_el6 = b_driver.find_element(By.ID, 'com.taobao.taobao:id/msgcenter_panel_input_edit')
    b_el6.send_keys("测试test1234")
    time.sleep(2)
    b_el7 = b_driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@content-desc="发送"]')
    b_el7.click()
    time.sleep(2)

rec_msg()