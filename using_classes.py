#!/usr/bin/env python

x = list()

print(x)

x.append('wombat')

print(x)

value = 5  #  value = int(5)

print(type(value), value)

class Vehicle:

    def beep(self):
        print("beep beep beep")

v1 = Vehicle()
v2 = Vehicle()
print(type(v1), type(v2))

v1.beep()
v2.beep()




