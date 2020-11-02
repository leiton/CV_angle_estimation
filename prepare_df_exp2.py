# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 06:33:44 2020

@author: Leo_Mazal
"""

#import utils
import glob
import os
import cv2
#import numpy as np
import pandas as pd
import pickle
from datetime import datetime
#import pdb

os.chdir('C:\\Users\\Leo Mazal\\Desktop\\LEO_Personal\\paper2\\inc_detection\\Experiment2\\')
min_size = 300

path1 = 'Normal\\'
list_files = glob.glob(path1 + '*.jpg')
print('The num of files in', path1, 'is:', len(list_files))

list_labels_N = []
list_images_N = []



list_angles = [cv2.cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE]

num_file = 0
for file in list_files:
    img = cv2.imread(file)
    img = cv2.resize(img, (min_size, min_size))
    j = 0
    
    new_label = 'N_R_' + str(num_file) + '_' + str(j) + '.jpg'
    cv2.imwrite(new_label, img)
    list_labels_N.append(0)
    list_images_N.append(img)
    j = 1
    
    for angle in list_angles:
        

        img_out = cv2.rotate(img, angle)
        new_label = 'N_R_' + str(num_file) + '_' + str(j) + '.jpg'
        cv2.imwrite(new_label, img_out)
        list_labels_N.append(0)
        list_images_N.append(img_out)
        j = j + 1
    num_file = num_file + 1

##############################################     
    
path2 = 'Inc1\\'
list_files_Inc1 = glob.glob(path2 + '*.jpg')
print('The num of files in', path2, 'is:', len(list_files_Inc1))

list_labels_I1 = []
list_images_I1 = []

num_file = 0
for file in list_files_Inc1:
   
    img = cv2.imread(file)
    img = cv2.resize(img, (min_size, min_size))
    j = 0
    
    new_label = 'I_R_' + str(num_file) + '_' + str(j) + '.jpg'
    cv2.imwrite(new_label, img)
    list_labels_N.append(1)
    list_images_N.append(img)
    j = 1
    
    for angle in list_angles:
        
        img_out = cv2.rotate(img, angle)
        #img_out = utils.rotate_img(img, angle)
        new_label = 'I_R_' + str(num_file) + '_' + str(j) + '.jpg'
        cv2.imwrite(new_label, img_out)
        list_labels_I1.append(1)
        list_images_I1.append(img_out)
        j = j + 1
    num_file = num_file + 1
    
# dictionary of lists 
dict = {'images': list_images_N + list_images_I1, 
        'labels': list_labels_N + list_labels_I1} 
  
df = pd.DataFrame(dict)

datestr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
file_name = 'df_images_exp2_0' + datestr + '.pckl' 

with open(file_name, 'wb') as f:
    pickle.dump(df,f)
    f.close()