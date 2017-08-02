#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:14:25 2017

@author: htomar
"""

from Pooling import MaxPooling
import numpy as np
import cv2
#==============================================================================
# a = np.array([5,7,1,8,
#      1,2,3,4,
#      4,5,6,7,
#      7,8,9,10])
# shape = (4,4,1)
# a.shape = shape
# out = MaxPooling(a,size=2,stride=2)
# print out
#==============================================================================

image = cv2.imread('0401.jpg')
output = MaxPooling(image, 8, 1)
out = cv2.imwrite('0402.jpg', output)