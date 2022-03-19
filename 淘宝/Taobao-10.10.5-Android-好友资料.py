'''
@File    :   Taobao-10.10.5-Android-好友资料.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/19 10:42   xyhu       10.10.5     949
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def friend_info():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el2 = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el2.click()
            time.sleep(2)
            el1_times += 1
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="A测试"]')
    el4.click()
    time.sleep(2)
    el5 =driver.find_element(By.XPATH,'//android.view.View[@content-desc="逛逛主页"]')
    el5.click()
    time.sleep(3)


friend_info()