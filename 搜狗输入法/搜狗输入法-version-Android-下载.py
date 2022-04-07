'''
@File    :   搜狗输入法-version-Android-下载.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 15:37   xyhu       11.2        None
'''
import time
from selenium.webdriver.common.by import By
import 搜狗输入法_Base as Sougou


def upload():
    driver = Sougou.driver
    el1 = driver.find_element(By.ID, 'com.sohu.inputmethod.sogou:id/brn')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="多语言键盘"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="添加"]')
    el4.click()
    time.sleep(5)


upload()
