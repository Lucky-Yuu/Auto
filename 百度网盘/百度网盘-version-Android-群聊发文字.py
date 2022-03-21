'''
@File    :   百度网盘-version-Android-群聊发文字.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/21 15:10   xyhu       11.20.3     None
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def group_send_msg():
    driver = BaiDuDisk.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_share')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.ID, 'com.baidu.netdisk:id/iv_close')
            el.click()
            time.sleep(2)
            el1_times += 1
    el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text="通讯录"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="我的群组"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="请输入消息..."]')
    el5.send_keys("测试test1234")
    time.sleep(2)
    el6 = driver.find_element(By.ID, 'com.baidu.netdisk:id/send_file_button')
    el6.click()
    time.sleep(2)


group_send_msg()