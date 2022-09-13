
from curses.ascii import isalpha

def shift(val):
    if not val.isalpha():
        return val 
    position = ord(val) + 13
    if position > 90:
        position = position - 26
    return chr(position)

def rot13(str):
    result = "".join([shift(item) for item in str])
    return result
    
        
print(rot13("SERR PBQR PNZC"))