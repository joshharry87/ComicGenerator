
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


def calc_result_centres(results, window=6):
    '''

    '''
    
    results = np.array(results)
    id_groupings = []
    centre = []
    
    for x in range(0,results.shape[0]):
        for y in range(0,results.shape[1]):
            section = np.sum(results[max(x-(int(window/2)), 
                                        0):min(x+(int(window/2)), results.shape[0]), 
                                    max(0,y-(int(window/2))):min(results.shape[1],y+(int(window/2)))])
            
            id_groupings.append(section)
            
            centre.append(f'{x}_{y}')
            

def calculate_relevance(constrast_sums, scalar=0.25):
    '''
            Returns tile collections based on scalable threshold for relevance, 
            can be applied for colour, black and white and greyscale images. 
            Basically identifying objects based on the contrast in values and clustering.
            
            Input: List of the sums of the computed differences in a pixel range. 
    
    '''
    indexes = []
    treshold = np.array(constrast_sums).max()  - ((
        np.array(constrast_sums).max() - np.array(constrast_sums
                                                  ).min())*scalar)

    i = 0
    for x in constrast_sums:
        if x > treshold:
            indexes.append(i)
            
        i +=1
    
    return indexes, treshold

