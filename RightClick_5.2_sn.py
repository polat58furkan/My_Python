# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 19:49:50 2023

@author: dell-pc
"""

import mouse
import keyboard
import time


while True:
    
    i=0 
    if keyboard.is_pressed("0"):
        while i<1:    
            mouse.click('left')
            time.sleep(5.2)
            if keyboard.is_pressed("1"):
                i=10
                break

    if keyboard.is_pressed("1"):
        break
    
exit()