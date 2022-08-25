def mutation(vak):
    test = set(vak[0]) & set(vak[1])
    target = list(vak[1])
    for item in target:
        if item not in test:
            return False
    return True

    
print(mutation(["hello", "hey"]))
    