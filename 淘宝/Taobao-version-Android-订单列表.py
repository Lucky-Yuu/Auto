'''
@File    :   Taobao-10.10.5-Android-订单列表.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/16 16:51   xyhu       10.10.5     951
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def order_list():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="我的订单"]')
    el2.click()
    time.sleep(2)


order_list()
