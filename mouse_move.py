#!/usr/bin/env python3
import pyautogui as pg
import time
import random
import subprocess
import ctypes

def get_size():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout = subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    return [resolution[0], resolution[1]]

def get_windows():
    user32 = ctypes.windll.user32
    screensize = [user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)]
    return screensize

def move_mouse(time_interv=500):
    time.sleep(time_interv)
    ssize = get_windows()
    pg.move(200, 0, duration=3)
    time.sleep(time_interv + random.randrange(0, 50))
    pg.move(0, -200, duration=2)
    time.sleep(time_interv + random.randrange(0, 100))
    pg.move(-200, 0, duration=1)
    time.sleep(time_interv + random.randrange(0, 300))
    pg.move(0, 200, duration = 2)

def scroll(amount = 300):
    pg.scroll(amount)
    time.sleep(30)
    pyautogui.scroll(-amount)
    time.sleep(60)


if __name__ == "__main__":
    while True:
        move_mouse(time_interv=1)
        scroll()
    
    
