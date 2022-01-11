


# Import functions: 

from Cimpl import *

# Vertical flip function:

def flip_vertical(image):
    new_image = copy(image)
    img_width = get_width(new_image)
    img_height = get_height(new_image)
    img_centre = img_height//2

    for x in range(img_width):
        for y in range(img_centre):
            r,g,b = get_color(new_image,x,y)
            r2,g2,b2 = get_color(new_image,x,img_height-y-1)
            set_color(new_image,x,y,create_color(r2,g2,b2))
            set_color(new_image,x,img_height-y-1,create_color(r,g,b))
    return new_image

# Main Script: 

if __name__ == "__main__":
    original_image = load_image(choose_file()) 
    Vertical = flip_vertical(original_image)
    show(Vertical)
