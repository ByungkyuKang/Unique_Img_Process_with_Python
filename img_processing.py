import img_comp as imgc
import img_name_change as inc

# Set values to 0
def image_process( img_list ):
    """ This method gathers image files, and prepare for the entire processes,
        such as the dictionary to store image names and their group numbers.
        This method calls the comparing method in img_comp,
        the name change method in img_name_change. """
    img_name_dict = {}
    for img_name in img_list:
        img_name_dict[img_name] = 0

    itr_cnt = 1

    # Run comparing processes - cv2 and hash
    for img_name in img_name_dict:
        if img_name_dict[img_name] == 0:
            comp_process_obj = imgc.img_comp_processes(img_name, img_list)
            comp_process = comp_process_obj.cv2_img_comp()
            
            for img_dict in img_name_dict:
                for img_comp in comp_process:
                    if img_dict == img_comp:
                        img_name_dict[img_dict] = itr_cnt
            itr_cnt += 1

    # Change image names and group them by the numbers added to the names
    sorted_dict_by_number = sorted(img_name_dict.items(), key=lambda item: item[1])
    inc.name_change(sorted_dict_by_number) 