import win32api
import win32con
import win32gui
# 要当背景的图片
path = r'C:\Users\86186\Desktop\jc.jpeg'
# 打开注册表
reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)

# 设置值
win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, '2')

# 设置壁纸
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
