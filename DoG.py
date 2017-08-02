#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:59:11 2017

@author: htomar
"""

import numpy as np
from scipy import ndimage
import glob
from skimage.io import imread, imsave

def Gauss(shape=(7,7),sigma=1):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

f1 = Gauss((7,7), 1)
f2 = Gauss((7,7), 2)

i=0

for filename in glob.glob("/home/htomar/Downloads/SNN/Dataset/Cropped_Faces/image_1.jpeg"):
    inp_image = imread(filename)
    #grey = inp_image[:,:,1]
    #g1 = ndimage.convolve(inp_image, f1, mode='constant', cval=0.0)
    #g2 = ndimage.convolve(inp_image, f2, mode='constant', cval=0.0)
    #out_img = g2-g1         #more blurred - less blurred
    #i+=1
    #imsave("/home/htomar/Downloads/SNN/Dataset/DoG_Faces/image_" + str(i) + ".jpeg", out_img)