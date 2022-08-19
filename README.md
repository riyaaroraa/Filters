Filters README for Filter Project - Version 1.0 - 18/08/2022

Contact Information: 
Author: Riya Arora
E-mail: riya.arora@carleton.ca

Description: 
-------------
This project contains multiple programs that allows the user to input an image and apply a desired filter(s) to the image.
The filters include: Red, Blue, Green, Three Tone, Extreme Contrast, Sepia Tinting, Posterize, Edge Detection, Curve Drawing, 
Vertical Flip, and Horizontal Flip. 
Upon selecting the desired filter(s) to the image, the program creates a new image with the filters applied and displays it. 

Installation:
-------------
This program will work on Python version 3 or newer. 
In order to use this program, you will need to have pillow installed. 
Open the command prompt and type one of the following commands: 

> pip install --upgrade Pillow
Or
> python –m pip install --upgrade pillow
Or
> py –m pip install --upgrade pillow

After installing pillow, you will need the Cimpl library (Cimpl.py) to be downloaded onto the same directory as the program.

Usage:
-------------
> python interactive_ui.py

When prompted, enter L to load your chosen image and the program will display it.
To add a filter you can enter one of the following commands (3) for 3-tone, (X) for xtreme contrast, 
(T) for sepia tint, (E) for edge detection, (D) for curve drawing, and (V) or (H) for vertical or horizontal flip and your new image will be displayed with the chosen filter.
To save your image with the filters applied you enter (S) when prompted the program will open your files for you to save it where you please. 
To quit the program you can simply enter the command (Q) and it will show your finished product. 
There is error control if you enter a command that is not listed the program will state "No such command" and display your current image.

> python batch_ui.py

When prompted, enter the file name of the text file containing all the images you want to change, 
the file name for the changed image to be saved to, and the list of the filter commands you want to be applied. 
The program will read the file and take your chosen image, apply the stated filters and save it as the file name given. 
An image will not be shown you must go to your files to see the finished product. 
There is no error control if your file contains an incorrect file type or a command that is not listed the program will stop running.

Credits: 
-------------
Green Filter = Riya Arora
Blue Filter = Riya Arora
Red Filter = Riya Arora
Combined Filter = Riya Arora
Green Test Function = Riya Arora
Blue Test Function = Riya Arora
Red Test Function = Riya Arora
Combined  Test Function = Riya Arora
Three tone filter = Riya Arora
Extreme contrast filter = Riya Arora
Sepia tinting filter = Riya Arora
Posterizing filter = Riya Arora
Three tone Test Function = Riya Arora
Extreme contrast Test Function = Riya Arora
Sepia tinting Test Function = Riya Arora
Posterizing Test Function = Riya Arora
Edge Detection Filter = Riya Arora
Curve Drawing Filter = Riya Arora
Vertical Flip Filter = Riya Arora
Horizontal Flip Filter = Riya Arora
Edge Detection Test Function = Riya Arora
Curve Drawing Test Function = Riya Arora
Vertical Flip Test Function = Riya Arora
Horizontal Flip Test Function = Riya Arora

License:
-------------
MIT License

Copyright (c) 2021 Riya Arora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



