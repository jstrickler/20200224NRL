#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Alphie")
print(d1)

d1.shuffle()

# print(d1._cards)


for i in range(5):
    print(d1.draw())


print(d1.get_dealer())

print(d1.dealer)
d1.dealer = 'Ferdinand'

print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
print(d1.dealer)

print(d1.get_ranks())

print(CardDeck.get_ranks())

print(CardDeck.RANKS)

j1 = JokerDeck("Emma")
j1.shuffle()
print(j1._cards)
j1.kill()
