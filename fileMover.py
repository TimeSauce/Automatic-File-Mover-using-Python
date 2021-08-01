# Script for automatically moving files from the downloads folder to their designated folders

import os

# Original path
original_path = r"{original file path}" + "\\"

# Target folders
img_folder = r"{target image folder}" + "\\"
video_folder = r"{target video folder}" + "\\"


# Main function
def main_function():

    # File moving function
    def move_files(file_path):
        os.rename(path + '\\' + file, file_path + file)


    # Get all files
    for path, dir, files in os.walk(original_path):
        if files:
            for file in files:      
                ext = file.lower().endswith

                # Start checking the extension
                if ext(('.img', '.jpg', '.png')):
                    move_files(img_folder)
                
                elif ext(('.mp4', '.flv', '.wlmp', '.mov')):
                    move_files(video_folder)
                    

# Check if new files appeared
if len(os.listdir(original_path)) != 7:
    main_function()


