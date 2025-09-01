import shutil as st
import imagehash as ihash
from PIL import Image as img
import numpy as np
import os

class Img_existence:
    """ Check if images exist. Return a list which stores image names.
        Return a message. """
    def __init__(self, working_dir):
        self.working_dir = working_dir
    
    def check_dir(self):
        image_extensions = ('.jpg', '.jpeg', '.png', 
                            '.gif', '.bmp', '.tiff', '.webp')
        image_files = [f for f in os.listdir(self.working_dir) 
                        if f.lower().endswith(image_extensions)]
        if image_files:
            print(f"Found {len(image_files)} image(s) in the directory.")
            # return image_files
        else:
            notification_msg = "No images found in the directory. " 
            notification_msg += "Exiting the program."
            print( notification_msg )
            # return
        return image_files
        

class Hash_comp:
    """
    This class is used to compare image hashes and separate unique images 
    from duplicates. 
    Hash_comp(hash_list, img_list, unique_dir, dup_dir)
    """
    def __init__(self, img_list, unique_dir, dup_dir):
        self.img_list = img_list
        self.unique_dir = unique_dir
        self.dup_dir = dup_dir
    # def __init__(self, hash_list, img_list, unique_dir, dup_dir):
    #     self.hash_list = hash_list
    #     self.img_list = img_list
    #     self.unique_dir = unique_dir
    #     self.dup_dir = dup_dir
    
    def hashes_comp_process(self):
        """Compare image hashes and separate unique images and duplicates."""
        log_content = 'Comparing hashes...\n\n'

        hash_list = []                              # List to store image hashes
        for image in self.img_list:
            opened_image = img.open(image)          # Open the image file
            image_hash = ihash.phash(opened_image)  # Compute the perceptual hash
            hash_list.append(image_hash)            # Append the hash to the list

        for hash in hash_list:
            found_flag = False   # Flag to check if a hash is already found
            for image in self.img_list:
                current_image = img.open(image)
                if ihash.phash(current_image) == hash:
                    if found_flag == True:
                        st.copy(image, self.unique_dir)
                        log_content += f"[{hash}] - {image} moved to "
                        log_content += "Duplicate_Images directory.\n"
                    else:
                        st.copy(image, self.dup_dir)
                        found_flag = True
                        log_content += f"[{hash}] - {image} moved to "
                        log_content += "Unique_Images directory.\n"
        return log_content


class Reduce_size_comp:
    """
    This class reduces the size of images and compares them. Then,
    move unique images to a unique directory and duplicates to a
    duplicate directory. Also, creat a log file with the results.
    at the end.
    Reduce_size_comp(image_list, unique_dir, dup_dir)
    """
    def __init__(self, img_list, unique_dir, dup_dir):
        self.img_list = img_list
        self.unique_dir = unique_dir
        self.dup_dir = dup_dir

    def reduce_size_process(self):
        """ 
        Reduce the size of images and compare images. 
        Then, separate unique images and duplicates.
        """
        # os.chdir(self.unique_dir)

        # final_unique_dir = './final_unique'
        # Move to the working directory
        if not os.path.exists(self.unique_dir):
            os.mkdir(self.unique_dir) 
            print(f"Created a new sub directory {self.unique_dir} to store unique \
                  images.")
        if not os.path.exists(self.dup_dir):
            os.mkdir(self.dup_dir)
            print(f"Created a new sub directory {self.dup_dir} to store \
                  duplicate images.")    
            
        log_content = 'comparing resized images...\n\n'

        while self.img_list:
            if len(self.img_list) > 1:
                # Get the current image and next image names
                current_img_name = self.img_list[0]
                print(f'\n\n{self.img_list}')
                self.img_list.remove(current_img_name)
                print(f'\n\n{self.img_list}')

                for image in self.img_list:
                    # Load the current image and next image
                    loaded_curr_img = img.open(current_img_name)
                    resized_curr_img = loaded_curr_img.resize((100,100))
                    loaded_next_img = img.open(image)
                    resized_next_img = loaded_next_img.resize((100,100))

                    # Get the pixel information
                    cur_img_fixel = np.array(resized_curr_img)
                    next_img_fixel = np.array(resized_next_img)

                    # Compare the arrays, and move the current image to the 
                    # final unique directory
                    if cur_img_fixel==next_img_fixel:
                        st.copy(current_img_name, self.unique_dir)
                    else:
                        st.copy(current_img_name, self.dup_dir)