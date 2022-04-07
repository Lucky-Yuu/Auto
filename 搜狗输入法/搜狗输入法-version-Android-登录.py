'''
@File    :   搜狗输入法-version-Android-登录.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 9:02     xyhu       11.2        None
'''
import time
from selenium.webdriver.common.by import By

import 搜狗输入法_Base as Sougou


def login():
    driver = Sougou.driver
    el1 = driver.find_element(By.ID, 'com.sohu.inputmethod.sogou:id/brn')
    el1.click()
    time.sleep(2)
    el2_times = 0
    while el2_times < 5:
        try:
            el2 = driver.find_element(By.XPATH, '//android.widget.TextView[contains(@text,"登录")]')
            el2.click()
            time.sleep(2)
            el3 = driver.find_element(By.CLASS_NAME, 'android.widget.CheckBox')
            el3.click()
            time.sleep(2)
            el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="搜狗通行证"]/..')
            el4.click()
            time.sleep(2)
            el5 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="输入用户名/手机号/邮箱"]')
            el5.send_keys(Sougou.sougou_account['username'])
            el6 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="输入密码"]')
            el6.send_keys(Sougou.sougou_account['password'])
            el7 = driver.find_element(By.XPATH, '//android.widget.Button[@text="登录"]')
            el7.click()
            time.sleep(3)
            break
        except:
            el2_times += 1
            el8 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
            el8.click()
            time.sleep(2)
            el9 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="隐私设置"]')
            el9.click()
            time.sleep(2)
            el10 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="个人信息查询"]')
            el10.click()
            time.sleep(2)
            el11 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="账户信息"]')
            el11.click()
            time.sleep(2)
            Sougou.swipe_up(20)
            time.sleep(3)
            el12 = driver.find_element(By.XPATH, '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="退出账号"]')
            el12.click()
            time.sleep(2)
            el13 = driver.find_element(By.XPATH, '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="马上就走"]')
            el13.click()
            time.sleep(2)


login()
