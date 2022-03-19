'''
@File    :   Taobao-10.10.5-Android-取消收藏.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/19 14:30   xyhu       10.10.5     170
'''
import time
from selenium.webdriver.common.by import By
import Taobao_Base as Taobao


def cancel_collect():
    driver = Taobao.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="我的淘宝"]')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="关闭按钮"]')
            el.click()
            time.sleep(2)
            el1_times += 1

    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="收藏"]')
    el2.click()
    time.sleep(2)
    el3 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="管理"]')
    el3.click()
    time.sleep(2)
    el4 = driver.find_element(By.XPATH,'//android.view.View[@content-desc="删除"]')
    el4.click()
    time.sleep(2)
    el5 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="删除" and @index="2"]')
    el5.click()
    time.sleep(2)
    el6 = driver.find_element(By.XPATH, '//android.view.View[@content-desc="完成"]')
    el6.click()
    time.sleep(2)


cancel_collect()
