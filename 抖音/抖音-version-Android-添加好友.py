'''
@File    :   抖音-version-Android-添加好友.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/29 11:01   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def add_friend():
    driver = DouYin.driver
    try:
        el = driver.find_element(By.XPATH, '//android.widget.Button[@text="我知道了"]')
        el.click()
        time.sleep(2)
    except:
        pass
    finally:
        TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(3)
    el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="我，按钮"]')
    el1.click()
    time.sleep(3)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="添加朋友"]')
    el2.click()
    time.sleep(3)
    el3 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="搜索用户名字/抖音号"]')
    el3.click()
    el3.send_keys("橙子")
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="搜索"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '(//android.widget.TextView[@text="关注"])[1]')
    el5.click()
    time.sleep(2)


add_friend()
