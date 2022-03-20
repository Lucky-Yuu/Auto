'''
@File    :   百度网盘-version-Android-搜索.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 16:55   xyhu       11.20.3     66
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def search():
    driver = BaiDuDisk.driver
    el1 = driver.find_element(By.ID,'com.baidu.netdisk:id/home_search_icon')
    el1.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="搜索"]')
    el3.click()
    time.sleep(2)

search()