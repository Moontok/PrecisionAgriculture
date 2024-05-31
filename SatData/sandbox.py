# Rename all files in a directory to the last sections of characters after splitting on "_"

import os
import shutil

def rename_files(directory):
    for filename in os.listdir(directory):
        new_filename = filename.split("_")[-1]
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed {filename} to {new_filename}")

rename_files("may_data")