def intersection(l1, l2, l3):
    a = [x for x in l2 if x in l1]
    b = [x for x in l3 if x in a]
    return b


print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
