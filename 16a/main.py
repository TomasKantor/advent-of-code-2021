#!/usr/bin/python3

# advent of code 2021 - Day 16 a

import os


hex_bin_table = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


# convert hex string to bin string
def hex_to_bin(string):
    res = ''
    for c in string:
        res += hex_bin_table[c]
    return res


# compute literal packet value and end index
def get_literal_value(string, index):
    value = 0
    while True:
        value <<= 4
        value += int(string[index+1:index+5], 2)
        if string[index] == '0':
            break
        index += 5

    return value, index + 5


# parse packet
def parse_packet(string, index):

    # read packet version - 3 bits
    packet_version = int(string[index:index+3], 2)
    index += 3

    # read type id - 3 bits
    type_id = int(string[index:index+3], 2)
    index += 3
    value = None

    # packet with literal value
    if type_id == 4:
        value, index = get_literal_value(string, index)
        return packet_version, index

    # operator packet containing multiple packets
    packet_version_sum = packet_version

    # packets given by length in bits
    if string[index] == '0':
        index += 1
        total_length_in_bits = int(string[index:index+15], 2)
        index += 15
        sub_index = index
        while index + total_length_in_bits > sub_index:
            value, sub_index = parse_packet(string, sub_index)
            packet_version_sum += value
        index = sub_index

    # packets given by their count
    else:
        index += 1
        number_of_sub_packets = int(string[index:index+11], 2)
        index += 11
        for _ in range(number_of_sub_packets):
            value, index = parse_packet(string, index)
            packet_version_sum += value

    return packet_version_sum, index


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    string = file.readline().strip()
    string = hex_to_bin(string)
    packet_version_sum, _ = parse_packet(string, 0)
    print(packet_version_sum)
