'''
@File    :   Taobao-10.10.5-Android-退出.py
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/15 9:18    xyhu       10.10.5     03
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def logout():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
    el1.click()
    time.sleep(7)
    el2 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="设置"]')
    el2.click()
    time.sleep(2)
    Taobao.swipe_up(20)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.Button[@text="直接退出"]')
    el4.click()
    time.sleep(2)


logout()
