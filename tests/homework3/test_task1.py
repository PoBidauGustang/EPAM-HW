from homework3.task1 import cache


def test_positional_dec_cache_positive():
    @cache(times=2)
    def func(a, b):
        return (a ** b) ** 2

    some = 10, 2

    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)

    assert val_1 is val_2
    assert val_1 is val_3
    assert val_2 is val_3
    assert val_1 is not val_4
    assert val_3 is not val_4
