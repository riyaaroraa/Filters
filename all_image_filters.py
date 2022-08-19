#Riya Arora


#Import functions from Cimpl module and import unit testing for all definitions
from Cimpl import *
from Cimpl import get_height, get_width, choose_file, load_image, copy, \
    set_color, create_color, \
    get_color, Image, show
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale
import numpy as np
from point_manipulation import*

#------------------------------------------------------------------------------
# DEFINITION for green filter
# By: Riya Arora

def green_channel (image) -> Image: 
    """
    Author: Riya Arora
    
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

#--------------------------------------------------------------------------------
# DEFINITION for blue filter
# By: Riya Arora

#function definition for blue channel
def blue_channel (image) -> Image: 
    """
    
    Author: Riya Arora
    
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

#--------------------------------------------------------------------------------
# DEFINITION for red filter
# By: Riya Arora

#function definition for red channel
def red_channel (image) -> Image: 
    
    """
    
    Author:Riya Arora
    
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

#--------------------------------------------------------------------------------
# DEFINITION for combined filter
#By: Riya Arora

def combine_all(first_pic:Image, second_pic: Image, third_pic: Image) -> Image:
    """
    Author: Riya Arora
    
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

#--------------------------------------------------------------------------------
# DEFINITION for three tone filter
# By: Riya Arora

def three_tone(image: Image, colour_1: str, colour_2: str, colour_3: str) -> Image:
    """
    Author : Riya Arora
    
    This three tone function will take any image and any of the colours from the following list of strings
    - black, white, blood, lime, blue, yellow, cyan, magenta, gray.
    
    Pixel's brightness between 0-84, corresponding pixel is set to colour_1.
    Pixel's brightness between 85-170, corresponding pixel is set to colour_2.
    Pixel's brightness between 171-8255, corresponding pixel is set to colour_3.
                
    >>>original_image = load_image(choose_file())
    >>>three_tone_filter = three_tone(original_image, "blood", "lime", "blue")
    >>>show(three_tone_filter)
    
    """
    #set all colours to their given values based on the table provided
    #this program will only accept these colours 
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    blood = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    
    #set each colour to the correspoding string that can be inputted by the user
    
    colours = [("black", black), ("white", white), ("blood", blood),
               ("lime", lime), ("blue", blue), ("yellow", yellow),
               ("cyan", cyan), ("magenta", magenta), ("gray", gray)]
    
    #create copy of the image and convert each pixel based on brightness
    filtered_image = copy(image)
    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        average = (r + g + b) / 3
        if (average >= 0) and (average < 85):
            for i in range(len(colours)):
                if colour_1 == colours[i][0]:
                    set_color(filtered_image, x, y, colours[i][1])
        elif (average > 84) and (average < 171):
            for i in range(len(colours)):
                if colour_2 == colours[i][0]:
                    set_color(filtered_image, x, y, colours[i][1])
        elif (average > 170) and (average < 256):
            for i in range(len(colours)):
                if colour_3 == colours[i][0]:
                    set_color(filtered_image, x, y, colours[i][1])

    #return new image
    return filtered_image
#--------------------------------------------------------------------------------

# DEFINITION for extreme contrast filter
# By: Riya Arora

def extreme_contrast (image) -> Image: 
    """ 
    Author : Riya Arora
    
    Returns an copy of an image where the contrast between the pixles has been maximized
                
    >>>original_image = load_image(choose_file())
    >>>ExtremeFilter = extreme_contrast(original_image)
    >>>show(ExtremeFilter) 
    """
    
    image_copy = copy(image)
    
    # Changes the (r,g,b) values accoriding the the conditions
    for x,y, (r,g,b) in image:
        if r <= 127:
            r = 0
        else:
            r = 255
        if g <= 127:
            g= 0
        else:
            g = 255
        if b <= 127:
            b = 0
        else:
            b = 255
        
        # New colour created and set to image with the new (r,g,b) values
        new_colour = create_color(r,g,b)
        set_color (image_copy, x, y, new_colour)
        
    #return new image
    return  image_copy

#--------------------------------------------------------------------------------

# DEFINITION for posterize filter
# By: Riya Arora

def _adjust_component(comp: int) -> int:
    """
    Author : Riya Arora
    
    Helper function created for the posterize filter. 
    Determines the quadrant in which a component lies and returns the 
    midpoint value of that quadrant.
                
    """        
    
    #checking all quadrants and assigning points 
    if comp in range(0,64):
                        comp = 31                       
    elif comp in range(64,128):
                        comp = 95  
    elif comp in range(128,192):
                        comp = 159      
    elif comp in range(191,256):
                        comp = 223 
      
    #comp will later be used in the posterize filter function
    return comp


def posterize(image: Image):
    """
    Author :Riya Arora
    
    Adjusts image to have smaller number of colours than the original using the helper
    adjust component function.
                
    >>>file = choose_file()
    >>>image = load_image(file)
    >>>posterize_img = posterize(image)
    >>>show(posterize_img)
    """    
    
    #copy image
    new_image = copy(image)
    for x,y, (r,g,b) in image:
        
        #nusing the colours from the helper function
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        post = create_color(r, g, b)  
        
        #set new colours
        set_color(new_image, x, y, post)
        
    #return new image
    return new_image  

#--------------------------------------------------------------------------------

# DEFINITION for sepia tinting filter
# By: Riya Arora

def sepia(original_image: Image) -> Image:
    """
    Author : Riya Arora
    
    Returns a copy of the original image in where all pixels have been 
    sepia tinted according to their range.
    
    >>> original_image = load_image(choose_file())
    >>> sepiaimage = sepia(original_image)
    >>> show(sepiaimage)
    """
    
    #create copy image
    new_image = copy(original_image)
    sepia_filter = grayscale(new_image)
    
    #using ranges multiply into the correct rgb value
    for pixel in sepia_filter:
        x, y, (r, g, b) = pixel
        if r < 63:
            r *= 1.1
            b *= 0.9

        if 63 <= r <= 191:
            r*= 1.15
            b *= 0.85

        if r > 191:
            r *= 1.08
            b *= 0.93
        
        #output new colour
        new_color = create_color(r, g, b)
        
        #set new colours
        set_color(sepia_filter, x, y, new_color)

    #return new image
    return sepia_filter

#--------------------------------------------------------------------------------
# DEFINITION for edge detection filter
# By: Riya Arora

def detect_edges(image: Image, threshold: float) -> Image:
    
    """
    Author: Riya Arora
    
    This filter takes any image (makes a copy) and changes the pixel's colour to black
    or white nased on their contrast, that looks like a pencil sketch 
    
    >>> original_image = load_image(choose_file())
    >>> show(detect_edges(original_image, 8))
    
    >>> original_image = load_image(choose_file())
    >>> show(detect_edges(original_image, 21))
    #example of using the same filter with another threshold
    
    The threshold controls how light or dark the sketch created will be.
    
    Returns image with detect_edges filter applied with a given threshold of 8
    without modifying original.
    
    """
    #create copy of an image
    image_copy = copy(image)

    #set colours to black and white
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    #get width of the image
    y_coor=get_height(image_copy)
    x_coor=get_width(image_copy)
    for x in range(x_coor):

        #get height of the image
        for y in range(y_coor - 1):

            #check pixel colour
            r, g, b = get_color(image_copy, x, y)
            r1, g1, b1 = get_color(image_copy, x, (y + 1))

            #change each pixel to black or white based on brightness
            brightness = (r + g + b) // 3
            brightness1 = (r1 + g1 + b1) // 3

            #set new colour
            if abs(brightness - brightness1) > threshold:
                set_color(image_copy, x, y, black)
            else:
                set_color(image_copy, x, y, white)
    
    for x in range(x_coor):       
        set_color(image_copy,x,y_coor-1,white)
       
     #return new image     
    return image_copy

#--------------------------------------------------------------------------------
# DEFINITION for horizontal flip filter
# By: Riya Arora

# Horizontal flip function
def flip_horizontal (image) -> Image: 
    """
    Author: Riya Arora
    
    Returns a copy of an image filpped along the vertical axis  
    
    >>>original_image = load_image(choose_file())
    >>>horizontalFilter = flip_horizontal(original_image)
    >>>show(horizontalFilter)
    
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
    
    #return new image 
    return image_copy

#--------------------------------------------------------------------------------
# DEFINITION for vertical flip filter
# By: Riya Arora

def flip_vertical(image): 
    """
    Author : Riya Arora
    
    Returns a copy of an image filpped along the horizontal axis  
    
    >>>original_image = load_image(choose_file()) 
    >>>Vertical = flip_vertical(original_image)
    >>>show(Vertical)
    
    """    
    # Gets the dimesions of the copied image.
    new_image = copy(image)
    img_width = get_width(new_image)
    img_height = get_height(new_image)
    img_centre = img_height//2

    # Changes the (r,g,b) values to the new flipped values
    for x in range(img_width):
        for y in range(img_centre):
            r,g,b = get_color(new_image,x,y)
            r2,g2,b2 = get_color(new_image,x,img_height-y-1)
            set_color(new_image,x,y,create_color(r2,g2,b2))
            set_color(new_image,x,img_height-y-1,create_color(r,g,b))
            
    #return new image 
    return new_image

#--------------------------------------------------------------------------------
# DEFINITION for curve drawing filter
# By: Riya Arora

#color constant definitions
black = create_color(0,0,0)
white = create_color(255,255,255)
blood = create_color(255,0,0)
green = create_color(0,255,0)
blue = create_color(0,0,255)
lemon = create_color(255,255,0)
cyan = create_color(0,255,255)
magenta = create_color(255,0,255)
gray = create_color(128,128,128)

def _image_border_finding(dim_list, interpol):
    
    '''
    Author:  Riya Arora 
    
    Takes image size (dim_list) and polynomial coefficients (interpol) 
    then returns a list containing the intersection points of the curve on the border.
    
    >>> _image_border_finding([(pixel_x, pixel_y], [7,4,-5]):
    [(0,10),(50,pixel_y)]
      
    '''
    
    #set height and wdith for the line or curve to be made
    new_width = dim_list[0]-1 #639
    new_length = dim_list[1]-1 #479
    cross_list  = []

    cof_of_zero = round(np.polyval(interpol, 0)) #if the curve crosses the vertical border or not
    cof_of_max = round(np.polyval(interpol, new_width)) #if the curve crosses the vertical border or not


    #if the curve crosses the horizontal border or not
    guess_cross0 = _exhaustive_search(new_width,interpol,0) #what value of checkcross0 when inputted into the "cof" function will equal the value of 0 
    
    #if the curve crosses the horizontal border or not
    guess_crossmax = _exhaustive_search(new_width, interpol, new_length) #what value of checkcrossmax when inputted into the "cof" function will equal the value of 479

    #checking  new length
    if 0 <= cof_of_zero <= new_length:
        cross_list.append((0, cof_of_zero))

    if 0 <= cof_of_max <= new_length:
        cross_list.append((new_width,cof_of_max))

    #return non if function does not equal
    if not(guess_cross0 == None):
        x = cross_list.append((guess_cross0 ,0))
    if not(guess_crossmax == None):
        y = cross_list.append((guess_crossmax,new_length))
    cross_list = cross_list.sort()
    
    #return 
    return cross_list


def  _exhaustive_search(max_x,coefs,val,):
    """
    Author :  Riya Arora 
     
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.
   
    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    """

    #set given values to one and zero
    EPS = 1
    guess = 0

    #solves for x between 0 and max value given by input
    while max_x>= guess and abs(np.polyval(coefs, guess)- val) >= EPS:
        guess+= 1
    if guess > max_x:
        return None
    
    #return new
    return  guess



def _interpolation(alteration2:list): #always has at least 2 coordinates
    
    '''
    Author :  Riya Arora 
    
    Takes the coordinates as inputs in a list of tuples (alteration2), 
    sorts them and returns the interpolating polynomial coefficients as a list 
    as well as a quadratic regression polynomial in the event that more than 3 points 
    were entered by the user.
    
    >>> _interpolation([ (2,0), (40,10), (50,15))
    [7, 4, -5]
    
    '''
    
    #set variable
    nxy = get_x_y_lists(alteration2)
    
    #only used if more than 3 points are put 
    #this is because the points wil form a curve
    if len(alteration2) < 3:
        return np.polyfit(nxy[0], nxy[1], 1)

    else:
        return np.polyfit(nxy[0], nxy[1], 2)
              


def draw_curve(img: Image, Col: str, pointlist: list = None) -> tuple:
    
    '''
    Author : Riya Arora 
    
    Takes three parameters: an image (img), the color of the line (col) to be used to highlight a part 
    in the image and an optional list of tuples (pointlist) which permits for testing and does not 
    require a user's input. Returns a tuple with a new image that has a curve on it as well as a 
    list of points on the image's border.
    
    >>> draw_curve('riveter.jpg', black, None)
    (riveter.jpg, (0,10),(50,pixel_y)])
        
    '''

    #set values for the following
    wide = get_width(img)
    hight = get_height(img)
    dim_list = [wide,hight]
    Newtemplate = copy(img)
    
  
    print(dim_list)
    Colour = input("Please enter a colour from this list: black, white,  blood, green, blue, lemon, cyan, magenta, gray:")
    
    #use if and else statements to allow user to choose what colour they want the line or curve to be in
    if Colour == 'black':
        Col = create_color(0,0,0)
    elif Colour == 'white':
        Col = create_color(255,255,255)
    elif Colour == 'blood':
        Col = create_color(255,0,0)
    elif Colour == 'green':
        Col = create_color(0,255,0)
    elif Colour == 'blue':
        Col = create_color(0,0,255) 
    elif Colour == 'lemon':
        Col = create_color(255,255,0) 
    elif Colour == 'cyan':
        Col = create_color(0,255,255)
    elif Colour == 'magenta':
        Col = create_color(255,0,255)
    elif Colour == 'gray':
        Col = create_color(128,128,128)
    if pointlist == None:

        #allow user input to choose a colour
        op = int(input("Please enter number of points must be at least 2:"))
        targ = op
        pointlist = []

        for i in range(targ) :
            
            #ask user to input the x,y coordinates of the points they choose
            x = int(input("Enter x cord of point n:"))
            y = int(input("Enter y cord of point n:"))
            pointlist.append((x,y))
        
        #sort points
        list.sort(pointlist)
        
    interpol = _interpolation(pointlist)

    bord_list = _image_border_finding(dim_list,interpol)

    #check x 
    for x in range(wide):
        newy = int((np.polyval(interpol, x)))
        
        #check y
        for k in range(newy-2, newy+3):
                if (0 <= x <= wide-1) and (0 <= k <= hight-1):
                    set_color(Newtemplate, x, k, Col)     
                    
    #return and display new line or curve
    return (Newtemplate, bord_list)

#--------------------------------------------------------------------------------
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
# Main Script for three tone

#This filter allows for user input of any string colour given in the list above.
#A main script has been created with three random colours to show an example
#This main script can also be commented out and typed in the shell to try different colours
#One can also simply edit the three string colours below to any of the 9 colours supported
#A simple UI could be created (as shown below) but Professorstated not to. 
#three_tone_filter = three_tone(original_image, input('Filter colour 1:'), input('Filter colour 2:'), input('Filter colour 3:'))

#Main Script
if __name__ == "__main__":
    original_image = load_image(choose_file())
    three_tone_filter = three_tone(original_image, "blood", "lime", "blue")
    show(three_tone_filter)

# Main Script for extreme contrast
original_image = load_image(choose_file())
ExtremeFilter = extreme_contrast(original_image)
show(ExtremeFilter) 

# Main Script for posterize 
file = choose_file()
image = load_image(file)
posterize_img = posterize(image)
show(posterize_img)

# Main Script for sepia tinting 
original_image = load_image(choose_file())
sepiaimage = sepia(original_image)
show(sepiaimage)

# Main Script for edge detection
original_image = load_image(choose_file())
show(detect_edges(original_image, 8))

# Main Script for horizontal flip 
original_image = load_image(choose_file())
horizontalFilter = flip_horizontal(original_image)
show(horizontalFilter)

# Main Script for vertical flip
if __name__ == "__main__":
    original_image = load_image(choose_file()) 
    Vertical = flip_vertical(original_image)
    show(Vertical)
    
# Main Script for curve drawing
if __name__ == '__main__':
    file = choose_file()
    img = load_image(file)

    new_img = draw_curve(img,white)
    show(new_img[0])
    print(new_img[1])