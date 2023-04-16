import os
from PIL import Image
import numpy as np
original_dog_path = "/school/dog_original/"
saved_dog_path= "/school/dog_saved/"
original_cat_path = "/school/cat_original/"
saved_cat_path= "/school/cat_saved/"
origin_dir = os.listdir(original_dog_path)
saved_dir = os.listdir(saved_dog_path)

for file in origin_dir:
    img = Image.open(original_dog_path + file)
    print(file)
    resize_img = img.resize((100,100))
    gray_img = resize_img.convert('L')
    gray_img.save(saved_dog_path + file)

