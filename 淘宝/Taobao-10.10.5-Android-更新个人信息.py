'''
@File    :   Taobao-10.10.5-Android-更新个人信息.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/16 15:57   xyhu       10.10.5     16
'''
import random
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def update_userinfo():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ID, 'com.taobao.taobao:id/layout_setting_page_user_block')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="性别"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH,'//android.widget.Button[@text="男"]')
    el5.click()
    time.sleep(2)

update_userinfo()
