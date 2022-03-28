'''
@File    :   抖音-version-Android-搜索.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/28 10:43   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def search():
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
    el1 = driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="搜索"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.ID,'com.ss.android.ugc.aweme:id/et_search_kw')
    el2.send_keys("男生女生向前冲")
    el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="搜索"]')
    el3.click()
    time.sleep(3)



search()