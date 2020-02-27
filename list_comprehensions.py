#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3", f3, '\n')

f4 = [f for f in fruits if "er" in f]
print("f4:", f4, '\n')

f5 = [f.upper()[:3] for f in fruits if len(f) > 6]
print("f5:", f5, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [n / 5 for n in nums]
print("n1:", n1, '\n')

f6 = [f.upper() if f.startswith('p') else f for f in fruits]
print("f6:", f6, '\n')

n2 = [(n, n**2, n**3) for n in nums]
print("n2:", n2, '\n')

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

last_names = [p[1] for p in people]
print("last names:", last_names, '\n')

last_names = [f"{p[2]} {p[1]}" for p in people]
print("last names:", last_names, '\n')

f1 = [f.upper() for f in fruits]

fgen = (f.upper() for f in fruits)
print(fgen)
