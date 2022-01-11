#Author: Stephen Okwudihshu - T012 - 101180912

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color, create_color, create_image, get_color, set_color,\
                  Image 


from unit_testing import check_equal
 
from T012_P3_filter_sepia import sepia
 

def test_sepia() -> None:
    
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
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


test_sepia()    