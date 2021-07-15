def read_magic_number(path: str) -> bool:
    with open(path) as file_input:
        line = file_input.readline()
        try:
            return True if 1 <= float(line) < 3 else False
        except:
            raise ValueError("Something went wrong")
