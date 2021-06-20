import os
import re
from PIL import Image

DATASET_DIRECTORY = "./../images/"

def get_highest_number():
    max_num = 0
    for filename in os.listdir(DATASET_DIRECTORY):
        if re.match(r'^img_\d+.jpg$', filename):
            file_num = list(map(int, re.findall(r'\d+', filename)))[0]
            max_num = file_num if file_num > max_num else max_num
    return max_num

def rename_images():
    print("================= Starting renaming dataset =================")
    file_num = get_highest_number()

    for filename in os.listdir(DATASET_DIRECTORY):
        if re.match(r'^img_\d+.jpg$', filename):
            continue

        file_num += 1

        new_filename = os.path.join(DATASET_DIRECTORY, "img_" + str(file_num) + ".jpg")
        old_filename = os.path.join(DATASET_DIRECTORY, filename)

        print("Renaming " + old_filename)
        print("New file name: " + new_filename)

        os.rename(old_filename, new_filename)
    
    print("================= Finished renaming dataset =================")

def resize_images():
    print("================= Starting resizing dataset =================")
    for filename in os.listdir(DATASET_DIRECTORY):
        path = os.path.join(DATASET_DIRECTORY, filename)
        image = Image.open(path)

        max_dim = 1024
        
        if image.size[0] > max_dim or image.size[1] > max_dim:
            image.thumbnail((max_dim, max_dim))
            image.save(path)
            print("Resized " + path)
    print("================= Finished resizing dataset =================")

if __name__ == "__main__":
    rename_images()
    resize_images()