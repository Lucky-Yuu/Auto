'''
@File    :   抖音-version-Android-评论.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/29 9:22   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def comment():
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
    el1 = driver.find_element(By.XPATH, '//android.widget.ImageView[contains(@content-desc,"评论")]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH,'//android.widget.EditText[@text="留下你的精彩评论吧"]')
    el2.send_keys("太棒了，给你点个赞！！！")
    el3 = driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="发送"]')
    el3.click()
    time.sleep(3)


comment()
