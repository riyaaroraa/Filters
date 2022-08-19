#Riya Arora

#MILESTONE2

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
from T012_P3_filter_three_tone import three_tone
from T012_P3_filter_extreme import extreme_contrast
from T012_P3_filter_posterize import _adjust_component,posterize
from T012_P3_filter_sepia import sepia

#import filters that will be tested (milestone 3 filters to be tested)
from T012_P4_filter_vertical import flip_vertical
from T012_P4_filter_edge import detect_edges
from T012_P4_filter_horizontal import flip_horizontal
from T012_P4_filter_draw import*

#--------------------------------------------------------------------------------
# TESTING for three tone filter
# By: Riya Arora

def three_tone_test() -> str: 
    """ 
    Author: Riya Arora
    
    A test function for three_tone
    
    >>> three_tone_test()
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
        check_equal('Checking pixels for three tone filter at (' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))  
        
    print("---TEST COMPLETED BY Ibramhim Ayman Al-Buhaisi ---")
    
#--------------------------------------------------------------------------------
# TESTING for extreme contrast filter
# By:  Riya Arora

def test_extreme_contrast() -> str:
    """
    
    Author: Riya Arora
    
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
        check_equal('Checking pixels for extreme contrast filter @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))

    print("---TEST COMPLETED BY Shebab Salama---")
#--------------------------------------------------------------------------------
# TESTING for posterize filter
# By: Riya Arora 

def test_posterize() -> None:
    """
    Author: Riya Arora
    
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
        
    print("---TEST COMPLETED BY Riya Arora---")

#--------------------------------------------------------------------------------
# TESTING for sepia tinting filter
# By:  Riya Arora

def test_sepia() -> None:
    """
    Author: Riya Arora
    
    A test function for sepia
    
    >>> test_sepia()    

    """    

    sepaioriginal = create_image(4, 1)
    set_color(sepaioriginal, 0, 0,  create_color(0, 0, 0))
    set_color(sepaioriginal, 1, 0,  create_color(149, 149, 149))
    set_color(sepaioriginal, 2, 0,  create_color(216, 216, 216))
    set_color(sepaioriginal, 3, 0,  create_color(45, 45, 45))
    
    # Create an image that's identical to the one a correct implementation of
    # invert should produce when it is passed original.

    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(171.35, 149, 126.65))
    set_color(expected, 2, 0,  create_color(233.28, 216, 200.88))
    set_color(expected, 3, 0,  create_color(49.5, 45, 40.5))
  
    

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    sepiatest = sepia(sepaioriginal)
    for x, y, col in sepiatest:  # col is the Color object for the pixel @ (x,y).
                                # There's no need to unpack that object into
                                # RGB components.
        check_equal('Checking pixels for sepia tinting filter @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY Bhavesh Bhatia---")
        
#--------------------------------------------------------------------------------
# TESTING for edge detection filter
# By: Riya Arora

def test_edge() -> None:
    """
    Author: Riya Arora
    
    A test function for sepia
    
    >>> test_edge()    

    """        
    
    threshold = 8
    
    edge_original = create_image(3, 3)
    set_color(edge_original, 0, 0,  create_color(0, 0, 0))
    set_color(edge_original, 0, 1,  create_color(221, 239, 5))
    set_color(edge_original, 1, 0,  create_color(31, 196, 250))
    set_color(edge_original, 1, 1,  create_color(185, 99, 238))
    set_color(edge_original, 1, 2,  create_color(6, 32, 30))
    set_color(edge_original, 2, 1,  create_color(209, 213, 106))
    set_color(edge_original, 2, 2,  create_color(51, 243, 60))
    set_color(edge_original, 0, 2,  create_color(4, 86, 34))
    set_color(edge_original, 2, 0,  create_color(197, 61, 2))
    
    # Create an image that's identical to the one a correct implementation of
    # invert should produce when it is passed original.

    expected = create_image(3, 3)
    set_color(expected, 0, 0,  create_color(0,0,0))
    set_color(expected, 0, 1,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 1,  create_color(0, 0, 0))
    set_color(expected, 1, 2,  create_color(255,255,255))
    set_color(expected, 0, 2,  create_color(255,255,255))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 1,  create_color(0, 0, 0))
    set_color(expected, 2, 2,  create_color(255,255,255))
    
    
    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.
    

    detectedge = detect_edges(edge_original, threshold)
    
    
    for x, y, col in detectedge: # col is the Color object for the pixel @ (x,y).
                                # There's no need to unpack that object into
                                # RGB components.
        check_equal('Checking pixels for edge detection filter @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY Bhavesh Bhatia---")

#--------------------------------------------------------------------------------
# TESTING for horizontal flip filter
# By: Riya Arora

def test_horizontal_flip() -> None: 
    """
    
    Author: Riya Arora
    
    A test function for the flip_vertical filter
    
    >>> test_horizontal_flip()
    
    """      
    
    #create original image and set test cases
    
    original = create_image(6, 1) 
    set_color(original, 0, 0,  create_color(127,55,231)) 
    set_color(original, 1, 0,  create_color(0,255,130)) 
    set_color(original, 2, 0,  create_color(55,128,2)) 
    set_color(original, 3, 0,  create_color(255,33,201)) 
    set_color(original, 4, 0,  create_color(55,0,152)) 
    set_color(original, 5, 0,  create_color(152,65,255))   
    
    # Create image with expected results
    
    expected = create_image(6, 1) 
    
    # Fill in the correct values in each location 
    
    set_color(expected, 0, 0,  create_color(152, 65, 255)) 
    set_color(expected, 1, 0,  create_color(55, 0, 152)) 
    set_color(expected, 2, 0,  create_color(255, 33, 201)) 
    set_color(expected, 3, 0,  create_color(55, 128, 2)) 
    set_color(expected, 4, 0,  create_color(0, 255, 130)) 
    set_color(expected, 5, 0,  create_color(127, 55, 231))
    
    #Use filter function on the original image
    
    actual_filtered_image = flip_horizontal(original)
    
    # Comparing the transformed image returned by the filter with the expected image, one pixel at a time.
    for x, y, col in actual_filtered_image: 
        check_equal('Checking pixels for horizontal filter @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY Riya Arora---")

#--------------------------------------------------------------------------------

# TESTING for vertical flip filter
# By: Riya Arora

def test_vertical_flip() -> None: 
    """
    
    Author: Riya Arora
    
    A test function for the flip_vertical filter
    
    >>> test_vertical_flip()
    
    """    

    #create original image and set test cases
    original = create_image(1, 6) 
    set_color(original, 0, 0,  create_color(127,55,231)) 
    set_color(original, 0, 1,  create_color(0,255,130)) 
    set_color(original, 0, 2,  create_color(55,128,2)) 
    set_color(original, 0, 3,  create_color(255,33,201)) 
    set_color(original, 0, 4,  create_color(55,0,152)) 
    set_color(original, 0, 5,  create_color(152,65,255))   
    
    # Create image with expected results
    expected = create_image(1, 6) 
    
    # Fill in the correct values in each location 
    set_color(expected, 0, 0,  create_color(152, 65, 255)) 
    set_color(expected, 0, 1,  create_color(55, 0, 152)) 
    set_color(expected, 0, 2,  create_color(255, 33, 201)) 
    set_color(expected, 0, 3,  create_color(55, 128, 2)) 
    set_color(expected, 0, 4,  create_color(0, 255, 130)) 
    set_color(expected, 0, 5,  create_color(127, 55, 231)) 
    
    #Use filter function on the original image
    actual_filtered_image = flip_vertical(original)
    
    # Comparing the transformed image returned by the filter with the expected image, one pixel at a time.
    for x, y, col in actual_filtered_image: 
        check_equal('Checking pixels for vertical test filter @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY Shebab Salama---")
#--------------------------------------------------------------------------------
# TESTING for curve drawing filter
# By: Riya Arora

def test_draw_curve() -> None:
    """
    Author: Riya Arora
    
    A test function for the draw curve filter
    
    >>> test_draw_curve()
    """
    
    # Create original image and test values covering all conditions.
    original = create_image(6, 6)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 0))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 1, 2, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(0, 0, 0))
    set_color(original, 2, 2, create_color(0, 0, 0))
    set_color(original, 0, 3, create_color(0, 0, 0))
    set_color(original, 3, 0, create_color(0, 0, 0))
    set_color(original, 3, 3, create_color(0, 0, 0))
    set_color(original, 3, 4, create_color(0, 0, 0))
    set_color(original, 0, 4, create_color(0, 0, 0))
    set_color(original, 4, 0, create_color(0, 0, 0))
    set_color(original, 4, 4, create_color(0, 0, 0))
    set_color(original, 4, 5, create_color(0, 0, 0))
    set_color(original, 0, 5, create_color(0, 0, 0))
    set_color(original, 5, 0, create_color(0, 0, 0))
    set_color(original, 5, 5, create_color(0, 0, 0))

    
    expected = create_image(6, 6)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 1, 2, create_color(255, 255, 255))
    set_color(expected, 2, 1, create_color(255, 255, 255))
    set_color(expected, 2, 2,create_color(255, 255, 255))
    set_color(expected, 0, 3, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 3, 3, create_color(255, 255, 255))
    set_color(expected, 3, 4, create_color(255, 255, 255))
    set_color(expected, 0, 4, create_color(0, 0, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 4, 4,create_color(255, 255, 255))
    set_color(expected, 4, 5, create_color(255, 255, 255))
    set_color(expected, 0, 5, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(255, 255, 255))
    set_color(expected, 5, 5, create_color(0, 0, 0))
   
    
    #Use filter function on the original image

    actual_filtered_image,border = draw_curve(original,create_color(255,255,255), [(1,0),(3,4),(5,0)])

    # Comparing the transformed image returned by the filter with the expected image, one pixel at a time.
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixels for draw curve filter @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        
    print("---TEST COMPLETED BY Ibramhim Ayman Al-Buhaisi---")

#--------------------------------------------------------------------------------

# Main Script for three tone testing
three_tone_test()

# Main Script for extreme contrast testing
test_extreme_contrast()

# Main Script for posterize testing
test_posterize() 

# Main Script for sepia tinting testing
test_sepia()    

# Main Script for edge detection testing
test_edge()

# Main Script for horizontal flip testing
test_horizontal_flip()    

# Main Script for vertical flip testing
test_vertical_flip()

# Main Script for curve drawing
test_draw_curve()