'''
@File    :   Taobao-10.10.5-Android-收货地址.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/16 0016 16:39   xyhu       10.10.5     955
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def address():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="我的收货地址"]')
    el3.click()
    time.sleep(2)

address()