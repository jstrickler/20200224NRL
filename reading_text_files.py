#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    whole_enchilada = mary_in.read()
    print("raw:")
    print(repr(whole_enchilada))
    print("cooked:")
    print(whole_enchilada)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    # or, as generator
    # all_lines_without_nl = (line.rstrip() for line in mary_in)
    print(all_lines_without_nl)

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        print(title, name)
