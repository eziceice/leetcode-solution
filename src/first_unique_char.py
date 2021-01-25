import collections


def first_unique_char(s: str) -> int:
    string_dict = collections.Counter(s)
    for key, item in string_dict.items():
        if item == 1:
            return s.find(key)
    return -1