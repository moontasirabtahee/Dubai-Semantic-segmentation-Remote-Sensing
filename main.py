import cv2
import numpy as np
from DevEnv import dataInfo,dataList,ImagePatchify

import numpy as np




dataset_root_path = 'Semantic segmentation dataset'
image_patch_size = 256

image_dataset =np.array(ImagePatchify.imagepatch(dataset_root_path, image_patch_size))
mask_dataset = np.array(ImagePatchify.maskpatch(dataset_root_path, image_patch_size))
if len(image_dataset) == len(mask_dataset):
    print("Image and Mask dataset are of same size")
    print("Image dataset shape:",image_dataset.shape)
    print("Mask dataset shape:",mask_dataset.shape)
# for i in range(len(image_dataset)):
#     cv2.imshow("image",image_dataset[i])
#     cv2.imshow("mask",mask_dataset[i])
#     cv2.waitKey(200)
#     cv2.destroyAllWindows()

