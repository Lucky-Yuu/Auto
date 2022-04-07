'''
@File    :   搜狗输入法-version-Android-关注.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 15:42   xyhu       11.2        None
'''
import time
from selenium.webdriver.common.by import By
import 搜狗输入法_Base as Sougou


def follow():
    driver = Sougou.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="搜索精美皮肤"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="搜索皮肤、作者"]')
    el2.send_keys("搜狗输入法")
    driver.keyevent('66')
    time.sleep(2)
    el3 = driver.find_element(By.ID,'com.sohu.inputmethod.sogou:id/b7k')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.ID, 'com.sohu.inputmethod.sogou:id/bt0')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//com.sogou.base.multi.ui.SogouCustomButton[@content-desc="关注"]')
    el5.click()
    time.sleep(2)



follow()
