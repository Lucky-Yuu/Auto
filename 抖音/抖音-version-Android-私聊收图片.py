'''
@File    :   抖音-version-Android-私聊收图片.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/30 10:19   xyhu       20.0.0      None
'''
import time
from appium import webdriver
import 抖音_Devices as Devices
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


def rec_pic():
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
    a_el3 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    a_el3.click()
    time.sleep(2)
    a_el4 = a_driver.find_element(By.XPATH, '//android.widget.Button[@text="发起聊天"]')
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
    b_el3 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    b_el3.click()
    time.sleep(2)
    b_el4 = b_driver.find_element(By.XPATH, '//android.widget.Button[@text="发起聊天"]')
    b_el4.click()
    time.sleep(2)
    b_el5 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="更多面板"]')
    b_el5.click()
    time.sleep(2)
    b_el6 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="拍摄"]')
    b_el6.click()
    time.sleep(2)
    b_el7_times = 0
    while b_el7_times < 5:
        try:
            b_el7 = b_driver.find_element(By.XPATH, '//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]')
            b_el7.click()
            time.sleep(3)
            break
        except:
            b_el8 = b_driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"允许")]')  # 第一次需授权
            b_el8.click()
            time.sleep(2)
            b_el7_times += 1
    b_el9 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="发送"]')
    b_el9.click()
    time.sleep(5)


rec_pic()
