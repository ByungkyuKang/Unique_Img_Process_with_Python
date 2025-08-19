import os               # Importing os for file operations
from PIL import Image as img  # Pillow library for image processing
import shutil as st     # Importing shutil for file operations
import imagehash as ihash # Importing imagehash for hashing images
import pathlib as pl  # Importing pathlib for path operations

import img_hash_comp as ihc  # Importing the custom image hash comparison module

##############################################################################
# Receive a directory where images are stored from the user                  #
##############################################################################
# image_dir = os.path.normpath(input("Enter the directory path where images: \
                                #    are stored.\n\t>> "))
image_dir = "C:\\Users\\tkaek\\Desktop\\pandas screenshots for Anki"

try:
    os.chdir(image_dir)
except FileNotFoundError:
    print("The directory you entered does not exist. Please check the path \
          and try again.")
else:
    print(f"The directory you entered exists: {image_dir}. Working here...")

##############################################################################
# Check if there is any image in the received directory (.jpg, jpeg, .png,   #
# .gif, .bmp, .tiff, .webp)                                                  #
##############################################################################
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)]

# If there is no image, print a message and exit the program.
# If there are images, create a new list to store the image hashes, and create
# a sub directory to store the processed images.
unique_dir = "Unique_Images"
dup_dir = "Duplicate_Images"

if image_files:
    print(f"Found {len(image_files)} image(s) in the directory.")
    
    if not os.path.exists(unique_dir):
        os.mkdir(unique_dir)  # Create a new sub dir for unique images
        print(f"Created a new sub directory {unique_dir} to store unique \
              images.")
    if not os.path.exists(dup_dir):
        os.mkdir(dup_dir) # Create a new sub dir for duplicates
        print(f"Created a new sub directory {dup_dir} to store \
              duplicate images.")    
else:
    print("No images found in the directory. Exiting the program.")

everything_in_dir = os.listdir(image_dir)    # List all files in the directory

image_list = []     # List to store image hashes
for thing in everything_in_dir:
    if thing.lower().endswith(image_extensions):
        image_list.append(thing)

# print(image_list)
hash_list = []  # List to store image hashes
for image in image_list:
    opened_image = img.open(image)  # Open the image file
    image_hash = ihash.phash(opened_image)  # Compute the perceptual hash
    hash_list.append(image_hash)  # Append the hash to the list

set_hash_list = set(hash_list)  

# Create an instance of the hash_comp class
process_with_hash_comp = ihc.hash_comp(set_hash_list, image_list, 
                                       unique_dir, dup_dir)  

# Create a log text file (how many images were processed, how many were 
# removed, and many were moved to the new directory - per hash).
path = pl.Path(image_dir)
log_content = process_with_hash_comp.hashes_comp_process()

pl.Path("log.txt").write_text(log_content)  # Write the log content to a file.