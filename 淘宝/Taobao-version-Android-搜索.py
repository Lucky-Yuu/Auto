'''
@File    :   Taobao-10.10.5-Android-搜索.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/16 23:09   xyhu       10.10.5     66
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def search():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="搜索栏"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.ID, 'com.taobao.taobao:id/searchEdit')
    el2.send_keys("毛绒玩具")
    el3 = driver.find_element(By.XPATH, '//android.widget.Button[@text="搜索"]')
    el3.click()
    time.sleep(2)


search()
