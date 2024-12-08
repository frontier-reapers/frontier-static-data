#!/usr/bin/env python3

import pickle
import json
import utils
import argparse
import os.path
import jsonpickle

parser = argparse.ArgumentParser('export_starmap.py')
parser.add_argument('--root', help='the root directory containing ResFiles.', required=True)
parser.add_argument('--output', help='file to output to', required=True)
parser.add_argument('--format', help='format to export the starmap to.', default='json')
args = parser.parse_args()

indexFiles = utils.get_indexfiles()
result = utils.find_resfile(args.root, 'res:/staticdata/starmapcache.pickle', indexFiles)

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)

with open(result.filepath, 'rb') as file:
    data = pickle.load(file)
    json_data = jsonpickle.encode(data)

with open(args.output, 'w') as json_file:
    json_file.write(json_data)
    json_file.write('\n')
