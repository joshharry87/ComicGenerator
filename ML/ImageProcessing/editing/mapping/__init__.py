import os
import numpy as np

import cv2




def get_asset_library_titles():
    filePaths = {}
    directories = []
    for folder,file, dir in os.walk(os.curdir):
        
        for filepath in dir:
            print(filepath)
            directories.append(filepath)
            
        filePaths['drawn'] = directories
        
        return filePaths

