# Attempt_SNN
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:15:54 2017

@author: htomar
"""
import numpy as np
import math

# Square Window of default size 2 with stride 2
def MaxPooling(inp, size=2, stride=2):
    # 2 Dimensional or greater
    if (len(inp.shape) ==  2):
       h,w = inp.shape
       d = 1
    else:
       h,w,d = inp.shape
 
# ========To take care of uneven kernel size with image========   
    kh = int(math.ceil((h-size)/float(stride) + 1))  
    kw = int(math.ceil((w-size)/float(stride) + 1))

    h = int(math.ceil(kh)*stride + size)
    w = int(math.ceil(kw)*stride + size)
# =============================================================
    out = np.zeros((kh,kw,d))
 
# ========Iteration over the image(s)==========================
    for z in range(d):                         # Iterate inwards last
        for y in range(0,h-size,stride):       # Iterate downwards second
           for x in range(0,w-size,stride):    # Iterate sideways first
               out[y/stride, x/stride, z] = np.amax(inp[y:y+size,x:x+size,z])
# ============================================================= 
    return out
