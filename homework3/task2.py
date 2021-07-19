import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def func_optimize_slow_calculate():
    start_time = time.time()
    with Pool(520) as p:
        sum_of_calc_time = p.map(slow_calculate, range(501))
    sum_slow_calc = sum(sum_of_calc_time)
    calc_time = time.time() - start_time
    return sum_slow_calc, calc_time
