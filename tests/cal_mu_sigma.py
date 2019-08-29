import numpy as np
import os
import sys
#import cv2
import time
import openslide
from glob import glob
import histomicstk as htk


def mk_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def load_data(root_path):
    filenames = np.loadtxt('./namelist.txt', dtype=bytes).astype(str)

    wsi_paths = []
    viable_paths = []
    whole_paths = []
    for filename in filenames:
        wsi_paths.append(glob(root_path + filename + '/*.[S, s][V, v][S, s]')[0])
        viable_paths.append(glob(root_path + filename + '/*viable.tif')[0])
        whole_paths.append(glob(root_path + filename + '/*whole.tif')[0])
    data_paths = list(zip(wsi_paths, viable_paths, whole_paths))

    train_paths = data_paths[:int(4*len(filenames)/5)]
    val_paths = data_paths[int(4*len(filenames)/5):]

    return train_paths, val_paths


data_path = '/home/shhxyao/huaxin/projects/ai/contest/PAIP2019/DatasetPAIP2019.Ver2/training/'
train_paths, val_paths = load_data(data_path)

'''
for train_path in train_paths:
    wsi_path, viable_path, whole_path = train_path    
    filename = wsi_path.split('/')[-2]
    
    print('Begin processing: ', filename, 'from:', wsi_path)
    
    mu, sigma = htk.preprocessing.color_normalization.reinhard_stats(wsi_path, 1.0)

    print('Finished: ', filename, mu, sigma)
'''
for val_path in val_paths:
    wsi_path, viable_path, whole_path = val_path
    filename = wsi_path.split('/')[-2]
    
    print('Begin processing: ', filename, 'from:', wsi_path)
    
    mu, sigma = htk.preprocessing.color_normalization.reinhard_stats(wsi_path, 1.0)

    print('Finished: ', filename, mu, sigma)
