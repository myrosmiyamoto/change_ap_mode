#!/usr/bin/env python
# -*- coding: utf-8 -*-

from djitellopy import Tello
import time

tello = Tello()
tello.connect()
time.sleep(5)
# connect_to_wifi('SSID', 'PASSWORD')
# 接続するSSIDとPASSWORDを指定
tello.connect_to_wifi('Buffalo-G-7C30', '60443182')
