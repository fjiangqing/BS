# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:31:04 2018

@author: fjiangqing
"""

import os  

def sysPZ():
    os.system("raspistill -o P1.jpg")   # 直接使用os.system调用一个echo命令  
    


sysPZ()