from collections import defaultdict
from typing import AnyStr, List
from unicodedata import category


def tokenize(input_file: AnyStr) -> List[List]:
    buffer = []
    words = []
    while char := input_file.read(1):
        if category(char) == "Ll" or category(char) == "Lu":
            buffer.append(char)
            continue
        else:
            if buffer:
                words.append(buffer)
                buffer = []
    return words


def get_longest_diverse_words(file_path: str, encoding="unicode-escape") -> List[str]:

    with open(file_path, "r", encoding=encoding) as file_input:
        list_prepared_words_num_char = []
        for word in tokenize(file_input):
            unique_char = len(set(word))
            list_prepared_words_num_char.append((unique_char, word))
        list_prepared_words_num_char = sorted(
            list_prepared_words_num_char, key=lambda x: x[0], reverse=True
        )
        list_prepared_words_num_char = list_prepared_words_num_char[0:10]
        list_prepared_words = []
        for item in list_prepared_words_num_char:
            list_prepared_words.append(item[1])
        list_prepared_words = sorted(
            list_prepared_words, key=lambda x: len(x), reverse=True
        )
        final_result = []
        for item in list_prepared_words:
            final_result.append("".join(item))
    return final_result


def get_rarest_char(file_path: str, encoding="unicode-escape") -> str:
    with open(file_path, "r", encoding=encoding) as file_input:
        dict_char = defaultdict(int)
        while char := file_input.read(1):
            dict_char[char] += 1
        rarest_char = sorted(dict_char, key=dict_char.get, reverse=False)[0]
    return rarest_char


def count_punctuation_chars(file_path: str, encoding="unicode-escape") -> int:
    with open(file_path, "r", encoding=encoding) as file_input:
        counter = 0
        while char := file_input.read(1):
            if category(char) == "Po":
                counter += 1
    return counter


def count_non_ascii_chars(file_path: str, encoding="unicode-escape") -> int:
    with open(file_path, "r", encoding=encoding) as file_input:
        counter = 0
        while char := file_input.read(1):
            for item in char:
                if not char.isascii():
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str, encoding="unicode-escape") -> str:
    with open(file_path, "r", encoding=encoding) as file_input:
        dict_char = defaultdict(int)
        while char := file_input.read(1):
            if not char.isascii():
                dict_char[char] += 1
        common_char = sorted(dict_char, key=dict_char.get, reverse=True)[0]
    return common_char
