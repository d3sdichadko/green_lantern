from typing import List


class OurException(Exception):
    pass


def create_list() -> List[int]:
    values_for_exclude = [6, 7]
    return [i for i in range(13) if i not in values_for_exclude]


print(create_list())


def some_stuff():

    try:
        raise ValueError
    except ValueError:
        pass

