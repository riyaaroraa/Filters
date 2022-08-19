
# Riya Arora

# DISCLAIMER: there are errors and the code isnt perfect yet.

# Import functions: 

from Cimpl import *
from unit_testing import check_equal
from T012_P3_filter_three_tone import three_tone

# Test function:

def three_tone_test() -> str: 
    """ 
    Compares and tests the RGB values from the filtered image
    to the expected ones.
    """
    # Create original image and set the test cases:
    
    original = create_image(6, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    # Create image with expected results and fill in the correct values in each location:
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(255, 0, 0))
    set_color(expected, 1, 0,  create_color(255, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(0, 255, 0))
    set_color(expected, 4, 0,  create_color(0, 0, 255))
    set_color(expected, 5, 0,  create_color(0, 0, 255))
    actual_filtered_image = three_tone (original, "blood", "lime", "blue")
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel at (' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))    

# Call functions: 

three_tone_test()