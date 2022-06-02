#!/usr/bin/python3

# advent of code 2021 - Day 4 a


# loads row of numbers to cross and all boards
def load_input(file):
    numbers = file.readline().split(',')

    numbers = [int(x) for x in numbers]

    boards = []

    while True:
        board = []
        if file.readline() == "":
            break

        for _ in range(5):
            line = file.readline().split()
            line = [int(x) for x in line]
            board.append(line)

        boards.append(board)

    return numbers, boards


# check if row contains only None
def check_row(board, index):

    for cell in board[index]:
        if cell is not None:
            return False

    return True


# check if column contains only None
def check_column(board, index):

    for row in board:
        if row[index] is not None:
            return False

    return True


# replace 'value' by None and return board if complete
def cross_value_in_boards(value, boards):

    for i in range(len(boards)):
        for j in range(len(boards[0])):
            for k in range(len(boards[0][0])):

                if boards[i][j][k] == value:
                    boards[i][j][k] = None
                    if check_column(boards[i], k) or check_row(boards[i], j):
                        return boards[i]

    return None


# get sum of numbers in board, ignore None
def get_board_sum(board):

    val = 0

    for row in board:
        for cell in row:
            if cell:
                val += cell

    return val


with open('input.txt') as file:

    numbers, boards = load_input(file)

    for num in numbers:
        board = cross_value_in_boards(num, boards)

        if board:
            answer = get_board_sum(board) * num
            print(answer)
            break
