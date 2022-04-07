'''
@File    :   搜狗输入法-version-Android-更新个人信息.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 15:36   xyhu       11.2        None
'''
import random
import time
from selenium.webdriver.common.by import By
import 搜狗输入法_Base as Sougou


def update_userinfo():
    driver = Sougou.driver
    el1 = driver.find_element(By.ID, 'com.sohu.inputmethod.sogou:id/brn')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="隐私设置"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="个人信息查询"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="账户信息"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="昵称"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="com.sohu.inputmethod.sogou:id/xc"]')
    el7.send_keys("测试test" + str(random.randint(0, 99)))
    el8 = driver.find_element(By.XPATH, '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="完成"]')
    el8.click()
    time.sleep(3)


update_userinfo()
