def chunkArrayInGroups(arr, size):
    newlist = []
    while len(arr) > 0:
        green = []
        for _ in range(size):
            green.append(arr.pop())
        newlist.append(green)
    return newlist
        

print(chunkArrayInGroups(["a", "b", "c", "d"], 2))