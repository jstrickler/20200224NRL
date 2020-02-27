#!/usr/bin/env python

d1 = dict()
d2 = {'a': 5, 'm': 16, 'c': 10, 'r': 94}
d3 = {}

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

print(airports['YCC'], '\n')
airports['DCA'] = "Washington Reagan"
airports['DCA'] = "National"
print(airports, '\n')

abbr = 'BWI'
if abbr in airports:
    print(airports[abbr])

print(airports.get(abbr))
print(airports.get(abbr, "NOT FOUND"))

print(len(airports))

print(airports.keys())
print(airports.values())

more_airports = {
    'ELM': 'Elmira, NY',
    'JFK': 'NYC Kennedy',
    'JAX': 'Jacksonville, FL',
    'MLB': 'Melbourne, FL',
    'DCA': 'Ronald Reagan',
}

airports.update(more_airports)
print(airports, '\n')

for abbr, name in airports.items():
    print(abbr, name)
print()

for wombat, name in sorted(airports.items()):
    print(wombat, name)
print()

