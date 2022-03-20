'''
@File    :   百度网盘-version-Android-退出.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 16:05   xyhu       11.20.3     03
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def logout():
    driver = BaiDuDisk.driver
    el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_about_me')
    el1.click()
    time.sleep(2)
    BaiDuDisk.swipe_up(20)
    BaiDuDisk.swipe_up(20)
    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="设置"]')
    el2.click()
    time.sleep(2)
    BaiDuDisk.swipe_up(20)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="退出登录"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.Button[@text="确定"]')
    el4.click()
    time.sleep(2)
    driver.close_app()
    driver.quit()


logout()
