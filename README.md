Files: 
    1. image_process_main.py   
        - Main file.

    2. dir_setting.py 
        - Move working directory/ create directories.
        - Methods:
            to_dir( dir_in ): Move working directory to dir_in.
            make_dirs( uniq_dir, dups_dir ): Create necessary directories
                                             (directory for unique images, and directory for duplicates)

    3. img_processing.py
        - Get image hashes, resize images, Compare images using the hashes and information of resized images.
        - Classes: 
            Img_existence: Working with directory which is given by users. 
                - Method:
                    check_dir: Check if images exist in the directory users enter.
                               If images exist, return a list of names of images.
                               If there are no images, return an empty list.
            Hash_comp: Receives the image name list, directories for unique images and duplicates.
                - Method:
                    hashes_comp_process: Find hashes of the images in the image name list.
                                         Classify the images and move them to their corresponding directories (Unique or duplicates).
                                         returns log contents.
            Reduce_size_comp: --! NOT COMPLETED YET. WORKING ON IT !--
                - Method: 
                    reduce_size_process: 