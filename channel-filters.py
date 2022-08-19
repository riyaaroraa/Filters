Riya Arora

#Import functions from Cimpl module and import unit testing for all definitions
from Cimpl import *
from unit_testing import check_equal

#------------------------------------------------------------------------------
# DEFINITION for combined filter
# By: Riya Arora - T007

def combine_all(first_pic:Image, second_pic: Image, third_pic: Image) -> Image:
    """
    Returns an image that is an combination of different RGB images, any order
    
    >>>image_one = load_image(choose_file())
    >>>image_two = load_image(choose_file())
    >>>image_three = load_image(choose_file())
    >>>combined_image = combine_all(image_one,image_two,image_three)
    >>>show(combined_image)
    
    """
    final_image = copy(first_pic) 
    
    for x,y,(r,g,b) in final_image:
    #First get RGB Values and Pixels that will be combined
        
        color_one = get_color(first_pic,x,y)
        color_two = get_color(second_pic,x,y)
        color_three = get_color(third_pic,x,y)
        
        #Now add the RGB values for red, blue and green
        
        red = color_one[0]+color_two[0]+color_three[0]
        
        green = color_one[1]+color_two[1]+color_three[1]
        
        blue = color_one[2]+color_two[2]+color_three[2]
        
        #Combine RGB values
        combined_color = create_color(red,green,blue)
        set_color(final_image,x,y,combined_color)
        
    return final_image 
    #Returning the final combined image!

#-------------------------------------------------------------------------------

# DEFINITION for green filter
# By: Riya Arora

def green_channel (image) -> Image: 
    """
    Returns a copy of the orignial image with only the green component of each 
    pixel and the red and blue values being zero
    
     >>> original_image = load_image(choose_file())
     >>> greenFilter = green_channel(original_image)
     >>> show(greenFilter)
    """
    image_copy = copy(image)
    
    for pixel in image_copy:
        x, y, (r,g,b) = pixel
        set_color (image_copy, x, y, create_color(0,r,0))
    return image_copy

# DEFINITION for blue filter
#By:  Riya Arora

#function definition for blue channel
def blue_channel (image) -> Image: 
    """
    Returns a copy of the orignial image with only the blue component of each 
    pixel and the red and green values being zero
    
     >>> original_image = load_image(choose_file())
     >>> blueFilter = blue_channel(original_image)
     >>> show(blueFilter)
    """
    
    image_copy = copy(image)
  
    for pixel in image_copy:
        x, y, (r,g,b) = pixel
        new_colour = create_color(0,0,b)        
        set_color (image_copy, x, y, new_colour)
    return image_copy

# DEFINITION for red filter
# By: Riya Arora

#function definition for red channel
def red_channel (image) -> Image: 
    
    """
    Returns a copy of the orignial image with only the red component of each 
    pixel and the blue and green values being zero
    
     >>> original_image = load_image(choose_file())
     >>> blueFilter = blue_channel(original_image)
     >>> show(blueFilter)
    """    

    image_copy = copy(image)

    for pixel in image_copy:
        x, y, (r,g,b) = pixel
        set_color (image_copy, x, y, create_color(r,0,0))
    return image_copy
    
#------------------------------------------------------------------------------
# TESTING function for green filter 
# By: Riya Arora

def test_green() -> None:
    """
    A test function for green_channel
    
    >>> test_green()
    
    """
    #create original image and set test cases
    original = create_image(3, 1) 
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 100, 100))
    set_color(original, 2, 0, create_color(300, 0, 100))
    
    # Create image with expected results
    expected = create_image(3, 1) 
    
    # Fill in the correct pixel values in each location    
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 100, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    

    #Use filter function on original image
    actual_filtered_image = green_channel (original)
    
    #Compare the new image returned by the filter with expected image by comparing one pixel at a time (checks 3 pixels)  
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixels applying the green filter (' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))

#------------------------------------------------------------------------------

# TESTING function for blue filter 
#By:  by Riya Arora

def test_blue() -> None:
    """
    A test function for blue_channel
    
    >>> test_blue()
    
    """
    
    #create original image and set test cases
    original = create_image(3, 1) 
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 100, 100))
    set_color(original, 2, 0, create_color(300, 0, 100))
    
    # Create image with expected results
    expected = create_image(3, 1)
    
    # Fill in the correct pixel values in each location
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 100))
    set_color(expected, 2, 0, create_color(0, 0, 100))
    
    #Use filter function on original image
    actual_filtered_image = blue_channel (original)
    
    #Compare the new image returned by the filter with expected image by comparing one pixel at a time (checks 3 pixels) 
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixels applying the blue filter (' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        
#------------------------------------------------------------------------------

# TESTING for red filter
# By: Riya Arora

def test_red() -> None: # Test function
    
    """
    A test function for red_channel
    
    >>> test_red()
    
    """    

    #create original image and set test cases
    original = create_image(3, 1) 
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(100, 100, 100))
    set_color(original, 2, 0, create_color(300, 0, 100))
    
    # Create image with expected results
    expected = create_image(3, 1)
    
    # Fill in the correct pixel values in each location
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(100, 0, 0))
    set_color(expected, 2, 0, create_color(255,0, 0))
    
    #Use filter function on original image
    actual_filtered_image = red_channel (original)
    
    #Compare the new image returned by the filter with expected image by comparing one pixel at a time (checks 3 pixels) 
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixels applying the red filter (' + str(x) + ', ' + str(y) + ')', col, get_color(expected, x, y))
        
#------------------------------------------------------------------------------

# TESTING for combined filter
# By: Riya Arora

def combine_test() -> None: 
    """
    Testing for the combine function definition
    
    >>> test_combine()
    
    """
    
    # Create first image with six pixels.
    red_image = create_image(3,2)
    
    set_color(red_image,0,0, create_color(0,0,0))
    set_color(red_image,1,0, create_color(50,0,0))
    set_color(red_image,2,0, create_color(125,0,0))
    set_color(red_image,0,1, create_color(170,0,0))
    set_color(red_image,1,1, create_color(220,0,0))
    set_color(red_image,2,1, create_color(255,0,0))
    
    # Create second image with six pixels.
    green_image = create_image(3,2)
    
    set_color(green_image,0,0, create_color(0,0,0))
    set_color(green_image,1,0, create_color(0,50,0))
    set_color(green_image,2,0, create_color(0,125,0))
    set_color(green_image,0,1, create_color(0,170,0))
    set_color(green_image,1,1, create_color(0,220,0))
    set_color(green_image,2,1, create_color(0,255,0))
    
    # Create third image with six pixels.
    blue_image = create_image(3,2)
    
    set_color(blue_image,0,0, create_color(0,0,0))
    set_color(blue_image,1,0, create_color(0,0,50))
    set_color(blue_image,2,0, create_color(0,0,125))
    set_color(blue_image,0,1, create_color(0,0,170))
    set_color(blue_image,1,1, create_color(0,0,220))
    set_color(blue_image,2,1, create_color(0,0,255))
    
    # Create the expected / orginal image that will be used to compare with
    expected = create_image(3,2)
    
    set_color(expected,0,0, create_color(0,0,0))
    set_color(expected,1,0, create_color(50,50,50))
    set_color(expected,2,0, create_color(125,125,125))
    set_color(expected,0,1, create_color(170,170,170))
    set_color(expected,1,1, create_color(220,220,220))
    set_color(expected,2,1, create_color(255,255,255))
    
    #Compare the new image with the created image
    
    combine_image = combine_all(red_image,green_image,blue_image)
    for x,y,color in combine_image:  
        
        check_equal("Checking pixels applying the combined filter (" + str(x) + "," + str(y) + ")" , color, get_color(expected,x,y))


#------------------------------------------------------------------------------
# Main Script for green
original_image = load_image(choose_file()) # Call functions
greenFilter = green_channel(original_image)
show(greenFilter)

# Main Script for blue
original_image = load_image(choose_file()) # Call functions
blueFilter = blue_channel(original_image)
show(blueFilter)

# Main Script for red
original_image = load_image(choose_file()) # Call functions
redFilter = red_channel(original_image)
show(redFilter)

# Main Script for combined filter
image_one = load_image(choose_file()) # Call functions
image_two = load_image(choose_file()) # Call functions
image_three = load_image(choose_file()) # Call functions

#------------------------------------------------------------------------------

#test calls for 3 filters
test_green()
test_blue()
test_red()

#testing for combined filter
combined_image = combine_all(image_one,image_two,image_three) 
show(combined_image)
combine_test()