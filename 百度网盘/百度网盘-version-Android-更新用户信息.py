'''
@File    :   百度网盘-version-Android-更新用户信息.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 16:33   xyhu       11.20.3     16
'''
import random
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def update_userinfo():
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
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="昵称"]')
    el4.click()
    time.sleep(2)
    el5 =driver.find_element(By.ID,'com.baidu.netdisk:id/input_edittext')
    el5.clear()
    el5.send_keys("测试test"+str(random.randint(0, 999)))
    el6 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="确定"]')
    el6.click()
    time.sleep(2)


update_userinfo()