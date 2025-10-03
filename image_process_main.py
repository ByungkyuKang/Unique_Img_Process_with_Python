import img_processing as imgp
import img_directory as ds
import tkinter as tk
from tkinter import filedialog

#############################################################
# Receive a directory where images are stored from the user #
#############################################################
root = tk.Tk()
root.withdraw() 

image_dir = filedialog.askdirectory(
    title="Select a directory"
)

# Enter the directory from users.
# input argument: image_dir
# return value: an image names list
img_exist = ds.move_dir_chk_img(image_dir)

# Start the process
# This will group similar images changing their names
imgp.image_process(img_exist) 