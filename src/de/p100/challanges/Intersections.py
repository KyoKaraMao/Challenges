import timeit

# starting the timer
start = timeit.default_timer()
print()

def intersection(list1, list2, list3, keep_duplicates):
    """
    :lists format: [1, 2, 3, 4, 5, ...]
    :param list1: list of numbers
    :param list2: list of numbers
    :param list3: list of numbers
    :param keep_duplicates: True or Falls
    :return: only numbers that are present in all three lists
    """

    def keep(list):
        dups = []
        for each in list:
            if each in list:
                dups.append(each)
                list.remove(each)
        return dups

    if keep_duplicates:
        return list(set(list1) &
                    set(list2) &
                    set(list3)
                    ) + \
               list(set(keep(list1)) &
                    set(keep(list2)) &
                    set(keep(list3))
                    )

    else:
        return set(list1) & set(list2) & set(list3)

print(intersection([1, 2, 3, 4, 5, 5], [2, 4, 6, 8, 5, 5], [3, 4, 5, 5],True))

# stopping the timer
stop = timeit.default_timer()
print('Time: ', stop - start)
print()