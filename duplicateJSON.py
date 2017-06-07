#!/usr/bin/python

import argparse
import json
from base64 import b64encode
import os
import shutil
import sys, getopt


def save2(filename, imagePath):
	encoded = b64encode(open(imagePath, "rb").read())

	with open(filename, 'rw+') as f:
		data = json.load(f)
		data['imagePath'] = imagePath
		data['imageData'] = encoded
		f.seek(0)        # should reset file position to the beginning.
    		json.dump(data, f, indent=2)
    		f.truncate()     # remove remaining part


def main(json_file, imagePath):
	
	nameJ,extJ = os.path.splitext(os.path.basename(json_file))
	nameI,_ = os.path.splitext(os.path.basename(imagePath))
	path_newJSON = os.path.dirname(json_file)
	path_newJSON = os.path.join(path_newJSON,nameI+extJ)
	shutil.copy(json_file, path_newJSON)
	save2(path_newJSON, imagePath)    

   
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Copy json LabelMe Annotation from other image')
	parser.add_argument('-i', '--image', help='Image File', required=True)
	parser.add_argument('-j', '--json', help='Json File', required=True)
	args = parser.parse_args()
	
	main(args.json, args.image)

