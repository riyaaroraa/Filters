
from Cimpl import*
import numpy as np
from point_manipulation import*

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
    Takes image size (dim_list) and polynomial coefficients (interpol) then returns a list containing the intersection points of the curve on the border.
    >>> _image_border_finding([(pixel_x, pixel_y], [7,4,-5]):
    [(0,10),(50,pixel_y)]
      
    '''
    new_width = dim_list[0]-1 #639
    new_length = dim_list[1]-1 #479
    cross_list  = []

    cof_of_zero = round(np.polyval(interpol, 0)) #if the curve crosses the vertical border or not
    
    cof_of_max = round(np.polyval(interpol, new_width)) #if the curve crosses the vertical border or not


    #if the curve crosses the horizontal border or not
    guess_cross0 = _exhaustive_search(new_width,interpol,0) #what value of checkcross0 when inputted into the "cof" function will equal the value of 0 
    
    #if the curve crosses the horizontal border or not
    guess_crossmax = _exhaustive_search(new_width, interpol, new_length) #what value of checkcrossmax when inputted into the "cof" function will equal the value of 479

    if 0 <= cof_of_zero <= new_length:
        cross_list.append((0, cof_of_zero))

    if 0 <= cof_of_max <= new_length:
        cross_list.append((new_width,cof_of_max))

    if not(guess_cross0 == None):
        x = cross_list.append((guess_cross0 ,0))
    if not(guess_crossmax == None):
        y = cross_list.append((guess_crossmax,new_length))
    cross_list = cross_list.sort()
    return cross_list


def  _exhaustive_search(max_x,coefs,val,):
    """
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

    EPS = 1

    guess = 0

    while max_x>= guess and abs(np.polyval(coefs, guess)- val) >= EPS:
        guess+= 1
    if guess > max_x:
        return None
    return  guess



def _interpolation(alteration2:list): #always has at least 2 coordinates
    
    '''
    Takes the coordinates as inputs in a list of tuples (alteration2), sorts them and returns the interpolating polynomial coefficients as a list as well as a quadratic regression polynomial in the event that more than 3 points were entered by the user.
    
    >>> _interpolation([ (2,0), (40,10), (50,15))
    [7, 4, -5]
    
    '''
        
    nxy = get_x_y_lists(alteration2)
    
    if len(alteration2) < 3:
        return np.polyfit(nxy[0], nxy[1], 1)

    else:
        return np.polyfit(nxy[0], nxy[1], 2)
              


def draw_curve(img: Image, Col: str, pointlist: list = None) -> tuple:
    
    '''
    Takes three parameters: an image (img), the color of the line (col) to be used to highlight a part in the image and an optional list of tuples (pointlist) which permits for testing and does not require a user's input. Returns a tuple with a new image that has a curve on it as well as a list of points on the image's border.
    
    >>> draw_curve('riveter.jpg', black, None)
    (riveter.jpg, (0,10),(50,pixel_y)])
        
    '''

    wide = get_width(img)
    hight = get_height(img)
    dim_list = [wide,hight]
    Newtemplate = copy(img)
    

    if pointlist == None:
        print(dim_list)
        op = int(input("Please enter number of points must be at least 2:"))
        targ = op
        pointlist = []

        for i in range(targ) :

            x = int(input("Enter x cord of point n:"))
            y = int(input("Enter y cord of point n:"))
            pointlist.append((x,y))
        
        list.sort(pointlist)
        
    interpol = _interpolation(pointlist)

    bord_list = _image_border_finding(dim_list,interpol)

    for x in range(wide):
        newy = int((np.polyval(interpol, x)))
        
        for k in range(newy-2, newy+3):
                if (0 <= x <= wide-1) and (0 <= k <= hight-1):
                    set_color(Newtemplate, x, k, Col)        
                    
    return (Newtemplate, bord_list)

# Main Script

if __name__ == '__main__':
    file = choose_file()
    img = load_image(file)

    new_img = draw_curve(img,white)
    show(new_img[0])
    print(new_img[1])

