#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:32:22 2017

@author: harshtomar
"""

import glob
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint
i = 1501
for filename in glob.glob("/home/htomar/Downloads/SNN/Dataset/Faces/image_0001.jpg"):
    inp_image = imread(filename)
    img_gray = rgb2gray(inp_image)
    #thresh = threshold_otsu(img_gray)
    #binary_thresh_img = img_gray & gt; thresh
    #print img_gray
    i+=1
    imsave("/home/htomar/Downloads/SNN/Dataset/GS_Faces/image_" + str(i) + ".jpg", img_gray)