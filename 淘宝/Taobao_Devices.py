'''
@File    :   Taobao_Devices.py    
@APPTYPE :   Android
@Model   :   Huawei P50

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/18 15:40   xyhu       10.10.5     None
此配置用于两台设备的交互
'''
#主设备
desired_caps_a = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '11',  # 设备系统版本号
    'deviceName': 'YSE0221921000592',  # 设备号 P50
    'appPackage': 'com.taobao.taobao',  # 包名
    'appActivity': 'com.taobao.tao.TBMainActivity',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': False,
    'resetKeyboard': False,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '60',
    'androidDeviceReadyTimeout': '3600'
}
#副设备
desired_caps_b = {
    'platformName': 'Android',  # 系统平台的名称
    'platformVersion': '10',  # 设备系统版本号
    'deviceName': 'HJS5T19506006942',  # 设备号，手动填写
    'appPackage': 'com.taobao.taobao',  # 包名
    'appActivity': 'com.taobao.tao.TBMainActivity',  # 启动入口
    'automationName': 'Uiautomator2',  # 自动化测试引擎
    'unicodeKeyboard': False,
    'resetKeyboard': False,
    'noReset': True,  # 是否重置应用
    'newCommandTimeout': '60',
    'androidDeviceReadyTimeout': '3600'
}

server_a = 'http://localhost:4723/wd/hub'
server_b = 'http://localhost:4725/wd/hub'

taobao_account_a = {
    'username': '',
    'password': 'huxinyu123..',
    'pay_password': '980097'
}

taobao_account_b = {
    'username': '',
    'password': '',
    'pay_password': '980097'
}
