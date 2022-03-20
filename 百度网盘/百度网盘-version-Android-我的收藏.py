'''
@File    :   百度网盘-version-Android-我的收藏.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 18:14   xyhu       11.20.3     960
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def my_collect():
    driver = BaiDuDisk.driver
    el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_about_me')
    el1.click()
    time.sleep(2)
    el2 =driver.find_element(By.XPATH,'//android.widget.TextView[@text="我的收藏"]')
    el2.click()
    time.sleep(2)

my_collect()