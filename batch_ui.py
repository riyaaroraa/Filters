#by Riya Arora
#Batch file interface

#import 
from T007_image_filters import *
from Cimpl import*

#Prompts user to enter the name of the text file "(batch_sample.txt)"
filename = input("Input the name of the desired image file:") 

batch_file1 = open(filename) 

#Applies the selected filters by the user to a copy of the original image 
for line in batch_file1:
    #split line command
    commands = line.split(" ") 
   
    original = load_image(commands[0])
    #the copied image where the filters will be applied
    filtered_image = copy(original)
    
    for i in range(2, len(commands)): 
        #convert to string
        command = str(commands[i]) 
        
        #posterize filter
        if command == "P":
            filtered_image = posterize(filtered_image)
           
        #3 tone filter                 
        elif command == "3":
            #hard coded values
            filtered_image = three_tone(filtered_image, 'blood', 'lemon', 'gray')
            
        #extreme contrast filter
        elif command == "X":
            filtered_image = extreme_contrast(filtered_image)
            
        #sepia tinting filter
        elif command == "T":
            filtered_image = sepia(filtered_image)
          
        #edge detection filter        
        elif command == "E":
            filtered_image = detect_edges(filtered_image, 15)       
    
        #vertical flip filter        
        elif command == "V":
            filtered_image = flip_vertical(filtered_image)
            
        #horizontal flip        
        elif command == "H":
            filtered_image = flip_horizontal(filtered_image)
            
    #saves the copied image where the filters were applied
    save_as(filtered_image, commands[1]) 

#Closes the batch file
batch_file1.close() 
