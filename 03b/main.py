#!/usr/bin/python3

# advent of code 2021 - Day 3 b


# loads input to array, removes \n
def input_to_array(file):

    input_array = []

    for line in file:
        line = line.strip()
        input_array.append(line)

    return input_array


# returns count of '1' and count of '0' at position 'index'
def counts_for_index(input_array, index):

    ones = 0
    zeros = 0

    for line in input_array:
        value = int(line[index])

        ones += value
        zeros += 1 - value  # turns 1 to 0 and 0 to 1

    return ones, zeros


# converts array of values '1' and '0' to number
def array_of_symbols_to_number(array):

    value = 0
    for c in array:
        value += int(c)
        value <<= 1

    return value >> 1


def compute_rating(rating_type, input_array):

    size = len(input_array[0])

    array_copy = input_array

    for i in range(size):

        ones, zeros = counts_for_index(array_copy, i)

        if rating_type == 'oxygen':

            if ones >= zeros:  # more common value, '1' if equal
                value_to_keep = '1'
            else:
                value_to_keep = '0'
        elif 'CO2':
            if ones < zeros:  # less common value, '0' if equal
                value_to_keep = '1'
            else:
                value_to_keep = '0'
        else:
            return None  # bad input

        array_copy = [x for x in array_copy if x[i] == value_to_keep]

        if len(array_copy) == 1:

            return array_of_symbols_to_number(array_copy[0])

    return None  # bad input


with open('input.txt') as file:

    input_array = input_to_array(file)

    oxygen_generator_rating = compute_rating('oxygen', input_array)
    co2_scrubber_rating = compute_rating('CO2', input_array)

    print(oxygen_generator_rating*co2_scrubber_rating)
