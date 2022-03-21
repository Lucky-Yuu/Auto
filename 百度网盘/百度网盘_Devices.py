'''
@File    :   百度网盘_Devices.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/20 15:25   xyhu       11.20.3     None
'''
# 该账号需在安全设备登录，即已登录过的设备
baidu_account = {
    'username': '17625056788',
    'password': '1.2.3..@'
}
friend = {
    'username': '13951457473'  # 被添加的账号
}
# 主设备
desired_caps_a = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '11',  # 设备系统版本号
    'deviceName': 'YSE0221921000592',  # 设备号 P50
    'appPackage': 'com.baidu.netdisk',  # 包名
    'appActivity': 'com.baidu.netdisk.ui.DefaultMainActivity',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '180',
    'androidDeviceReadyTimeout': '3600'
}
# 副设备
desired_caps_b = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '10',  # 设备系统版本号
    'deviceName': 'HJS5T19506006942',  # 设备号，手动填写
    'appPackage': 'com.baidu.netdisk',  # 包名
    'appActivity': 'com.baidu.netdisk.ui.DefaultMainActivity',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '180',
    'androidDeviceReadyTimeout': '3600'
}

server_a = 'http://localhost:4723/wd/hub'
server_b = 'http://localhost:4725/wd/hub'
