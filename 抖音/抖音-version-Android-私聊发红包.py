'''
@File    :   抖音-version-Android-私聊发红包.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/29 15:18   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin
import 抖音_Devices as Devices


def send_red_env():
    driver = DouYin.driver
    try:
        el = driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        el.click()
        time.sleep(2)
    except:
        pass
    try:
        el0 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="点击进入直播间"]')
        if el0:
            time.sleep(2)
    except:
        TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    el1 = driver.find_element(By.XPATH, '//*[@resource-id="com.ss.android.ugc.aweme:id/root_view"]/android.widget.FrameLayout[4]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="创建群聊"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.Button[@text="发起聊天"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="更多面板"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="红包"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/edit_text')
    el7.send_keys("0.01")
    el8 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="大吉大利"]')
    el8.send_keys("测试test1234")
    el9 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="发红包"]')
    el9.click()
    time.sleep(2)
    el10 = driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,"抖音零钱")]')
    el10.click()
    time.sleep(2)
    el11 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="确认支付"]')
    el11.click()
    time.sleep(2)
    for i in Devices.douyin_account['pay_password']:
        el12 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="'+i+'"]')
        el12.click()
        time.sleep(1)
    time.sleep(3)

send_red_env()
