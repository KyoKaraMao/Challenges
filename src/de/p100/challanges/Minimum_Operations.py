import timeit
import pandas as pd


operations = []
values = []


def min_operations(x, y):
    """
    :param x: First Number, must be integer
    :param y: Second Number, must be integer
    :return: Number of operations needed to go from x to y while
             only subtracting 1 from x or multiplying x by 2
             and the actual operations that need to be done
    """

    # no calculations needed when x = y
    if x == y:
        return 0

    # if x > y subtract 1
    if x > y:
        if x - y > 1:
            operations.append('- 1 ({}x)'.format(int(x - y)))
        else:
            operations.append('- 1')
        values.append(int(x))
        return x - y

    # not possible when x is negative and y is positive
    if x <= 0 < y:
        print('Impossible')
        return -1

    # y > x and y is odd, so subtract 1 from x
    if y % 2 == 1:
        operations.append('- 1')
        values.append(int(y - 1))
        return 1 + min_operations(x, y + 1)

    # y is even, so multiply x by 2
    else:
        operations.append('* 2')
        values.append(int(y / 2))
        return 1 + min_operations(x, y / 2)


# rerunning the program
run = 'y'


while run == 'y':
    # Enter x value and check if it's an integer
    first = input('Enter x-value: ')
    try:
        int(first)
    except:
        print('Numbers must be integers!')
        print()
        continue

    # enter y value and check if it's an integer
    second = input('Enter y-value: ')
    try:
        int(second)
    except:
        print('Numbers must be integers!')
        print()
        continue

    # starting the timer
    start = timeit.default_timer()
    values.append(second)
    print()

    # running the function with the numbers from input
    print('Operations needed to go from {} to {}:'.format(first, second),
          '\033[1m' + str(int(min_operations(int(first), int(second)))) + '\033[0m')

    # reversing the lists of operations so they fit the way from x to z
    operations.reverse()
    operations.append(' ')
    values.reverse()

    # making the lists into a dataframe
    operation_list = pd.DataFrame(
        {'x': values,
         'op': operations
         })
    print(operation_list)
    print()

    # stopping the timer
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    print()

    # resetting the lists
    operations = []
    values = []

    # run the function again if input is y
    run = input('Run Again? (y/n): ')
    print()

# goodbye message
print('Thank you for calculating!')
