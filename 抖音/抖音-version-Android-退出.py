'''
@File    :   抖音-version-Android-退出.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/25 15:09   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin

def logout():
    driver = DouYin.driver()
    TouchAction(driver).tap(x=600, y=1268).perform()
    time.sleep(3)
    el1 = driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="我，按钮"]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.ID,'com.ss.android.ugc.aweme:id/iuk')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="设置"]')
    el3.click()
    time.sleep(3)
    DouYin.swipe_up(20)
    el4 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="退出登录"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH,'//android.widget.Button[@text="退出"]')
    el5.click()
    time.sleep(2)


logout()