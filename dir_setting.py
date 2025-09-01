import os               # Importing os for file operations

def to_dir(dir_in):
    """ Setting the working directory """
    try:
        os.chdir(dir_in)
    except FileNotFoundError:
        error_msg = "The directory you entered does not exist. Please check "
        error_msg += "the path and try again."
        print(error_msg)
    else:
        print(f"Entering {dir_in}. Working here...")


def make_dirs(uniq_dir, dups_dir):
    """ Creating directories for unique pictures and duplicates """
    if not os.path.exists(uniq_dir):
        os.mkdir(uniq_dir)  # Create a new sub dir for unique images
        print(f"{uniq_dir} is created to store unique images.")
    if not os.path.exists(dups_dir):
        os.mkdir(dups_dir)  # Create a new sub dir for duplicates
        print(f"{dups_dir} is created to store duplicate images.")