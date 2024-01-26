'''
Настрйоки и константы для игры будут временно (или нет, я не знаю) находиться здесь
Спасибо за внимание :)

Определяется размеры экрана и подгоняет окно игры, но не сам уровень.
'''

from ctypes  import *
print(windll.user32.GetSystemMetrics(0))
print(windll.user32.GetSystemMetrics(1))

# размер уровня: 4096 X 512 (исходный 1024 Х 128)
WIDTH_LEVEL = 4096
HEIGHT_LEVEL = 512

# окно игры
WIDTH = windll.user32.GetSystemMetrics(0)
HEIGHT = windll.user32.GetSystemMetrics(1)
FPS = 60