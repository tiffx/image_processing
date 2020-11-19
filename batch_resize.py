import cv2
import os

def load_filename_from_folder(folder):
    image_files = []
    for filename in os.listdir(folder):
        img_file = os.path.basename(filename)
        if img_file is not None:
            image_files.append(img_file)
    return image_files

folder = "sample_images"

def batch_resizing():
    newpath = "resized_images"
    beg_name = "Resized"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for image in load_filename_from_folder(folder):
        img = cv2.imread(f"{folder}/{image}", 1)
        resized_image = cv2.resize(img,(100,100))
        cv2.imwrite(f"{newpath}/{beg_name} {image}", resized_image)
    return "Resize successful!"

print(batch_resizing())