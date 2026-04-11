
'''
To-Do  : clean  and abstract these functions meaningfully.

'''
from skimage import io, filters, measure, segmentation
import matplotlib.pyplot as plt

from PIL import Image, ImageFilter, ImageEnhance
import cv2
import numpy as np

from ImageProcessing.tile import Tile, TileRange
# to be reworked and intedgrated into library

import sys 
import os



# to do clean up group as data classes etc. 


def get_image_array(filepath):
    '''
        grab rgb array from filepath
    '''
    
    return cv2.imread(filepath)



def get_greyscale_array(filepath):
    '''grab greyscale from filepath'''
    return cv2.cvtColor(get_image_array(filepath), cv2.COLOR_BGR2GRAY) 



def black_pixels(array, scalar=255, delta=0):
    ''' 
        based on delta and scaling flip all dark pixels to black 
        and light pixels to white.
    '''
    return np.round((array+delta)/scalar)*255




def group_interesting_tiles(indexes, chunksin, iteration_step):
    '''
        takes in the Relevant Discovered Tiles, 
        compares with the chunked original image and defines
        the x, y range of the images discovered.
    
    '''
    
    groups = []
    
    #  create an object / class for this preferably data class
    group = {
        'start_x' : 0,
        'start_y' : 0,
        'end_x' : 0,
        'end_y' : 0,
        'tile' : False
    }

    # to do - review logic - clean up and rework.
    for index  in indexes:
        new_group_flag = False
        tile_flag = True
        # print(index)
        x , y = int(chunksin[indexes][1].split("_")[0])*iteration_step, int(chunksin[index][1].split("_")[1])*iteration_step
        for collection in groups:
            if (collection['end_y'] == y and (x >= collection['start_x'] and x <= collection['end_x'])  ):
                collection['end_y'] = y +iteration_step
                tile_flag = False         
            elif (x == collection['end_x'] and y + iteration_step == collection['end_y']):
                collection['end_x'] = x + iteration_step
                tile_flag = False

            elif  (collection['end_y'] >= y  and collection['start_y'] <= y  
                   and (x >= collection['start_x'] and x <= collection['end_x'])  ):
                print("exists")
                tile_flag = False
            
            else:
                new_group_flag = True
        
        
        if (new_group_flag and tile_flag):
                
            new_group =  {
                            'start_x' : x-iteration_step,
                            'start_y' : y-iteration_step,
                            'end_x' : x+iteration_step,
                            'end_y' :  y +iteration_step,
                        } 
            groups.append(new_group)

        if len(groups) == 0:
            new_group =  {
                                'start_x' : x-iteration_step,
                                'start_y' : y-iteration_step,
                                'end_x' : x+iteration_step,
                                'end_y' :  y +iteration_step,
                            } 
            print(group)
            groups.append(new_group)
        # print(groups)
        tile_flag == True
    for collection in groups:
        collection['end_y'] = collection['end_y'] + iteration_step
        collection['end_x'] = collection['end_x'] + iteration_step
    remove = []
    
    #  for review - look into ways to improve this logic
    for i in range(0, len(groups)):
        for ii in range(0, len(groups)):
            if groups[i]['end_y'] >= groups[ii]['start_y'] and groups[i]['start_y'] >= groups[ii]['start_y'] and groups[i]['start_y'] <= groups[ii]['end_y'] and i != ii:
                groups[i]['end_y'] =  max(groups[i]['end_y'], groups[ii]['end_y'])
                groups[i]['start_y'] =  min(groups[i]['start_y'], groups[ii]['start_y'])
                groups[i]['end_x'] =  max(groups[i]['end_x'], groups[ii]['end_x'])
                groups[i]['start_x'] =  min(groups[i]['start_x'], groups[ii]['start_x'])
                groups[ii]['end_y'] =  max(groups[i]['end_y'], groups[ii]['end_y'])
                groups[ii]['start_y'] =  min(groups[i]['start_y'], groups[ii]['start_y'])
                groups[ii]['end_x'] =  max(groups[i]['end_x'], groups[ii]['end_x'])
                groups[ii]['start_x'] =  min(groups[i]['start_x'], groups[ii]['start_x'])
                print("overlap y")
                
            

     
    unique = []
    
    #  this needs to be cleaned
    for item in groups:
        try:
            if iteration_step < 100:
                item["end_x"] = item["end_x"] + iteration_step
            unique.index(item)
        except:

            unique.append(item)

    
    return  unique
                
            

        
        