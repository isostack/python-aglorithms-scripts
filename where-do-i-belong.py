def getIndexToIns(list, num):
    list.append(num)
    list.sort()
    return list.index(num)


print(getIndexToIns([40, 60], 70))

    

    