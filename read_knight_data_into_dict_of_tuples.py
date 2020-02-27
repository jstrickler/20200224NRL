#!/usr/bin/env python
from pprint import pprint

def main():
    data = read_info()
    pretty_print(data)
    print(get_field(data, 'Arthur', 2))

    print_titles(data)


def read_info():
    knight_info = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_info[name] = [title, color, quest, comment]
    return knight_info

def pretty_print(info):
    pprint(info)

def get_field(info, knight, field):
    return info[knight][field]

def print_titles(info):
    for name, data in info.items():
        print(data[0], name, data[1])

if __name__ == '__main__':
    main()
