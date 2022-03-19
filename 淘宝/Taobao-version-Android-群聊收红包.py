'''
@File    :   Taobao-10.10.5-Android-群聊收红包.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/19 9:44   xyhu       10.10.5     None
'''
import time
from appium import webdriver
from selenium.webdriver.common.by import By
import Taobao_Devices as Taobao


def group_rec_red_env():
    a_driver = webdriver.Remote(Taobao.server_a, Taobao.desired_caps_a)
    b_driver = webdriver.Remote(Taobao.server_b, Taobao.desired_caps_b)
    a_el1_times = 0
    while a_el1_times < 3:
        try:
            a_el1 = a_driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            a_el1.click()
            time.sleep(2)
            break
        except:
            a_el2 = a_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            a_el2.click()
            time.sleep(2)
            a_el1_times += 1
    a_el3 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    a_el3.click()
    time.sleep(2)
    a_el4 = a_driver.find_element(By.XPATH, '//android.view.View[@content-desc="群聊"]')
    a_el4.click()
    time.sleep(2)
    a_el5 = a_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    a_el5.click()
    time.sleep(2)
    b_el1_times = 0
    while b_el1_times < 3:
        try:
            b_el1 = b_driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="消息"]')
            b_el1.click()
            time.sleep(2)
            break
        except:
            b_el2 = b_driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            b_el2.click()
            time.sleep(2)
            b_el1_times += 1
    b_el3 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="联系人"]')
    b_el3.click()
    time.sleep(2)
    b_el4 = b_driver.find_element(By.XPATH, '//android.view.View[@content-desc="群聊"]')
    b_el4.click()
    time.sleep(2)
    b_el5 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="A测试"]')
    b_el5.click()
    time.sleep(2)
    b_el6 = b_driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="功能面板"]')
    b_el6.click()
    time.sleep(2)
    b_el7 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="红包"]')
    b_el7.click()
    time.sleep(2)
    b_el8 = b_driver.find_element(By.XPATH, '//android.widget.EditText[@text="填写个数"]')
    b_el8.send_keys("1")
    b_el9 = b_driver.find_element(By.XPATH, '//android.widget.EditText[@text="填写金额"]')
    b_el9.send_keys("0.01")
    b_el10 = b_driver.find_element(By.XPATH, '//android.widget.EditText[@text="恭喜发财，大吉大利！"]')
    b_el10.send_keys("测试test1234")
    b_el11 = b_driver.find_element(By.XPATH, '(//android.view.View[@content-desc="发红包"])[2]')
    b_el11.click()
    time.sleep(2)
    b_el12 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="确认付款"]')
    b_el12.click()
    time.sleep(2)
    b_el13_times = 0
    while b_el13_times < 3:
        try:
            for i in Taobao.taobao_account_b['pay_password']:
                b_el13 = b_driver.find_element(By.ID, 'com.taobao.taobao:id/au_num_' + i)
                b_el13.click()
            time.sleep(1)
            break
        except:
            b_el14 = b_driver.find_element(By.XPATH, '//android.widget.TextView[@text="使用密码"]')
            b_el14.click()
            time.sleep(2)
            b_el13_times += 1
    time.sleep(3)
    try:
        a_el6 = a_driver.find_element(By.XPATH, '//android.view.View[@content-desc="测试test1234"]')
        a_el6.click()
        time.sleep(3)
        a_el7 = a_driver.tap([(503, 1330), (718, 1545)], 20)
        time.sleep(3)
    except:
        a_el8 = a_driver.find_element(By.XPATH, '(//android.view.View[@content-desc="测试test1234"])[2]')
        a_el8.click()
        time.sleep(3)
        a_el9 = a_driver.tap([(503, 1330), (718, 1545)], 20)
        time.sleep(3)


group_rec_red_env()
