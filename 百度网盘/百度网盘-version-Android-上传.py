'''
@File    :   百度网盘-version-Android-上传.py
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 17:25   xyhu       11.20.3     28
'''
import time
from selenium.webdriver.common.by import By
import 百度网盘_Base as BaiDuDisk


def upload():
    driver = BaiDuDisk.driver
    el1_times = 0
    while el1_times < 3:
        try:
            el1 = driver.find_element(By.ID, 'com.baidu.netdisk:id/rb_filelist')
            el1.click()
            time.sleep(2)
            break
        except:
            el = driver.find_element(By.ID, 'com.baidu.netdisk:id/iv_close')
            el.click()
            time.sleep(2)
            el1_times += 1

    el2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="测试"]')
    el2.click()
    time.sleep(2)
    el3_times = 0
    while el3_times < 3:
        try:
            el3 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="上传文档"]')
            el3.click()
            time.sleep(2)
            el4_times = 0
            while el4_times < 3:
                try:
                    el4 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="测试test.txt"]')
                    el4.click()
                    time.sleep(1)
                    el5 = driver.find_element(By.ID, 'com.baidu.netdisk:id/button_select_ok')
                    el5.click()
                    time.sleep(2)
                    break
                except:
                    el6 = driver.find_element(By.XPATH,
                                              '//android.widget.CheckBox[@resource-id="com.baidu.netdisk:id/checkbox_upload" and @checked="true"]')
                    el6.click()
                    time.sleep(2)
                    el4_times += 1
            break
        except:
            el7 = driver.find_element(By.ID, 'com.baidu.netdisk:id/file_list_title_right_one')
            el7.click()
            time.sleep(2)
            el8 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="选择文件"]')
            el8.click()
            time.sleep(2)
            el9 = driver.find_element(By.ID, 'com.baidu.netdisk:id/edit_right_button')
            el9.click()
            time.sleep(2)
            el10 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="删除"]')
            el10.click()
            time.sleep(2)
            el11 = driver.find_element(By.XPATH, '//android.widget.Button[@text="确认删除"]')
            el11.click()
            time.sleep(3)
            el3_times += 1


upload()
