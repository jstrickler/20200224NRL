#!/usr/bin/env python

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]
        if first_letter not in letter_counts:  # if letter_counts is NOT a key in the dict
            letter_counts[first_letter] = 1
        else:
            letter_counts[first_letter] = letter_counts[first_letter] + 1

    words_in.seek(0)   # now can re-read file if desired
print(letter_counts)
