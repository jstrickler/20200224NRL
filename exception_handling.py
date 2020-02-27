#!/usr/bin/env python

FILE_NAME = 'DATA/wombats.txt'

try:
    with open(FILE_NAME) as wombats_in:
        pass
except FileNotFoundError as err:
    print(err)


x = ['a', 'b', 'c', 'd', 'e', 'f']
try:
    print(x[99])
except IndexError as err:
    print(err)


for i in 5, 8, 0, 11, 3, 7:
    try:
        result = 22 / i
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print("oof!")
