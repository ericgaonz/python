'''
需要安装的模块
pip install pywin32
pip install pygame
pip install pyinstaller
pip install pillow
'''
import pygame
import time
path = r'C:\Users\86186\Desktop\人间精品起来嗨.mp3'
# 需要初始化
pygame.mixer.init()
# 加载音乐
pygame.mixer.music.load(path)
# 播放
pygame.mixer.music.play()
# 给个停留的时间
time.sleep(20)
