#!/usr/bin/env python
from typing import Union

def get_message():
    return "Hello, NRL world"

m = get_message()
print(m)
print(get_message())

get_message()


def hello():
    x = get_message()
    print(x)

hello()


def a():
    b()

def b():
    print("hello from b()")

a()

Numeric = Union[int, float]

def spam(x: Numeric, y: Numeric) -> Numeric:
    return x * y

print(spam(10, 5))

print(spam('=', 50))

def dash():
    print("-" * 60)

dash()
dash()





print(spam.__annotations__)

def greet(greeting, *people):
    for person in people:
        print(greeting, person)
    print()

greet("Hello", "Mom", "Dad")
greet("Hello", "Mom")
greet("Hello")
greet("Hiya", "Mom", "Dad", "Sis", 'Aunt Fanny', 'Bob the wonder llama')

greetees = 'Alex', 'Kaily', 'Duane'

greet(None)





