# TEST for posterize filter
# By: Riya Arora- T007 (Team Leader)

#P3T2
#SUBMITTED: June 2nd, 2021

#Import functions from Cimpl module and import unit testing for all definitions
from Cimpl import *
import numpy as np
from point_manipulation import*
from Cimpl import get_height, get_width, choose_file, load_image, copy, \
    set_color, create_color, \
    get_color, Image, show
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale

#import filters that will be tested (milestone 2 filters to be tested)
from T007_P3_filter_posterize import _adjust_component,posterize

#------------------------------------------------------------------------------

def test_posterize() -> None:
    """
    Author: Riya Arora T007
    
    A test function for posterize
    
    >>> test_posterize() 

    """
    # Main script
    
    # Create original image and test values covering all conditions.
    original = create_image(8, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(200, 0, 0))
    set_color(original, 2, 0,  create_color(0, 129, 0))
    set_color(original, 3, 0,  create_color(0, 0, 111))
    set_color(original, 4, 0,  create_color(200, 129, 111))    
    set_color(original, 5, 0,  create_color(216, 89, 45))    
    set_color(original, 6, 0,  create_color(67, 2, 162))    
    set_color(original, 7, 0,  create_color(90, 149, 19))    
        
    # Create an image that's identical to the original with the expected results.
    expected = create_image(8, 1)
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(223, 31, 31))
    set_color(expected, 2, 0,  create_color(31, 159, 31))
    set_color(expected, 3, 0,  create_color(31, 31, 95))
    set_color(expected, 4, 0,  create_color(223, 159, 95))
    set_color(expected, 5, 0,  create_color(223, 95, 31))
    set_color(expected, 6, 0,  create_color(95, 31, 159))
    set_color(expected, 7, 0,  create_color(95, 159, 31))
        
    #Use filter function on the original image
    testpost = posterize(original)
    
    # Now compare the transformed image returned by the filter with the expected image, one pixel at a time.    
    for x, y, col in testpost:
        check_equal('Checking pixels for posterize filter @(' + str(x) + ', ' + str(y) + ')',col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY RIYA ARORA---")