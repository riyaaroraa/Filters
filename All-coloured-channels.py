""" ECOR 1042 - individual filters """

from Cimpl import *

# red filter

def bright_red_channel(image):
   """ (Cimpl.Image) -> None
   
   Maximize the red component of every pixel in image,
   leaving the green and blue components unchanged.
   
   >>> image = load_image(choose_file()) 
   >>> red_channel(image)
   >>> show(image)   
   """   
   # The for loop "visits" each pixel in image, row-by-row, starting with the
   # pixel in the upper-left corner and finishing with the pixel in the 
   # lower-right corner. For each pixel, we unpack its x and y coordinates
   # and its red, green and blue components, binding them to variables
   # x, y, r, g, and b, respectively. 
   
   # After a pixel's components are unpacked, the body of the for 
   # loop is executed. A new Color object is created, using the original
   # green and blue components, but with with the red component set to its
   # maximum value (255). The pixel's colour is changed to this new colour.
   # The for loop then visits the next pixel in the sequence, and the unpacking 
   # and modify-colour steps are repeated for that pixel.

   for x, y, (r, g, b) in image:
      new_color = create_color(255, g, b)
      set_color(image, x, y, new_color)
       
# light blue filter

def light_blue_channel(image):
   """  (Cimpl.Image) -> None
   
   Reduce the red component of every pixel in image to 50%
   of its current value to create a light blue filter.
   
   >>> image = load_image(choose_file()) 
   >>> light_blue_channel(image)
   >>> show(image)
   """
   for x, y, (r, g, b) in image:
      # decrease red component by 50%
      new_color = create_color(r * 0.5, g, b)
      set_color(image, x, y, new_color)
      
# green filter
            
def green_channel(image):
   """  (Cimpl.Image) -> None
   
   Maximize the green component of every pixel in image,
   leaving the red and blue components unchanged.
   
   >>> image = load_image(choose_file()) 
   >>> green_channel(image)
   >>> show(image)
   """   
   for x,y, (r,g,b) in image:
      new_color = create_color(r, 255, b)
      set_color(image, x, y, new_color)
      
# blue filter
      
def blue_channel(image): 
   """  (Cimpl.Image) -> None
   
   Maximize the blue component of every pixel in image,
   leaving the red and green components unchanged.
   
   >>> image = load_image(choose_file()) 
   >>> blue_channel(image)
   >>> show(image)
   """   
   for x,y, (r,g,b) in image:
      new_color = create_color(r, g, 255)
      set_color(image, x, y, new_color)   
      
# purple filter
      
def purple_channel(image):
   """  (Cimpl.Image) -> None
   
   Reduce the green component of every pixel in image to 50%
   of its current value to create a purple filter.
   
   >>> image = load_image(choose_file()) 
   >>> purple_channel(image)
   >>> show(image)
   """
   for x, y, (r, g, b) in image:
      # decrease green component by 50%
      new_color = create_color(r, g*0.5, b)
      set_color(image, x, y, new_color)
      
# yellow filter
      
def yellow_channel(image):
   """  (Cimpl.Image) -> None
   
   Reduce the blue component of every pixel in image to 50%
   of its current value to create a yellow filter.
   
   >>> image = load_image(choose_file()) 
   >>> yellow_channel(image)
   >>> show(image)
   """
   for x, y, (r, g, b) in image:
      # decrease blue component by 50%
      new_color = create_color(r, g, b*0.5)
      set_color(image, x, y, new_color)      
      

# Test function for red filter

def test_red_channel () -> None:
   
   #create original image and set up 
   original = create_image(3,1)
   set_color(original, 0,0, create_color(0,0,0))
   set_color(original, 1,0, create_color(100,100,100))
   set_color(original, 2,0, create_color(300,0,100))
   
   #create image with expected results 
   expected = create_image(3,1)
   
   #fill in coorect values in each location
   set_color(expected, 0,0, create_color(0,0,0))
   set_color(expected, 1,0, create_color(100,0,0))
   set_color(expected, 2,0, create_color(300,0,0))
   
   #use the filter function on original image
   actual_filtered_image = red_channel (original)
   
   #compare the new image returned by the filter with the expected image one pixel at a time
   for x, y, col in actual_filtered_image:
      check_equal('Checking pixel @(' + str(x) + ',' + str(y) + ')', col, get_color(expected, x, y))


