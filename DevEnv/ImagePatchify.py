
import os
from DevEnv import dataInfo, dataList
from PIL import Image
import numpy as np
from patchify import patchify, unpatchify
from sklearn.preprocessing import MinMaxScaler
import cv2


def imagepatch(dataset_root_path, image_patch_size):
    # just like the above snippet i need to make a function that will patchify the images and set them in to a array
    image_path = dataList.imagelist(dataset_root_path)
    image_dataset = []
    for imgp in image_path:
        filename = imgp.split(os.path.sep)[-1]
        img = cv2.imread(imgp)
        x_size = (img.shape[1] // image_patch_size) * image_patch_size
        y_size = (img.shape[0] // image_patch_size) * image_patch_size

        img = Image.fromarray(img)
        img = img.crop((0, 0, x_size, y_size))
        img = np.array(img)
        patches_img = patchify(img, (image_patch_size, image_patch_size, 3), step=image_patch_size)
        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):
                single_patch_img = patches_img[i, j, :, :]
                single_patch_img = MinMaxScaler().fit_transform(single_patch_img.reshape(-1, single_patch_img.shape[-1])).reshape(single_patch_img.shape)
                single_patch_img = single_patch_img[0]
                print("Patching Image.. from:",imgp,"\nfilename:",filename,"------->",single_patch_img.shape)
                image_dataset.append(single_patch_img)


    return image_dataset

def maskpatch(dataset_root_path, image_patch_size):
    # just like the above snippet i need to make a function that will patchify the masks and set them in to a array
    mask_path = dataList.masklist(dataset_root_path)
    mask_dataset = []
    for msk in mask_path:
        filename = msk.split(os.path.sep)[-1]
        img = cv2.imread(msk)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x_size = (img.shape[1] // image_patch_size) * image_patch_size
        y_size = (img.shape[0] // image_patch_size) * image_patch_size

        img = Image.fromarray(img)
        img = img.crop((0, 0, x_size, y_size))
        img = np.array(img)
        patches_img = patchify(img, (image_patch_size, image_patch_size, 3), step=image_patch_size)
        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):
                single_patch_img = patches_img[i, j, :, :]
                single_patch_img = MinMaxScaler().fit_transform(single_patch_img.reshape(-1, single_patch_img.shape[-1])).reshape(single_patch_img.shape)
                single_patch_img = single_patch_img[0]
                print("Patching Image.. from:",msk,"\nfilename:",filename,"------->",single_patch_img.shape)
                mask_dataset.append(single_patch_img)



    return mask_dataset
