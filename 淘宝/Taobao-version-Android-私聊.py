'''
@File    :   Taobao-10.10.5-Android-私聊.py
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/18 10:54   xyhu       10.10.5     01
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def chat():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="搜索栏"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.ID, 'com.taobao.taobao:id/searchEdit')
    el2.send_keys("熊先生玩具专营店")
    el3 = driver.find_element(By.XPATH, '//android.widget.Button[@text="搜索"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="店铺"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.ID,'com.taobao.taobao:id/dynamic_container')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH,'//android.widget.LinearLayout[@content-desc="客服"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="发给客服"]')
    el7.click()
    time.sleep(2)


chat()