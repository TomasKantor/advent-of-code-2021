#!/usr/bin/python3

# advent of code 2021 - Day 5 a

import re


class Line:

    def __init__(self, ls):
        self.x1 = ls[0]
        self.y1 = ls[1]
        self.x2 = ls[2]
        self.y2 = ls[3]


class SeaFloor:

    def __init__(self):
        self.floor = dict()

    # adds all points on line to floor
    def add_line(self, line):

        # vertical or horizontal lines only
        if not (line.x1 == line.x2 or line.y1 == line.y2):
            return

        xmin = min(line.x1, line.x2)
        xmax = max(line.x1, line.x2)

        ymin = min(line.y1, line.y2)
        ymax = max(line.y1, line.y2)

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                count = self.floor.get((x, y), 0)
                self.floor[(x, y)] = count + 1

    # counts number of points that are crossed by more than 'value' lines
    def count_points_bigger_than(self, value):

        count = 0
        for floor_value in self.floor.values():
            if floor_value > value:
                count += 1

        return count


# loads floor from file
def load_floor(file):

    floor = SeaFloor()

    for row in file:
        values = re.findall("[0-9]+", row)
        values = [int(x) for x in values]
        line = Line(values)
        floor.add_line(line)

    return floor


with open('input.txt') as file:
    floor = load_floor(file)

    count = floor.count_points_bigger_than(1)
    print(count)
