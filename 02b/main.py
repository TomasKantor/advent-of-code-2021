#!/usr/bin/python3

# advent of code 2021 - Day 2 b

with open('input.txt') as file:

    depth = 0
    horizontal = 0
    aim = 0

    for line in file:
        words = line.split()

        direction = words[0]
        value = int(words[1])

        if direction == "forward":
            horizontal += value
            depth += aim*value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

    print(depth*horizontal)
