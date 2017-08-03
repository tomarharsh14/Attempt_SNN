#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:50:20 2017

@author: htomar
"""

import nest
import cv2
import glob
import numpy as np
#==============================================================================
# Load images from the given path and concatenate the images along axis 2
# Images required to be of same height and width; Assume they are DoG images; CHANGE IT

for filename in glob.glob("~~~PATH/TO/IMAGES/~~~"):    
    inp_image = cv2.imread(filename)
    #shape = inp_image.shape
    inp_matrix = []
    inp_matrix = np.concatenate(inp_matrix, inp_image, 2)

#==============================================================================
# TODO: Introduce Discrete Event Simulation Time Parameter

#==============================================================================
# Initialize the First Layer of Neurons. No of nuerons = No of pixels in height*width

h,w,d = inp_matrix.shape
n_Neurons = h*w

#==============================================================================

#==============================================================================
# Get the details of the nest Layer for initializing the neronal connections
nh = None
nw = None
#==============================================================================

#==============================================================================
# Create the neurons and 'connect' them in a way that if the contrast is high, the latency of spike is low.
ndict = {"tau_syn_ex double": 0.0, "tau_syn_in double": 0.0, }  # Rise Time set to 0 for non-leakiness
neuronpop = nest.Create("iaf_psc_alpha", n_Neurons, params=ndict) 
#==============================================================================

#==============================================================================
# Obtain the firing time of the neurons
def get_Firing_Time(neuron):    # Since learning is one layer at a time, I can keep track of the firing times one layer a time.
      
#==============================================================================

#==============================================================================
# Potential Update Rule of a Neuron
# TODO: I will have to use Nest to Update the neuron connection itself
def Update_Potential(V, W, fire_time, position):     # I need the neuron's previous potential, the weights associated with all pre-layer neurons, if those fired or not
    
    V[position] =  V[position] + np.dot(W[position,:],fire_time)                             # and the location of that particular neuron
#==============================================================================

#==============================================================================
# Weight Initialization of Synapses and Update Rule
#prev_Layer = None
#next_Layer = None
#n_Synapses = prev_Layer*next_Layer

a_minus = 0.003
a_plus = 0.004

#Assume all-to-all connection for now
n_Synapses = (h*w)*(nh*nw)  # nh and nw from next layer
W = np.random.normal(0.8, 0.05, n_Synapses)   #n_Synapses = Number of connections b/n pre and post neurons

# i = previous layer neurons; j = next layer neurons
 
def Update_Weights(pre_h, pre_w, post_h, post_w):
    for i in range(pre_h*pre_w):
        for j in range(post_h*post_w):
            if (get_Firing_Time(j) > get_Firing_Time(i):    # fire time of postsynaptic greater than fire time of presynaptic neuron
                W[i][j] = a_minus*W[i][j](1 - W[i][j])
            else:
                W[i][j] = a_plus*W[i][j](1 - W[i][j])
#==============================================================================


