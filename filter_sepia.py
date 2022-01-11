# DEFINITION for sepia tint filter
# By: Riya Arora- T007 (Team Leader)

#P3T2
#SUBMITTED: June 2nd, 2021

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

def sepia(original_image: Image) -> Image:
    """
    Author : Riya Arora T007
    
    Returns a copy of the original image in where all pixels have been 
    sepia tinted according to their range.
    
    >>> original_image = load_image(choose_file())
    >>> sepiaimage = sepia(original_image)
    >>> show(sepiaimage)
    """
    
    #create copy image
    new_image = copy(original_image)
    sepia_filter = grayscale(new_image)
    
    #using ranges multiply into the correct rgb value
    for pixel in sepia_filter:
        x, y, (r, g, b) = pixel
        if r < 63:
            r *= 1.1
            b *= 0.9

        if 63 <= r <= 191:
            r*= 1.15
            b *= 0.85

        if r > 191:
            r *= 1.08
            b *= 0.93
        
        #output new colour
        new_color = create_color(r, g, b)
        
        #set new colours
        set_color(sepia_filter, x, y, new_color)

    #return new image
    return sepia_filter

# Main Script for sepia tinting 
original_image = load_image(choose_file())
sepiaimage = sepia(original_image)
show(sepiaimage)