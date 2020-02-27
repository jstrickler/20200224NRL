#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

def ignore_case(s):
    return s.lower()

f1 = sorted(fruits, key=ignore_case)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom_sort(x):
    return len(x), x.lower()

f4 = sorted(fruits, key=custom_sort)
print("f4:", f4, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]


for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)


for person in sorted(people, key=lambda p: (p[-1])):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(e):
    return e[1], e[0]

for abbr, name in sorted(airports.items(), key=by_value, reverse=True):
    print(abbr, name)
print()


f1 = sorted(fruits, key=ignore_case, reverse=True)
print("f1:", f1, '\n')
