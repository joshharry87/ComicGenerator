


import numpy as np
import cv2

    
def cut_section(array, x, y, iteration_step):
    '''
        Returns array section based on coord and iteration gap
    
    '''
    
    return np.array(array[((x)*iteration_step):(iteration_step*(x+1)), 
                            ((y)*iteration_step):iteration_step*(y+1)])


def convert_to_grey(array):
    ''' NP array input conversion'''
    return cv2.cvtColor(array, cv2.COLOR_BGR2GRAY) 

