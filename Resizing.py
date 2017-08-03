#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:35:00 2017

@author: harshtomar
"""

from __future__ import division
import glob
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage import img_as_uint
from PIL import Image

from resizeimage import resizeimage
i=0
for filename in glob.glob("/home/htomar/Downloads/SNN/Dataset/GS_Faces/*.jpg"):
    #inp_image = imread(filename)
    fd_img = open(filename, 'r')
    img = Image.open(fd_img)
    x,y = img.size
    if(y>160):
        img = resizeimage.resize_height(img, 160)
        i+=1
        #imsave("/home/harshtomar/Downloads/SNN/Dataset/Cropped_Bikes/image_" + str(i) + ".jpg", img) 
        img.save("/home/htomar/Downloads/SNN/Dataset/Cropped_Faces/image_" + str(i) + ".jpeg", img.format)
    fd_img.close()