'''
@File    :   搜狗输入法-version-Android-搜索.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/4/1 10:27    xyhu       11.2        None
'''
import time
from selenium.webdriver.common.by import By
import 搜狗输入法_Base as Sougou


def search():
    driver = Sougou.driver
    el1 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="搜索精美皮肤"]')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="搜索皮肤、作者"]')
    el2.send_keys("桃子")
    driver.keyevent('66')
    time.sleep(2)


search()
