


import numpy as np

    
def cut_section(array, x, y, iteration_step):
    '''
        Returns array section based on coord and iteration gap
    
    '''
    
    return np.array(array[((x)*iteration_step):(iteration_step*(x+1)), 
                            ((y)*iteration_step):iteration_step*(y+1)])
    