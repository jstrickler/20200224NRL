#!/usr/bin/env python
from carddeck import CardDeck

class Villain:
    def kill(self):
        print("STAB STAB STAB")

class JokerDeck(CardDeck, Villain):

    def _make_cards(self):
        super()._make_cards()
        j1 = 'Joker-1'
        j2 = 'Joker-2'
        self._cards.append(j1)
        self._cards.append(j2)

