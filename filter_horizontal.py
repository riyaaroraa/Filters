
from Cimpl import *

# Horizontal flip function
def flip_horizontal (image) -> Image: 
    """Returns a copy of an image filpped along the vertical axis  
    >>> flip_horizonatal()
    """
    # Gets the dimesions of the copied image.
    image_copy = copy(image)
    img_width = get_width(image_copy)
    img_height = get_height(image_copy)
    img_centre = img_width // 2    

    # Changes the (r,g,b) values to the new flipped values
    for y in range(img_height):
        for x in range(img_centre):
            r,g,b = get_color(image_copy,x,y)
            new_r,new_g,new_b = get_color(image_copy,img_width-1-x,y)
            set_color(image_copy,x,y,create_color(new_r,new_g,new_b))
            set_color(image_copy,img_width-x-1,y,create_color(r,g,b))
    return image_copy

# Main script
original_image = load_image(choose_file())
horizontalFilter = flip_horizontal(original_image)
show(horizontalFilter)
