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

filenames = os.listdir(os.path.join(img_dir))

for f in filenames:
	string = '![{}]({}{})'.format(f, img_dir, f)
	print(f)
	print(string)
