#!/usr/bin/python3

# advent of code 2021 - Day 1 b

with open('input.txt') as file:

    a = None
    b = None
    c = None

    count = 0
    previous_sum = None
    current_sum = None

    for line in file:
        c = b
        b = a
        a = int(line)

        if b and c:
            current_sum = a + b + c

        if previous_sum and current_sum > previous_sum:
            count += 1

        if current_sum:
            previous_sum = current_sum

    print(count)
