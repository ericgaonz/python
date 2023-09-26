import pygame
import time
import win32api
import win32con
import win32gui
import threading

def play_music():
    for i in range(5):
        path = r'C:\Users\86186\Desktop\res\{}.mp3'.format(i)
        # 需要初始化
        pygame.mixer.init()
        # 加载音乐
        pygame.mixer.music.load(path)
        # 播放
        pygame.mixer.music.play()
        # 给个停留的时间
        time.sleep(10)


# 更改桌面背景
def change_wallpaper():
    for i in range(9):
        # 要当背景的图片
        path = r'C:\Users\86186\Desktop\res\{}.jpg'.format(i)
        # 打开注册表
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        # 设置值
        win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, '2')
        # 设置壁纸
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
        time.sleep(5)


# 开启一个线程去做一个事
threading.Thread(target=play_music).start()
# 更改桌面背景
change_wallpaper()

# pyinstaller -F -w -i jc.jpeg .\整蛊小程序.py
