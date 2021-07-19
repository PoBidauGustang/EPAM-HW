from homework1.task2 import check_fibonacci


def test_fibonacci_case_full():
    """Testing that given sequence is fib sequence"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])


def test_fibonacci_case_sub():
    """Testing that given sequence is fib sequence"""
    assert check_fibonacci([0, 1, 1])


def test_fibonacci_case_empty():
    """Testing that given sequence is fib sequence"""
    assert not check_fibonacci([])


def test_fibonacci_case_zero():
    """Testing that given sequence is fib sequence"""
    assert check_fibonacci([0])


def test_not_fibonacci_case():
    """Testing that given sequence is NOT fib sequence"""
    assert not check_fibonacci([5, 3, 1])
