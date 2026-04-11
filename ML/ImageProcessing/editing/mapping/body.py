import numpy as np
# Work in progress - build framework for generating colours, rotations 
# and position information for linking artefacts together
# 


def split_frame(array, perspective):
    
    
    #  calculate splits based on perspective
    
    return array, array, array, array, array, array 
    


def create_full_frame_mapping(array, perspective):
    
    array_set = split_frame(array)
    
    create_upper_body_mapping(array_set[0])
    create_lower_body_mapping(array_set[1])
    create_shoulder_r_mapping(array_set[2])
    create_shoulder_l_mapping(array_set[3])
    create_groin_r_mapping(array_set[4])
    create_groin_l_mapping(array_set[5])
    
    return 
    


def create_upper_body_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    
    
    return array



def create_lower_body_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    return array

def create_shoulder_r_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    return array


def create_shoulder_l_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    return array


def create_groin_r_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    return array



def create_groin_l_mapping(array, perspective='f'):
    """
        Generates numpy array mapping behaviour for each x y pixel.
        (Colour gradient, movement etc.)
    Args:
        Input array 
        Perspective

    Returns:
        
    """
    
    return array


