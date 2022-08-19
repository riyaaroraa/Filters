# by Riya Arora
#Text-based Interactive User Interface

#imports
from Cimpl import *

#code commented out since we are using the user interface and image filters as an import
from T007_user_interface import *
from T007_image_filters import *

#to slow down
import time 

#display filters
command = "Start"
image = None

#display menu
while command != "Q":
    command = str.upper(input("\nPlease enter one of the following commands: \n L)oad  S)ave-as \n 3)-tone  X)treme  T)int sepia  P)osterize \n E)dge detect  D)raw  V)ertical  H)orizontal flip \n Q)uit \n\n: "))
    
    #allows user to seletec any filter (lower or upper case)
    filter_selection(command)
    
    
    #if command == "L":
        #image = load_image(choose_file())
    
    #elif type(image) != Image:
        #print("No image loaded")
        #time.sleep(1)
        
    #elif command == "S" :
        #save_as(image)
    
    #elif command == "3" :
        #image = three_tone(image,'blood','lemon','gray')
    
    #elif command == "X" :
        #image = extreme_contrast(image)
    
    #elif command == "T" :
        #image = sepia(image)
    
    #elif command == "P" :
        #image = posterize(image)
    
    #elif command == "E" :
        #threshold = int(input("Enter a contrast threshold: "))
        #image = detect_edges(image,threshold)
    
    #elif command == "D" :
        #mod_image = draw_curve(image,'cyan')
        #image = mod_image[0]
    
    #elif command == "V" :
        #image = flip_vertical(image)
    
    #elif command == "H" :
        #image = flip_horizontal(image)
    
    #elif command == "Q":
        #print("Program finished")       
        
    #else:
        #print("No such command")
        #time.sleep(1)
        
        #if image != None:
            #show(image)          
