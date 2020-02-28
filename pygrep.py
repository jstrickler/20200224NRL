#!/usr/bin/env python
import argparse
import re

#  script.py option ... argument ...

parser = argparse.ArgumentParser(description="Faux grep")

parser.add_argument('-i', dest="ignore_case", action="store_true", help="Ignore case")

parser.add_argument('-n', dest="show_file_name",
                    action="store_true", help="Display file name")

parser.add_argument('pattern', help="Pattern to find")

parser.add_argument('files', nargs="*", help="Files to search")

args = parser.parse_args()  # defaults to sys.argv

print(args)

if args.ignore_case:
    re_pattern = re.compile(args.pattern, re.I)
else:
    re_pattern = re.compile(args.pattern)

for file_name in args.files:
    with open(file_name) as file_in:
        for line in file_in:
            if re_pattern.search(line):
                if args.show_file_name:
                    print("{}:".format(file_name), end=' ')
                print(line, end='')

