'''
@File    :   百度网盘-version-Android-收藏.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 18:29   xyhu       11.20.3     55
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def collect():
    driver = BaiDuDisk.driver
    el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_filelist')
    el1.click()
    time.sleep(2)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="测试"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.ID, 'com.baidu.netdisk:id/file_list_title_right_one')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="选择文件"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.ID, 'com.baidu.netdisk:id/edit_right_button')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="更多"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="收藏"]')
    el7.click()
    time.sleep(2)


collect()