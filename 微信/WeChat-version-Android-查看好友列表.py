"""
@File    :   WeChat-version-Android-HUAWEI-查看好友列表.py
@APPTYPE :   Android

@Modify Time      @Author    @Version    @Action
------------      -------    --------    -----------
2022/3/9 9:31     xyhu       8.0.19      12
"""
import time
import WeChat_Base as WeChat


def friend_list():
    driver = WeChat.driver
    WeChat.tap_once(416, 2546, 502, 2601, 20)
    WeChat.swipe_up(20)
    time.sleep(2)


friend_list()
