# User Interface
#by Riya Arora

#imports 
from Cimpl import *
from T007_image_filters import *
import time 

#start with no image loaded
image = None

#definition for filter selection by user
def filter_selection(command):
    global image

    #must load an image first
    if command == "L":
        image = load_image(choose_file())
    
    #error will be displayed if no image is loaded
    elif type(image) != Image:
        print("No image loaded")
        time.sleep(1)
    
    #sepia
    elif command == "S" :
        save_as(image)
    
    #3tone
    elif command == "3" :
        image = three_tone(image,'blood','lemon','gray')
    
    #extreme
    elif command == "X" :
        image = extreme_contrast(image)
    
    #sepia tint
    elif command == "T" :
        image = sepia(image)
    
    #posterize
    elif command == "P" :
        image = posterize(image)
    
    #edge detect
    elif command == "E" :
        threshold = int(input("Enter a contrast threshold: "))
        image = detect_edges(image,threshold)
    
    #draw curve
    elif command == "D" :
        mod_image = draw_curve(image,'cyan')
        image = mod_image[0]
    
    #vertical flop
    elif command == "V" :
        image = flip_vertical(image)
    
    #horizontal flip
    elif command == "H" :
        image = flip_horizontal(image)
    
    #when the user wants to quit the program 
    elif command == "Q":
        print("Program finished")       
        
    else:
        print("No such command")
        
        #time used to slow down program 
        time.sleep(1)
    
    if image != None:
        show(image)    
        
        


