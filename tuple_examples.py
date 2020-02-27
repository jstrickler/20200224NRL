#!/usr/bin/env python

person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(person[0])
print(person[1])

rp = reversed(person)
for thing in rp:
    print(thing)

first_name, last_name, product, dob = person

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
]

for person in people:
    print(person)
print('-' * 60)

for person in people:
    (first_name, last_name, *product, dob) = person
    print(first_name, last_name, dob)
print('-' * 60)

for (first_name, last_name, *product, dob) in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name, product, dob)
print('-' * 60)

data = [('comsat', 3), ('telstar', 8), ('sputnik', 3)]

print(data[0])
print(data[0][0])
print(data[0][0][0])

for d in data:
    print(d)
print()

for sat_name, sat_number in data:
    print(sat_name, sat_number)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

print(len(people), len(data))
print(len(people[0]))
print(len(people[0][0]))
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(min(people), min(data), min(nums))
print(max(people), max(data), max(nums))
print(sorted(data))
print(sorted(nums))

rnums = reversed(nums)
print(rnums)
for i in rnums:
    print(i, end=' ')
print()

satellites = ['telstar', 'comsat', 'sputnik']
years = [1958, 1962, 1956]
origins = ['US', 'US', "USSR"]

x = zip(satellites, years, origins)
print(x)

for name, number, origin in x:
    print(name, number, origin)

x = zip(satellites, reversed(years), origins)
print(list(x))

for sat in satellites:
    print(sat)
print()

# print(list([list(x) for x in enumerate(satellites)]))

print(list(enumerate(satellites)))
print(list(enumerate(satellites, 1)))


