from homework7.task3 import tic_tac_toe_checker


def test_from_example_1():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_from_example_2():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_x_wins():
    board = [["-", "x", "o"], ["-", "x", "o"], ["-", "x", "o"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_wins():
    board = [["x", "x", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_unfinished_1():
    board = [["x", "x", "o"], ["o", "x", "x"], ["-", "-", "o"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_unfinished_2():
    board = [["x", "x", "o"], ["o", "x", "-"], ["x", "-", "o"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_draw_1():
    board = [["x", "x", "o"], ["o", "x", "x"], ["-", "o", "o"]]
    assert tic_tac_toe_checker(board) == "draw!"


def test_draw_2():
    board = [["x", "o", "-"], ["x", "-", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(board) == "draw!"
