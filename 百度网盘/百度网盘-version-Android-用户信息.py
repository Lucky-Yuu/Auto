'''
@File    :   百度网盘-version-Android-用户信息.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 16:29   xyhu       11.20.3     163
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def userinfo():
    driver = BaiDuDisk.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_about_me')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.ID, 'com.baidu.netdisk:id/iv_close')
            el.click()
            time.sleep(2)
            el1_times += 1
    BaiDuDisk.swipe_up(20)
    BaiDuDisk.swipe_up(20)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="个人信息"]')
    el3.click()
    time.sleep(2)


userinfo()
