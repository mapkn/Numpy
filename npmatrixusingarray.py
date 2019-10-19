# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:15:32 2017

@author: patemi
"""
import numpy as np
import pandas as pd


x= np.arange(10)

is_spt=np.zeros((2,1))
is_spt[0,0]=0
is_spt[1,0]=0.4

is_spt_t=is_spt.transpose()

mu=np.matmul(is_spt,is_spt_t)

mu_high=np.maximum(2*mu-1,1.25*mu)

mu_low=np.minimum(0.75*mu,1*mu)

