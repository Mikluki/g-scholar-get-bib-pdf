#!/usr/bin/env python3
import re
import argparse

# (\\(.*?)\{) to[
# } to]
# \$ to none


if __name__ == "__main__":
    description = "strip latex symbols"
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('ltxstr', type=str, nargs='+', help="latex strings")

    args = parser.parse_args()

    for i, lstr in enumerate(args.ltxstr):
        lstr = re.sub(r'\\.*?\{', '[', lstr)
        lstr = re.sub('}', ']', lstr)
        lstr = re.sub(r'\$', '', lstr)
        print(lstr)
