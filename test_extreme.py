

#Import functions from Cimpl module
from Cimpl import *

#Import unit testing
from unit_testing import check_equal

from T046_P3_ import extreme_contrast

#function definition for red filter testing

def test_extreme_constrast() -> str:
    """
    A test function for extreme_contrast
    
    >>> test_extreme_contrast()
    
    """
    #create original image and set test cases
    original = create_image(3, 1) 
    set_color(original, 0, 0, create_color(0, 255, 0))
    set_color(original, 1, 0, create_color(128, 127, 20))
    set_color(original, 2, 0, create_color(127, 128, 128))
    
    # Create image with expected results
    expected = create_image(3, 1) 
    # Fill in the correct values in each location    
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 255, 255))
    

    #Use filter function on the original image
    actual_filtered_image = extreme_contrast(original)
    
    # Comparing the transformed image returned by the filter with the expected image, one pixel at a time.    
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))

test_extreme_constrast()
