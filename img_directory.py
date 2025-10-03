import os               # Importing os for file operations

def move_dir_chk_img(dir_in):
    """ Move to the entered directory, and check if images exist.
        Input Parameter: working directory
        Output : a list of image names  (when images exist) 
                 False (when images dont exist) """
    
    # Check if the received directory exists
    try:
        os.chdir(dir_in)
    except:
        error_msg = "The directory you entered does not exist. Please check "
        error_msg += "the path and try again."
        print(error_msg)
        return exit(0)  # terminate this program when no directory found.
    else:
        print(f'Directory "{dir_in}" exists.')

    # Check if images exist
    image_extensions = ('.jpg', '.jpeg', '.png', 
                        '.gif', '.bmp', '.tiff', '.webp')
    image_files = [f for f in os.listdir(dir_in) 
                        if f.lower().endswith(image_extensions)]
    
    if image_files:
        print(f"{len(image_files)} image(s) exist(s) in the directory.")
    else:
        notification_msg = "No images found in the directory. " 
        notification_msg += "Exiting the program."
        print( notification_msg )
    return image_files 