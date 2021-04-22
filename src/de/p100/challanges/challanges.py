import timeit

def min_operations(x, y):
    # multiply by 2
    # substract by 1
    calc = y

    result = list()
    while calc != x:
        if calc < x:
            result_end = [1] * int(x - calc)
            result.extend(result_end)
            break
        if ((calc %2) == 0):
            calc = calc / 2
            result.append(2)
        else:
            calc = calc + 1
            result.append(1)

    best_result = result

    end_result = ""
    for each in best_result:
        end_result = end_result + "("
    end_result = end_result + format(x)
    for each in best_result:
        if each == 1:
            end_result = end_result + " - 1)"
        if each == 2:
            end_result = end_result + " * 2)"

    end_result = end_result + "= {} : {} operations needed only".format(y,len(best_result))

    return end_result

start = timeit.default_timer()

print(min_operations(42357, 87877346))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
stop = timeit.default_timer()
print('Time: ', stop - start)
print()