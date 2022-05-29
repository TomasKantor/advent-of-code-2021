#!/usr/bin/python3

# advent of code 2021 - Day 1 a

with open('input.txt') as file:
    previous = None
    count = 0

    for line in file:
        value = int(line)
        if previous and value > previous:
            count += 1

        previous = value

    print(count)
