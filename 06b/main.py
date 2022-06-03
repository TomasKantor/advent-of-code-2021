#!/usr/bin/python3

# advent of code 2021 - Day 6 b


def load_input(file):

    # number of fish for each number of days left in cycle
    fish = [0]*9

    for line in file:
        words = line.split(',')

        for w in words:
            number = int(w)
            fish[number] += 1

    return fish


def step(fish):
    fish_next = [0]*9

    for i, count in enumerate(fish):
        if i == 0:
            fish_next[6] += count
            fish_next[8] += count
        else:
            fish_next[i-1] += count

    return fish_next


with open('input.txt') as file:

    fish = load_input(file)
    for _ in range(256):
        # print(fish)
        fish = step(fish)

    print(sum(fish))
