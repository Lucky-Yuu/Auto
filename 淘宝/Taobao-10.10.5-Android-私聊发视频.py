'''
@File    :   Taobao-10.10.5-Android-私聊发视频.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/17 11:01   xyhu       10.10.5     765
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def send_video():
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
    el5 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="发消息"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="功能面板"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="短视频"]')
    el7.click()
    time.sleep(2)
    el8_times = 0
    while el8_times < 5:
        try:
            el8 = driver.find_element(By.ID, 'com.taobao.taobao:id/btn_record')
            el8.click()
            time.sleep(20)
            break
        except :
            try:
                el9 = driver.find_element(By.XPATH, '//android.widget.Button[@text="仅使用期间允许"]')  # 第一次需授权
                el9.click()
                time.sleep(2)
                el8_times +=1
            except:
                el9 = driver.find_element(By.XPATH, '//android.widget.Button[@text="允许所有文件"]')  # 第一次需授权
                el9.click()
                time.sleep(2)
                el8_times += 1
    el10 = driver.find_element(By.ID, 'com.taobao.taobao:id/btn_record')
    el10.click()
    time.sleep(3)
    el11 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="确定"]')
    el11.click()
    time.sleep(7)


send_video()