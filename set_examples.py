#!/usr/bin/env python

kaily_countries = [
    'Belgium', 'Mexico', "France", "Italy", "Spain"
]

duane_countries = [
    'Spain', 'Mexico', 'Columbia', 'Thailand', 'Brazil'
]

kaily = set(kaily_countries)
duane = set(duane_countries)

print("common:", kaily & duane)
print("not common:", kaily ^ duane)

print("all:", kaily | duane)
print("just Kaily:", kaily - duane)
print("just Duane:", duane - kaily)

