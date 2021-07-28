#!/usr/bin/python3
"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"

"""
from itertools import chain, product
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    all_values = [symbol for line in board for symbol in line]
    dash = 0
    all_possible_vertical_and_diagonal_combinations = list(
        product(board[0], board[1], board[2])
    )
    horizontal_lines = [x for x in board]

    vertical_and_diagonal_lines = []
    values_for_win_lines = [0, 5, 13, 21, 26]
    for index, line in enumerate(all_possible_vertical_and_diagonal_combinations):
        if index in values_for_win_lines:
            vertical_and_diagonal_lines.append(line)

    win_lines = chain(vertical_and_diagonal_lines, horizontal_lines)
    for line in win_lines:
        if line.count("x") == 3:
            return "x wins!"
        if line.count("o") == 3:
            return "o wins!"
    for value in all_values:
        if value == "-":
            dash += 1
    if dash == 2 and all_values[4] == "-" or dash <= 1:
        return "draw!"
    return "unfinished!"
