import os
import numpy as np

from ImageProcessing.mapping import get_asset_library_titles

import cv2
# needs to be logically mapped to relevant folder structure

# def get_asset_library_titles():
#     filePaths = {}
#     directories = []
#     for folder,file, dir in os.walk(os.curdir):
        
#         for filepath in dir:
#             print(filepath)
#             directories.append(filepath)
            
#         filePaths['drawn'] = directories
        
#         return filePaths



def store_asset(assetarray, category, gender, perspective, dim=3):
    filePaths = get_asset_library_titles()
    iteration = int(filePaths[category][gender][-1].split("_")[-1].split(".")[0]) + 1
    file_name = f'{category}_{gender}_{perspective}_{iteration}.npz'
    
    np.save(file_name, assetarray)
    
    img_array = np.array()
    match dim:
        case 3:
            img_array = assetarray[:,:,:]
        case 2:
            img_array = assetarray[:,:]

    
    
    cv2.imwrite(file_name.replace(".npz", ".jpg"), img_array)
    
    
    return f"Stored asset in {file_name}"
    
    
    
    
    
    
    
    