import cv2
import imagehash as ihash
from PIL import Image as img

class img_comp_processes():
    """ This class will run two methos continuously. 
        1. cv2_img_comp
        2. img_has_comp """
    
    def __init__(self, img_name, img_list):
        self.img_name = img_name
        self.img_list = img_list


    def cv2_img_comp(self):
        """ This method recevies a image name and image list, compares it to other
            , and returns a list which has names of similar or same images """

        might_be_similar_imgs = []
        might_be_diff_imgs = []
        
        for img in self.img_list:
            if self.img_name != img:
                curr_img = cv2.imread(self.img_name, cv2.IMREAD_GRAYSCALE)
                img_from_list = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
                
                orb = cv2.ORB_create()

                kpoint_curr, curr_desc = orb.detectAndCompute(curr_img, None)
                kpoint_list_img, list_img_desc = orb.detectAndCompute(img_from_list, None)

                bfm = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

                matches = bfm.match(curr_desc, list_img_desc)
                matches = sorted(matches, key=lambda x: x.distance)

                num_matches = len(matches)
                
                if num_matches > 150:
                    might_be_similar_imgs.append(img)
                else:
                    might_be_diff_imgs.append(img)

        hash_comp_result = self.img_hash_comp(self.img_name, might_be_diff_imgs)
        might_be_similar_imgs = might_be_similar_imgs + hash_comp_result

        return list(set(might_be_similar_imgs))
    

    def img_hash_comp(self, img_name, img_list):
        curr_image = img.open(self.img_name)
        curr_image_hash = ihash.phash(curr_image)
        
        might_be_similar_imgs = []
        for image in self.img_list:
            list_image = img.open(image)
            list_image_hash = ihash.phash(list_image)
            if curr_image_hash == list_image_hash:
                might_be_similar_imgs.append(image)
                
        return might_be_similar_imgs 