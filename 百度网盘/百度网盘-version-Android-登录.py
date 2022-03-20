'''
@File    :   百度网盘-version-Android-登录.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 15:30   xyhu       11.20.3     02
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk
import 百度网盘_Devices as Devices


def login():
    driver = BaiDuDisk.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="百度帐号登录"]')
            el1.click()
            time.sleep(2)
            el2 = driver.find_element(By.XPATH, '//android.view.View[@text="换个帐号"]')
            el2.click()
            time.sleep(2)
            el3 = driver.find_element(By.XPATH,
                                      '//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
            el3.send_keys(Devices.baidu_account['username'])
            el4 = driver.find_element(By.XPATH, '//android.widget.Button[@index="0"]')
            el4.click()
            time.sleep(1)
            el5 = driver.find_element(By.XPATH, '//android.widget.Button[@text="下一步"]')
            el5.click()
            time.sleep(2)
            el6 = driver.find_element(By.XPATH, '//android.widget.Button[@text="帐号密码登录"]')
            el6.click()
            time.sleep(2)
            el7 = driver.find_element(By.XPATH,
                                      '//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText')
            el7.send_keys(Devices.baidu_account['password'])
            el8 = driver.find_element(By.XPATH, '//android.widget.Button[@text="登 录"]')
            el8.click()
            time.sleep(2)
            break
        except:
            el9 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_about_me')
            el9.click()
            time.sleep(2)
            BaiDuDisk.swipe_up(20)
            BaiDuDisk.swipe_up(20)
            el10 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
            el10.click()
            time.sleep(2)
            BaiDuDisk.swipe_up(20)
            el11 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]')
            el11.click()
            time.sleep(2)
            el12 = driver.find_element(By.XPATH, '//android.widget.Button[@text="确定"]')
            el12.click()
            time.sleep(2)
            el1_times += 1


login()
