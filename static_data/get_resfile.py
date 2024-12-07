#!/usr/bin/env python3

import csv
import argparse
import os.path
import utils

parser = argparse.ArgumentParser('get_resfile')
parser.add_argument('--root', help='the root directory containing the ResFiles folder.', required=True)
parser.add_argument('--file', help='the relative name of the resource file', required=True)
args = parser.parse_args();

indexFiles = utils.get_index_files()

print(f'Searching for {utils.clr.CYAN}{args.file}{utils.clr.ENDC} in {len(indexFiles)} files.')

output = utils.find_resfile(args.root, args.file, indexFiles)

if (output is None):
    print(f'{utils.clr.WARNING}unable to find resource{utils.clr.ENDC}')
    exit(1)

print(f'found {utils.clr.CYAN}{args.file}{utils.clr.ENDC} located at {utils.clr.GREEN}{output.res}{utils.clr.ENDC} in {output.index}')

