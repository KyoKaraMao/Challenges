def intersection(list1, list2, list3):
    """
    :lists format: [1, 2, 3, 4, 5, ...]
    :param list1: list of numbers
    :param list2: list of numbers
    :param list3: list of numbers
    :return: only numbers that are present in all three lists
    """
    a = [x for x in list2 if x in list1]
    b = [x for x in list3 if x in a]
    return b


print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))

help(intersection)