#!/usr/bin/python3

# advent of code 2021 - Day 17 a

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
def run(area, speed_x, speed_y):

    pos_x = 0
    pos_y = 0

    step_count = 0

    max_y = 0

    while pos_y >= min(area[2], area[3]):
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

    return 0


# find minimal x speed that gets to area
def find_ideal_x_speed(area):

    speed_to_check = 0

    while True:
        speed_to_check += 1
        total_distance = speed_to_check*(speed_to_check+1) // 2
        if total_distance >= area[0] and total_distance <= area[1]:
            return speed_to_check


# find max y position, and its initial speed
def find_max(area, y_speed_limit):

    max_y = 0
    max_y_speeds = None

    speed_x = find_ideal_x_speed(area)

    for speed_y in range(y_speed_limit):
        res = run(area, speed_x, speed_y)

        if res > max_y:
            max_y = res
            max_y_speeds = (speed_x, speed_y)

    return max_y, max_y_speeds


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    area = load_input(file)
    y_speed_limit = 1000
    res = find_max(area, y_speed_limit)
    print(res)
