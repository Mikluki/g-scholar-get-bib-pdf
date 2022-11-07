#!/usr/bin/env python3

import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--pubs', type=str, nargs='+')
args = parser.parse_args()
print(args.pubs)

def write_to_file(bibtex, fname='out.bib'):
    xlist = np.arange(1, 10)
    ylist = np.arange(10, 20)
    with open(name+'.dat', "w") as f:
        for xi, yi in zip(xlist,ylist):
            f.write(f"{xi},{yi}\n")
        # f.write('\n')
