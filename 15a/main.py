#!/usr/bin/python3

# advent of code 2021 - Day 15 a

import os
import math


# load input to 2D array
def load_input(file):

    array = []
    for line in file:
        line = line.strip()
        row = [int(c) for c in line]
        array.append(row)
    return array


# heuristics - manhattan distance from destination
def h(x, y, width, height):
    return (width-x) + (height-y)


# https://en.wikipedia.org/wiki/A*_search_algorithm
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path = [current] + total_path

    return total_path


# total cost - cost of every tile of path except start
def path_total_cost(array, path,):
    total = 0

    for place in path[1:]:
        p_x = place[0]
        p_y = place[1]
        total += array[p_y][p_x]

    return total


# check if coordinates are still inside array
def check_valid_coords(x, y, width, height):
    return x >= 0 and y >= 0 and x < width and y < height


# https://en.wikipedia.org/wiki/A*_search_algorithm
def a_star(array):
    height = len(array)
    width = len(array[0])

    goal = (width-1, height-1)

    start_x = 0
    start_y = 0
    start = (start_x, start_y)

    open_set = {start}
    came_from = dict()

    g_score = dict()
    g_score[start] = 0

    f_score = dict()
    f_score[start] = h(start_x, start_y, width, height)

    while len(open_set) > 0:
        current = min(open_set, key=lambda k: f_score[k])
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.discard(current)
        current_x = current[0]
        current_y = current[1]
        neighbors = [(current_x+1, current_y),
                     (current_x-1, current_y),
                     (current_x, current_y+1),
                     (current_x, current_y-1)]

        for n in neighbors:
            n_x = n[0]
            n_y = n[1]
            if not check_valid_coords(n_x, n_y, width, height):
                continue
            tentative_g_score = g_score.get(current, math.inf) + array[n_y][n_x]
            if tentative_g_score < g_score.get(n, math.inf):
                came_from[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = tentative_g_score + h(n_x, n_y, width, height)
                if n not in open_set:
                    open_set.add(n)

    return None  # fail


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    array = load_input(file)
    path = a_star(array)
    print(path_total_cost(array, path))
