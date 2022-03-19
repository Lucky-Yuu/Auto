'''
@File    :   Taobao-10.10.5-Android-群聊发红包.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/18 10:29   xyhu       10.10.5     None
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def group_send_red_env():
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
    el6 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="功能面板"]')
    el6.click()
    time.sleep(2)
    el7 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="红包"]')
    el7.click()
    time.sleep(2)
    el8 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="填写个数"]')
    el8.send_keys("1")
    el9 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="填写金额"]')
    el9.send_keys("0.01")
    el10 = driver.find_element(By.XPATH, '//android.widget.EditText[@text="恭喜发财，大吉大利！"]')
    el10.send_keys("测试test1234")
    el11 = driver.find_element(By.XPATH, '(//android.view.View[@content-desc="发红包"])[2]')
    el11.click()
    time.sleep(2)
    el12 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="确认付款"]')
    el12.click()
    time.sleep(2)
    el13_times = 0
    while el13_times < 3:
        try:
            for i in Taobao.taobao_account['pay_password']:
                el13 = driver.find_element(By.ID, 'com.taobao.taobao:id/au_num_' + i)
                el13.click()
            time.sleep(1)
            time.sleep(1)
            break
        except:
            el14 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="使用密码"]')
            el14.click()
            time.sleep(2)
            el13_times += 1
    time.sleep(3)


group_send_red_env()
