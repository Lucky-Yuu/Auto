'''
@File    :   抖音-version-Android-取消点赞.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/28 9:40   xyhu       20.0.0      None
'''
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import 抖音_Base as DouYin


def cancellike():
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
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="喜欢"]')
    el2.click()
    time.sleep(3)
    el3 = driver.find_element(By.ID,'com.ss.android.ugc.aweme:id/cnj')
    el3.click()
    time.sleep(5)
    TouchAction(driver).tap(x=600, y=1268).perform().release()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[contains(@content-desc,"已点赞")]')
    el4.click()
    time.sleep(3)

cancellike()