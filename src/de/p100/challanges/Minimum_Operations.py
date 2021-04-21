import timeit
import pandas as pd


operations = []
def min_operations(x, y):
    # no calculations needed when x = y
    if x == y:
        return 0

    # if x > y subtract 1
    if x > y:
        operations.append('- 1 ({}x)'.format(int(x - y)))
        return x - y

    # not possible when x is negative and y is positive
    if x <= 0 < y:
        print('Impossible')
        return -1

    # y > x and y is odd, so subtract 1 from x
    if y % 2 == 1:
        operations.append('- 1')
        return 1 + min_operations(x, y + 1)

    # y is even, so multiply x by 2
    else:
        operations.append('* 2')
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

    start = timeit.default_timer()
    print()
    print('Operations needed to go from {} to {}:'.format(first, second),
          '\033[1m' + str(int(min_operations(int(first), int(second)))) + '\033[0m')
    operations.reverse()
    operations = pd.DataFrame({' ': operations})
    print(operations)
    print()
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    operations = []
    run = input('Run Again? (y/n): ')
    print()
