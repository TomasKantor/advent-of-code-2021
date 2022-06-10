#!/usr/bin/python3

# advent of code 2021 - Day 13 b

import os


# load a set of 2D points and a list of fold instructions
def load_input(file):

    loading_points = True

    points = set()
    instructions = []

    for line in file:
        if line == '\n':
            loading_points = False
            continue
        if loading_points:
            words = line.split(',')
            x = int(words[0])
            y = int(words[1])
            points.add((x, y))
        else:

            words = line.split('=')
            value = int(words[1])
            axis = words[0][-1]
            instructions.append((axis, value))

    return points, instructions


# create new set of points created by folding paper containing given points
# along axis in instruction
def fold_points(points, instruction):
    axis = instruction[0]
    fold_coord = instruction[1]

    axis = 0 if axis == 'x' else 1

    new_points = set()

    for point in points:
        point_value = point[axis]

        # convert to list, which is mutable
        point = list(point)

        if point_value > fold_coord:
            diff = abs(fold_coord - point_value)
            point[axis] = fold_coord - diff
        point = tuple(point)
        new_points.add(point)

    return new_points


# print points in readable format
def print_points(points):

    max_x_tuple = max(points, key=lambda item: item[0])
    max_y_tuple = max(points, key=lambda item: item[1])

    max_x = max_x_tuple[0] + 1
    max_y = max_y_tuple[1] + 1

    array = [[' ']*max_x for _ in range(max_y)]

    for x, y in points:
        array[y][x] = '#'

    for row in array:
        print(*row)


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    points, instructions = load_input(file)
    for i in instructions:
        points = fold_points(points, i)

    print_points(points)
