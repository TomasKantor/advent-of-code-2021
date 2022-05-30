#!/usr/bin/python3

# advent of code 2021 - Day 2 a

with open('input.txt') as file:

    depth = 0
    horizontal = 0

    for line in file:
        words = line.split()

        direction = words[0]
        value = int(words[1])

        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value

    print(depth*horizontal)
