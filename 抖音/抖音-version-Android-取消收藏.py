'''
@File    :   抖音-version-Android-取消收藏.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/28 15:28   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def cancelcollect():
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
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="我，按钮"]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="收藏"]')
    el2.click()
    time.sleep(3)
    el3 = driver.find_element(By.XPATH, '//android.view.View[contains(@content-desc,"视频")]')
    el3.click()
    time.sleep(5)
    TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.LinearLayout[contains(@content-desc,"分享")]')
    el4.click()
    time.sleep(3)
    el5 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="取消收藏"]')
    el5.click()
    time.sleep(2)

cancelcollect()
