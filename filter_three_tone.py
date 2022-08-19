# Riya Arora

from Cimpl import *
def three_tone(image: Image) -> Image:
    """ Return an with certain colors to 3 shades or colors(black,gray,white)
    based on original brightness.
    
    >>>image = load_image(choose_file())
    >>>new_image = blue_filter(image)
    >>>show(new_image)
    """
    new_image = copy(image)
    
    for x, y, (r,g,b) in image:
        black_color = create_color(0,0,0)
        gray_color = create_color(128,128,128)
        white_color = create_color(255,255,255)
        brightness = (r + g + b) // 3
        if 0 < brightness < 84 :
            set_color(new_image, x, y, black_color)
        elif 85 < brightness < 170 :
            set_color(new_image, x, y, gray_color)
        elif 171 < brightness < 255 :
            set_color(new_image, x, y, white_color)
        
    return new_image
    
    
    
def three_tone_test() -> str: 
    """ 
    """ 
    original = create_image(6, 1) 
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(255, 0, 0))
    set_color(expected, 1, 0,  create_color(255, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(0, 255, 0))
    actual_filtered_image = three_tone (original, "blood", "lime", "blue")





    
    
