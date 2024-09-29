# Tello EDUをWi-Fiアクセスポイントへ接続する設定（Wi-Fi子機になるモード）に変更する方法

tag_name: FY2024, きのくにICT教育
最終更新日時: 2024年9月29日 15:00

# はじめに

Tello EDUには自らがWi-Fiアクセスポイントになるモード（Wi-Fi親機モード）とWi-Fi子機になりWi-Fiアクセスポイントへ接続しにいくモード（Wi-Fi子機モード）がある。Wi-Fi子機モードに設定すると一つの操作を複数のTello EDUで実行する編隊飛行が実現できる。
ここでは、Wi-Fi親機モードからWi-Fi子機モードへ変更する方法を記す。また、Wi-Fi子機モードからWi-Fi親機モードに戻す方法についても記す。

# Wi-Fi親機モードからWi-Fi子機モードへ変更する方法

Wi-Fi親機モードに設定されているTello EDUに接続し、以下のプログラムを実行する。Tello EDUの再起動がはじまりWi-Fi子機モードに変更される。

```python
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
```

# Wi-Fi子機モードからWi-Fi親機モードに戻す方法

電源ON時にボタンを5秒以上長押しするとWi-Fi親機モードにリセットされる。