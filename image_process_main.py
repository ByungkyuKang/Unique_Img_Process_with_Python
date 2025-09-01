import os               # Importing os for file operations
from PIL import Image as img  # Pillow library for image processing
## Need to delete!! --> import shutil as st     # Importing shutil for file operations
import imagehash as ihash # Importing imagehash for hashing images
import pathlib as pl  # Importing pathlib for path operations

import img_processing as ihc  # Importing the custom image hash comparison module
import dir_setting as ds

##############################################################################
# Receive a directory where images are stored from the user                  #
##############################################################################
# image_dir = os.path.normpath(input("Enter the directory path where images: \
                                #    are stored.\n\t>> "))
image_dir = "C:\\Users\\tkaek\\Desktop\\pandas screenshots for Anki"

# Change working dir.
ds.to_dir(image_dir)

unique_dir = "unique_pics"
dup_dir = "dubplicated_pics"

# Save a list to store image names.
img_file_list = ihc.Img_existence(image_dir).check_dir()

# Make directories for hash-comparison
ds.make_dirs(unique_dir, dup_dir)

# Process hash comparison if pictures exist
if img_file_list:
    logs = ihc.Hash_comp(img_file_list, unique_dir, dup_dir).hashes_comp_process()
else:
    print("No files. Program terminated.")
    exit()

# Enter the unique directory for the process with reduced size
reduce_process_wd = f"{image_dir}\\{unique_dir}"
ds.to_dir(reduce_process_wd)

final_unique_dir = "final_unique_dir"

# Make directories for hash-comparison
ds.make_dirs(final_unique_dir, dup_dir)

######################################################
##### NEED TO MAKE "reduced-size comparison" LOGIC.
######################################################

pl.Path("log.txt").write_text(logs)  # Write the log content to a file.