#!/usr/bin/env python

actor = "Chris Hemsworth"
value = 42
factor = 123.35787382

print(actor)
print(value)

print(actor, value, factor)
print("next")
print("next")

print(actor, value, factor, sep="/")
print(actor, value, factor, sep=":")
print("a", end=",")
print("b", end=",")
print("c")

print("factor is", factor)
print("factor is {:.2f}".format(factor))

city = "Beverly Hills"

print("{} lives in {}".format(actor, city))
print(f"{actor} lives in {city}")

x = 42

print("{0}|{0:4d}|{0:04d}|{0:04x}".format(x))

w = "wombat"

print("{0}|{0:12s}|{0:^12s}|{0:>12s}".format(w))

