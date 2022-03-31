'''
@File    :   抖音-version-Android-发布作品.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/31 15:01   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def post():
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
    el1 = driver.find_element(By.XPATH, '//*[@resource-id="com.ss.android.ugc.aweme:id/root_view"]/android.widget.FrameLayout[3]')
    el1.click()
    time.sleep(3)
    el2_times = 0
    while el2_times < 5:
        try:
            el2 = driver.find_element(By.ID,'com.ss.android.ugc.aweme:id/lbq')
            TouchAction(driver).long_press(el2, duration=3000).wait(3000).perform()
            time.sleep(5)
            break
        except:
            el3 = driver.find_element(By.XPATH, '//android.widget.Button[contains(@text,"允许")]')  # 第一次需授权
            el3.click()
            time.sleep(2)
            el2_times += 1
    el4 = driver.find_element(By.XPATH, '//android.widget.Button[@text="下一步"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH,'//android.widget.EditText[@text="添加作品描述.."]')
    el5.send_keys("测试test1234")
    el6 = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="发布，按钮"]')
    el6.click()
    time.sleep(3)
    try:
        el7 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="继续发布"]')
        el7.click()
    except:
        pass
    time.sleep(5)


post()