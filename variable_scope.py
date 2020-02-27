#!/usr/bin/env python

x = 100   # global variable

def spam():
    y = 42  # LOCAL variable
    return y


wombat = spam()
print(x, wombat)


