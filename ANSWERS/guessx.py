#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    max_value = int(sys.argv[1]) + 1
else:
    user_input = input("Enter max value: ")
    max_value = int(user_input)  + 1

min_value = 0
tries = 0

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    if answer == "h":
        max_value = guess
        tries += 1
    elif answer == "l":
        min_value = guess
        tries += 1
    elif answer == "y":
        print("I got it in {} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")


