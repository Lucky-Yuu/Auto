'''
@File    :   抖音-version-Android-私聊拨打语音通话.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/29 15:20   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def call_voice():
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
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="消息，按钮"]')
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
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="语音通话"]')
    el6.click()
    time.sleep(5)


call_voice()
