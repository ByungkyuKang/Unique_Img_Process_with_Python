import os               # Importing os for file operations
from PIL import Image   # Pillow library for image processing

# Receive a directory where images are stored from the user


# Check if there is any image in the received directory (.jpg, jpeg, .png, .gif, .bmp, .tiff, .webp)


# If there is no image, print a message and exit the program.
# If there are images, create a new list to store the image hashes, and create a sub directory to store the processed images.



# Remove duplicated image hashes - Keep unique hashes.


# Find images per each hash. Then, compare the images which have the same hash, and check the size (resolution) of the images. Images which have the best resolution per each hash will be moved to the new sub directory, and the others will be removed.
# Create a log text file (how many images were processed, how many were removed, and many were moved to the new directory - per hash).