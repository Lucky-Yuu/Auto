'''
@File    :   Taobao-version-Android-登录.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/14 16:52   xyhu       10.10.5     02
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def login():
    driver = Taobao.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
    el1.click()
    time.sleep(2)
    times = 0
    while times < 5:

        try:
            el2 = driver.find_element(By.XPATH, '//android.widget.EditText[@text=" 请输入密码"]')
            el2.send_keys(Taobao.taobao_account['password'])
            time.sleep(2)
            el3 = driver.find_element(By.XPATH, '//android.widget.Button[@text="登录"]')
            el3.click()
            time.sleep(2)
            el4 = driver.find_element(By.XPATH, '//android.widget.Button[@text="同意"]')
            el4.click()
            time.sleep(2)
            break
        except:
            times += 1
            el5 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="设置"]')
            el5.click()
            time.sleep(2)
            Taobao.swipe_up(20)
            el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]')
            el6.click()
            time.sleep(2)
            el7 = driver.find_element(By.XPATH, '//android.widget.Button[@text="直接退出"]')
            el7.click()
            time.sleep(2)


login()
