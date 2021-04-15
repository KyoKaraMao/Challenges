def min_operations(x, y):
    # multiply by 2
    # substract by 1
    operations = 1
    if x == y:
        print(operations)

    newTable = list()
    table = find_min_operations(x,y,operations, 1, newTable, 20)
    myBestTable = table
    table = find_min_operations(x,y,operations, 2, newTable, len(myBestTable))
    myBestTable = myBestTable[:-1]
    if len(myBestTable) > len(table):
        myBestTable = table
    print(myBestTable)

    # plan:
    # Schleife solange bis x == y oder x > y wenn x am Anfang < y war
    # Testen schnellster weg mit wenn anzahl schritt > als vorheriger weg dann dieser weg
    # wenn mehr schritte dann ein schritt zurück und das andere testen

def find_min_operations(x, y, operations, calc, startTable, max):
    bestTable = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    currentTable = startTable
    currentTable.insert(operations, calc)
    if calc == 1:
        x = x-1
    else:
        x = x*2
    if x==y:
        return currentTable
    if len(currentTable) >= max:
        return bestTable
    table = find_min_operations(x,y,operations+ 1, 2, currentTable, max)
    try:
        if len(bestTable) > len(table):
            bestTable = table
            if max > len(bestTable):
                max = len(bestTable)
    except:
        bestTable = table
    currentTable = table[:-1]
    table = find_min_operations(x,y,operations + 1, 1, currentTable, max)
    try:
        if len(bestTable) > len(table):
            bestTable = table
            if max > len(bestTable):
                max = len(bestTable)
    except:
        bestTable = table

    return bestTable

print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
