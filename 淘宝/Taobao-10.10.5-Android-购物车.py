'''
@File    :   Taobao-10.10.5-Android-购物车.py
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/19 15:57   xyhu       10.10.5     997
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def my_cart():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="购物车"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el.click()
            time.sleep(2)
            el1_times += 1


my_cart()
