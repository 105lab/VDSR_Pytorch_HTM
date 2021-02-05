# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:27:35 2021

@author: user
"""

import h5py#HDF5的读取：  
f = h5py.File('./data/train.h5','r')   #打开h5文件  # 可以查看所有的主键  
for key in f.keys():      
    print(f[key].name)      
    print(f[key].shape)      
    print(f[key].value)
