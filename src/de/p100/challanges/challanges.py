def min_operations(x, y):
    # multiply by 2
    # substract by 1
    operations = 0
    if x == y:
        print(operations)
    elif x > y:
        operator = "<"
    else:
        operator = ">"

    table = find_min_operations(x,y,operations,operator,-1)


    print()
    # plan:
    # Schleife solange bis x == y oder x > y wenn x am Anfang < y war
    # Testen schnellster weg mit wenn anzahl schritt > als vorheriger weg dann dieser weg
    # wenn mehr schritte dann ein schritt zurück und das andere testen

def find_min_operations(x, y, operations, operator, calc, bestTable = None):
    if x==y:
        return bestTable
    if operator == '>':
        if x * 2-5 > y:
            return bestTable

    bestTable[operations] = calc
    table = find_min_operations(x,y,operations +1,operator,-1)
    try:
        if len(bestTable) > len(table):
            bestTable = table
    except:

        bestTable = table

    return bestTable

print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
