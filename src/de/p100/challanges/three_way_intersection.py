def intersection(l1, l2, l3):
    return_list = list()
    for each in l1:
        if (each in l2) and (each in l3):
            return_list.append(each)
    return return_list

print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))