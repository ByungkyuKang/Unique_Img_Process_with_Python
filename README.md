📸 Helper to Organize Images

📌 Overview

This program is a Python-based application designed to simplify personal 
photo management. It groups similar/same images by inserting a 
series of numbers at the beginning of their names, so it helps me to 
manage duplicate images.


🎯 Motivation

Managing photos from different apps and sources often leads to scattered
duplicates, making backups inefficient and time-consuming. This project
 was created to streamline photo management by grouping image files.


⚙️ How It Works

Conduct the ORB Algorithm to find similar or the same images.
Organizes results:
    It will insert numbers at the beginning of image names. Similar or the same 
    images have the same number.


🔧 Current Status

Complete, but I'll update if I find some functions to add. 


🗂 Files

image_process_main.py: Main execution file.

img_processing.py: This method gathers image files and prepares them for the entire
                   processes, such as the dictionary to store image names and 
                   their group numbers. This method calls the comparing method 
                   in the img_comp module and the name change method in 
                   img_name_change module.

    - Method: 
        image_process: 
            1. Creates a dictionary. This dictionary has all image names as 
               key and 0 as value initially. Then, it calls the image_comparing
               method in the img_comp module, entering each image name as a 
               image_comparing's argument. After it receives a dictionary as
               a result, this method changes the values to increment numbers 
               in the dictionary if the keys of the dictionary are found in the 
               dictionary that is the result of image_comparing. (value 0 
               means "this image is not checked yet, or not a similar image of
               any image, so don't skip this image." and other numbers mean 
               "This image is either already checked or a similar image of 
               another image, so skip this one.")
            
            2. Insert numberings at the beginning of images. Similar images
               have the same number. 

img_comp.py
    - This file receives a file name and compares it to other images.
    - This returns a list that has image names. 
    - Method:
        image_comparing: Compare the input image to other images using ORB
                         algorithm. If the same or similar images are found,
                         store the found images' names as keys and 'marked' as
                         values in a dictionary, and return the dictionary. 
                         The first file in the dictionary is always the input
                         image.
        img_hash_comp: Compare the image to other images using image hashes.
                       This method will figure out if images in the comparison 
                       process have the same image hashes. If image hashes are
                       the same, they are considered as same images.

img_name_change.py
    - This file receives a sorted dictionary, which is the result of img_comp.
    - Method: 
        name_change: Change image names by inserting numbers that are values 
                     in the input dictionary to their names.

img_directory.py
    - This file receives a directory from users. 
    - This moves the working directory received.
    - This finds if or not the directory exists
    - This finds if or not images exist in the input directory
    - Method:
        move_dir_chk_img: Moves to the working directory and checks if images
                          exist in the directory. 

🌐 GitHub Repository:

    https://github.com/ByungkyuKang/Unique_Img_Process_with_Python.git
