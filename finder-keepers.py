def fintElement(list,func):
    for item in list:
        if func(item):
            return item
    return None

print(fintElement([1,2,3,4,5], lambda x: x % 2 == 0))

    

    