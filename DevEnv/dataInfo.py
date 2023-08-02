import os
import numpy as np
import cv2

def get_dataset_info(dataset_root_path):
    for dirs , subdirs, files in os.walk(dataset_root_path):
        dirname = dirs.split(os.path.sep)[-1]
        print(dirname)
        print("<-------------------------------->")
        if dirname == 'images':
            print('------------------')
            for file in files:
                image_path = os.path.join(dirs, file)
                image = cv2.imread(image_path)
                print(image_path,'---___---' ,image.shape)
                print('------------------')
        elif dirname == 'masks':
            print('------------------')
            for file in files:
                mask_path = os.path.join(dirs, file)
                mask = cv2.imread(mask_path)
                print(mask_path,"___---___", mask.shape)
                print('------------------')


