📸 Automated Duplicate Image Organizer

📌 Overview
Automated Duplicate Image Organizer is a Python-based console application designed to simplify personal photo management. It consolidates images from multiple directories and removes duplicates to create a clean, well-organized backup.

🎯 Motivation
Managing photos from different apps and sources often leads to scattered duplicates, making backups inefficient and time-consuming. This project was created to streamline photo management by automating the consolidation and de-duplication process, ensuring users can easily access unique images while managing duplicates efficiently.

⚙️ How It Works
Collects images from user-specified directories.
Generates hash values for each image and performs resized image comparisons for higher accuracy.
Organizes results into:
Unique folder: contains original, non-duplicate images
Duplicate folder: contains duplicates for easy review and removal

🔧 Current Status
Core logic implemented and functional.
Actively refining performance and accuracy of image comparison.

🗂 Files
image_process_main.py
    Main execution file.

dir_setting.py
    Handles working directory setup and folder creation.
    Methods:
        to_dir(dir_in): Move working directory to dir_in.
        make_dirs(uniq_dir, dups_dir): Create directories for unique and duplicate images.

img_processing.py
    Handles image hashing, resizing, and comparison.
    Classes:
        Img_existence: Manages user-provided directories.
            check_dir(): Returns list of image names if images exist; empty list otherwise.
        Hash_comp: Classifies images into unique or duplicate folders.
            hashes_comp_process(): Computes image hashes, classifies images, moves them to corresponding directories, and returns log contents.
        Reduce_size_comp (in progress)
            reduce_size_process(): Resize-based comparison under development.

🌐 GitHub Repository:
    https://github.com/ByungkyuKang/Unique_Img_Process_with_Python.git