'''
@File    :   抖音-version-Android-群聊收文字.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/30 10:21   xyhu       20.0.0      None
'''
import time
from appium import webdriver
import 抖音_Devices as Devices
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


def group_rec_msg():
    a_driver = webdriver.Remote(Devices.server_a, Devices.desired_caps_a)
    b_driver = webdriver.Remote(Devices.server_b, Devices.desired_caps_b)
    try:
        a_el = a_driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        a_el.click()
        time.sleep(2)
    except:
        pass
    try:
        a_el0 = a_driver.find_element(By.XPATH,'//android.view.View[@content-desc="点击进入直播间"]')
        if a_el0:
            time.sleep(2)
    except:
        TouchAction(a_driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    a_el1 = a_driver.find_element(By.XPATH, '//*[@resource-id="com.ss.android.ugc.aweme:id/root_view"]/android.widget.FrameLayout[4]')
    a_el1.click()
    time.sleep(3)
    a_el2 = a_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="创建群聊"]')
    a_el2.click()
    time.sleep(2)
    a_el3 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="已加入的群聊"]')
    a_el3.click()
    time.sleep(2)
    a_el4 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    a_el4.click()
    time.sleep(2)
    try:
        b_el = b_driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        b_el.click()
        time.sleep(2)
    except:
        pass
    try:
        b_el0 = b_driver.find_element(By.XPATH,'//android.view.View[@content-desc="点击进入直播间"]')
        if b_el0:
            time.sleep(2)
    except:
        TouchAction(b_driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    b_el1 = b_driver.find_element(By.XPATH,
                                  '//*[@resource-id="com.ss.android.ugc.aweme:id/root_view"]/android.widget.FrameLayout[4]')
    b_el1.click()
    time.sleep(3)
    b_el2 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="创建群聊"]')
    b_el2.click()
    time.sleep(2)
    b_el3 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="已加入的群聊"]')
    b_el3.click()
    time.sleep(2)
    b_el4 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    b_el4.click()
    time.sleep(2)
    b_el5 = b_driver.find_element(By.XPATH, '//android.widget.EditText[@text="发送消息"]')
    b_el5.send_keys("测试test1234")
    b_el6 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="发送"]')
    b_el6.click()
    time.sleep(2)


group_rec_msg()
