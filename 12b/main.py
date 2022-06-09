#!/usr/bin/python3

# advent of code 2021 - Day 12 b

import os


# load input as dictionary of lists of adjacent vertexes
def load_input(file):

    graph = {}

    for line in file:
        v1, v2 = line.strip().split('-')
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]

        if v2 in graph:
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]

    return graph


# count number of all paths from beginning of 'path' to 'end'
# single lowercase vertex can be visited at most twice
# remaining lowercase vertexes can be visited at most once
def count_paths(graph, path, end, double_small_cave):

    start = path[0]
    current_vertex = path[-1]
    count = 0

    for vertex in graph[current_vertex]:
        if vertex == end:
            count += 1
            continue
        if vertex == start:
            continue

        if vertex.islower() and vertex in path:
            if not double_small_cave:
                count += count_paths(graph, path + [vertex], end, True)
            continue

        count += count_paths(graph, path + [vertex], end, double_small_cave)

    return count


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    graph = load_input(file)
    path = ['start']
    end = 'end'
    double_small_cave = False
    count = count_paths(graph, path, end, double_small_cave)
    print(count)
