"""
@File    :   WeChat-version-Android-HUAWEI-登录.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:34     xyhu       8.0.19      02
"""
import time
from selenium.webdriver.common.by import By
import WeChat_Base as WeChat


def login():
    print("确定当前手机有登录缓存再进行测试")
    driver = WeChat.driver
    times = 0
    while times < 3:
        try:
            el1 = driver.find_element(By.ID, "com.tencent.mm:id/cd6")
            el1.send_keys(WeChat.wechat_account['password'])
            time.sleep(2)
            el2 = driver.find_element(By.ID, "com.tencent.mm:id/g5v")
            el2.click()
            time.sleep(3)
            break
        except:
            WeChat.tap_once(1028, 2546, 1114, 2601, 20)
            time.sleep(3)
            el3 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="设置"]')
            el3.click()
            time.sleep(2)
            WeChat.swipe_up(20)
            time.sleep(2)
            el4 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="退出"]')
            el4.click()
            el5 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="退出登录"]')
            el5.click()
            time.sleep(7)
            times += 1


login()
