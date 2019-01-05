from PIL import Image
import os, sys

# Update this: This path points to where the original images are.
path = '/Users/PaulYim/desktop/Photos/'
dirs = os.listdir(path)

new_path = path + 'resized/'
print(new_path)
if not os.path.exists(new_path):
	os.makedirs(new_path)


def resize():
    for item in dirs:
        print(item)
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,480), Image.ANTIALIAS)
            imResize.save(new_path + f'{item[:-4]}_resized.jpg', 'JPEG', quality=100)

resize()