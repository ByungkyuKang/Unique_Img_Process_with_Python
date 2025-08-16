import os               # Importing os for file operations
from PIL import Image as img  # Pillow library for image processing
import shutil as st     # Importing shutil for file operations
import imagehash as ihash # Importing imagehash for hashing images
import pathlib as pl  # Importing pathlib for path operations

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
if image_files:
    print(f"Found {len(image_files)} image(s) in the directory.")
    
    if not os.path.exists("Unique_Images"):
        os.mkdir("Unique_Images")  # Create a new sub dir for unique images
        print("Created a new sub directory 'Unique_Images' to store unique \
              images.")
    if not os.path.exists("Duplicate_Images"):
        os.mkdir("Duplicate_Images") # Create a new sub dir for duplicates
        print("Created a new sub directory 'Duplicate_Images' to store \
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
    # print(f"{image_hash}")  # Print image name and its hash
    # image_hash = str(image_hash)  # Convert the hash to string for easier handling
    hash_list.append(image_hash)  # Append the hash to the list

set_hash_list = set(hash_list)  # Convert the list to a set to remove duplicates

# Go through the set of hashes. Compare each hash with the images in the 
# image_list. Only the first image with the hash will be moved to the 
# "Unique_Images" directory, and the rest will be moved to the "Duplicate_Images"
# directory.
log_content = 'This time...\n\n'
for hash in set_hash_list:
    found_flag = False   # Flag to check if a hash is already found
    for image in image_list:
        current_image = img.open(image)
        if ihash.phash(current_image) == hash:
            if found_flag == True:
                st.copy(image, "Duplicate_Images")
                log_content += f"[{hash}] - {image} moved to "
                log_content += "Duplicate_Images directory.\n"
            else:
                st.copy(image, "Unique_Images")
                found_flag = True
                log_content += f"[{hash}] - {image} moved to "
                log_content += "Unique_Images directory.\n"

# Find images per each hash. Then, compare the images which have the same hash, and check the size (resolution) of the images. Images which have the best resolution per each hash will be moved to the new sub directory, and the others will be removed.


# Create a log text file (how many images were processed, how many were removed, and many were moved to the new directory - per hash).
path = pl.Path(image_dir)
print(path)
# pl.write_text(f"{path}\\log.txt", log_content)
pl.Path("log.txt").write_text(log_content)  # Write the log content to a file