from Cimpl import *
from point_manipulation import*
import numpy as np
from simple_Cimpl_filters import grayscale



def choose_col(a:str):
    '''return color(r,g,b)
    '''

    if a == "black":
        ch_col = Color(0, 0, 0)
    elif a == "gray":
        ch_col = create_color(128, 128, 128)
    elif a == "white":
        ch_col = create_color(255, 255, 255) 
    elif a == "blood":
        ch_col = create_color(255, 0, 0)
    elif a == "green":
        ch_col = create_color(0, 255, 0)
    elif a == "blue":
        ch_col = create_color(0, 0, 255)
    elif a == "lemon":
        ch_col = create_color(255, 255, 0)
    elif a == "cyan":
        ch_col = create_color(0, 255, 255)
    elif a == "magenta":
        magenta = create_color(255, 0, 255)            
    return ch_col

def three_tone(image, color1:str, color2:str, color3:str)->Image:
    '''(image, str, str, str) -> image
    Return a copy of an image with only three colors
    >>> image = load_image(file)
    >>> three_tone(image, black, gray, white)
    '''
    new_image = copy(image)
      
    for pixel in image:
        x,y, (r,g,b) = pixel    
        Luminance = (r + g + b)/3
        if Luminance < 85:
            new_color = choose_col(color1)
            set_color(new_image, x, y, new_color)
        elif Luminance <170:
            new_color = choose_col(color2)
            set_color(new_image, x, y, new_color)
        elif Luminance <= 255:
            new_color = choose_col(color3)
            set_color(new_image, x, y, new_color)    
            
    return new_image


def extreme_contrast(image) -> Image:
    """Returns a copy of the image with maximized contrast.
    >>> image = load_image(choose_file())
    >>> extreme = extreme_contrast(image)
    >>> show(extreme)

    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if r <= 127:
            r = 0
        else:
            r = 255
        if g <= 127:
            g = 0
        else:
            g = 255
        if b <= 127:
            b = 0
        else:
            b = 255
        e = create_color(r, g, b)
        set_color(new_image, x, y, e)

    return new_image


def sepia(image: Image) -> Image:
    """
   Returns a copy of the input image in which all the pixels have been
   sepia-tinted.
    >>> sepia(original_image)
    """
    copy_sepia = copy(image)
    gray_tint = grayscale(copy_sepia)
    
    for pixel in gray_tint:
        x, y, (r, g, b) = pixel
        if r<63:
            pixel_tinting = create_color (r * 1.1, g, b*0.9)
            set_color (gray_tint, x, y, pixel_tinting)
        elif r>=63 or r<=191:
            pixel_tinting_1 = create_color (r * 1.15, g, b*0.85)
            set_color (gray_tint, x, y, pixel_tinting_1)
        elif r>191:
            pixel_tinting_ = create_color (r * 1.08, g, b*0.93)
            set_color (gray_tint, x, y, pixel_tinting_2)        
            
    return gray_tint

def _adjust_component (r: int, g: int, b: int)->int:
    """
    This helper function decreases the colour in a picture to four quadrants and 
    returns the midpoint of whichever quadrant the colour falls in.
    """    
    # Setting intial value of R, G, and B to ZERO
    R = 0 
    G = 0
    B = 0
    
    # Range checking
    if 0 <= r <= 63:
        R = 31
    if 64 <= r <= 127:
        R = 95
    if 128 <= r <= 191:
        R = 159
    if 192 <= r <= 255:
        R = 223
        
    if 0 <= g <= 63:
        G = 31
    if 64 <= g <= 127:
        G = 95
    if 128 <= g <= 191:
        G = 159
    if 192 <= g <= 255:
        G = 223
        
    if 0 <= b <= 63:
        B = 31
    if 64 <= b <= 127:
        B = 95
    if 128 <= b <= 191:
        B = 159
    if 192 <= b <= 255:
        B = 223    
    
    return (R, G, B)

def posterize(image):
    """
    Returns a posterized filter of the original image. The filter takes the values 
    from the midpoints of the four quadrants and applies them to the image.
    """
    
    new_image = copy(image)
    for x,y, (r,g,b) in new_image:
        colors = get_color (new_image, x, y)
        
        red = colors[0]
        green = colors [1]
        blue = colors [2]
        
        A = _adjust_component (red, green, blue)
        
        RED = A[0]
        GREEN = A[1]
        BLUE = A[2]
        
        P = create_color (RED, GREEN, BLUE)
        set_color (new_image, x, y, P)

    return new_image

def detect_edges(image, threshold:float):
    '''(image, float) -> image
    Return a copy of an image with edge detection
    >>> image = load_image(file)
    >>> detect_edges(image, 6)
    '''
    
    new_image = copy(image)
    height = get_height(new_image)-1
    for pixel in image:      
        x,y, ( r1, g1, b1 ) = pixel
        if y<height:
            y=y+1
            color2 = get_color(new_image, x, y)
            (r,g,b)=color2
            brightness1 = (r1 + g1 + b1)/3
            brightness2 = (r + g + b)/3
            if brightness1 -brightness2 > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            if brightness1 -brightness2 <= threshold:
                set_color(new_image, x, y, create_color(255, 255, 255))
        elif y==height:
            
            new_color = create_color(255,255,255)
            set_color(new_image, x, y, new_color)                    
    return new_image

def daw_curve(image,points_ls:list,color1:str):
    """
    Return a new image with curve line through specific points
    >>> image = load_image(file)
    >>>daw_curve(image,[(20,50), (200,250), (170,300)],"lemon")
    """

    xy_list=get_x_y_lists(points_ls)
    #s_xy_list=sort_points(xy_list)
    x=xy_list[0]
    y=xy_list[1]
    
    curve=np.polyfit(x,y,3)
    poly=np.poly1d(curve)
    print(poly)
       
    new_image = copy(image)
    for pixel in image:
        x,y, (r,g,b) = pixel
        y=poly(x)
        y=round(y)
        if y>=2 and y<get_height(new_image)-2:
            new_color = choose_col(color1)
            set_color(new_image, x, y, new_color)
            set_color(new_image, x, y-2, new_color)
            set_color(new_image, x, y-1, new_color)
            set_color(new_image, x, y+1, new_color)            
            set_color(new_image, x, y+2, new_color)        
        
    return new_image

def flip_vertical (image) -> Image: 
    """
    Returns a copy of an image filpped along the horizontal axis as if it were mirrored.

    >>>image = load_image(file)
    >>>horizontalFilter = flip_horizontal(image)
    >>>show(horizontalFilter)

    """    

    new_image = copy(image)
    imge_width = get_width(new_image)
    imge_height = get_height(new_image)
    imge_centre = imge_height // 2
    
    for y in range(imge_centre):
        for x in range(imge_width):
        
            r,g,b = get_color(new_image,x,y)
            new_r,new_g,new_b = get_color(new_image,x,imge_height-1-y)
            set_color(new_image,x,y,create_color(new_r,new_g,new_b))
            set_color(new_image,x,imge_height-1-y,create_color(r,g,b))

    return new_image



def flip_horizontal (image) -> Image: 
    """
    Returns a copy of an image filpped along the vertical axis as if it were mirrored.

    >>>image = load_image(file)
    >>>horizontalFilter = flip_horizontal(image)
    >>>show(horizontalFilter)

    """
    # Gets the dimesions of the copied image.
    new_image = copy(image)
    imge_width = get_width(new_image)
    imge_height = get_height(new_image)
    imge_centre = imge_width // 2

    for y in range(imge_height):
        for x in range(imge_centre):
            r,g,b = get_color(new_image,x,y)
            new_r,new_g,new_b = get_color(new_image,imge_width-1-x,y)
            set_color(new_image,x,y,create_color(new_r,new_g,new_b))
            set_color(new_image,imge_width-x-1,y,create_color(r,g,b))
    
    return new_image

def red_filter(image):
    """
    return new image only with red value
    >>>red_filter(image):->Image
    """

    new_image = copy(image)
    for pixel in image:
        x,y, (r,g,b) = pixel
        new_color = create_color(r,0,0)
        set_color(new_image, x, y, new_color)
    return new_image

def green_filter(image):
    """
    return new image only with green value
    >>>green_filter(image):->Image
    """    
    new_image = copy(image)
    for pixel in image:
        x,y, (r,g,b) = pixel
        new_color = create_color(0,g,0)
        set_color(new_image, x, y, new_color)
    return new_image

def blue_filter(image):
    """
    return new image only with blue value
    >>>blue_filter(image):->Image
    """    
    new_image = copy(image)
    for pixel in image:
        x,y, (r,g,b) = pixel
        new_color = create_color(0,0,b)
        set_color(new_image, x, y, new_color)
    return new_image

