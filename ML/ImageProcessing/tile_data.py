'''
    Functions for determining relevant objects within an image.



'''
import numpy as np
import ImageProcessing.calcs as calcs
import ImageProcessing.editing_arrays as e





def calc_contrast_and_averages(image_array, iteration_step = 128):
    '''
        Takes an image array in,, splits into chunks defined in pixels
        by the iteration step value
    
    '''
    
    chunks = []
    averages = []
    diffs = []
    results = []
    
    for x in range(0, int(image_array.shape[0]/iteration_step)):
        x_run = []

        
        
        for y  in range(0, round(image_array.shape[1]/iteration_step)):
            section = e.cut_section(image_array, x, y, iteration_step)
            
            scale_contrast = calcs.scale_contrast(section)
            
            contrast = calcs.calc_contrast(scale_contrast)

            inverted =   calcs.invert_values(section)
          
            chunks.append((inverted, f'{x}_{y}', section))
            averages.append(np.sum(section))
            diffs.append(np.sum(contrast))
            x_run.append(np.sum(contrast))
        
        
    results.append(x_run)
    
    
    return (chunks, averages, diffs, results)



    
    