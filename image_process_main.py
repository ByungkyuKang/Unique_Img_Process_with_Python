import img_processing as imgp
import img_directory as ds
import os

##############################################################################
# Receive a directory where images are stored from the user                  #
##############################################################################
input_massage = "Enter the entire directory path to work on.\n\t>>"
image_dir = os.path.normpath(input(input_massage))
# image_dir = "C:\\Users\\tkaek\\Desktop\\pandas screenshots for Anki"

# Change to working dir.
# input argument: image_dir
# return value: an image names list
img_exist = ds.move_dir_chk_img(image_dir)

# Start the process
# This will group similar images changing their names
imgp.image_process(img_exist)
