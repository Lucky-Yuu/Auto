'''
@File    :   抖音-version-Android-举报.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/28 20:42   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def report():
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
    el1 = driver.find_element(By.XPATH, '//android.widget.LinearLayout[contains(@content-desc,"分享")]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="举报"]')
    el2.click()
    time.sleep(5)
    print(driver.page_source)
    el3 = driver.find_element(By.XPATH,'//android.view.View[@text="危险行为"]')
    el3.click()
    time.sleep(3)
    el4 = driver.find_element(By.XPATH,'//android.widget.EditText')
    el4.send_keys("测试test1234")
    el5 = driver.find_element(By.XPATH,'//android.view.View[@text="提交"]')
    el5.click()
    time.sleep(3)


report()