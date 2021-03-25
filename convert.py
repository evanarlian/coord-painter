import sys
from os import path
from argparse import ArgumentParser

import PIL
from PIL import Image
import numpy as np



parser = ArgumentParser()
parser.add_argument("image", type=str, help="any image file")
parser.add_argument("-o", "--output", type=str, help="output name in npy format")
args = parser.parse_args()


def determine_path(args):

	dir_name = path.dirname(args.image)
	file_name = path.splitext(path.basename(args.image))[0]
	
	if args.output is not None:
		dir_name = dir_name = path.dirname(args.output)
		file_name = path.splitext(path.basename(args.output))[0]

	read_from = args.image
	save_to = path.join(dir_name, file_name + ".npy")
	
	return read_from, save_to


def read_image(image_path):

	FAIL = "\033[91m"
	ENDC = "\033[0m"

	try:
		image = Image.open(image_path).convert("RGB")
	except PIL.UnidentifiedImageError:
		print(f"{FAIL}PIL cannot read the image.{ENDC}")
		sys.exit(1)
	except FileNotFoundError:
		print(f"{FAIL}File not found.{ENDC}")
		sys.exit(1)
	except:
		print(f"{FAIL}Unknown error.{ENDC}")
		sys.exit(1)

	image = np.array(image)
	return image


def to_coordinate(arr):

	arr = arr.astype(np.int32)

	# search for non-white color
	arr = arr.sum(axis=2) != 255 * 3
	h, w = arr.shape

	# create cartesian coordinate
	yy, xx = np.mgrid[0:h, 0:w]
	yy = yy[arr]
	xx = xx[arr]

	return np.stack((yy, xx), axis=1)


def save_coords(save_path, coords):
	OKGREEN = "\033[92m"
	ENDC = "\033[0m"
	np.save(save_path, coords)
	print(f"{OKGREEN}File saved to {save_path}{ENDC}")



if __name__ == "__main__":

	read_from, save_to = determine_path(args)
	image = read_image(read_from)
	coords = to_coordinate(image)
	save_coords(save_to, coords)
	