def is_armstrong(number: int) -> bool:

    num_to_str = lambda x: str(x)

    def powered_digits(str_num):
        result = list(map(lambda x: int(x) ** len(str_num), str_num))
        return result

    return (number >= 0) and (sum(powered_digits(num_to_str(number))) == number)
