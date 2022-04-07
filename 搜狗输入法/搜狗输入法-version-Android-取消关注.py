'''
@File    :   搜狗输入法-version-Android-取消关注.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 15:42   xyhu       11.2        None
'''
import time
from selenium.webdriver.common.by import By
import 搜狗输入法_Base as Sougou


def cancelfollow():
    driver = Sougou.driver
    el1 = driver.find_element(By.ID, 'com.sohu.inputmethod.sogou:id/brn')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="我的关注"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="搜狗输入法"]')
    el3.click()
    time.sleep(5)
    el4 = driver.find_element(By.XPATH,
                              '//com.sogou.base.multi.ui.SogouCustomButton[@resource-id="com.sohu.inputmethod.sogou:id/eo"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH,
                              '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="确定"]')
    el5.click()
    time.sleep(2)


cancelfollow()
