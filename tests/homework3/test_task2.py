import pytest

from homework3.task2 import func_optimize_slow_calculate


def test_slow_calculate():
    sum_slow_calcm, time_calc = func_optimize_slow_calculate()
    assert time_calc <= 60
    assert sum_slow_calcm == 1025932
