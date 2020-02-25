#!/usr/bin/env python

actor = "Chris Hemsworth"

print(actor)
print(actor.upper())
print(actor.lower())
print(actor.count('h'))
print(actor.count('wort'))
print(actor.count('H'))
t = actor.lower()
print(t.count('h'))
print(actor.lower().count('h'))
print(actor.startswith("Liam"))
print(actor.startswith("Chris"))
print(actor.endswith('wombat'))


s = "     All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxxyyyyxxyAll my exes live in Texasyyxyyxyyxyyxyxy"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

print(s.replace('x', ''))
print(s.replace('x', 'T'))

data = "one|two|three|four"

print(data.split("|"))

print(actor.index("Hem"))
print(actor.find("Hem"))
print(actor.find("Liam"))

print("Hem" in actor)
print("Haw" in actor)

