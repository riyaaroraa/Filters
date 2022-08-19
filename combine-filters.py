Riya Arora

# This code prodcues a combined image filter

#Import functions from Cimpl module and import unit testing
from Cimpl import *
from unit_testing import check_equal

# DEFINITION for combined filter

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

# TESTING for combined filter

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


#-------------------------------------------------------------------------------

# Main Script for combined filter
image_one = load_image(choose_file()) # Call functions
image_two = load_image(choose_file()) # Call functions
image_three = load_image(choose_file()) # Call functions

#-------------------------------------------------------------------------------

#testing for combined filter
combined_image = combine_all(image_one,image_two,image_three) 
show(combined_image)
combine_test()