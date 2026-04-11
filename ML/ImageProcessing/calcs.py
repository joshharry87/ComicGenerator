
'''
Basic image processing math calcs.

'''



import numpy as np



def scale_contrast(array):
    return (np.square(array / (np.ones(array.shape)*255)))*255
    


def calc_contrast(array):
    return abs(array- (np.ones(array.shape)*np.average(array)))



def invert_values(array, upper = 255):
    '''
    Inverts values in np array 
    
    '''
    return ( array - (np.ones(array.shape)*upper))*-1