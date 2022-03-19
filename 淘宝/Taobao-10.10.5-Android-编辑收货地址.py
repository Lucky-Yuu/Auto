'''
@File    :   Taobao-10.10.5-Android-编辑收货地址.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/19 16:38   xyhu       10.10.5     787
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def add_address():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el.click()
            time.sleep(2)
            el1_times += 1
    el2 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="我的收货地址"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="添加收货地址"]')
    el4.click()
    time.sleep(2)
    el5_times = 0
    while el5_times < 3:
        try:
            el5 = driver.find_element(By.XPATH,'//android.widget.EditText[@text="名字"]')
            el5.send_keys("测试test")
            el6 = driver.find_element(By.XPATH,'//android.widget.EditText[@text="手机号"]')
            el6.send_keys("13888888888")
            break
        except:
            el7 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="一键清空"]')
            el7.click()
            time.sleep(1)
            el5_times += 1
    el8 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="省、市、区、街道"]')
    el8.click()
    time.sleep(2)
    el9 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="南京市"]')
    el9.click()
    time.sleep(2)
    el10 = driver.find_element(By.XPATH,'//android.widget.EditText[@text="小区楼栋/乡村名称"]')
    el10.send_keys("云龙山路88号")
    time.sleep(2)
    el11 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="云龙山路88号"]')
    el11.click()
    time.sleep(2)
    el12 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="保存"]')
    el12.click()
    time.sleep(2)



add_address()