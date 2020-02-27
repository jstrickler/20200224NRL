#!/usr/bin/env python

scores = {}
total_of_scores = 0

with open("../DATA/testscores.dat") as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores[name] = score
        total_of_scores += score


def get_grade(score):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def by_value(e):
    return e[1]

for student, score in sorted(scores.items(), key=by_value,
                             reverse=True):
    print("{:<20s} {:2d} {}".format(student, score, get_grade(score)))

average = total_of_scores / len(scores)
print("\naverage score is  {:.2f}\n".format(average))
