'''
@File    :   抖音-version-Android-群聊收红包.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/30 10:21   xyhu       20.0.0      None
'''
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Devices as Devices


def group_rec_red_env():
    a_driver = webdriver.Remote(Devices.server_a, Devices.desired_caps_a)
    b_driver = webdriver.Remote(Devices.server_b, Devices.desired_caps_b)
    try:
        a_el = a_driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        a_el.click()
        time.sleep(2)
    except:
        pass
    try:
        a_el0 = a_driver.find_element(By.XPATH, '//android.view.View[@content-desc="点击进入直播间"]')
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
        b_el0 = b_driver.find_element(By.XPATH, '//android.view.View[@content-desc="点击进入直播间"]')
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
    b_el5 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="更多面板"]')
    b_el5.click()
    time.sleep(2)
    b_el6 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="红包"]')
    b_el6.click()
    time.sleep(2)
    b_el7 = b_driver.find_element(By.XPATH, '//android.widget.RelativeLayout[1]/android.widget.EditText')
    b_el7.send_keys("0.01")
    b_el8 = b_driver.find_element(By.XPATH, '//android.widget.RelativeLayout[2]/android.widget.EditText')
    b_el8.send_keys("1")
    b_el9 = b_driver.find_element(By.XPATH, '//android.widget.EditText[@text="大吉大利"]')
    b_el9.send_keys("测试test1234")
    b_el10 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="发红包"]')
    b_el10.click()
    time.sleep(2)
    b_el11 = b_driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,"抖音零钱")]')
    b_el11.click()
    time.sleep(2)
    b_el12 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="确认支付"]')
    b_el12.click()
    time.sleep(2)
    for i in Devices.douyin_account['pay_password']:
        b_el13 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="' + i + '"]')
        b_el13.click()
        time.sleep(1)
    time.sleep(5)
    a_el5 = a_driver.find_element(By.XPATH,
                                  '//android.widget.TextView[@text="测试test1234" and @resource-id="com.ss.android.ugc.aweme:id/bm"]')
    a_el5.click()
    time.sleep(2)
    a_el6 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="开红包"]')
    a_el6.click()


group_rec_red_env()
