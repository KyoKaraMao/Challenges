def min_operations(x, y):
    # multiply by 2
    # substract by 1
    calc = x
    result = list()
    operations = 0
    if (y < x) and ((y%2)==0):
        while calc != y:
            if (y % calc) == 0:
                calc = calc * 2
                result.append(2)
                operations += 1
            else:
                calc = calc - 1
                result.append(1)
                operations += 1
    else:
        while calc != y:
            if (((y+1) % calc) == 0) and (calc<y):
                calc = calc * 2
                result.append(2)
                operations += 1
            else:
                calc = calc - 1
                result.append(1)
                operations += 1
    try:
        if(len(result) < len(best_result)):
            best_result = result
    except:
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

    end_result = end_result + "= {} : {} operations needed only".format(y,operations)

    return end_result


print(min_operations(73, 287))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
