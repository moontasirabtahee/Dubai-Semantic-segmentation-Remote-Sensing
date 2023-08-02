import os
def imagelist(dataset_root_path):
    imagepath = []
    for dirs,subdirs,files in os.walk(dataset_root_path):
        dirname = dirs.split(os.path.sep)[-1]
        if dirname == 'images':
            for file in files:
                image_path = os.path.join(dirs,file)
                print("Loading....:",image_path)
                imagepath.append(image_path)
    return imagepath
def masklist(dataset_root_path):
    maskpath = []
    for dirs,subdirs,files in os.walk(dataset_root_path):
        dirname = dirs.split(os.path.sep)[-1]
        if dirname == 'masks':
            for file in files:
                mask_path = os.path.join(dirs,file)
                print("Loading....:",mask_path)
                maskpath.append(mask_path)
    return maskpath