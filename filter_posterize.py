#Import functions from Cimpl module and import unit testing definition
from Cimpl import *
from Cimpl import get_height, get_width, choose_file, load_image, copy, \
    set_color, create_color, \
    get_color, Image, show
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale
import numpy as np
from point_manipulation import*

#------------------------------------------------------------------------------

def _adjust_component(comp: int) -> int:
    """

    
    Helper function created for the posterize filter. 
    Determines the quadrant in which a component lies and returns the 
    midpoint value of that quadrant.
                
    """        
    
    #checking all quadrants and assigning points 
    if comp in range(0,64):
                        comp = 31                       
    elif comp in range(64,128):
                        comp = 95  
    elif comp in range(128,192):
                        comp = 159      
    elif comp in range(191,256):
                        comp = 223 
      
    #comp will later be used in the posterize filter function
    return comp


def posterize(image: Image):
    """

    
    Adjusts image to have smaller number of colours than the original using the helper
    adjust component function.
                
    >>>file = choose_file()
    >>>image = load_image(file)
    >>>posterize_img = posterize(image)
    >>>show(posterize_img)
    """    
    
    #copy image
    new_image = copy(image)
    for x,y, (r,g,b) in image:
        
        #nusing the colours from the helper function
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        post = create_color(r, g, b)  
        
        #set new colours
        set_color(new_image, x, y, post)
        
    #return new image
    return new_image  

# Main Script for posterize 
file = choose_file()
image = load_image(file)
posterize_img = posterize(image)
show(posterize_img)
