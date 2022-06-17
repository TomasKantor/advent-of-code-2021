#!/usr/bin/python3

# advent of code 2021 - Day 17 b

import os
import re


# load list of area borders
def load_input(file):
    line = file.readline()
    pattern = '-?\\d+'  # positive or negative integer
    nums = re.findall(pattern, line)
    return [int(n) for n in nums]


# check if position is in area
def is_in_area(area, pos_x, pos_y):

    res = (pos_x >= area[0] and
           pos_x <= area[1] and
           pos_y >= area[2] and
           pos_y <= area[3])
    return res


# run probe and find max y position
# return None if misses area
def run(area, speed_x, speed_y):

    pos_x = 0
    pos_y = 0

    step_count = 0

    max_y = 0

    while pos_y >= min(area[2], area[3]) and pos_x <= max(area[0], area[1]):
        step_count += 1
        in_area = is_in_area(area, pos_x, pos_y)

        if in_area:
            return max_y

        pos_x += speed_x
        pos_y += speed_y

        max_y = max(max_y, pos_y)

        if speed_x > 0:
            speed_x -= 1
        elif speed_x < 0:
            speed_x += 1

        speed_y -= 1

    return None


# find minimal x speed that gets to area
def find_min_x_speed(area):

    speed_to_check = 0

    while True:
        speed_to_check += 1
        total_distance = speed_to_check*(speed_to_check+1) // 2
        if total_distance >= area[0] and total_distance <= area[1]:
            return speed_to_check


# find minimal y speed that gets to area
def find_max_y_speed(area):
    y_speed_limit = 1000
    max_y = 0
    max_y_speed = None

    speed_x = find_min_x_speed(area)

    for speed_y in range(y_speed_limit):
        res = run(area, speed_x, speed_y)

        if res and res > max_y:
            max_y = res
            max_y_speed = speed_y

    return max_y_speed


# count all initial speeds, that get to area
def count_all(area):

    count = 0
    min_x = find_min_x_speed(area)
    max_x = area[1]

    min_y = area[2]
    max_y = find_max_y_speed(area)

    for speed_x in range(min_x, max_x+1):
        for speed_y in range(min_y, max_y+1):
            res = run(area, speed_x, speed_y)
            if res is not None:
                count += 1

    return count


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    area = load_input(file)
    res = count_all(area)
    print(res)
