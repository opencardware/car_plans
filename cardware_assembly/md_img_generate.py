'''
NOTE: Run this from cardware_assembly/
'''

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('image_dir', help='Prints strings that reference images, formatted for markdown.', type=str)
args = parser.parse_args()

img_dir = args.image_dir

path = os.getcwd()
# print(path)

filenames = os.listdir(os.path.join(img_dir))
# print(filenames)

github_dir = 'https://github.com/opencardware/car/blob/20181103_dev/cardware_assembly/imgs_drivetrain/'

for f in filenames:
	string = '![alt text]({}{} "{}")'.format(github_dir, f, f)
	print(string)