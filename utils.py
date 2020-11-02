# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 07:28:24 2020

@author: LeonelMazal
"""

import numpy as np
import pdb


def rotate_img(img, angle):
    D = np.round(np.array([[np.cos(angle), -np.sin(angle)], [+np.sin(angle), np.cos(angle)]]))

    Xm = img.shape[0]
    Ym = img.shape[1]
    Zm = img.shape[2]

    im_out = np.zeros((Ym, Xm, Zm))

    for jj in np.arange(0, Ym, 1):
        for i in np.arange(0, Xm, 1):
            pos_in = np.array([i, jj])
            
            pos_out = np.round(np.matmul(D, pos_in) + np.array([Ym - 1, 0])).astype(int)
            pdb.set_trace()
            for k in np.arange(0, Zm, 1):
                if i == 1:
                    pdb.set_trace()
                im_out[pos_out[0], pos_out[1], k] = img[i, jj, k]

    return im_out.astype(np.uint8)
