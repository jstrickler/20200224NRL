#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in sorted(fruits):
        fruitlist_out.write(fruit + '\n')


with open('DATA/knights.txt') as knights_in:
    with open('knightnames.txt', 'w') as knightnames_out:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            # knightnames_out.write(title + ' ' + name + '\n')
            knightnames_out.write("{} {}\n".format(title, name))
