#!/usr/bin/env python
import random

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'C D H S'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_cards()

    def _make_cards(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = "{}-{}".format(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def get_dealer(self):
        return self._dealer

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

