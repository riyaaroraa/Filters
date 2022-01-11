
from Cimpl import *

# Main script

# Extreme contrast function
def extreme_contrast (image) -> Image: 
    """Returns an copy of an image where the contrast between the pixles has been maximized
    >>> extreme_contrast()
    """
    
    filter_image = image
    
    # Changes the (r,g,b) values accoriding the the conditions
    for x,y, (r,g,b) in filter_image:
        if red1 <= 127:
            r2 = 0
        else:
            red1 = 255
        if green1 <= 127:
            green1= 0
        else:
            green1 = 255
        if blue1 <= 127:
            blue2 = 0
        else:
            blue2 = 255
        
        # New colour created and set to image with the new (r,g,b) values
        new_colour = create_color(,g,b)
        set_color (filter_image, x, y, new_colour)
    return  filter_image

# Shows extreme contrast of chosen image   
original_image = load_image(choose_file())
ExtremeFilter = extreme_contrast(original_image)
show(ExtremeFilter) 

