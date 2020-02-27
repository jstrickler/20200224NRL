#!/usr/bin/env python

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

ops = {
    '+': add, '-': sub, '*': mul, '/': div
}

while True:
    expr = input("Enter a math expression: ")

    if expr.lower() == 'q':
        break

    v1, op, v2 = expr.split()
    v1 = float(v1)
    v2 = float(v2)

    if op in ops:
        result = ops[op](v1, v2)
    else:
        print("Bad operator!")
        continue

    print("{:.3f}".format(result))
