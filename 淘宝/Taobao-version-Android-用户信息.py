'''
@File    :   Taobao-10.10.5-Android-用户信息.py
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/16 13:11   xyhu       10.10.5     163
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def userinfo():
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


userinfo()
