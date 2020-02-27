#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

for ctemp in ctemps:
    ftemp = ((9 * ctemp) / 5) + 32
    print("{}\u00B0 C is {}\u00B0 F".format(ctemp, ftemp))


fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

clean_fruits = [f.strip().lower() for f in fruits]
print(clean_fruits)
