'''
@File    :   Taobao-10.10.5-Android-群聊发送图文链接.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/18 15:20   xyhu       10.10.5     494
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def group_send_link():
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
    el4 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="群聊"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="宝贝"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="发送"]')
    el7.click()
    time.sleep(2)


group_send_link()