#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1
else:
    limit = 101

flags = [True] * limit
# print(flags)

count = 0
for num in range(2, limit):
    if flags[num]:
        print(num, end=' ')
        count += 1
        for i in range(2 * num, limit, num):
            flags[i] = False
print()
print("There were {} primes".format(count))
