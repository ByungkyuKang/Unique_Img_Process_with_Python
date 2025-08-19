import shutil as st
import imagehash as ihash
from PIL import Image as img

class hash_comp:
    """
    This class is used to compare image hashes and separate unique images 
    from duplicates. 
    hash_comp(hash_list, img_list, unique_dir, dup_dir)
    """
    def __init__(self, hash_list, img_list, unique_dir, dup_dir):
        self.hash_list = hash_list
        self.img_list = img_list
        self.unique_dir = unique_dir
        self.dup_dir = dup_dir

    def hashes_comp_process(self):
        """Compare image hashes and separate unique images and duplicates."""
        log_content = 'This time...\n\n'

        for hash in self.hash_list:
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