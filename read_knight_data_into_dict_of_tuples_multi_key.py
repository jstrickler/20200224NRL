#!/usr/bin/env python
from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name, title] = color, quest, comment

pprint(knight_info)

print(knight_info['Bedevere', 'Sir'][0])
print(knight_info['Arthur', 'Sir'][1])
print(knight_info['Arthur', 'King'][1])
print('-' * 60)

for name_title, data in knight_info.items():
    print(name_title[1], name_title[0], data[0])
